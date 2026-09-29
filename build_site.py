from pathlib import Path
import html
root=Path('/mnt/data/site_build')
items=[
('MAGALLANES','2025','FICCIÓN','Foley Mixer','MV5BYjU1MTIxOTItZGY2Ny00MDNhLWI1ZGUtYmM0MmNjMWFlMWU4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg','https://www.youtube.com/watch?v=A0iOYjj3Lm4'),
('3000 KMS EN BICICLETA','2024','DOCUMENTAL','Sonido directo','Dise-o-sin-t-tulo-95.png','https://www.youtube.com/watch?v=JPdvYrza_ys'),
('EL AGUJERITO','2024','DOCUMENTAL','Diseño de sonido','poster.webp','https://www.youtube.com/watch?v=Fy_4O2gwRx0'),
('HABÍA UNA VEZ UN MAGO','2024','DOCUMENTAL','Diseño de sonido','foto-noticia-habia-una-vez-un-mago.jpg','https://www.youtube.com/watch?v=1omt2M0qC3g'),
('HABITAR LA SOMBRA','2022','DOCUMENTAL','Diseño de sonido','FLYER-HABITAR-LA-SOMBRA-1.0-Viviana-De-Rosa.jpeg','https://www.youtube.com/watch?v=MNH-IP2zR6c'),
('GAUCHO, GAUCHO','2022-2023','DOCUMENTAL','Sonido directo','Screen Shot 2024-06-04 at 18.01.46.png','https://www.youtube.com/watch?v=08BVd9UwwyY'),
('BENDITA','2023','FICCIÓN','Sonido directo','MV5BZGFjYjEwNGUtMmNhNi00M2RjLWFkNDItOTI3NmNjMWI2MzZiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg','https://www.youtube.com/watch?v=5FaMV5dW66E'),
('ARGENTINA, 1985','2020','FICCIÓN','Sonido directo','ARGENTINA-1985-PV-esp-2-scaled.jpg','https://www.youtube.com/watch?v=8xOqgolOHPg'),
('SERAFINA','2024','FICCIÓN','Edición de ambientes y efectos / grabación de ADR','Screen Shot 2024-12-10 at 11.15.01.png','https://www.youtube.com/watch?v=2RtyoqqtFvo'),
('TODAS LAS COSAS QUE LLEVO CONMIGO','2023','FICCIÓN','Sonido directo','MV5BYmIwNzE1ZWYtMWZhZC00NGNiLWI3MTYtY2MzMzY0ZTM4ZDcyXkEyXkFqcGdeQXVyMTY1MjM4NTQ1._V1_FMjpg_UX1000_.jpg','https://www.youtube.com/watch?v=BPW6AdXc6eQ'),
('EL CASTILLO','2023','DOCUMENTAL','Edición de ambientes y efectos','El_castillo-612766431-large.jpg','https://youtu.be/Pi-XXOef1Xo'),
('EL ESPACIO DE LOS CUERPOS','2021','DOCUMENTAL','Sonido directo','odeon_afiche_prod.jpg','https://www.dailymotion.com/video/x9gwkj0'),
('SELENKAY','2021 - 2022','Serie Disney LA','Sonido directo','scale.png','https://www.youtube.com/watch?v=VzK6YQ9Eovg'),
('LEGÍTIMA DEFENSA','2021','FICCIÓN','Sonido directo','Screen Shot 2023-01-28 at 09.49.32.png','https://www.youtube.com/watch?v=KdZ_gB0rfLU'),
('LA EDUCACIÓN DE LOS CERDOS','2021','FICCIÓN','Sonido directo','la educacion.jpeg','https://www.youtube.com/watch?v=y2UQJpEfrEA'),
('LOS AGITADORES','2021','FICCIÓN','Sonido directo','Los agitadores.jpeg','https://www.youtube.com/watch?v=_UTho-OKn6I'),
('ENRIQUETA','2021','DOCUMENTAL','Diseño de sonido','Screen Shot 2023-03-18 at 11.55.04.png','https://www.youtube.com/watch?v=TFwRj1IdsWc'),
('SECTOR VIP','2020','FICCIÓN','Edición de ambientes y efectos','sector_vip-785933933-large.jpg','https://www.youtube.com/watch?v=3_dfFPRWLtA'),
('EL FORTIN, MÁS ALLÁ DE LA FRONTERA','2020','DOCUMENTAL','Diseño de sonido / Sonido directo','El Fortín.jpg','https://www.youtube.com/watch?v=AlZQ3NAHibw'),
('ÉRASE UNA VEZ EN QUIZCA','2020','DOCUMENTAL','Edición de diálogos, ambientes y efectos','EuVeQ Póster Web ES.jpg','https://www.youtube.com/watch?v=PNk6sZqfYFo'),
('CRÍMENES IMPOSIBLES','2019','FICCIÓN','Edición de diálogos y ambientes y efectos','Cr_menes_imposibles-610836921-large.jpg','https://www.youtube.com/watch?v=XGgqYMqQH40'),
('GO! VIVE A TU MANERA','2019','Serie Netflix','Edición de ambientes y efectos','a115bd513f1c55c8585b9e5ed5cca59fca8caeba.jpg','https://www.youtube.com/watch?v=91WQNnsk9yo'),
('EL RITUAL DEL ALCAUCIL','2017–2019','DOCUMENTAL','Diseño de sonido / Sonido directo / Edición de ambientes y efectos / Foley / Diálogos','124581001_823654531757045_3871179103717635930_n.jpg','https://www.youtube.com/watch?v=iXUuonChQ3I'),
('EL BOSQUE DE LOS PERROS','2018','FICCIÓN','Edición de ambientes y efectos','MV5BYWZiOWQwNjUtZTc4NC00ZDY0LThmOGQtMTgzN2RlNmFhZTY5XkEyXkFqcGdeQXVyMTk2NTkyMzY_._V1_SY1000_CR0,0,697,1000_AL_.jpg','https://www.youtube.com/watch?v=iiORhS9UjWY'),
('MANIFIESTO','2019','FICCIÓN','Edición de ambientes y efectos','150443154_10224928010404887_5716926996733604327_n.jpg','https://www.youtube.com/watch?v=JJS81F9Fl9E'),
('MATAR AL DRAGÓN','2019','FICCIÓN','Edición de ambientes y efectos','1320661.jpg','https://www.youtube.com/watch?v=pTalS2Ccvy4'),
('EXPANSIVAS','2019','FICCIÓN','Edición de ambientes y efectos','MV5BNGY5OTZmYTctZDcwZC00NDBmLWI2YTQtNjUyMTYxYTE4Y2E3XkEyXkFqcGdeQXVyMjY3NTQyOTA@._V1_SY1000_CR0,0,702,1000_AL_.jpg','https://www.youtube.com/watch?v=4SwL_4SrTp4'),
('SHI ZONG','2019','FICCIÓN','Edición de ambientes y efectos','Screen Shot 2023-10-24 at 20.39.28.png','https://www.imdb.com/es-es/title/tt12043620/?ref_=nm_flmg_job_1_accord_1_cdt_t_20'),
('UNA CASA LEJOS','2019','FICCIÓN','Edición de Ambientes y efectos','UCL Poster Spanish WEB.jpeg','https://www.youtube.com/watch?v=td5mdFmGUSg'),
('BRONCO, LA SERIE','2019','Serie Tv México','Coordinadora de Postproducción, Edición de ambientes y efectos','t_a49f1b7d0eef4f90a1482d218bc87949_name_bronco_serie.png','https://www.youtube.com/watch?v=1R4OW8MlGVg'),
('LUCIFERINA','2018','FICCIÓN','Edición de ambientes y efectos','MV5BMmNlMjRmOTUtODM3MC00NmY3LTk2NjItZjFkNmQxMTIyZjM0XkEyXkFqcGdeQXVyNTA5ODMyMDU_._V1_.jpg','https://www.youtube.com/watch?v=fjhhG05bXmc'),
('APNEA','2018','FICCIÓN','Diseño de sonido / Sonido directo','poster-apnea_BAJA.jpg','https://www.youtube.com/watch?v=YohmjWop2oY&t=6s'),
('PISTOLERO','2018','FICCIÓN','Edición de ambientes y efectos','Pistolero-828658835-large.jpg','https://www.youtube.com/watch?v=ZMvCDnNWlPQ'),
('HIJOS DE NADIE','2018','DOCUMENTAL','Edición de diálogos y ambientes y efectos','hijos_de_nadie_una_pelicula_sobre_los_adolfos_rap-721447895-large.jpg','https://www.youtube.com/watch?v=sl6lapS1-FU'),
('ERDOSAIN','2018','FICCIÓN','Edición de ambientes y efectos, grabación de FX','Erdosain.jpg','https://www.youtube.com/watch?v=1-hsTU8ZiU4'),
('CON NOMBRE DE FLOR','2018','DOCUMENTAL','Edición de diálogos, ambientes y efectos','festival-catapulta-catalogo-Con-nombre-de-flor-poster.jpg','https://www.youtube.com/watch?v=xZ7Taq2OIsw'),
('CICLOS','2018','DOCUMENTAL','Edición de ambientes y efectos','MV5BYTIwYTM5ODktZTAxZS00Yjk5LTg5MTctODAyMTU4YmNjMzBlXkEyXkFqcGdeQXVyMjU5MzU0MzU_._V1_SY1000_CR0,0,699,1000_AL_.jpg','https://www.youtube.com/watch?v=NrfWNExJ-s4'),
('NAFTA SÚPER','2016','Serie TV Argentina','Edición de ambientes y efectos','MV5BOTIwNTlkYmEtNGU5Yy00MzE1LWEyNTctOGE1ODNjODY4ODU0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNzExMTcxODY_._V1_SY1000_CR0,0,728,1000_AL_.jpg','https://www.youtube.com/watch?v=4ArxLAJER9g'),
('LA NOSTALGIA DEL CENTAURO','2017','DOCUMENTAL','Edición de ambientes y efectos','la_nostalgia_del_centauro-116880483-large.jpg','https://www.youtube.com/watch?v=jISuo89Cjfw'),
('ALPTRAUM','2016','FICCIÓN','Edición de ambientes y efectos','MV5BYTkyZmM2Y2UtNjM4Zi00Mzg4LTg3OTUtNzI2ZjhjZGYxZDI4XkEyXkFqcGdeQXVyODgxMDAxMjY@._V1_.jpg','https://www.youtube.com/watch?v=s5ayT749yH8'),
('YOLANDA','2016','FICCIÓN','Edición de ambientes y efectos','CvaY9RYWgAUdj6Y.jpg','https://www.youtube.com/watch?v=s8pNVnbivYc'),
]

