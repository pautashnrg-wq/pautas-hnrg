"""Genera el sitio (para Vercel), los QR, las URLs para grabar en los NFC y la hoja imprimible de QR.

Uso:  python3 generar.py [BASE_URL]
Por defecto BASE_URL = https://pautas-hnrg.vercel.app
Si el sitio termina en otra dirección, se vuelve a correr con esa URL y se regeneran QR y NFC.
"""
import csv, html, os, shutil, sys
import qrcode, qrcode.image.svg
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from contenido import PAUTAS

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://pautas-hnrg.vercel.app").rstrip("/")
OUT = os.path.dirname(os.path.abspath(__file__))
SITE, QR = os.path.join(OUT, "sitio"), os.path.join(OUT, "qr")
HOSPITAL = "Hospital de Niños Ricardo Gutiérrez · Guardia"

FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&display=swap">'

CSS = """
/* Ficha de bolsillo: una columna angosta, la alarma en rojo arriba de todo, lo demás tranquilo */
:root{
  --bg:#F4F7F8; --card:#FFFFFF; --ink:#13303A; --muted:#536A73; --line:#D9E3E6;
  --alarm:#B42318; --alarm-bg:#FDEDEB; --alarm-ink:#7A1A12;
  --azul:#1F5FA6; --ambar:#9A5B00; --verde:#2A7148;
  --f-display:"Bricolage Grotesque", "Arial Rounded MT Bold", system-ui, sans-serif;
  --f-body:"Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0E1A1F; --card:#15252B; --ink:#E6EFF1; --muted:#9CB2B9; --line:#26393F;
  --alarm:#FF8A7A; --alarm-bg:#3A1714; --alarm-ink:#FFD6CF;
  --azul:#7DB3F0; --ambar:#F2B657; --verde:#7FCB9C; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0E1A1F; --card:#15252B; --ink:#E6EFF1; --muted:#9CB2B9; --line:#26393F;
  --alarm:#FF8A7A; --alarm-bg:#3A1714; --alarm-ink:#FFD6CF;
  --azul:#7DB3F0; --ambar:#F2B657; --verde:#7FCB9C; color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:18px;line-height:1.5}
.wrap{max-width:34rem;margin:0 auto;padding-inline:16px;padding-block:20px 40px;display:flex;flex-direction:column;gap:20px}
.hosp{font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700}
header{display:flex;flex-direction:column;gap:4px;padding-bottom:16px;border-bottom:3px solid var(--tema)}
h1{font-family:var(--f-display);font-weight:800;font-size:2.4rem;line-height:1.05;margin:4px 0 0;text-wrap:balance}
.sub{color:var(--muted);font-size:1.05rem}
h2{font-family:var(--f-display);font-weight:600;font-size:1.3rem;margin:0 0 8px;text-wrap:balance}
ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
li{display:grid;grid-template-columns:1.4rem 1fr;gap:8px;align-items:start}
li>span{min-width:0}
.mk{font-weight:700;line-height:1.5;text-align:center}
.intro p{margin:0 0 6px}
.alarma{background:var(--alarm-bg);border:2px solid var(--alarm);border-radius:14px;padding:16px}
.alarma h2{color:var(--alarm)}
.alarma li{color:var(--alarm-ink)}
.alarma .mk{color:var(--alarm)}
.alarma .pie{margin:12px 0 0;font-weight:700;color:var(--alarm)}
.cuidados .mk{color:var(--tema)}
.evitar .mk{color:var(--muted)}
footer{border-top:1px solid var(--line);padding-top:14px;color:var(--muted);font-size:.9rem;display:flex;flex-direction:column;gap:4px}
footer strong{color:var(--ink)}
.t-azul{--tema:var(--azul)} .t-ambar{--tema:var(--ambar)} .t-verde{--tema:var(--verde)}
.chip{align-self:flex-start;font-size:.8rem;font-weight:700;color:var(--tema);border:1.5px solid var(--tema);border-radius:999px;padding:1px 10px}
nav.temas{display:flex;flex-wrap:wrap;gap:8px}
nav.temas a{font-weight:700;color:var(--tema);text-decoration:none;border:1.5px solid var(--tema);border-radius:999px;padding:6px 14px}
nav.temas a:focus-visible{outline:3px solid var(--ink);outline-offset:2px}
.borrador{background:var(--card);border:1px dashed var(--muted);border-radius:10px;padding:10px 12px;font-size:.85rem;color:var(--muted)}
.sep{height:28px}
"""

e = html.escape

def lista(items, marca):
    return "<ul>" + "".join(f'<li><span class="mk" aria-hidden="true">{marca}</span><span>{e(i)}</span></li>' for i in items) + "</ul>"

def ficha(p, tag="article", id_=""):
    idattr = f' id="{id_}"' if id_ else ""
    return f"""<{tag} class="t-{p['color']}"{idattr} style="display:flex;flex-direction:column;gap:20px">
<header><div class="hosp">{e(HOSPITAL)}</div><h1>{e(p['titulo'])}</h1><div class="sub">{e(p['subtitulo'])}</div></header>
<section class="intro">{''.join(f'<p>{e(x)}</p>' for x in p['que_es'])}</section>
<section class="alarma"><h2>Volvé a la guardia si…</h2>{lista(p['alarma'], '!')}<p class="pie">Ante la duda, consultá. La guardia atiende las 24 horas.</p></section>
<section class="cuidados"><h2>Cuidados en casa</h2>{lista(p['cuidados'], '✓')}</section>
<section class="evitar"><h2>Qué no hacer</h2>{lista(p['evitar'], '✕')}</section>
<footer><strong>Guardá esta página en tu celular.</strong><span>Esta información no reemplaza la consulta médica.</span></footer>
</{tag}>"""

