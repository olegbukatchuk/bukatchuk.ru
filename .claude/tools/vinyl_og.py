#!/usr/bin/env python3
"""Делает картинки превью ссылок (1200×630) для раздела «Винил».

Запуск из корня репозитория:
    python3 .claude/tools/vinyl_og.py            # для релизов, у которых превью ещё нет, и для общей страницы
    python3 .claude/tools/vinyl_og.py --all      # пересоздать все
    python3 .claude/tools/vinyl_og.py <имя> ...  # только для названных файлов из _vinyl/ (без .md)

Картинка кладётся в assets/img/vinyl/og/<имя>.jpg, путь записывается в поле image релиза.
Для общей страницы — assets/img/vinyl/og/index.jpg. Нужны Google Chrome и sips (macOS).
Оформление то же, что у обложек статей: стили берутся из tmp/post-cover.html.
"""
import glob, html, os, re, subprocess, sys, tempfile

REPO = os.getcwd()
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = "assets/img/vinyl/og"
WORK = os.path.join(tempfile.gettempdir(), "bukatchuk-vinyl-og")

EXTRA = """
body{padding-bottom:36px}
.og{display:flex;gap:48px;align-items:center;margin-top:34px}
.og__cover{width:372px;height:372px;flex:none;object-fit:cover;border:2px solid var(--ink);box-shadow:8px 8px 0 var(--ink)}
.og__a{font-size:19px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--safety)}
.og h1{margin-top:14px;line-height:1.04;overflow-wrap:anywhere}
.og__m{font-family:'IBM Plex Sans',sans-serif;font-size:25px;line-height:1.4;color:#222;margin-top:20px}
.og__c{font-size:15px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-top:12px}
.strip{display:flex;gap:18px;margin-top:38px}
.strip img{width:160px;height:160px;object-fit:cover;border:2px solid var(--ink);box-shadow:4px 4px 0 var(--ink)}
"""


def esc(s):
    return html.escape(str(s), quote=False)


def base_css():
    tpl = open(os.path.join(REPO, "tmp/post-cover.html"), encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", tpl, re.S).group(1)
    return css.replace("../assets", "file://" + REPO + "/assets") + EXTRA


def front(path):
    src = open(path, encoding="utf-8").read()
    fm = src[: src.index("\n---", 3)]
    data = {}
    for key in ("artist", "title", "year", "original_year", "label", "format", "color", "cover"):
        m = re.search(r"^%s:\s*(.*)$" % key, fm, re.M)
        if m:
            v = m.group(1).strip()
            if len(v) > 1 and v[0] == '"' and v[-1] == '"':
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            data[key] = v
    return data


def title_size(title, width=612):
    n = len(title)
    size = 66 if n <= 12 else 54 if n <= 24 else 44 if n <= 44 else 36
    longest = max(len(w) for w in title.split())
    return int(min(size, width / (0.6 * longest)))


def page(body, rubric, foot, css):
    return f"""<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="brand"><img src="file://{REPO}/assets/logo.png" alt=""><b>bukatchuk</b><i></i><span>{esc(rubric)}</span></div>
{body}
<div class="foot"><span>{esc(foot)}</span><b>bukatchuk.ru</b></div>
</body></html>"""


def shoot(name, markup):
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    src, png = os.path.join(WORK, name + ".html"), os.path.join(WORK, name + ".png")
    open(src, "w", encoding="utf-8").write(markup)
    # --headless=old: в новом режиме область просмотра ниже заданной и низ картинки обрезается
    subprocess.run([CHROME, "--headless=old", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1200,630", "--virtual-time-budget=3000", "--allow-file-access-from-files",
                    "--user-data-dir=" + os.path.join(WORK, "profile-" + name), "--screenshot=" + png, "file://" + src],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    jpg = os.path.join(OUT, name + ".jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82", png, "--out", jpg],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return jpg


def set_image(path, image):
    src = open(path, encoding="utf-8").read()
    end = src.index("\n---", 3)
    fm, rest = src[:end], src[end:]
    if re.search(r"^image:", fm, re.M):
        fm = re.sub(r"^image:.*$", "image: " + image, fm, flags=re.M)
    else:
        fm += "\nimage: " + image
    open(path, "w", encoding="utf-8").write(fm + rest)


def release(slug, css):
    path = f"_vinyl/{slug}.md"
    d = front(path)
    edition = f"издание {d['year']}" if d.get("year") and d.get("year") != d.get("original_year") else ""
    meta = " · ".join(x for x in (d.get("original_year"), d.get("label"), d.get("format")) if x)
    extra = " · ".join(x for x in (d.get("color"), edition) if x)
    body = f"""<div class="og"><img class="og__cover" src="file://{REPO}{d['cover']}" alt="">
<div><div class="og__a">{esc(d['artist'])}</div>
<h1 style="font-size:{title_size(d['title'])}px">{esc(d['title'])}</h1>
<div class="og__m">{esc(meta)}</div>{f'<div class="og__c">{esc(extra)}</div>' if extra else ''}</div></div>"""
    shoot(slug, page(body, "Винил", "Коллекция пластинок", css))
    set_image(path, f"/{OUT}/{slug}.jpg")


def index(css):
    covers = sorted(glob.glob("assets/img/vinyl/thumbs/*.jpg"))
    step = max(1, len(covers) // 6)
    picked = covers[::step][:6]
    strip = "".join(f'<img src="file://{REPO}/{c}" alt="">' for c in picked)
    body = f"""<h1 style="margin-top:34px">Винил</h1>
<p class="lead">Коллекция пластинок: издания, лейблы, треклисты по сторонам</p>
<div class="strip">{strip}</div>"""
    shoot("index", page(body, "Коллекция", "Виниловые пластинки", css))


def main():
    args = sys.argv[1:]
    css = base_css()
    slugs = sorted(os.path.basename(p)[:-3] for p in glob.glob("_vinyl/*.md"))
    if args and args[0] != "--all":
        todo = args
    elif args:
        todo = slugs
    else:
        todo = [s for s in slugs if not os.path.exists(f"{OUT}/{s}.jpg")]
    for slug in todo:
        release(slug, css)
        print("ok", slug)
    if not args or args[0] == "--all" or todo:
        index(css)
        print("ok index")


if __name__ == "__main__":
    main()