def esc(x): return html.escape(x,quote=True)
nav='''<nav class="nav"><div class="brand"><a href="index.html">CAMILA RUIZ DIAZ ODENA</a><div class="tagline">Sound · Film · Social Research</div></div><div class="menu"><a href="sound-in-film.html">SOUND IN FILM</a><a href="research.html" class="section">RESEARCH</a><a href="sound-identities.html" class="sub">SOUND IDENTITIES</a><a href="research-projects.html" class="sub">RESEARCH PROJECTS</a><a href="about.html" class="section">ABOUT</a><a href="contact.html">CONTACT</a></div><div class="clock" id="clock"></div></nav>'''
htmlout=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sound in Film — Camila Ruiz Diaz Odena</title><link rel="stylesheet" href="styles.css"></head><body>',nav,'<main class="content"><h1 class="page-title">SOUND IN FILM</h1><hr class="rule"><div class="sound-grid">']
for title,year,typ,role,img,href in items:
    wide=' wide' if img in ['scale.png','t_a49f1b7d0eef4f90a1482d218bc87949_name_bronco_serie.png'] else ''
    htmlout.append(f'<article class="sound-item{wide}"><a class="poster-link" href="{esc(href)}" target="_blank" rel="noopener"><img class="sound-poster" src="assets/posters/{esc(img)}" alt="{esc(title)} poster"></a><div class="sound-caption"><div class="sound-title">{esc(title)}</div><div>{esc(year)}</div><div>{esc(typ)}</div><div>{esc(role)}</div></div></article>')