# Medición futura: la página lee ?s=nfc o ?s=qr. Cuando esté Supabase, acá se registra el evento.
TRACK = """<script>
(function(){try{var s=new URLSearchParams(location.search).get('s')||'directo';
var tema=document.body.dataset.tema;
/* TODO medición: enviar {tema, origen:s, fecha} a Supabase */
}catch(e){}})();
</script>"""

def doc(titulo, cuerpo, tema=""):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)} · Guardia HNRG</title>{FONTS}<style>{CSS}</style></head>
<body data-tema="{tema}"><main class="wrap">{cuerpo}</main>{TRACK}</body></html>"""

def url(p, origen): return f"{BASE}/{p['slug']}?s={origen}"

def main():
    for d in (SITE, QR): shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    # 1. Sitio para Vercel
    for p in PAUTAS:
        os.makedirs(os.path.join(SITE, p["slug"]))
        open(os.path.join(SITE, p["slug"], "index.html"), "w").write(doc(p["titulo"], ficha(p, "div"), p["slug"]))
    nav = "".join(f'<a class="t-{p["color"]}" href="/{p["slug"]}">{e(p["titulo"])}</a>' for p in PAUTAS)
    open(os.path.join(SITE, "index.html"), "w").write(doc("Pautas", f'<header class="t-azul"><div class="hosp">{e(HOSPITAL)}</div><h1>Pautas para casa</h1></header><nav class="temas">{nav}</nav>'))
    open(os.path.join(SITE, "vercel.json"), "w").write('{"cleanUrls": true, "trailingSlash": false}\n')

    # 2. QR (PNG para imprimir, SVG para diseño) y URLs NFC
    with open(os.path.join(OUT, "urls_nfc_qr.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["tema", "url_para_grabar_en_NFC", "url_del_QR"])
        for p in PAUTAS:
            w.writerow([p["titulo"], url(p, "nfc"), url(p, "qr")])
            q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
            q.add_data(url(p, "qr")); q.make(fit=True)
            q.make_image(fill_color="black", back_color="white").save(os.path.join(QR, f"{p['slug']}.png"))
            qrcode.make(url(p, "qr"), image_factory=qrcode.image.svg.SvgPathImage, border=2).save(os.path.join(QR, f"{p['slug']}.svg"))

    # 3. Hoja imprimible A4 con las tarjetas QR (7 x 9 cm, para tarjetero o llavero)
    c = canvas.Canvas(os.path.join(OUT, "tarjetas_QR.pdf"), pagesize=A4)
    W, H = A4; cw, ch = 7 * cm, 9 * cm
    for i, p in enumerate(PAUTAS):
        col, row = i % 2, i // 2
        x = 2.5 * cm + col * (cw + 1.5 * cm); y = H - 2 * cm - (row + 1) * (ch + 1 * cm)
        c.setDash(3, 3); c.setStrokeGray(.6); c.roundRect(x, y, cw, ch, 8); c.setDash()
        c.setFont("Helvetica-Bold", 18); c.drawCentredString(x + cw / 2, y + ch - 1.2 * cm, p["titulo"])
        c.setFont("Helvetica", 9); c.drawCentredString(x + cw / 2, y + ch - 1.7 * cm, p["subtitulo"])
        c.drawImage(os.path.join(QR, f"{p['slug']}.png"), x + 1 * cm, y + 1.4 * cm, 5 * cm, 5 * cm)
        c.setFont("Helvetica", 8.5); c.drawCentredString(x + cw / 2, y + .8 * cm, "Escaneá con la cámara del celular")
        c.setFont("Helvetica", 7); c.setFillGray(.4); c.drawCentredString(x + cw / 2, y + .4 * cm, "Guardia · Hospital de Niños R. Gutiérrez"); c.setFillGray(0)
    c.save()

    # 4. Vista previa (una sola página con los tres temas) para revisar en el celular
    navp = "".join(f'<a class="t-{p["color"]}" href="#{p["slug"]}">{e(p["titulo"])}</a>' for p in PAUTAS)
    fichas = '<div class="sep"></div>'.join(ficha(p, "article", p["slug"]) for p in PAUTAS)
    prev = (f"<title>Pautas Guardia HNRG</title>{FONTS}<style>{CSS}</style><main class=\"wrap\">"
            f'<div class="borrador">Vista previa · borrador para revisar con residentes. Cada tema tendrá su propia página, NFC y QR.</div>'
            f'<nav class="temas">{navp}</nav>{fichas}</main>')
    open(os.path.join(OUT, "vista_previa.html"), "w").write(prev)
    shutil.make_archive(os.path.join(OUT, "sitio_vercel"), "zip", SITE)
    print("OK", BASE)

if __name__ == "__main__":
    main()
