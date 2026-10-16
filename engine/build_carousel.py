#!/usr/bin/env python3
"""
Gerador de carrosséis da Clínica Binhame.

Uso:
    python build_carousel.py ../specs/urgencia.json --out ../saida/urgencia

Entrada : um arquivo .json com o conteúdo (veja ../specs/ e o README).
Saída   : slide-01.png, slide-02.png... (1080x1350, formato vertical do Instagram)
Requer  : Python 3.9+, `pip install playwright`, `playwright install chromium`
Fontes  : Lora e Poppins (carregam do Google Fonts se houver internet; senão precisam estar instaladas).
"""
import argparse, html, json, shutil, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"

def _svg(p, w=3):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
BADGE_ICONS = {
    "alert": _svg('<path d="M12 8v5M12 17h.01"/><circle cx="12" cy="12" r="10"/>'),
    "question": _svg('<circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/>'),
    "bulb": _svg('<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V17h6v-.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2Z"/>'),
    "check": _svg('<path d="M20 6 9 17l-5-5"/>'),
    "x": _svg('<path d="M6 6l12 12M18 6 6 18"/>'),
    "none": "",
}
CTA_ICONS = {
    "comment": _svg('<path d="M21 12a8 8 0 0 1-12 7l-5 1.5 1.5-5A8 8 0 1 1 21 12Z"/>', 2.2),
    "send": _svg('<path d="M22 2 11 13M22 2l-7 20-4-9-9-4Z"/>', 2.2),
    "save": _svg('<path d="M5 3h14v18l-7-5-7 5Z"/>', 2.2),
}
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def esc(t): return html.escape(str(t), quote=False)

def foot(clinic, n, total):
    return (f'<div class="foot"><div class="who"><div class="avatar"></div><div>'
            f'<b>{esc(clinic["nome_dentista"])}</b><span>{esc(clinic["nome_curto"])}</span></div></div>'
            f'<div class="count">{n}/{total}</div></div>')

def r_cover(s, clinic, n, total, k, kt):
    t = s["title"]; t = "<br>".join(esc(x) for x in t) if isinstance(t, list) else esc(t)
    return (f'<section class="slide cover"><div class="tag">{esc(s["tag"])}</div><h1>{t}</h1>'
            f'<p class="sub">{esc(s["sub"])}</p><div class="ring"></div><div class="glow"></div>'
            f'<img class="photo" src="assets/tiago_cut.webp" alt="">'
            f'<div class="foot"><div class="swipe" style="color:var(--gl)">Arraste para o lado{ARROW}</div></div></section>')

def r_content(s, clinic, n, total, k, kt):
    cls = s.get("color", "gold")
    return (f'<section class="slide sign"><div class="top"><span class="badge {cls}">{BADGE_ICONS[s.get("icon","alert")]}{esc(s["badge"])}</span>'
            f'<span class="of">{k} de {kt}</span><h2>{esc(s["title"])}</h2></div>'
            f'<div class="panel"><h3>{esc(s["headline"])}</h3><p>{esc(s["text"])}</p>'
            f'<div class="doit"><span class="ic">{BADGE_ICONS["check"]}</span><span>{esc(s["action"])}</span></div>'
            f'{foot(clinic, n, total)}</div></section>')

def r_myth(s, clinic, n, total, k, kt):
    return (f'<section class="slide sign mito"><div class="top"><span class="badge red">{BADGE_ICONS["x"]}Mito</span>'
            f'<span class="of">{k} de {kt}</span><h2>{esc(s["claim"])}</h2></div>'
            f'<div class="panel"><span class="badge ok">{BADGE_ICONS["check"]}Na verdade</span>'
            f'<h3>{esc(s["headline"])}</h3><p>{esc(s["text"])}</p>{foot(clinic, n, total)}</div></section>')

def r_list(s, clinic, n, total, k, kt):
    lis = "".join(f'<li><span class="ic">{BADGE_ICONS["check"]}</span><span>{esc(i["title"])}<small>{esc(i.get("detail",""))}</small></span></li>' for i in s["items"])
    return (f'<section class="slide sign routine"><div class="top"><span class="badge gold">{esc(s["badge"])}</span>'
            f'<h2>{esc(s["title"])}</h2></div><div class="panel"><ul>{lis}</ul>{foot(clinic, n, total)}</div></section>')