htmlout += ['</div></main><script src="script.js"></script></body></html>']
(root/'sound-in-film.html').write_text(''.join(htmlout),encoding='utf8')

nav2=nav
research='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research — Camila Ruiz Diaz Odena</title><link rel="stylesheet" href="styles.css"></head><body>'''+nav2+'''<main class="content"><h1 class="page-title">RESEARCH</h1><hr class="rule"><div class="intro"><div class="lead">Sound, listening and social experience.</div><p>My research explores sound as a social and ethnographic experience, with a particular interest in listening practices, sound identities and the ways in which people experience and give meaning to their sonic environments.</p></div><div class="section-block"><a href="sound-identities.html"><strong>SOUND IDENTITIES</strong></a></div><div class="section-block"><a href="research-projects.html"><strong>RESEARCH PROJECTS</strong></a></div></main><script src="script.js"></script></body></html>'''
(root/'research.html').write_text(research,encoding='utf8')

si='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sound Identities — Camila Ruiz Diaz Odena</title><link rel="stylesheet" href="styles.css"></head><body>'''+nav+'''<main class="content"><h1 class="page-title">SOUND IDENTITIES</h1><hr class="rule"><div class="intro"><p>An ongoing collection of sound recordings and short texts exploring the relationship between sound, place, memory and social experience.</p></div><div class="section-block"><div class="section-title">SOUND IDENTITIES #01</div><div class="project"><h2>SAN TELMO</h2><p>sonic environment</p><p>Buenos Aires, Argentina<br>2020</p><div class="audio-entry"><audio controls preload="metadata"><source src="assets/audio/san-telmo.wav" type="audio/wav">Your browser does not support audio playback.</audio></div><div class="field-notes"><span>Location: San Telmo, Buenos Aires, Argentina</span><span>Date: 2020</span></div></div></div></main><script src="script.js"></script></body></html>'''
(root/'sound-identities.html').write_text(si,encoding='utf8')

