# Pautas Guardia HNRG — resumen para retomar en Claude Code

## Qué es el proyecto
Fichas digitales con pautas de alarma y cuidados en casa para los motivos de consulta más frecuentes y de menor gravedad de la guardia externa del Hospital de Niños Ricardo Gutiérrez (Buenos Aires).

Al cerrar la consulta, el pediatra acerca un tag NFC (uno por tema, en llavero o tarjetero) al celular del cuidador. El QR queda como respaldo. El cuidador se lleva la ficha en el celular.

Objetivos del proyecto:
- Medir cantidad de usos por tema y por origen (NFC o QR).
- Evaluar si mejora el tiempo de entrega de pautas y la comprensión en el hogar.
- Primero presentación interna, después presentación o publicación externa.

## Decisiones ya tomadas
- **Stack definitivo:** Vercel (hosting) + Supabase (registro de escaneos). Prioridad: que funcione y pueda crecer. La medición es un requisito transitorio.
- **Cuenta raíz del proyecto:** pautas.hnrg@gmail.com. Todos los servicios (Vercel, Supabase, GitHub) se crean con esa cuenta.
- **URL fija por tema, con el origen en un parámetro:**
  - NFC → `https://pautas-hnrg.vercel.app/<tema>?s=nfc`
  - QR → `https://pautas-hnrg.vercel.app/<tema>?s=qr`
  - Una vez impresos los QR y grabados los NFC, estas URLs no pueden cambiar. El contenido de la página sí puede cambiar.
- **Contenido:** se arma con los residentes de primer año. El de este prototipo es un borrador redactado por Claude con pautas pediátricas estándar y todavía no fue revisado.
- **Estilo de redacción:** español rioplatense (voseo), frases cortas, lenguaje para cuidadores.

## Temario
- **Prototipo (hecho):** catarro, fiebre, gastroenteritis (se muestra como "Diarrea y vómitos").
- **Pendientes:** tos (separada de catarro), constipación, conjuntivitis, dolor abdominal, cefalea, TEC leve.

## Estado actual del código
Todo se genera desde Python con un solo comando:

```
pautas-hnrg/
├── contenido.py          # Textos de cada pauta (lista PAUTAS). Se edita acá.
├── generar.py            # python3 generar.py [BASE_URL] → regenera todo
├── sitio/                # Sitio estático listo para Vercel
│   ├── index.html        # Índice de temas (uso interno)
│   ├── catarro/index.html
│   ├── fiebre/index.html
│   ├── gastroenteritis/index.html
│   └── vercel.json       # cleanUrls: true
├── qr/                   # QR por tema (PNG y SVG), apuntan a ?s=qr
├── tarjetas_QR.pdf       # Hoja A4 con tarjetas de 7×9 cm para imprimir
├── urls_nfc_qr.csv       # URLs exactas para grabar en cada NFC y en cada QR
├── vista_previa.html     # Las 3 fichas en una sola página (revisión)
└── sitio_vercel.zip
```

- Dependencias: `qrcode`, `pillow`, `reportlab`.
- Cada ficha tiene: explicación breve → **"Volvé a la guardia si…"** (recuadro rojo) → cuidados en casa → qué no hacer → pie ("Guardá esta página…", "No reemplaza la consulta médica").
- Fuentes: Atkinson Hyperlegible (cuerpo) y Bricolage Grotesque (títulos), desde Google Fonts. Tiene modo claro y oscuro. Pensado para celular.
- Cada página tiene un `<body data-tema="...">` y un script que ya lee `?s=` con un `TODO` donde va el envío a Supabase. **Todavía no registra nada.**
- `BASE_URL` por defecto: `https://pautas-hnrg.vercel.app`. Si Vercel asigna otra dirección, hay que correr `python3 generar.py <nueva_url>` antes de imprimir o grabar nada.

## Próximos pasos sugeridos para Code
1. Inicializar un repo git en GitHub con la cuenta del proyecto y subir el código.
2. Conectar el repo a Vercel con el proyecto llamado **pautas-hnrg**, publicando la carpeta `sitio/` (o mover el build a la raíz). Confirmar la URL final y regenerar QR y CSV si cambia.
3. Supabase:
   - Crear una tabla `escaneos` con: `id`, `tema`, `origen` (nfc / qr / directo), `creado_en`, y opcionalmente `user_agent`.
   - Permitir solo inserción anónima (RLS) y bloquear la lectura pública.
   - Completar el `TODO` del script para insertar el evento. Que no rompa la página si falla.
4. Evaluar migrar el generador a algo más mantenible (por ejemplo, contenido en Markdown/JSON y build en el propio Vercel) si el temario crece.
5. Agregar los temas pendientes a medida que los residentes entreguen el contenido.

## Pendientes del usuario (no de código)
- Revisar el contenido clínico con los residentes. Hay un modelo previo de catarro que podría reemplazar al borrador.
- Los NFC todavía no llegaron. Al llegar: grabarlos con NFC Tools (Escribir → URL) usando `urls_nfc_qr.csv`, probarlos y bloquear la escritura.
- **No imprimir `tarjetas_QR.pdf` hasta que el sitio esté online** en la URL definitiva.
