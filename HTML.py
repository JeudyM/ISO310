<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hospital Salud y Vida</title>
  <!-- Icons CDN (Font Awesome) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <style>
    :root {
      --primary: #1565c0;
      --primary-dark: #0d47a1;
      --accent: #00bcd4;
      --white: #fff;
      --gray-bg: #f7faff;
      --shadow: 0 4px 24px rgba(21,101,192,0.09);
      --text-main: #1a237e;
      --card-gradient: linear-gradient(135deg, #e3f0ff 60%, #b3e5fc 100%);
    }
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
      background: var(--gray-bg);
      min-height: 100vh;
    }
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      color: var(--text-main);
      min-height: 100vh;
      margin: 0;
      background: var(--gray-bg);
      overflow-x: hidden;
      position: relative;
    }
    .hidden { display: none !important; }

    /* PARTICLES BACKGROUND */
    #bgParticles {
      position: fixed;
      top:0; left:0; width:100vw; height:100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.22;
    }

    /* LOGIN SLIDESHOW FONDO */
    #loginScreen {
      position: fixed;
      z-index: 50;
      top: 0; left: 0; width: 100vw; height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: none;
      transition: background 0.5s;
      overflow: hidden;
    }
    .bg-slideshow {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      z-index: 1;
      overflow: hidden;
      pointer-events: none;
    }
    .bg-slide {
      position: absolute;
      top: 0; left: 0; width: 100vw; height: 100vh;
      object-fit: cover;
      opacity: 0;
      transition: opacity 1s;
      filter: brightness(0.6) blur(1px);
    }
    .bg-slide.active { opacity: 1; z-index: 2; }
    .login-container {
      position: relative;
      z-index: 3;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      width: 100vw;
      animation: fadeInBox .9s cubic-bezier(.68,-0.55,.27,1.55);
    }
    .login-box {
      background: rgba(255,255,255, 0.98);
      border-radius: 20px;
      box-shadow: 0 10px 40px rgba(21,101,192,0.17);
      padding: 40px 34px 34px 34px;
      min-width: 340px;
      max-width: 95vw;
      border: 1.5px solid #e3eaff;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      backdrop-filter: blur(1.5px);
      position: relative;
      overflow: hidden;
    }
    .login-box::before {
      content:"";
      position:absolute;
      left:0;top:0;right:0;bottom:0;
      background: radial-gradient(circle at 85% 5%, #b3e5fc55 0px, transparent 220px),
                  radial-gradient(circle at 10% 90%, #1565c022 0px, transparent 180px);
      z-index: 0;
      pointer-events: none;
    }
    @keyframes fadeInBox {
      from { opacity: 0; transform: scale(.9);}
      to { opacity: 1; transform: scale(1);}
    }
    .login-logo {
      font-size: 2.2em;
      font-weight: bold;
      color: #1565c0;
      margin-bottom: 20px;
      letter-spacing: 1px;
      display: flex;
      align-items: center;
      gap: 12px;
      justify-content: center;
      text-shadow: 0 2px 12px #1565c020;
      z-index: 1;
    }
    .login-logo .pulse {
      animation: pulseHeart 1.5s infinite;
      color: #ff1744;
    }
    @keyframes pulseHeart {
      0%,100% { transform: scale(1);}
      50% { transform: scale(1.15);}
    }
    .login-tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 30px;
      justify-content: center;
      z-index: 1;
    }
    .login-tabs button {
      background: #e3eaff;
      color: #0d47a1;
      padding: 8px 36px;
      border: none;
      border-radius: 8px 8px 0 0;
      cursor: pointer;
      font-weight: bold;
      font-size: 1.07em;
      transition: background .2s, color .2s;
      z-index: 1;
    }
    .login-tabs .active {
      background: #1565c0;
      color: #fff;
      box-shadow: 0px 2px 8px #1565c020;
    }
    .login-form, .register-form {
      display: flex;
      flex-direction: column;
      width: 100%;
      max-width: 330px;
      text-align: left;
      margin: 0 auto;
      z-index: 1;
    }
    label {
      font-weight: 500;
      margin-bottom: 5px;
      color: #375da6;
    }
    input {
      width: 100%;
      padding: 11px;
      margin-bottom: 16px;
      border-radius: 5px;
      border: 1.3px solid #b3cfff;
      font-size: 1em;
      background: #f7faff;
      color: #003366;
      transition: border .2s, box-shadow .2s;
      outline: none;
    }
    input:focus {
      border: 1.5px solid #1565c0;
      box-shadow: 0 0 0 2px #1565c055;
    }
    button[type="submit"] {
      background: linear-gradient(90deg, #1565c0, #00bcd4 82%);
      color: #fff;
      padding: 13px 0;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 1.09em;
      font-weight: bold;
      margin-top: 12px;
      box-shadow: 0 2px 8px #1565c022;
      transition: background .2s, transform .19s;
    }
    button[type="submit"]:hover {
      background: linear-gradient(90deg, #0d47a1, #1565c0 82%);
      transform: scale(1.04);
    }
    .login-message {
      min-height: 28px;
      font-size: 1.01em;
      margin-top: 8px;
      font-weight: 500;
      text-align: center;
      transition: color .3s;
    }
    .forgot-link {
      color: #1565c0;
      text-decoration: none;
      font-size: 0.98em;
      float: right;
      margin: -10px 0 18px 0;
      transition: color .2s;
    }
    .forgot-link:hover {
      color: #0d47a1;
      text-decoration: underline;
    }
    /* HEADER CON SLIDESHOW DE FONDO */
    header {
      color: var(--white);
      padding: 0;
      text-align: center;
      border-radius: 0 0 18px 18px;
      box-shadow: var(--shadow);
      position: relative;
      z-index: 2;
      overflow: hidden;
      min-height: 210px;
      background: var(--primary);
    }
    .header-bg-hospital {
      width: 100%;
      height: 210px;
      object-fit: cover;
      display: block;
      filter: brightness(0.60) blur(0.5px);
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
      border-radius: 0 0 18px 18px;
      pointer-events: none;
      user-select: none;
      opacity: 0;
      transition: opacity 1s;
    }
    .header-bg-hospital.active {
      opacity: 1;
      z-index: 2;
    }
    .header-content {
      position: relative;
      z-index: 3;
      padding: 36px 0 14px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
      min-height: 210px;
    }
    .header-title {
      font-size: 2.3em;
      font-weight: bold;
      color: #fff;
      text-shadow: 0 2px 8px rgba(21,101,192,0.34),0 1px 0 #144c96;
      margin: 0 0 12px 0;
      display: flex;
      align-items: center;
      gap: 14px;
      background: rgba(21,101,192,0.14);
      border-radius: 18px 18px 12px 12px;
      padding: 10px 25px 6px 25px;
      box-shadow: 0 2px 5px #1565c015;
      animation: fadeInBox .7s;
    }
    nav ul {
      list-style: none;
      padding: 0;
      margin: 0 0 0 0;
      display: flex;
      justify-content: center;
      gap: 32px;
      flex-wrap: wrap;
      position: relative;
      z-index: 3;
      background: rgba(21,101,192,0.82);
      border-radius: 0 0 14px 14px;
    }
    nav a, .btn-nav {
      color: var(--white);
      text-decoration: none;
      font-weight: bold;
      background: none;
      border: none;
      cursor: pointer;
      font-size: 1em;
      padding: 8px 14px;
      border-radius: 4px;
      transition: background .2s, transform .15s;
    }
    nav a:hover, .btn-nav:hover {
      background: var(--primary-dark);
      color: #fff;
      transform: scale(1.06);
    }
    main {
      padding: 24px;
      max-width: 1100px;
      margin: auto;
      position: relative;
      z-index: 1;
    }
    section {
      margin-bottom: 38px;
      background: var(--white);
      border: 1.5px solid #e3eaff;
      padding: 32px 20px;
      border-radius: 16px;
      box-shadow: 0 4px 32px #1565c012;
      animation: fadein 0.9s;
      position: relative;
      transition: background .4s, border .4s;
    }
    .icon-section {
      font-size: 2.2em;
      color: var(--primary-dark);
      margin-bottom: 14px;
      text-align: center;
      animation: bounceIn .8s;
    }
    @keyframes bounceIn {
      0% { transform: scale(.5);}
      60% { transform: scale(1.15);}
      100% { transform: scale(1);}
    }
    .hero-img {
      width: 100%;
      max-width: 590px;
      margin: 20px auto 0 auto;
      border-radius: 12px;
      box-shadow: var(--shadow);
      border: 2px solid #e3eaff;
      background: var(--white);
      display: block;
      transition: box-shadow .18s, transform .15s;
      animation: fadeInBox .7s;
    }
    .hero-img:hover {
      box-shadow: 0 10px 36px #1565c033;
      transform: scale(1.015) rotate(-1deg);
    }
    .info-cards {
      display: flex;
      flex-wrap: wrap;
      gap: 22px;
      justify-content: space-between;
      margin-top: 22px;
    }
    .info-card {
      flex: 1 1 230px;
      background: var(--card-gradient);
      border: 1.2px solid #e3eaff;
      border-radius: 12px;
      box-shadow: 0 2px 10px #1565c00c;
      padding: 18px 18px 12px 18px;
      margin-bottom: 10px;
      min-width: 200px;
      margin-right: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: transform .22s, box-shadow .18s, background .3s;
      position: relative;
      overflow: hidden;
    }
    .info-card:last-child { margin-right: 0; }
    .info-card .fa-solid, .info-card .fa-regular, .info-card .fa-brands {
      color: var(--primary-dark);
      font-size: 2.1em;
      margin-bottom: 8px;
      filter: drop-shadow(0 1px 1px #b3e5fc);
      animation: pulseCard 1.6s infinite alternate;
    }
    @keyframes pulseCard {
      0% { filter: drop-shadow(0 0px 0px #b3e5fc);}
      100% { filter: drop-shadow(0 3px 7px #00bcd4aa);}
    }
    .info-card-title {
      font-weight: bold;
      margin-bottom: 6px;
      color: var(--primary);
      font-size: 1.08em;
      text-align: center;
    }
    .servicios-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 22px;
      margin-top: 22px;
    }
    .card {
      background: var(--card-gradient);
      color: var(--primary-dark);
      padding: 18px 10px;
      border-radius: 14px;
      text-align: center;
      font-size: 1.12em;
      font-weight: 500;
      border: 1.2px solid #e3eaff;
      box-shadow: 0 2px 10px #1565c00f;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      justify-content: center;
      position: relative;
      z-index: 1;
      overflow: hidden;
      transition: transform .22s, box-shadow .15s, background .3s;
      animation: fadeInBox .5s;
    }
    .card::before {
      content: "";
      position: absolute;
      top: -25px; right: -25px;
      width: 60px; height: 60px;
      background: radial-gradient(circle, #b3e5fc80 0%, transparent 70%);
      border-radius: 50%;
      z-index: 0;
      pointer-events: none;
      transition: opacity .2s;
      opacity: .7;
    }
    .card i { font-size: 1.25em; color: var(--primary); z-index: 1;}
    .card:hover, .card:focus-visible {
      background: linear-gradient(135deg, #e3f0ff 80%, #00bcd4 120%);
      transform: translateY(-6px) scale(1.05);
      box-shadow: 0 8px 22px #1565c033;
      z-index: 10;
    }
    .card:active {
      transform: scale(0.97);
    }
    .service-info-modal {
      display: none;
      position: fixed;
      z-index: 1000;
      left: 0; top: 0; width: 100vw; height: 100vh;
      background: rgba(0,0,0,0.34);
      align-items: center;
      justify-content: center;
      animation: fadein .19s;
    }
    .service-info-modal.active {
      display: flex;
    }
    .service-info-content {
      background: #fff;
      border-radius: 16px;
      padding: 38px 30px 28px 30px;
      max-width: 350px;
      box-shadow: 0 6px 32px #1565c027;
      text-align: center;
      position: relative;
      animation: fadeInBox .4s;
      border-top: 4px solid var(--accent);
    }
    .service-info-title {
      font-size: 1.32em;
      font-weight: bold;
      color: #1565c0;
      margin-bottom: 9px;
      display: flex;
      align-items: center;
      gap: 9px;
      justify-content: center;
    }
    .service-info-title i { color: var(--accent);}
    .service-info-text {
      color: #25487e;
      margin-bottom: 16px;
    }
    .close-modal-btn {
      position: absolute;
      top: 11px; right: 13px;
      background: none;
      border: none;
      font-size: 1.2em;
      color: #0d47a1;
      cursor: pointer;
      transition: color .22s;
    }
    .close-modal-btn:hover { color: #e53935; }
    /* Glow highlight for modal */
    .service-info-content::after {
      content: "";
      display:block;
      position: absolute;
      pointer-events: none;
      left: 0; right:0; bottom:0;
      height: 16px;
      background: linear-gradient(90deg, #b3e5fc00, #00bcd4aa 60%, #b3e5fc00 100%);
      border-radius: 0 0 14px 14px;
      opacity: .44;
    }
    /* Equipo médico embellecedor */
    .team-card {
      background: var(--card-gradient);
      border: 1.2px solid #e3eaff;
      border-radius: 14px;
      box-shadow: 0 2px 10px #1565c00e;
      padding: 18px 14px 14px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: box-shadow .19s, transform .15s;
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .team-card:hover {
      box-shadow: 0 8px 26px #1565c044;
      transform: translateY(-5px) scale(1.03);
    }
    .team-card::before {
      content: "";
      position: absolute;
      top: -20px; left: -20px;
      width: 50px; height: 50px;
      background: radial-gradient(circle, #00bcd4 0%, transparent 70%);
      border-radius: 50%;
      z-index: 0;
      opacity: .15;
      pointer-events: none;
      transition: opacity .2s;
    }
    .team-icon {
      font-size: 2.7em;
      margin-bottom: 7px;
      color: var(--primary-dark);
      filter: drop-shadow(0 1px 2px #00bcd4);
    }
    .team-name {
      font-weight: bold;
      font-size: 1.12em;
      margin-bottom: 2px;
      color: var(--primary);
    }
    .team-id {
      font-size: 0.97em;
      color: #375da6;
    }
    form label {
      display: block;
      margin-top: 10px;
    }
    form input, form textarea {
      width: 100%;
      padding: 9px;
      margin-top: 5px;
      margin-bottom: 15px;
      border-radius: 4px;
      border: 1px solid #b3cfff;
      font-size: 1em;
      background: #f7faff;
      color: #003366;
    }
    form input:focus, form textarea:focus {
      border: 1.5px solid var(--primary);
      background: #e3f0ff;
    }
    form button {
      background: var(--primary);
      color: var(--white);
      padding: 10px 0;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1.06em;
      font-weight: bold;
      margin-top: 6px;
      box-shadow: 0 2px 8px #1565c012;
      transition: background .2s;
    }
    form button:hover {
      background: var(--primary-dark);
    }
    #respuesta {
      color: var(--primary-dark);
      margin-top: 10px;
      font-size: 1.05em;
      min-height: 22px;
      transition: color .3s;
    }
    footer {
      background: #e3f0ff;
      color: #0d47a1;
      text-align: center;
      padding: 16px 0;
      margin-top: 32px;
      border-radius: 12px 12px 0 0;
      border: 1.5px solid #e3eaff;
      box-shadow: 0 2px 14px #1565c008;
      position: relative;
      overflow: hidden;
    }
    footer::before {
      content: "";
      position: absolute;
      left: 50%; top:0;
      transform: translateX(-50%);
      width: 80vw; height: 50px;
      background: radial-gradient(circle, #00bcd4 0%, transparent 70%);
      opacity: .13;
      z-index: 0;
      pointer-events: none;
      border-radius: 0 0 90px 90px;
    }
    @media (max-width: 900px) {
      .info-cards { flex-direction: column; gap: 12px;}
      .info-card { margin-right: 0; min-width: 0;}
    }
    @media (max-width: 650px) {
      .servicios-grid { grid-template-columns: 1fr; }
      .hero-img { max-width: 100%; }
      main { padding: 7px; }
      section { padding: 14px 3px;}
      .login-box { padding: 14px 6px 14px 6px; min-width: 0;}
      .bg-slide, .header-bg-hospital { height: 140px; }
      .header-content {min-height: 90px;}
      .header-title { font-size: 1.1em;}
      .service-info-modal .service-info-content { padding: 18px 4vw 18px 4vw; }
    }
    @keyframes fadein {
      from { opacity: 0; transform: translateY(28px);}
      to { opacity: 1; transform: none;}
    }
  </style>
</head>
<body>
  <canvas id="bgParticles"></canvas>
  <!-- Pantalla de login/register nueva y dinámica -->
  <div id="loginScreen">
    <div class="bg-slideshow">
      <img class="bg-slide active" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" alt="Hospital 1">
      <img class="bg-slide" src="https://images.unsplash.com/photo-1460672985063-6764ac8b9c74?auto=format&fit=crop&w=1200&q=80" alt="Hospital 2">
      <img class="bg-slide" src="https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=1200&q=80" alt="Personal médico">
      <img class="bg-slide" src="https://images.unsplash.com/photo-1519494080410-f9aa8f52f234?auto=format&fit=crop&w=1200&q=80" alt="Sala hospital">
    </div>
    <div class="login-container">
      <div class="login-box">
        <div class="login-logo">
          <i class="fa-solid fa-heart-pulse pulse"></i>
          Salud y Vida
        </div>
        <div class="login-tabs">
          <button id="loginTab" class="active">Iniciar Sesión</button>
          <button id="registerTab">Registrarse</button>
        </div>
        <form id="loginForm" class="login-form">
          <label for="loginEmail">Correo electrónico</label>
          <input type="email" id="loginEmail" required autocomplete="email" placeholder="tucorreo@ejemplo.com">
          <label for="loginPassword">Contraseña</label>
          <input type="password" id="loginPassword" required autocomplete="current-password" placeholder="********">
          <a class="forgot-link" href="#">¿Olvidaste tu contraseña?</a>
          <button type="submit">Entrar</button>
          <div class="login-message" id="loginMsg"></div>
        </form>
        <form id="registerForm" class="register-form" style="display:none;">
          <label for="regName">Nombre completo</label>
          <input type="text" id="regName" required autocomplete="name" placeholder="Tu nombre completo">
          <label for="regEmail">Correo electrónico</label>
          <input type="email" id="regEmail" required autocomplete="email" placeholder="tucorreo@ejemplo.com">
          <label for="regPassword">Contraseña</label>
          <input type="password" id="regPassword" required autocomplete="new-password" placeholder="Crea una contraseña">
          <button type="submit">Crear cuenta</button>
          <div class="login-message" id="registerMsg"></div>
        </form>
      </div>
    </div>
  </div>
  <!-- Modal para mostrar información de servicios -->
  <div id="serviceInfoModal" class="service-info-modal">
    <div class="service-info-content">
      <button class="close-modal-btn" id="closeServiceInfo" title="Cerrar"><i class="fa fa-times"></i></button>
      <div class="service-info-title" id="serviceInfoTitle"></div>
      <div class="service-info-text" id="serviceInfoText"></div>
    </div>
  </div>
  <!-- Contenido principal (se oculta hasta login) -->
  <div id="mainContent" class="hidden">
    <header>
      <img class="header-bg-hospital active" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" alt="Hospital fondo 1">
      <img class="header-bg-hospital" src="https://images.unsplash.com/photo-1460672985063-6764ac8b9c74?auto=format&fit=crop&w=1200&q=80" alt="Hospital fondo 2">
      <img class="header-bg-hospital" src="https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=1200&q=80" alt="Personal médico trabajando">
      <img class="header-bg-hospital" src="https://images.unsplash.com/photo-1519494080410-f9aa8f52f234?auto=format&fit=crop&w=1200&q=80" alt="Sala de hospital">
      <div class="header-content">
        <div class="header-title">
          <i class="fa-solid fa-hospital-symbol"></i> Hospital Salud y Vida
        </div>
      </div>
      <nav>
        <ul>
          <li><a href="#inicio" class="nav-link">Inicio</a></li>
          <li><a href="#nosotros" class="nav-link">Acerca de</a></li>
          <li><a href="#servicios" class="nav-link">Servicios</a></li>
          <li><a href="#equipo" class="nav-link">Equipo Médico</a></li>
          <li><a href="#contacto" class="nav-link">Contacto</a></li>
          <li><button id="logoutBtn" class="btn-nav"><i class="fa-solid fa-right-from-bracket"></i> Cerrar Sesión</button></li>
        </ul>
      </nav>
    </header>
    <main>
      <section id="inicio" class="slide-in">
        <div class="icon-section"><i class="fa-solid fa-heart-pulse"></i></div>
        <h2>Bienvenidos a Hospital Salud y Vida</h2>
        <p>Tu salud, nuestra prioridad. Ofrecemos atención médica de calidad para ti y tu familia.</p>
        <img src="https://images.unsplash.com/photo-1504439468489-c8920d796a29?auto=format&fit=crop&w=800&q=80" alt="Fachada de hospital moderno" class="hero-img">
        <div class="info-cards">
          <div class="info-card">
            <i class="fa-solid fa-calendar-check"></i>
            <div class="info-card-title">Agenda tu cita</div>
            <div>Solicita tu cita médica desde nuestra página web o al teléfono <b>+1 (829) 973-6716</b>.</div>
          </div>
          <div class="info-card">
            <i class="fa-solid fa-users"></i>
            <div class="info-card-title">Atención personalizada</div>
            <div>Nuestro equipo está dedicado a brindarte la mejor experiencia, con trato humano y profesional.</div>
          </div>
          <div class="info-card">
            <i class="fa-solid fa-clock"></i>
            <div class="info-card-title">Horario</div>
            <div>Lunes a Domingo, 24 horas. Emergencias siempre disponibles.</div>
          </div>
        </div>
      </section>
      <section id="nosotros" class="fade-in">
        <div class="icon-section"><i class="fa-solid fa-building"></i></div>
        <h2>Acerca de Nosotros</h2>
        <p>
          <b>Hospital Salud y Vida</b> es una institución líder con más de 20 años de experiencia, comprometida con la salud y el bienestar de nuestra comunidad. 
          Contamos con tecnología de punta, instalaciones modernas y un equipo multidisciplinario de profesionales.<br><br>
          <b>Misión:</b> Proveer atención médica integral, humana y de calidad.<br>
          <b>Visión:</b> Ser el hospital de referencia en innovación y excelencia clínica.<br>
          <b>Valores:</b> Ética, respeto, compromiso y profesionalismo.
        </p>
        <div class="info-cards">
          <div class="info-card">
            <i class="fa-solid fa-stethoscope"></i>
            <div class="info-card-title">Especialidades</div>
            <div>Cardiología, pediatría, traumatología, ginecología, medicina general y más.</div>
          </div>
          <div class="info-card">
            <i class="fa-solid fa-award"></i>
            <div class="info-card-title">Reconocimientos</div>
            <div>Acreditados por <b>Salud MX</b> y premiados por excelencia clínica.</div>
          </div>
        </div>
      </section>
      <section id="servicios" class="fade-in">
        <div class="icon-section"><i class="fa-solid fa-briefcase-medical"></i></div>
        <h2>Nuestros Servicios</h2>
        <div class="servicios-grid" id="serviciosGrid">
          <div class="card" data-serv="urgencias"><i class="fa-solid fa-truck-medical"></i>Urgencias 24/7</div>
          <div class="card" data-serv="consultas"><i class="fa-solid fa-user-doctor"></i>Consultas generales y especializadas</div>
          <div class="card" data-serv="laboratorio"><i class="fa-solid fa-vials"></i>Laboratorio clínico</div>
          <div class="card" data-serv="imagen"><i class="fa-solid fa-x-ray"></i>Rayos X y ultrasonido</div>
          <div class="card" data-serv="cirugia"><i class="fa-solid fa-scalpel-line"></i>Cirugías</div>
          <div class="card" data-serv="hospitalizacion"><i class="fa-solid fa-bed-pulse"></i>Hospitalización</div>
          <div class="card" data-serv="cardiologia"><i class="fa-solid fa-heart-circle-plus"></i>Cardiología</div>
          <div class="card" data-serv="pediatria"><i class="fa-solid fa-baby"></i>Pediatría</div>
        </div>
      </section>
      <section id="equipo" class="fade-in">
        <div class="icon-section"><i class="fa-solid fa-user-nurse"></i></div>
        <h2>Equipo Médico</h2>
        <div class="team-grid">
          <div class="team-card">
            <div class="team-icon"><i class="fa-solid fa-user-doctor"></i></div>
            <div class="team-name">Jesús García</div>
            <div class="team-id">A00118637</div>
          </div>
          <div class="team-card">
            <div class="team-icon"><i class="fa-solid fa-user-doctor"></i></div>
            <div class="team-name">Yeremi Javier</div>
            <div class="team-id">A00119038</div>
          </div>
          <div class="team-card">
            <div class="team-icon"><i class="fa-solid fa-user-doctor"></i></div>
            <div class="team-name">Jhosua Encarnacion Castro</div>
            <div class="team-id">A00118649</div>
          </div>
          <div class="team-card">
            <div class="team-icon"><i class="fa-solid fa-user-doctor"></i></div>
            <div class="team-name">Peniel</div>
            <div class="team-id">A00119230</div>
          </div>
          <div class="team-card">
            <div class="team-icon"><i class="fa-solid fa-user-doctor"></i></div>
            <div class="team-name">Jeudy</div>
            <div class="team-id">A00113445</div>
          </div>
        </div>
      </section>
      <section id="contacto" class="fade-in">
        <div class="icon-section"><i class="fa-solid fa-envelope"></i></div>
        <h2>Contacto</h2>
        <form id="contactForm" autocomplete="off">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" required>
          <label for="email">Email:</label>
          <input type="email" id="email" required>
          <label for="mensaje">Mensaje:</label>
          <textarea id="mensaje" rows="4" required></textarea>
          <button type="submit">Enviar</button>
        </form>
        <div id="respuesta"></div>
        <div class="info-cards" style="margin-top:20px;">
          <div class="info-card">
            <i class="fa-solid fa-phone"></i>
            <div class="info-card-title">Teléfono</div>
            <div>+1 (829) 973-6716</div>
          </div>
          <div class="info-card">
            <i class="fa-solid fa-location-dot"></i>
            <div class="info-card-title">Dirección</div>
            <div>Av. Salud y Vida #123, Ciudad Esperanza, México</div>
          </div>
          <div class="info-card">
            <i class="fa-brands fa-facebook"></i>
            <div class="info-card-title">Redes Sociales</div>
            <div>
              <a href="#" style="color:#1877f3;text-decoration:none;font-size:1.1em;">
                <i class="fa-brands fa-facebook"></i> Peniel de jesus
              </a><br>
              <a href="#" style="color:#1da1f2;text-decoration:none;font-size:1.1em;">
                <i class="fa-brands fa-x-twitter"></i> hospital5
              </a><br>
              <a href="#" style="color:#1877f3;text-decoration:none;font-size:1.1em;">
                <i class="fa-brands fa-instagram"></i> @penieldejesuss
              </a>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer>
      <p>&copy; 2025 Hospital Salud y Vida. Todos los derechos reservados.</p>
    </footer>
  </div>
  <script>
    // PARTICLES BACKGROUND EFFECT
    (function(){
      const canvas = document.getElementById('bgParticles');
      const ctx = canvas.getContext('2d');
      let w = window.innerWidth, h = window.innerHeight;
      let particles = [];
      function resize() {
        w = window.innerWidth; h = window.innerHeight;
        canvas.width = w; canvas.height = h;
      }
      window.addEventListener('resize', resize);
      resize();
      for(let i=0;i<26;i++){
        particles.push({
          x: Math.random()*w,
          y: Math.random()*h,
          r: Math.random()*2.5+1.3,
          dx: (Math.random()-.5)*0.5,
          dy: Math.random()*0.2+0.08,
          color: `rgba(0,188,212,${Math.random()*0.5+0.2})`
        });
      }
      function draw(){
        ctx.clearRect(0,0,w,h);
        for(let p of particles){
          ctx.beginPath();
          ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
          ctx.fillStyle = p.color;
          ctx.shadowColor = "#00bcd4";
          ctx.shadowBlur = 7;
          ctx.fill();
          ctx.shadowBlur = 0;
          p.x += p.dx; p.y += p.dy;
          if(p.x<0||p.x>w) p.x=Math.random()*w;
          if(p.y>h) p.y=0;
        }
        requestAnimationFrame(draw);
      }
      draw();
    })();

    // LOGIN SLIDESHOW FONDO
    (function(){
      const slides = document.querySelectorAll('.bg-slide');
      let idx = 0;
      setInterval(() => {
        slides[idx].classList.remove('active');
        idx = (idx + 1) % slides.length;
        slides[idx].classList.add('active');
      }, 3000);
    })();

    // HEADER SLIDESHOW (después del login)
    (function(){
      const slides = document.querySelectorAll('.header-bg-hospital');
      if (!slides.length) return;
      let idx = 0;
      setInterval(() => {
        slides[idx].classList.remove('active');
        idx = (idx + 1) % slides.length;
        slides[idx].classList.add('active');
      }, 3000);
    })();

    // LOGIN/REGISTER LOGIC
    const STORAGE_KEY = "usuarios_hospital";
    const loginTab = document.getElementById('loginTab');
    const registerTab = document.getElementById('registerTab');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginMsg = document.getElementById('loginMsg');
    const registerMsg = document.getElementById('registerMsg');
    loginTab.onclick = () => {
      loginTab.classList.add('active');
      registerTab.classList.remove('active');
      loginForm.style.display = "";
      registerForm.style.display = "none";
      loginMsg.textContent = '';
      registerMsg.textContent = '';
    }
    registerTab.onclick = () => {
      loginTab.classList.remove('active');
      registerTab.classList.add('active');
      loginForm.style.display = "none";
      registerForm.style.display = "";
      loginMsg.textContent = '';
      registerMsg.textContent = '';
    }
    // Register
    registerForm.onsubmit = function(e) {
      e.preventDefault();
      const name = document.getElementById('regName').value.trim();
      const email = document.getElementById('regEmail').value.trim().toLowerCase();
      const pass = document.getElementById('regPassword').value;
      let usuarios = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      if (usuarios.find(u => u.email === email)) {
        registerMsg.textContent = "Ese correo ya está registrado.";
        registerMsg.style.color = "#e53935";
        return;
      }
      usuarios.push({ name, email, pass });
      localStorage.setItem(STORAGE_KEY, JSON.stringify(usuarios));
      registerMsg.textContent = "Registro exitoso. Ahora puedes iniciar sesión.";
      registerMsg.style.color = "#1565c0";
      setTimeout(() => {
        loginTab.click();
        registerForm.reset();
      }, 1300);
    };
    // Login
    loginForm.onsubmit = function(e) {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim().toLowerCase();
      const pass = document.getElementById('loginPassword').value;
      let usuarios = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      const user = usuarios.find(u => u.email === email && u.pass === pass);
      if (user) {
        loginMsg.textContent = "¡Bienvenido, " + user.name + "!";
        loginMsg.style.color = "#1565c0";
        setTimeout(() => {
          entrarAlSistema(user.name);
        }, 850);
      } else {
        loginMsg.textContent = "Usuario o contraseña incorrectos.";
        loginMsg.style.color = "#e53935";
      }
      loginForm.reset();
    };
    function entrarAlSistema(nombre) {
      document.getElementById('loginScreen').classList.add('hidden');
      document.getElementById('mainContent').classList.remove('hidden');
      sessionStorage.setItem("sesion", "1");
    }
    // Logout
    document.getElementById('logoutBtn').onclick = function() {
      document.getElementById('mainContent').classList.add('hidden');
      document.getElementById('loginScreen').classList.remove('hidden');
      sessionStorage.removeItem("sesion");
    }
    // Si ya inició sesión, mostrar contenido
    if (sessionStorage.getItem("sesion") === "1") {
      document.getElementById('loginScreen').classList.add('hidden');
      document.getElementById('mainContent').classList.remove('hidden');
    }
    // CONTACTO
    document.getElementById('contactForm').addEventListener('submit', function(e) {
      e.preventDefault();
      document.getElementById('respuesta').textContent = "¡Gracias por contactarnos! Pronto nos pondremos en contacto contigo.";
      this.reset();
    });
    // Navegación suave
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if(target){
          e.preventDefault();
          target.scrollIntoView({behavior: 'smooth'});
        }
      });
    });

    // INFORMACIÓN DE SERVICIOS
    const SERVICIOS_INFO = {
      urgencias: {
        icon: '<i class="fa-solid fa-truck-medical"></i>',
        title: 'Urgencias 24/7',
        text: 'Atención médica inmediata para emergencias en cualquier momento del día, los 365 días del año. Nuestro equipo está preparado para responder a situaciones críticas y estabilizar a los pacientes con rapidez y eficacia.'
      },
      consultas: {
        icon: '<i class="fa-solid fa-user-doctor"></i>',
        title: 'Consultas generales y especializadas',
        text: 'Ofrecemos consultas médicas con especialistas en diversas áreas, así como atención general para chequeos, diagnósticos y seguimiento de tu salud.'
      },
      laboratorio: {
        icon: '<i class="fa-solid fa-vials"></i>',
        title: 'Laboratorio clínico',
        text: 'Contamos con laboratorio equipado para realizar análisis de sangre, orina, perfil lipídico, pruebas de embarazo, y más. Resultados rápidos y confiables.'
      },
      imagen: {
        icon: '<i class="fa-solid fa-x-ray"></i>',
        title: 'Rayos X y ultrasonido',
        text: 'Realizamos estudios de imagen como radiografías, ultrasonidos, mamografías y otros. Diagnóstico oportuno y preciso con tecnología moderna.'
      },
      cirugia: {
        icon: '<i class="fa-solid fa-scalpel-line"></i>',
        title: 'Cirugías',
        text: 'Procedimientos quirúrgicos programados o de emergencia realizados por un equipo multidisciplinario en quirófanos equipados con los más altos estándares de calidad y seguridad.'
      },
      hospitalizacion: {
        icon: '<i class="fa-solid fa-bed-pulse"></i>',
        title: 'Hospitalización',
        text: 'Áreas cómodas y seguras para la recuperación de pacientes, atención de enfermería 24/7 y monitoreo constante por médicos especializados.'
      },
      cardiologia: {
        icon: '<i class="fa-solid fa-heart-circle-plus"></i>',
        title: 'Cardiología',
        text: 'Prevención, diagnóstico y tratamiento de enfermedades cardiovasculares. Electrocardiogramas, pruebas de esfuerzo y consulta con cardiólogos certificados.'
      },
      pediatria: {
        icon: '<i class="fa-solid fa-baby"></i>',
        title: 'Pediatría',
        text: 'Atención médica integral a niños y adolescentes, seguimiento de crecimiento, vacunación y tratamiento de enfermedades infantiles.'
      }
    };
    // Asocia eventos a las tarjetas de servicio
    document.addEventListener('DOMContentLoaded', () => {
      const grid = document.getElementById('serviciosGrid');
      const modal = document.getElementById('serviceInfoModal');
      const titleEl = document.getElementById('serviceInfoTitle');
      const textEl = document.getElementById('serviceInfoText');
      const closeBtn = document.getElementById('closeServiceInfo');
      if (grid) {
        grid.addEventListener('click', (e) => {
          let card = e.target;
          while (card && !card.classList.contains('card') && card !== grid) {
            card = card.parentElement;
          }
          if (card && card.classList.contains('card') && card.dataset.serv) {
            const data = SERVICIOS_INFO[card.dataset.serv];
            if (data) {
              titleEl.innerHTML = data.icon + " " + data.title;
              textEl.textContent = data.text;
              modal.classList.add('active');
            }
          }
        });
      }
      // Cerrar modal
      closeBtn.onclick = () => modal.classList.remove('active');
      modal.addEventListener('click', function(e) {
        if (e.target === modal) modal.classList.remove('active');
      });
      document.addEventListener('keydown', function(e){
        if(e.key === "Escape") modal.classList.remove('active');
      });
    });
  </script>
</body>
</html>