def r_cta(s, clinic, n, total, k, kt):
    acts = "".join(f'<li><span class="ic">{CTA_ICONS[a["icon"]]}</span>{esc(a["text"])}</li>' for a in s["actions"])
    note = f'<p class="note">{esc(s["note"])}</p>' if s.get("note") else ""
    return (f'<section class="slide cta"><h2>{esc(s["title"])}</h2><ul class="acts">{acts}</ul>{note}'
            f'<div class="ring"></div><img class="photo" src="assets/tiago_cut.webp" alt="">'
            f'<div class="card"><img src="assets/logo.jpeg" alt=""><div><div class="t">{esc(s.get("card_title", clinic["cta_titulo_padrao"]))}</div>'
            f'<p><b>WhatsApp {esc(clinic["whatsapp_exibido"])}</b><br>{esc(clinic["endereco"])}</p></div></div></section>')

RENDER = {"cover": r_cover, "content": r_content, "myth": r_myth, "list": r_list, "cta": r_cta}

FIT_JS = """
() => {
  const rep = [];
  document.querySelectorAll('.sign').forEach((sl, i) => {
    const sr = sl.getBoundingClientRect(), panel = sl.querySelector('.panel'), foot = sl.querySelector('.foot'), h2 = sl.querySelector('.top h2');
    let fs = parseFloat(getComputedStyle(h2).fontSize);
    while ((h2.getBoundingClientRect().bottom - sr.top) > (panel.getBoundingClientRect().top - sr.top) - 40 && fs > 48) { fs -= 2; h2.style.fontSize = fs + 'px'; }
    const p = panel.querySelector('p'), last = panel.querySelector('.doit') || panel.querySelector('ul') || p;
    let pf = p ? parseFloat(getComputedStyle(p).fontSize) : 0;
    while (last.getBoundingClientRect().bottom > foot.getBoundingClientRect().top - 28 && pf > 26) { pf -= 1; p.style.fontSize = pf + 'px'; }
    const titleSlack = (panel.getBoundingClientRect().top - sr.top) - (h2.getBoundingClientRect().bottom - sr.top);
    const bodySlack = foot.getBoundingClientRect().top - last.getBoundingClientRect().bottom;
    rep.push({slide: Array.from(document.querySelectorAll('.slide')).indexOf(sl) + 1, titleSlack: Math.round(titleSlack), bodySlack: Math.round(bodySlack), titleFont: fs, bodyFont: pf});
  });
  return rep;
}
"""

def main():
    ap = argparse.ArgumentParser(description="Gera um carrossel (PNG 1080x1350) a partir de um arquivo de conteúdo .json")
    ap.add_argument("spec"); ap.add_argument("--out", default=None); ap.add_argument("--keep", action="store_true", help="manter a pasta de trabalho (debug)")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    clinic = json.loads((HERE / "clinic.json").read_text(encoding="utf-8"))
    out = Path(a.out or (HERE.parent / "saida" / spec.get("slug", "carrossel"))).resolve(); out.mkdir(parents=True, exist_ok=True)
    work = out / "_work"; (work / "assets").mkdir(parents=True, exist_ok=True)
    for f in ("tiago_cut.webp", "logo.jpeg"): shutil.copy(ASSETS / f, work / "assets" / f)
    shutil.copy(HERE / "carousel.css", work / "carousel.css")

    slides = spec["slides"]; total = len(slides)
    kt = sum(1 for s in slides if s["type"] in ("content", "myth")); k = 0; secs = []
    for n, s in enumerate(slides, 1):
        if s["type"] in ("content", "myth"): k += 1
        secs.append(RENDER[s["type"]](s, clinic, n, total, k, kt))
    (work / "slides.html").write_text('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="carousel.css"></head><body>' + "\n".join(secs) + "</body></html>", encoding="utf-8")

    problems = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1100, "height": 1400})
        pg.goto((work / "slides.html").as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
        rep = pg.evaluate(FIT_JS)
        for r in rep:
            if r["titleSlack"] < 0 or r["bodySlack"] < 0:
                problems += 1; print(f'  ATENÇÃO slide {r["slide"]}: texto grande demais (folga título {r["titleSlack"]}px, corpo {r["bodySlack"]}px). Encurte o texto.')
            elif r["bodyFont"] and r["bodyFont"] < 30:
                print(f'  aviso slide {r["slide"]}: texto longo, fonte reduzida para {r["bodyFont"]}px. Considere encurtar.')
        els = pg.locator(".slide")
        for i in range(els.count()): els.nth(i).screenshot(path=str(out / f"slide-{i+1:02d}.png"))
        b.close()
    if not a.keep: shutil.rmtree(work, ignore_errors=True)
    print(f"{total} slides gerados em {out}" + ("" if not problems else f" ({problems} com problema)"))
    sys.exit(2 if problems else 0)

if __name__ == "__main__": main()
