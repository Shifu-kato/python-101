<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>The Unseen Studios — Avant-garde & Visionary</title>
  <!-- Google Fonts: elegant serif + modern sans -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 (free icons) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      background-color: #050505;
      font-family: 'Inter', sans-serif;
      color: #eaeaea;
      line-height: 1.4;
      scroll-behavior: smooth;
      overflow-x: hidden;
    }

    /* custom scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0a0a0a;
    }
    ::-webkit-scrollbar-thumb {
      background: #3a3a3a;
      border-radius: 12px;
    }

    /* Typography */
    h1, h2, h3, .logo, .nav-links, .hero-sub {
      font-family: 'Cormorant Garamond', serif;
    }

    h2 {
      font-size: 3rem;
      font-weight: 400;
      letter-spacing: -0.02em;
      margin-bottom: 1rem;
    }

    .section-subhead {
      font-size: 0.85rem;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: #a07c5c;
      margin-bottom: 1rem;
      font-weight: 400;
    }

    /* Container */
    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 40px;
    }

    /* Navigation */
    nav {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      padding: 28px 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      background: rgba(5, 5, 5, 0.75);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.05);
      transition: all 0.2s ease;
    }

    .logo {
      font-size: 1.8rem;
      font-weight: 500;
      letter-spacing: 1px;
      background: linear-gradient(135deg, #f0e6d0, #b89a7a);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }
    .logo span {
      font-weight: 300;
      font-style: italic;
      color: #b89a7a;
      background: none;
      -webkit-background-clip: unset;
      background-clip: unset;
    }

    .nav-links {
      display: flex;
      gap: 42px;
      list-style: none;
    }
    .nav-links a {
      text-decoration: none;
      color: #ddd;
      font-size: 1rem;
      letter-spacing: 1px;
      transition: 0.3s;
      font-weight: 400;
    }
    .nav-links a:hover {
      color: #cb9e72;
    }
    .menu-toggle {
      display: none;
      font-size: 1.8rem;
      cursor: pointer;
    }

    /* Hero Section - full bleed with cinematic overlay */
    .hero {
      height: 100vh;
      width: 100%;
      background: url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1794&auto=format') center/cover no-repeat;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .hero::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 20% 30%, rgba(0,0,0,0.6), rgba(0,0,0,0.85));
    }
    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 880px;
      padding: 0 20px;
    }
    .hero-badge {
      font-family: 'Inter', sans-serif;
      font-size: 0.8rem;
      letter-spacing: 6px;
      text-transform: uppercase;
      color: #cb9e72;
      background: rgba(0,0,0,0.5);
      display: inline-block;
      padding: 6px 16px;
      backdrop-filter: blur(4px);
      border-radius: 40px;
      margin-bottom: 24px;
    }
    .hero h1 {
      font-size: 5rem;
      font-weight: 500;
      line-height: 1.1;
      margin-bottom: 24px;
      color: #fff5ea;
    }
    .hero-sub {
      font-size: 1.2rem;
      font-weight: 300;
      max-width: 600px;
      margin: 0 auto 32px;
      color: #ccc9c2;
    }
    .btn-group {
      display: flex;
      gap: 20px;
      justify-content: center;
    }
    .btn {
      padding: 14px 32px;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 2px;
      font-weight: 500;
      border: none;
      cursor: pointer;
      transition: 0.3s;
      background: none;
      font-family: 'Inter', sans-serif;
    }
    .btn-primary {
      background: #cb9e72;
      color: #0a0a0a;
      border: 1px solid #cb9e72;
    }
    .btn-primary:hover {
      background: transparent;
      color: #cb9e72;
    }
    .btn-outline {
      border: 1px solid rgba(203,158,114,0.7);
      color: #e6d5c0;
      background: transparent;
    }
    .btn-outline:hover {
      background: rgba(203,158,114,0.15);
      border-color: #cb9e72;
    }

    /* Philosophy / Studio tagline */
    .philosophy {
      padding: 120px 0 80px;
      background: #030303;
    }
    .philosophy-grid {
      display: flex;
      gap: 60px;
      align-items: center;
      flex-wrap: wrap;
    }
    .philosophy-text {
      flex: 1.2;
    }
    .philosophy-text p {
      font-size: 1.4rem;
      font-weight: 300;
      line-height: 1.5;
      font-family: 'Cormorant Garamond', serif;
      color: #cfcfcf;
      border-left: 3px solid #cb9e72;
      padding-left: 28px;
    }
    .philosophy-stats {
      flex: 1;
      display: flex;
      gap: 40px;
    }
    .stat {
      text-align: center;
    }
    .stat h3 {
      font-size: 2.8rem;
      font-weight: 300;
      color: #cb9e72;
    }
    .stat p {
      font-size: 0.75rem;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    /* Featured Work - Grid (cinematic cards) */
    .work {
      padding: 100px 0;
      background: #050505;
    }
    .section-title {
      text-align: center;
      margin-bottom: 70px;
    }
    .work-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 40px;
    }
    .work-card {
      position: relative;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.4s cubic-bezier(0.2, 0.9, 0.4, 1.1);
      background: #111;
      border-radius: 4px;
    }
    .work-card:hover {
      transform: translateY(-10px);
    }
    .card-img {
      height: 460px;
      background-size: cover;
      background-position: center;
      transition: transform 0.7s ease;
    }
    .work-card:hover .card-img {
      transform: scale(1.04);
    }
    .card-overlay {
      padding: 24px 20px;
      background: linear-gradient(0deg, #050505 0%, rgba(5,5,5,0.7) 100%);
      transition: all 0.2s;
    }
    .card-overlay h3 {
      font-size: 1.7rem;
      font-weight: 400;
      margin-bottom: 8px;
    }
    .card-overlay p {
      font-size: 0.8rem;
      color: #b4a287;
      letter-spacing: 1px;
    }
    .card-category {
      font-size: 0.7rem;
      text-transform: uppercase;
      color: #cb9e72;
      margin-bottom: 8px;
    }

    /* immersion reel / video-like gallery */
    .showreel {
      background: #0a0a0a;
      padding: 90px 0;
    }
    .reel-container {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 50px;
    }
    .reel-video {
      flex: 1.2;
      background: #1a1a1a;
      box-shadow: 0 25px 40px -12px black;
      aspect-ratio: 16 / 9;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
      color: #cb9e72;
      background-image: url('https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?q=80&w=1674&auto=format');
      background-size: cover;
      background-position: center;
      position: relative;
      cursor: pointer;
      transition: 0.3s;
    }
    .reel-video i {
      background: rgba(0,0,0,0.6);
      padding: 20px;
      border-radius: 100px;
      font-size: 3rem;
      backdrop-filter: blur(8px);
    }
    .reel-text {
      flex: 1;
    }
    .reel-text h3 {
      font-size: 2rem;
      font-weight: 400;
      margin-bottom: 20px;
    }
    .reel-text p {
      color: #aaa;
      line-height: 1.6;
    }

    /* Services / unseen approach */
    .services {
      padding: 100px 0;
      background: #030303;
    }
    .services-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
      margin-top: 40px;
    }
    .service-item {
      text-align: center;
      padding: 40px 20px;
      border: 1px solid rgba(203,158,114,0.2);
      background: rgba(10,10,10,0.6);
      transition: 0.2s;
    }
    .service-item i {
      font-size: 2.8rem;
      color: #cb9e72;
      margin-bottom: 20px;
    }
    .service-item h4 {
      font-size: 1.4rem;
      margin-bottom: 12px;
      font-weight: 400;
    }
    .service-item p {
      font-size: 0.85rem;
      color: #888;
    }

    /* Testimonials / unseen whispers */
    .testimonials {
      padding: 80px 0;
      background: url('https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?q=80&w=2070&auto=format') center/cover fixed;
      position: relative;
    }
    .testimonials::before {
      content: "";
      background: rgba(0,0,0,0.8);
      position: absolute;
      inset: 0;
    }
    .testimonial-inner {
      position: relative;
      z-index: 2;
      text-align: center;
      max-width: 800px;
      margin: 0 auto;
    }
    .quote {
      font-size: 3rem;
      font-family: serif;
      color: #cb9e72;
    }
    .testimonial-text {
      font-size: 1.5rem;
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      line-height: 1.4;
      margin: 20px 0;
    }
    .client {
      letter-spacing: 2px;
      font-size: 0.8rem;
      text-transform: uppercase;
      color: #ccb393;
    }

    /* Footer */
    footer {
      background: #010101;
      padding: 60px 40px 40px;
      border-top: 1px solid rgba(203,158,114,0.2);
    }
    .footer-flex {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 40px;
      margin-bottom: 50px;
    }
    .footer-col p {
      color: #777;
      max-width: 300px;
      margin-top: 12px;
      font-size: 0.85rem;
    }
    .footer-col h4 {
      font-size: 1rem;
      letter-spacing: 2px;
      margin-bottom: 20px;
      color: #cb9e72;
    }
    .footer-col ul {
      list-style: none;
    }
    .footer-col li {
      margin-bottom: 10px;
    }
    .footer-col a {
      text-decoration: none;
      color: #aaa;
      transition: 0.2s;
    }
    .footer-col a:hover {
      color: #cb9e72;
    }
    .social-icons {
      display: flex;
      gap: 20px;
    }
    .social-icons a {
      font-size: 1.4rem;
      color: #ccc;
    }
    .copyright {
      text-align: center;
      font-size: 0.7rem;
      color: #555;
      border-top: 1px solid #131313;
      padding-top: 32px;
    }

    @media (max-width: 980px) {
      .container { padding: 0 24px; }
      nav { padding: 20px 24px; }
      .nav-links { display: none; }
      .menu-toggle { display: block; color: #cb9e72; }
      .hero h1 { font-size: 3rem; }
      .services-grid { grid-template-columns: 1fr; }
      .philosophy-grid { flex-direction: column; }
      .reel-container { flex-direction: column; }
      .work-grid { grid-template-columns: 1fr; }
      .btn-group { flex-direction: column; align-items: center; gap: 16px;}
    }

    /* mobile menu (simple) */
    .nav-links.active {
      display: flex;
      flex-direction: column;
      position: absolute;
      top: 80px;
      left: 0;
      width: 100%;
      background: #050505ee;
      backdrop-filter: blur(20px);
      padding: 32px;
      gap: 24px;
      text-align: center;
      border-bottom: 1px solid #2a2a2a;
    }
    .lightbox {
      display: none;
      position: fixed;
      top:0; left:0; width:100%; height:100%;
      background: rgba(0,0,0,0.95);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      cursor: pointer;
    }
    .lightbox.active {
      display: flex;
    }
    .lightbox img {
      max-width: 85%;
      max-height: 85%;
      border: 1px solid #cb9e72;
      box-shadow: 0 0 30px rgba(0,0,0,0.7);
    }
  </style>
</head>
<body>

<nav>
  <div class="logo">UNSEEN<span> STUDIOS</span></div>
  <div class="menu-toggle" id="menuToggle"><i class="fas fa-bars"></i></div>
  <ul class="nav-links" id="navLinks">
    <li><a href="#home">HOME</a></li>
    <li><a href="#work">WORK</a></li>
    <li><a href="#studio">STUDIO</a></li>
    <li><a href="#services">EXPERTISE</a></li>
    <li><a href="#contact">CONTACT</a></li>
  </ul>
</nav>

<!-- Hero Section -->
<section id="home" class="hero">
  <div class="hero-content">
    <div class="hero-badge">EST. 2019 · LONDON / NYC</div>
    <h1>Vision beyond<br>the visible frame.</h1>
    <div class="hero-sub">Avant-garde creative direction, immersive experiences & cinematic identity for those who defy conventions.</div>
    <div class="btn-group">
      <button class="btn btn-primary" id="exploreBtn">EXPLORE THE UNSEEN</button>
      <button class="btn btn-outline" id="reelBtn">WATCH SHOWREEL</button>
    </div>
  </div>
</section>

<!-- Philosophy -->
<section class="philosophy" id="studio">
  <div class="container philosophy-grid">
    <div class="philosophy-text">
      <div class="section-subhead">MANIFESTO</div>
      <p>“We don’t just create — we unearth the intangible. Blurring the line between art, technology, and raw emotion, The Unseen Studios crafts visual experiences that linger beneath the skin.”</p>
    </div>
    <div class="philosophy-stats">
      <div class="stat"><h3>15+</h3><p>AWARDS</p></div>
      <div class="stat"><h3>8Y</h3><p>OF BOUNDLESS WORK</p></div>
      <div class="stat"><h3>120+</h3><p>PROJECTS</p></div>
    </div>
  </div>
</section>

<!-- Featured Work -->
<section id="work" class="work">
  <div class="container">
    <div class="section-title">
      <div class="section-subhead">CURATED PORTFOLIO</div>
      <h2>Fragments of the unseen</h2>
    </div>
    <div class="work-grid" id="workGrid">
      <!-- project 1 -->
      <div class="work-card" data-img="https://images.unsplash.com/photo-1543158266-0066955047b1?q=80&w=1887&auto=format">
        <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1543158266-0066955047b1?q=80&w=1887&auto=format');"></div>
        <div class="card-overlay">
          <div class="card-category">Fashion Film</div>
          <h3>ÆTHERIAL</h3>
          <p>AWARD-WINNING CAMPAIGN · GUCCI</p>
        </div>
      </div>
      <!-- project 2 -->
      <div class="work-card" data-img="https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?q=80&w=1969&auto=format">
        <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?q=80&w=1969&auto=format');"></div>
        <div class="card-overlay">
          <div class="card-category">Digital Installation</div>
          <h3>METAMORPH</h3>
          <p>AI-GENERATED SCULPTURE · MOMA</p>
        </div>
      </div>
      <!-- project 3 -->
      <div class="work-card" data-img="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=1974&auto=format">
        <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=1974&auto=format');"></div>
        <div class="card-overlay">
          <div class="card-category">Music Video</div>
          <h3>ECHOES IN VOID</h3>
          <p>DIRECTED BY R. SINCLAIR</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Showreel / Immersive -->
<section class="showreel" id="reel">
  <div class="container reel-container">
    <div class="reel-video" id="reelTrigger">
      <i class="fas fa-play"></i>
    </div>
    <div class="reel-text">
      <div class="section-subhead">CINEMATIC REEL</div>
      <h3>Where shadows meet brilliance.</h3>
      <p>An anthology of our most evocative work — from high-fashion editorials to interactive new media. The unseen force behind culture-defining visuals. <br><br> <strong>Click to play the immersive showreel (conceptual)</strong></p>
    </div>
  </div>
</section>

<!-- Services / Expertise -->
<section id="services" class="services">
  <div class="container">
    <div class="section-title">
      <div class="section-subhead">EXPERTISE</div>
      <h2>What we unveil</h2>
    </div>
    <div class="services-grid">
      <div class="service-item"><i class="fas fa-video"></i><h4>Cinematography</h4><p>Narrative-driven visual poetry & high-end production.</p></div>
      <div class="service-item"><i class="fas fa-cube"></i><h4>3D & Virtual Prod.</h4><p>Unreal Engine, volumetric capture & CGI worlds.</p></div>
      <div class="service-item"><i class="fas fa-palette"></i><h4>Creative Direction</h4><p>Brand identity, art direction & innovative campaigns.</p></div>
      <div class="service-item"><i class="fas fa-vr-cardboard"></i><h4>Immersive Experience</h4><p>XR installations, projection mapping & sensory design.</p></div>
      <div class="service-item"><i class="fas fa-music"></i><h4>Sound Design</h4><p>Atmosphonic scoring & spatial audio.</p></div>
      <div class="service-item"><i class="fas fa-photo-video"></i><h4>Post-Mystery Lab</h4><p>Color grading, VFX & AI-driven post-production.</p></div>
    </div>
  </div>
</section>

<!-- Testimonials -->
<section class="testimonials">
  <div class="testimonial-inner">
    <i class="fas fa-quote-right quote"></i>
    <div class="testimonial-text">“The Unseen Studios doesn't just deliver work — they orchestrate emotion. Each frame feels like a living painting, provocative and timeless.”</div>
    <div class="client">— ELENA V. , CREATIVE DIRECTOR · VISIONAIRE</div>
  </div>
</section>

<!-- Footer + Contact -->
<footer id="contact">
  <div class="container">
    <div class="footer-flex">
      <div class="footer-col">
        <h3 style="font-size: 1.8rem; font-weight:400;">UNSEEN<span style="color:#cb9e72;"> STUDIOS</span></h3>
        <p>Awakening the intangible. Based in London & New York, operating globally.</p>
      </div>
      <div class="footer-col">
        <h4>STUDIO</h4>
        <ul>
          <li><a href="#">hello@unseenstudios.com</a></li>
          <li><a href="#">+44 (0)20 7946 0138</a></li>
          <li><a href="#">86 Shoreditch High St, London</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>FOLLOW THE UNSEEN</h4>
        <div class="social-icons">
          <a href="#"><i class="fab fa-instagram"></i></a>
          <a href="#"><i class="fab fa-vimeo-v"></i></a>
          <a href="#"><i class="fab fa-behance"></i></a>
          <a href="#"><i class="fab fa-x-twitter"></i></a>
        </div>
      </div>
    </div>
    <div class="copyright">
      <p>© 2026 THE UNSEEN STUDIOS — All rights reserved. Visionary narratives.</p>
    </div>
  </div>
</footer>

<!-- lightbox for images -->
<div id="lightbox" class="lightbox">
  <img id="lightboxImg" src="" alt="expanded view">
</div>

<script>
  // mobile menu toggle
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
  // close mobile menu after clicking link 
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  // lightbox for work images
  const workCards = document.querySelectorAll('.work-card');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  workCards.forEach(card => {
    card.addEventListener('click', (e) => {
      e.stopPropagation();
      const imgUrl = card.getAttribute('data-img') || card.querySelector('.card-img')?.style.backgroundImage.match(/url\(["']?(.*?)["']?\)/)?.[1];
      if (imgUrl) {
        lightboxImg.src = imgUrl;
        lightbox.classList.add('active');
      }
    });
  });
  lightbox.addEventListener('click', () => {
    lightbox.classList.remove('active');
  });

  // showreel / simulation - alert after play icon click 
  const reelTrigger = document.getElementById('reelTrigger');
  const reelBtn = document.getElementById('reelBtn');
  function showReelMessage() {
    alert("▶️ SHOWREEL // 'UNSEEN: FRAGMENTS' — a cinematic journey through our latest audiovisual works. (Full version available upon private request)");
  }
  if(reelTrigger) reelTrigger.addEventListener('click', showReelMessage);
  if(reelBtn) reelBtn.addEventListener('click', showReelMessage);

  // explore button -> smooth scroll to work section
  const exploreBtn = document.getElementById('exploreBtn');
  if(exploreBtn) {
    exploreBtn.addEventListener('click', () => {
      document.getElementById('work').scrollIntoView({ behavior: 'smooth' });
    });
  }

  // Nav link smooth scrolling
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      if(targetId && targetId !== "#") {
        const targetElement = document.querySelector(targetId);
        if(targetElement) targetElement.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
</script>
</body>
</html>
