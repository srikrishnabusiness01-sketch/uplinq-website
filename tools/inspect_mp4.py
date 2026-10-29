import struct
import os

def parse_mp4(filepath):
    print(f"\n==========================================")
    print(f"FILE: {filepath}")
    size = os.path.getsize(filepath)
    print(f"File Size: {size / (1024*1024):.2f} MB ({size} bytes)")
    
    with open(filepath, 'rb') as f:
        data = f.read(min(size, 500000)) # read first 500KB
    
    # search for tkhd (track header) to get width & height
    idx = 0
    tkhds = []
    while True:
        idx = data.find(b'tkhd', idx)
        if idx == -1:
            break
        # tkhd box starts 4 bytes before 'tkhd'
        box_start = idx - 4
        version = data[box_start + 8]
        if version == 0:
            # version 0: 32-bit fields
            # width and height are at offset 76 and 80 from box start
            w_fixed = struct.unpack('>I', data[box_start + 76:box_start + 80])[0]
            h_fixed = struct.unpack('>I', data[box_start + 80:box_start + 84])[0]
        else:
            # version 1: 64-bit fields
            w_fixed = struct.unpack('>I', data[box_start + 88:box_start + 92])[0]
            h_fixed = struct.unpack('>I', data[box_start + 92:box_start + 96])[0]
        width = w_fixed >> 16
        height = h_fixed >> 16
        if width > 0 and height > 0:
            tkhds.append((width, height))
        idx += 4

    print("Tracks (width x height):", tkhds)
    if tkhds:
        w, h = tkhds[0]
        print(f"Resolution: {w} x {h} px | Ratio: {round(w/h, 2)}:1")

    # Search for mvhd to get duration
    idx = data.find(b'mvhd')
    if idx != -1:
        box_start = idx - 4
        version = data[box_start + 8]
        if version == 0:
            timescale = struct.unpack('>I', data[box_start + 20:box_start + 24])[0]
            duration = struct.unpack('>I', data[box_start + 24:box_start + 28])[0]
        else:
            timescale = struct.unpack('>I', data[box_start + 28:box_start + 32])[0]
            duration = struct.unpack('>Q', data[box_start + 32:box_start + 40])[0]
        if timescale > 0:
            dur_sec = duration / timescale
            print(f"Duration: {dur_sec:.2f} seconds")

# Test on existing and uploaded
parse_mp4(r'site\assets\mdn\video-website-loop-ucoly5mp4-t0wMA.mp4')
parse_mp4(r'C:\Users\Asus\.gemini\antigravity\brain\1a96c3e4-4d36-437b-9a4e-5e24e4977eeb\.user_uploaded\media_1793261977131_44da9415.mp4')
