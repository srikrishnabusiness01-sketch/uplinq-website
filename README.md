# Check (wearecheck.co) - Complete Website & Motion Clone

A pixel-perfect, animation-complete clone of [wearecheck.co](https://wearecheck.co) — the award-winning unconventional digital design and technology company.

This clone preserves the full visual identity, interactive dynamics, motion capture, animations, and high-fidelity assets of the original site with **100% self-contained local assets**.

---

## 🌟 Included Pages & Routes

1. **Home (`/`)**:
   - Interactive pre-loader with percentage progress counter and fill animation.
   - Dynamic hero header with interactive floating badges, video loop embeds, and magnetic CTA buttons.
   - Smooth text reveals and line-by-line GSAP SplitText typography animations.
   - Interactive About section with animated SVG sketch paths using GSAP DrawSVG.
   - Interactive Services accordion (Strategy, Digital, Brand) with custom SVG diagrams.
   - Featured Case Studies showcase (NLNG, Quidax, Kele, Autograph, Propel) with video previews and hover interactions.
   - Full responsive navigation with page section progress indicator and interactive full-screen menu overlay.
   - Footer with social channels, newsletter CTA, and direct mail link.
2. **About (`/about`)**:
   - Company manifesto, culture overview, interactive team gallery, and design philosophy.
3. **Services (`/services`)**:
   - Detailed breakdown of Strategy, Digital Products, and Living Brands offerings.
4. **Careers (`/careers`)**:
   - Open positions, working principles, culture photographs, and application links.
5. **Work Showcase (`/work`)**:
   - Comprehensive directory of case studies and agency portfolio.
6. **Case Studies**:
   - **NLNG (`/case/nlng`)**: Interactive 36-year energy giant repositioning case study with 7 video motion capture reels, interactive shot grids, and responsive narrative layouts.
   - **Quidax (`/work/quidax`)**: High-definition announcement video embed, case study animations, visual identity breakdown, and interactive GIFs.
   - **Kele (`/work/kele`)**: Financial accessibility app case study with app UI flow GIFs and interactive brand assets.
   - **Autograph (`/work/autograph`)**: Stationery brand case study with packaging mockups and visual identity gallery.
   - **Propel (`/work/propel`)**: Future of work platform case study with video previews and communications design.

---

## 🎬 Motion Design, GSAP & Asset Highlights

- **All Motion Capture & Hover Videos Included**:
  - Menu navigation hover videos (`video-home`, `video-about-us`, `video-work`, `video-services`, `video-blog`, `video-careers`, `video-showreel`, `video-year-in-review`, etc.).
  - Case study video motion capture reels (`video-ship-compressed`, `video-moving-cards`, `video-revolving-globe`, `video-business-man`, `video-scrolls`, `video-improve-lives`, `video-energy`, `video-pan-around`).
  - High-definition Quidax brand launch video (31.8 MB).
  - Background loop videos and hero media.
- **GSAP Plugins Suite**:
  - `DrawSVGPlugin`: SVG line drawing and sketch stroke animations.
  - `SplitText`: Smooth character, word, and line typography reveal animations.
  - `CustomEase`: Custom easing curves matching Check's snappy kinetic style.
  - `InertiaPlugin`: Momentum-based smooth dragging and physics interactions.
- **Complete Typography Suite**:
  - Full MangoGrotesque font family (Thin, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black + Italics).
  - Full PolySans font family (Slim, Neutral, Median, Bulky + Italics).
  - Webflow Icon fonts.
- **100% Offline & Self-Contained**:
  - All 248 assets (154+ MB) are hosted locally under `site/` with 0 missing dependencies.
  - No external CDN or third-party asset calls required for rendering or animations.

---

## 🐳 Docker Deployment

The website is fully containerized using an optimized, high-performance Nginx Alpine configuration with built-in byte-range MP4 video streaming (`Accept-Ranges: bytes`), gzip compression, and clean SPA route handling.

### 1. Run Container (Already active on port 3000)

```bash
# Start with Docker Compose
docker compose up -d

# Check running container
docker ps
```

Visit the website at:
👉 **[http://localhost:3000](http://localhost:3000)**

### 2. Stop or Restart Container

```bash
# Stop
docker compose down

# Restart / Rebuild
docker compose up -d --build
```

### 3. Upload / Push to Docker Hub

To push your Docker image to Docker Hub or any remote registry:

```bash
# 1. Login to Docker Hub
docker login

# 2. Tag image with your Docker Hub username
docker tag wearecheck-website:latest <your-dockerhub-username>/wearecheck-website:latest

# 3. Push to Docker Hub
docker push <your-dockerhub-username>/wearecheck-website:latest
```

---

## 🚀 Quick Start (Local Node.js Development)

The project includes an HTTP server with HTTP/1.1 byte-range streaming support (essential for seamless MP4 video seeking and animation playback in modern browsers).

### Requirements
- Node.js (v16+)

### Run Locally

```bash
# Clone or navigate to the directory
cd Uplinq_website_final

# Start the local server
npm start
```

Open your browser at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## 📂 Project Structure

```text
Uplinq_website_final/
├── site/                     # Standalone production-ready site
│   ├── index.html            # Home page
│   ├── about/index.html      # About page
│   ├── services/index.html   # Services page
│   ├── careers/index.html    # Careers page
│   ├── work/index.html       # Work index
│   ├── case/nlng/index.html  # NLNG featured case study
│   ├── work/quidax/          # Quidax case study
│   ├── work/kele/            # Kele case study
│   ├── work/autograph/       # Autograph case study
│   ├── work/propel/          # Propel case study
│   ├── _nuxt/                # Nuxt JS bundles, CSS stylesheets & core SVGs
│   ├── assets/
│   │   ├── fonts/            # MangoGrotesque & PolySans typography
│   │   ├── mdn/              # GSAP plugins, MP4 motion capture & WebM videos
│   │   └── cdn/              # High-res case study photos, mockups & UI GIFs
│   ├── cdn-cgi/              # Cloudflare email decode support
│   ├── favicon.png           # Favicon
│   └── webclip.png           # Apple touch icon
├── tools/                    # Automated crawler & verification utilities
│   ├── crawler.js            # Site crawler & asset pipeline
│   ├── download_menu_videos.js # Menu motion capture downloader
│   ├── download_single.js    # Resilient stream downloader
│   ├── fix_email.js          # Email decoder generator
│   └── verify_all.js         # Comprehensive 0-missing-asset validator
├── server.js                 # HTTP server with video Range-header streaming
├── vercel.json               # Vercel 1-click deployment configuration
├── netlify.toml              # Netlify 1-click deployment configuration
└── package.json              # NPM scripts
```

---

## ☁️ Deployment

### 1. Vercel
Simply import this repository into Vercel. The included [`vercel.json`](vercel.json) automatically maps clean URLs and static asset routes.

### 2. Netlify
Deploy to Netlify and point the publish directory to `site`. The included [`netlify.toml`](netlify.toml) configures redirects and routing.

### 3. Nginx / Apache / Docker
Serve the files in `site/` with any static web server or reverse proxy.
Ensure your web server enables byte-range requests for `.mp4` and `.webm` files (`Accept-Ranges: bytes`) for smooth video playback.