rp='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Research Projects — Camila Ruiz Diaz Odena</title><link rel="stylesheet" href="styles.css"></head><body>'''+nav+'''<main class="content"><h1 class="page-title">RESEARCH PROJECTS</h1><hr class="rule"><div class="intro"><p>This section brings together research projects, texts and materials that form part of my ongoing field of inquiry into sound ethnography.</p></div><div class="project-list"><article class="project"><h2>LOS SONIDOS DEL ENCIERRO</h2><p>An ongoing research project of a sound ethnography in a prison context.</p><p class="material"><a href="https://revistasacademicas.unsam.edu.ar/index.php/dyp/article/view/2023" target="_blank" rel="noopener">Article ↗</a></p></article><article class="project"><h2>SOUND MAPS</h2><p>Sonidos que habitan nuestro entorno: mapa sonoro</p><p class="material"><a href="https://mapasonorounsam.neocities.org/" target="_blank" rel="noopener">Website ↗</a></p><p>Long description about the UNSAM Miguelete Campus sound research project, listening as a tool for recognizing territories, techniques for direct recording and editing and meaningful soundscapes, an interactive sound map open to the community, tools for other social and artistic contexts, and the expansion of social studies of sound through science-creation.</p></article><article class="project"><h2>READING / RESEARCH MATERIALS</h2><p>A selection of recent papers, texts and other materials.</p><p><strong>#01</strong><br>CIUDADES QUE SUENAN, MEMORIAS QUE VIBRAN. Usos sociales y políticos de la música y el sonido.<br>Verónika Diaz Abrahan y Verónica Cannarozzo, compiladoras<br>2026</p><p class="material"><a href="assets/ciudades-que-suenan.pdf" target="_blank" rel="noopener">PDF ↗</a></p></article></div></main><script src="script.js"></script></body></html>'''
(root/'research-projects.html').write_text(rp,encoding='utf8')
print('built',len(items),'sound projects')
