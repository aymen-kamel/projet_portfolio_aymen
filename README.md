# Aymen Kamel Portfolio (v2)

Static one-page portfolio. Black hero with a giant headline and a cursor-reactive, pullable portrait (WebGL), then projects with expandable case studies, expertise, journey and a contact form.

## Run locally
Open `index.html`. No install, no server. Portraits are embedded so it works from a double-click.

## Deploy on Netlify
Drag this folder into Netlify (or connect the repo). The contact form uses Netlify Forms: the `form` tag already has `data-netlify="true"` and a honeypot, so submissions appear in Site > Forms after the first deploy. Turn on email notifications there.

## Edit
1. Edit `src/index.template.html`. Projects are the `projects` array in the script. Journey and About are plain HTML.
2. Run `python3 build.py` to re-embed the portraits into `index.html`.

## SEO files
`robots.txt`, `sitemap.xml`, `assets/og.png` (share image), `favicon.png`, `apple-touch-icon.png`. Canonical and og URLs assume `https://aymenkamel.netlify.app/`; change them in the template head if the domain changes.

## Portrait states
base (rest), smile (hover face or CTA), hovered (stay on face ~3s), held (press), pulled (drag, elastic stretch), dazed (release after a pull), fedUp (third pull in a row).

## To add
CV PDF (add `assets/Aymen-Kamel-CV.pdf` and a Download CV button next to LinkedIn), links for SmartPlayAI and HeroScore, project screenshots or clips inside each case study.
