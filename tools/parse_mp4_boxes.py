import struct
import os

def walk_boxes(f, offset, length, indent=0):
    boxes = []
    end = offset + length
    f.seek(offset)
    while f.tell() < end:
        pos = f.tell()
        header = f.read(8)
        if len(header) < 8:
            break
        box_size, box_type = struct.unpack('>I4s', header)
        box_type = box_type.decode('latin1', errors='ignore')
        if box_size == 1:
            box_size = struct.unpack('>Q', f.read(8))[0]
            header_len = 16
        else:
            header_len = 8
        if box_size == 0:
            box_size = end - pos
        
        boxes.append((box_type, pos, box_size))
        
        if box_type in ['moov', 'trak', 'mdia', 'minf', 'stbl']:
            walk_boxes(f, pos + header_len, box_size - header_len, indent + 2)
        elif box_type == 'tkhd':
            f.seek(pos + header_len)
            version = struct.unpack('>B', f.read(1))[0]
            f.seek(pos + header_len + (88 if version == 1 else 76))
            w = struct.unpack('>I', f.read(4))[0] >> 16
            h = struct.unpack('>I', f.read(4))[0] >> 16
            if w > 0 and h > 0:
                print(' ' * indent + f"TRACK RESOLUTION: {w}x{h} (ratio: {w/h:.2f}:1)")
        elif box_type == 'mvhd':
            f.seek(pos + header_len)
            version = struct.unpack('>B', f.read(1))[0]
            f.seek(pos + header_len + 4)
            if version == 0:
                f.seek(pos + header_len + 12)
                timescale, duration = struct.unpack('>II', f.read(8))
            else:
                f.seek(pos + header_len + 20)
                timescale, duration = struct.unpack('>IQ', f.read(12))
            if timescale > 0:
                print(' ' * indent + f"MOVIE DURATION: {duration / timescale:.2f}s")
                
        f.seek(pos + box_size)
    return boxes

for path in [
    r'site\assets\mdn\video-website-loop-ucoly5mp4-t0wMA.mp4',
    r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793261977131_44da9415.mp4'
]:
    print(f"\nParsing: {path} ({os.path.getsize(path)/1024:.1f} KB)")
    with open(path, 'rb') as f:
        walk_boxes(f, 0, os.path.getsize(path))
