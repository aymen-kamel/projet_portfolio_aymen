# Aymen Kamel Portfolio (v2)

One-page portfolio with a black hero (giant headline and a cursor-reactive, pullable portrait rendered with WebGL), then projects with expandable case studies, expertise, journey and a contact form.

The site is a single self-contained `index.html`. It has no framework and no npm install. The only build step embeds the portrait images into the HTML.

Live: https://aymenkamel.netlify.app/

## Repository layout

```
src/index.template.html   the source you edit (all HTML, CSS and JS)
assets/portraits/*.png    portrait sources, one per expression
assets/portraits/*.webp   portrait images that build.py embeds
assets/og.png             share image (1200x630)
build.py                  embeds the portraits into the template
index.html                generated output, deployed as-is
favicon.png, apple-touch-icon.png, robots.txt, sitemap.xml
```

## The pipeline

```
assets/portraits/*.png
        │  (1) convert to WebP
        ▼
assets/portraits/*.webp
        │  (2) python build.py
        │      replaces __base__, __smile__, … in src/index.template.html
        │      with data:image/webp;base64,… URIs
        ▼
index.html   (≈ 800 KB, works by double-click, no server)
        │  (3) commit and push
        ▼
Netlify       (publishes index.html on every push)
```

### 1. Portraits: PNG to WebP
Each expression is a PNG with transparency. Export it as WebP next to it, using the same base name. The seven expressions are `base`, `smile`, `hovered`, `held`, `pulled`, `dazed` and `fedUp`. Any tool works; with Python and Pillow:

```powershell
python -m pip install pillow
python -c "from PIL import Image; import pathlib; [Image.open(p).save(p.with_suffix('.webp'), 'WEBP', quality=80) for p in pathlib.Path('assets/portraits').glob('*.png')]"
```

Keep the file names exact. `build.py` looks them up by name.

### 2. Build: embed the portraits
```powershell
python build.py
```
This reads `src/index.template.html`, replaces each `__name__` placeholder with the base64 WebP data, and writes `index.html`. Run it every time you change the template or a portrait. Commit the regenerated `index.html` too, because Netlify serves that file directly.

### 3. Preview
Open `index.html` in a browser. There is no server to start.

## Editing the content

- **Projects:** the `projects` array in the `<script>` at the bottom of `src/index.template.html`. Each entry has `n` (name), `t` (tag line), `d` (description), `chips`, and optional `pts` (bullet points), `links` and `open` (expanded by default). The first item gets the "Featured" label and the fourth starts "More work".
- **Journey, About, Contact:** plain HTML sections in the template body.
- **No-JS fallback:** the `<noscript>` list under "Selected work" mirrors the projects array. Update both when you add or rename a project.
- **Head metadata:** title, description, Open Graph and JSON-LD sit at the top of the template. The canonical and og URLs assume `https://aymenkamel.netlify.app/`. Change them if the domain changes, and update `sitemap.xml` and `robots.txt` too.

## Deploy on Netlify

The site is static. Netlify only needs to publish the repository root.

**Option A (recommended): connect the GitHub repo.** In Netlify, choose Add new site > Import an existing project > GitHub, pick `aymen-kamel/projet_portfolio_aymen`, leave the build command empty and set the publish directory to `.`. Every push to `main` then redeploys.

**Option B: CLI, one-off deploy.**
```powershell
npx netlify-cli login
npx netlify-cli deploy --prod --dir . --no-build
```

### Contact form
The form uses Netlify Forms. The `<form>` already has `data-netlify="true"` and a honeypot field (`bot-field`). Submissions appear under Site > Forms after the first deploy with the form detected. Turn on email notifications there. The form also posts to `/` via `fetch`, so the page shows a status message without reloading.

## Checklist before a release
1. `python build.py` ran after the last template change, and `index.html` is committed.
2. Open `index.html` on a phone width (no horizontal scroll) and with JavaScript disabled (the project list falls back to the `<noscript>` list).
3. The OG image and canonical URL still point at the live domain.

## Portrait states
base (rest), smile (hover face or CTA), hovered (stay on face ~3s), held (press), pulled (drag, elastic stretch), dazed (release after a pull), fedUp (third pull in a row).

## To add
- CV PDF: add `assets/Aymen-Kamel-CV.pdf` and a Download CV button next to LinkedIn.
- Links for SmartPlayAI and HeroScore.
- Project screenshots or clips inside each case study.
