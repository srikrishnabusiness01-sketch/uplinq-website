css_path = 'site/_nuxt/entry.DzM0mqX9.css'
css_txt = open(css_path, encoding='utf-8').read()

marker = '/* ============================================================\n   MOBILE RESPONSIVE STYLES (Screen sizes below 768px)'
idx = css_txt.find(marker)
if idx == -1:
    marker = 'MOBILE RESPONSIVE STYLES'
    idx = css_txt.find(marker)
    # find the comment start
    idx = css_txt.rfind('/*', 0, idx)

desktop_part = css_txt[:idx]

new_mobile_block = '''/* ============================================================
   MOBILE RESPONSIVE STYLES (Screen sizes below 768px)
   Applied strictly to mobile only. Desktop view remains 100% untouched.
   ============================================================ */
@media screen and (max-width: 767.98px) {
  /* --- General & Foundational Rules --- */
  html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100vw !important;
    position: relative !important;
    -webkit-overflow-scrolling: touch;
  }

  *, *::before, *::after {
    box-sizing: border-box !important;
  }

  .padding-global,
  .padding-global.cc-large,
  .padding-global.cc-small {
    padding-left: 20px !important;
    padding-right: 20px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .c-container {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
  }

  img, svg, video {
    max-width: 100% !important;
  }

  .c-button,
  button,
  .menu-button,
  .social-link,
  .c-checkbox {
    min-height: 44px !important;
    touch-action: manipulation;
  }

  /* --- 1. NAVIGATION --- */
  /* Logo stays top left */
  /* Menu button and hamburger icon visible */
  /* Stack nav links vertically, readable and tappable */
  .c-nav {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 99 !important;
    opacity: 1 !important;
    transform: none !important;
    background-color: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(8px) !important;
    -webkit-backdrop-filter: blur(8px) !important;
  }

  .nav-inner {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 16px 20px !important;
    width: 100% !important;
    position: relative !important;
  }

  .nav-logo {
    display: flex !important;
    align-items: center !important;
    width: 110px !important;
    max-width: 120px !important;
    margin: 0 !important;
    z-index: 2 !important;
  }

  .nav-logo .c-img {
    height: 30px !important;
    width: auto !important;
    object-fit: contain !important;
  }

  .menu-button,
  .c-nav .menu-button,
  .nav-wrapper .menu-button {
    display: flex !important;
    visibility: visible !important;
    pointer-events: auto !important;
    opacity: 1 !important;
    align-items: center !important;
    cursor: pointer !important;
    background: transparent !important;
    border: none !important;
    padding: 8px 6px !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    color: #000 !important;
    z-index: 99 !important;
  }

  .menu-icon {
    width: 28px !important;
    height: 18px !important;
    margin-left: 8px !important;
    background-image: url(/assets/images/open.svg) !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    background-size: contain !important;
    display: inline-block !important;
  }

  .c-nav .page-progress {
    display: none !important;
  }

  /* Full-Screen Mobile Menu Drawer */
  .menu-top {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    padding: 20px 24px !important;
    margin-bottom: 24px !important;
    width: 100% !important;
  }

  .menu-link_cta {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    padding: 0 24px !important;
    margin-bottom: 30px !important;
    margin-top: 0 !important;
  }

  .menu-link_flex {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    margin: 0 !important;
  }

  .menu-link_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 12px !important;
  }

  .menu-link {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    font-size: clamp(30px, 8vw, 42px) !important;
    line-height: 1.1 !important;
    padding: 10px 0 !important;
    min-height: 48px !important;
    width: 100% !important;
    text-decoration: none !important;
  }

  .menu-link .menu-tag {
    font-size: 14px !important;
    margin-left: 10px !important;
    opacity: 0.7 !important;
  }

  /* --- 2. HERO SECTION --- */
  /* Headline font scales down to fit mobile */
  /* Text does not overflow or get cut off */
  /* Sticker labels reposition to stay visible */
  /* Images/mockups stack below text */
  .section-header {
    padding-top: 76px !important;
    overflow: hidden !important;
  }

  .header-inner.cc-home {
    height: auto !important;
    min-height: auto !important;
    max-height: none !important;
    padding: 20px 20px 32px !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
  }

  .header-title_wrapper,
  .header-title_wrapper.cc-top,
  .header-title_wrapper.cc-bottom {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 auto 6px !important;
    padding: 0 !important;
  }

  .header-title_wrapper.cc-top.cc-expand {
    padding-right: 0 !important;
  }

  .relative-block.header-re,
  .relative-block.header-think,
  .relative-block.header-subtext {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    width: 100% !important;
    margin: 0 0 4px !important;
    position: relative !important;
  }

  .heading-h1 {
    font-size: clamp(34px, 11vw, 54px) !important;
    line-height: 0.95 !important;
    letter-spacing: -0.02em !important;
    text-align: center !important;
    width: 100% !important;
    word-break: normal !important;
    overflow-wrap: normal !important;
  }

  .header-video_block.cc-top,
  .header-video_block.cc-bottom.cc-desktop {
    display: none !important;
  }

  .header-tag,
  .header-tag.cc-digital,
  .header-tag.cc-strategy,
  .header-tag.cc-strategy.cc-yellow {
    position: relative !important;
    display: inline-block !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    transform: none !important;
    font-size: 14px !important;
    line-height: 1 !important;
    padding: 4px 8px !important;
    margin: 4px auto !important;
    border-radius: 4px !important;
    vertical-align: middle !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;
  }

  /* Hero Video Card - Scaled to fill box cleanly with zero white border */
  .header-video_block.cc-mobile {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    aspect-ratio: 16 / 9 !important;
    height: auto !important;
    margin: 18px 0 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    position: relative !important;
    -webkit-clip-path: none !important;
    clip-path: none !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06) !important;
    background-color: #fff !important;
  }

  .header-video_block.cc-mobile > img,
  .header-video_mobile {
    position: absolute !important;
    inset: 0 !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    object-position: center center !important;
    transform: scale(1.9) !important;
    transform-origin: center center !important;
    display: block !important;
  }

  /* --- 3. ABOUT STRIP & HERO CTA --- */
  /* Text center align */
  /* CTA button full width */
  .header-subtext_container {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    margin-top: 14px !important;
    padding: 0 !important;
  }

  .header-text_wrapper {
    text-align: center !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 auto 14px !important;
  }

  .header-text_wrapper p {
    font-size: 15px !important;
    line-height: 1.45 !important;
    text-align: center !important;
    margin: 0 auto !important;
    color: #333 !important;
  }

  .header-subtext_container .c-button,
  .c-button.home {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    max-width: 100% !important;
    min-height: 50px !important;
    height: 50px !important;
    background-color: #000 !important;
    color: #fff !important;
    border-radius: 6px !important;
    opacity: 1 !important;
    visibility: visible !important;
    margin: 8px auto 0 !important;
    padding: 0 16px !important;
    cursor: pointer !important;
  }

  .header-subtext_container .c-button_inner,
  .c-button.home .c-button_inner {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 20px !important;
    color: #fff !important;
  }

  /* --- 4. TRANSITION SECTION --- */
  /* Large heading scales down */
  /* Illustrations stack in 2x2 grid */
  .section-about {
    padding: 40px 0 !important;
    overflow: hidden !important;
  }

  .about-inner {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
  }

  .about-text_wrapper {
    text-align: center !important;
    margin-bottom: 12px !important;
  }

  .about-text_wrapper p {
    font-size: 15px !important;
    text-align: center !important;
  }

  .about-title_wrapper {
    text-align: center !important;
    width: 100% !important;
    margin-bottom: 24px !important;
  }

  .about-title_wrapper .heading-h3 {
    font-size: clamp(26px, 8vw, 38px) !important;
    line-height: 1.1 !important;
    text-align: center !important;
    width: 100% !important;
  }

  .about-sketch_wrapper {
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 16px !important;
    width: 100% !important;
    max-width: 320px !important;
    margin: 0 auto !important;
    justify-items: center !important;
    align-items: center !important;
  }

  .about-sketch_wrapper .sketch-divider {
    display: none !important;
  }

  .about-sketch_block {
    width: 100% !important;
    max-width: 130px !important;
    aspect-ratio: 1 / 1 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 8px !important;
  }

  .about-sketch_block img {
    max-width: 100% !important;
    max-height: 100px !important;
    object-fit: contain !important;
  }

  /* --- 5. SERVICES SECTION (Fixes text collisions) --- */
  /* 3 service blocks stack vertically */
  /* Each block full width */
  .section-services {
    padding: 30px 0 !important;
    overflow: hidden !important;
  }

  .services-flex_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
  }

  .services-absolute {
    display: none !important;
  }

  .services-block_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 20px !important;
  }

  .services-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: stretch !important;
    justify-content: flex-start !important;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    min-height: auto !important;
    padding: 24px 20px !important;
    margin: 0 !important;
    border-radius: 12px !important;
    position: relative !important;
    box-sizing: border-box !important;
    overflow: visible !important;
  }

  .service-block_inner {
    position: relative !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    display: flex !important;
    flex-direction: column !important;
  }

  .service-block_title {
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    gap: 10px !important;
    margin: 0 0 12px 0 !important;
    position: relative !important;
  }

  .service-block_title .heading-h2 {
    font-size: clamp(28px, 8vw, 36px) !important;
    line-height: 1 !important;
    margin: 0 !important;
  }

  .service-tag {
    font-size: 13px !important;
    padding: 3px 8px !important;
    border-radius: 4px !important;
  }

  .service-text_wrapper {
    width: 100% !important;
    position: relative !important;
    margin: 0 0 16px 0 !important;
  }

  .service-text_wrapper p {
    font-size: 15px !important;
    line-height: 1.5 !important;
    margin: 0 !important;
    color: #333 !important;
  }

  /* Decouple SVG illustration so it sits cleanly below paragraph */
  .service-block_sketch {
    position: relative !important;
    inset: auto !important;
    top: auto !important;
    right: auto !important;
    bottom: auto !important;
    left: auto !important;
    width: 100% !important;
    max-width: 180px !important;
    height: auto !important;
    margin: 16px auto 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    clear: both !important;
  }

  .service-block_sketch img {
    position: relative !important;
    width: 100% !important;
    max-height: 150px !important;
    height: auto !important;
    object-fit: contain !important;
    display: block !important;
  }

  /* Hide stray blue decorative scribbles on mobile */
  .stats-sketch,
  .stats-sketch.cc-wide,
  .stats-sketch.cc-align-bottom {
    display: none !important;
  }

  /* --- 6. IMPACT WORDS SECTION (Fixes photo collision with words) --- */
  /* Text scales down and center */
  .win-category_wrapper {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    padding: 30px 0 !important;
    position: relative !important;
  }

  .win-text_wrapper {
    text-align: center !important;
    margin: 0 auto 12px !important;
    width: 100% !important;
    position: relative !important;
    z-index: 5 !important;
  }

  .win-text_wrapper p {
    text-align: center !important;
    font-size: 15px !important;
    color: #555 !important;
    margin: 0 !important;
  }

  .win-category {
    display: flex !important;
    justify-content: center !important;
    text-align: center !important;
    width: 100% !important;
    margin: 2px 0 !important;
    position: relative !important;
    z-index: 5 !important;
    align-self: center !important;
    margin-left: 0 !important;
  }

  .win-category.cc-impact,
  .win-category.cc-speed {
    align-self: center !important;
    margin-left: 0 !important;
  }

  .win-category div {
    font-size: clamp(38px, 11vw, 56px) !important;
    line-height: 1 !important;
    text-align: center !important;
  }

  /* Hide colliding top container */
  .win-img_container.cc-top {
    display: none !important;
  }

  /* Clean 2x2 grid container below the text */
  .win-img_container.cc-bottom {
    position: relative !important;
    width: 100% !important;
    max-width: 320px !important;
    height: auto !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    margin: 24px auto 0 !important;
    display: block !important;
    align-self: center !important;
  }

  .win-img_wrapper.cc-bottom {
    position: relative !important;
    display: grid !important;
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
    width: 100% !important;
    height: auto !important;
    inset: auto !important;
  }

  .win-img_block,
  .win-img_block.cc-bottom,
  .win-img_block.cc-one,
  .win-img_block.cc-two,
  .win-img_block.cc-three {
    position: relative !important;
    inset: auto !important;
    top: auto !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    transform: none !important;
    width: 100% !important;
    height: auto !important;
    aspect-ratio: 4 / 3 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
  }

  .win-img_block img {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    display: block !important;
  }

  /* --- 7. COMPANY STORY SECTION (Fixes illustration cutoffs & text alignment) --- */
  /* Left paragraph and right stat block stack vertically */
  /* Globe/map illustration scales down */
  .services-inner.cc-stats,
  .stats-block_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    gap: 28px !important;
  }

  .stats-block {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 0 20px 0 !important;
    padding: 0 !important;
  }

  .stats-block_flex,
  .stats-block_flex.cc-align-top,
  .stats-block_flex.cc-align-bottom {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    min-height: auto !important;
    padding: 0 !important;
    margin: 0 0 16px 0 !important;
    gap: 10px !important;
  }

  .stats-text_wrapper {
    font-size: clamp(20px, 5.5vw, 24px) !important;
    line-height: 1.3 !important;
    text-align: center !important;
    width: 100% !important;
    margin: 0 auto 10px !important;
  }

  .stats-figure {
    font-family: var(--title) !important;
    font-size: clamp(48px, 14vw, 68px) !important;
    line-height: 1 !important;
    text-align: center !important;
    margin: 0 auto !important;
    justify-content: center !important;
  }

  .stats-details_text,
  .stats-details_text.cc-last {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    font-size: 18px !important;
    line-height: 1.2 !important;
    margin: 4px auto !important;
    width: 100% !important;
  }

  .stats-sketch_block,
  .stats-sketch_block.cc-globe,
  .stats-sketch_block.cc-town {
    display: block !important;
    position: relative !important;
    width: 100% !important;
    max-width: 300px !important;
    height: auto !important;
    max-height: none !important;
    aspect-ratio: 16 / 10 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    margin: 16px auto !important;
    padding: 0 !important;
    inset: auto !important;
  }

  .stats-sketch_block img,
  .stats-sketch_block video {
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    display: block !important;
  }

  .stats-details_block.cc-country {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    margin: 10px 0 !important;
  }

  /* --- 8. WORK SECTION --- */
  /* Project cards stack vertically */
  /* Each card full width */
  .section-projects {
    padding: 36px 0 !important;
  }

  .projects-header_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    margin-bottom: 20px !important;
  }

  .projects-title_wrapper .heading-h2 {
    font-size: clamp(32px, 9.5vw, 48px) !important;
    line-height: 1 !important;
    margin-bottom: 6px !important;
  }

  .projects-text_wrapper p {
    font-size: 15px !important;
    line-height: 1.45 !important;
  }

  .project-block_wrapper {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 24px !important;
  }

  .c-project {
    display: block !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 0 24px 0 !important;
    text-decoration: none !important;
  }

  .project-thumbnail {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    aspect-ratio: 16 / 9 !important;
    max-height: 220px !important;
    border-radius: 8px !important;
    overflow: hidden !important;
  }

  .thumbnail-img_block,
  .thumbnail-img_block img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
  }

  .project-details {
    margin-top: 12px !important;
    width: 100% !important;
  }

  .project-name {
    font-size: clamp(26px, 7vw, 36px) !important;
    line-height: 1.1 !important;
    margin-bottom: 6px !important;
  }

  .project-description {
    font-size: 15px !important;
    line-height: 1.45 !important;
    color: #444 !important;
  }

  /* --- 9. CTA BLOCK --- */
  /* Text center align */
  /* Button full width */
  .footer-header_wrapper {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    width: 100% !important;
    margin-bottom: 36px !important;
  }

  .footer-title_wrapper {
    text-align: center !important;
    width: 100% !important;
    margin-bottom: 18px !important;
  }

  .footer-title_wrapper p {
    text-align: center !important;
    font-size: 16px !important;
    margin-bottom: 8px !important;
  }

  .footer-title_wrapper .heading-h2 {
    font-size: clamp(30px, 8.5vw, 46px) !important;
    line-height: 1.05 !important;
    text-align: center !important;
  }

  .footer-cta_wrapper {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
  }

  .footer-text_wrapper {
    text-align: center !important;
    margin-bottom: 18px !important;
    width: 100% !important;
  }

  .footer-text_wrapper p {
    text-align: center !important;
    font-size: 15px !important;
    line-height: 1.45 !important;
  }

  .footer-cta_wrapper .c-button {
    width: 100% !important;
    max-width: 100% !important;
    display: block !important;
  }

  .footer-cta_wrapper .c-button_inner {
    width: 100% !important;
    justify-content: center !important;
    min-height: 52px !important;
    font-size: 24px !important;
  }

  /* --- 10. FOOTER --- */
  /* Links stack vertically */
  /* Logo and copyright centered */
  .c-footer {
    padding: 36px 0 28px !important;
    overflow: hidden !important;
  }

  .footer-socials {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
    gap: 10px !important;
    margin: 28px 0 !important;
  }

  .footer-socials .social-link {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
    max-width: 300px !important;
    min-height: 44px !important;
    padding: 12px 18px !important;
    border: 1px solid var(--dark-grey) !important;
    border-radius: 6px !important;
    font-size: 15px !important;
    text-decoration: none !important;
  }

  .footer-bottom_wrapper,
  .footer-bottom {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    text-align: center !important;
    gap: 14px !important;
    width: 100% !important;
    margin-top: 20px !important;
  }

  .footer-logo {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
    margin: 0 auto !important;
  }

  .footer-logo img,
  .footer-logo svg {
    margin: 0 auto !important;
    max-width: 120px !important;
  }

  .footer-links {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    gap: 10px !important;
    width: 100% !important;
    text-align: center !important;
  }

  .footer-link {
    min-height: 44px !important;
    display: inline-flex !important;
    align-items: center !important;
    font-size: 14px !important;
  }

  .footer-copyright,
  .copyright {
    text-align: center !important;
    width: 100% !important;
    font-size: 13px !important;
    color: #666 !important;
    margin-top: 8px !important;
  }

  /* --- 11. CONTACT FORM POPUP --- */
  /* Form full width */
  /* Checkboxes easily tappable */
  /* Heading font scales down */
  .contact-wrapper {
    width: 100vw !important;
    max-width: 100vw !important;
    height: 100vh !important;
    inset: 0 !important;
    border-radius: 0 !important;
    padding: 0 !important;
  }

  .contact-form,
  .contact-form_inner,
  .contact-form_block {
    width: 100% !important;
    max-width: 100% !important;
  }

  .form-controls-wrapper {
    padding: 14px 18px !important;
    width: 100% !important;
  }

  .form-inner_wrapper {
    padding: 14px 18px 20px !important;
    width: 100% !important;
  }

  .form-title_wrapper {
    font-size: clamp(30px, 8vw, 42px) !important;
    line-height: 0.95 !important;
    margin-bottom: 12px !important;
  }

  .form-title_wrapper div {
    font-size: clamp(30px, 8vw, 42px) !important;
    line-height: 0.95 !important;
  }

  .form-subtext {
    font-size: 15px !important;
    line-height: 1.4 !important;
    margin-bottom: 16px !important;
  }

  .c-checkbox {
    display: flex !important;
    align-items: center !important;
    min-height: 52px !important;
    padding: 14px 16px !important;
    margin-bottom: 10px !important;
    border-radius: 6px !important;
    width: 100% !important;
    cursor: pointer !important;
  }

  .checkbox-check,
  .c-checkmark {
    width: 22px !important;
    height: 22px !important;
    flex: none !important;
    margin-right: 14px !important;
  }

  .checkbox-label {
    font-size: 15px !important;
    line-height: 1.25 !important;
  }

  .form-button_wrapper {
    padding: 14px 18px !important;
    width: 100% !important;
  }

  .form-button_wrapper .c-button {
    min-height: 48px !important;
    font-size: 22px !important;
  }
}
'''

full_new_css = desktop_part + new_mobile_block
open(css_path, 'w', encoding='utf-8').write(full_new_css)
print("SUCCESS: Full mobile responsive CSS updated in entry.DzM0mqX9.css!")
