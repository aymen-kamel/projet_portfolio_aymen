"""Rebuilds index.html by embedding assets/portraits/*.webp into src/index.template.html.
Run: python3 build.py   (embedding keeps index.html working when opened by double-click)."""
import base64, pathlib
root = pathlib.Path(__file__).parent
html = (root / "src" / "index.template.html").read_text(encoding="utf-8")
for n in ["base", "dazed", "fedUp", "held", "hovered", "pulled", "smile"]:
    data = base64.b64encode((root / "assets" / "portraits" / f"{n}.webp").read_bytes()).decode()
    html = html.replace(f"__{n}__", "data:image/webp;base64," + data)
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html rebuilt")
