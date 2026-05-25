#!/usr/bin/env python3
"""Inject dev-header + main-stage into downloaded demo HTML files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROJECTS = [
    ("galaxia-texto-morph.html", "40", "Galáxia — Texto Morph Pro",
     "Texto e partículas em galáxia 3D com morph animado; digite e use o mouse."),
    ("coracao-neon.html", "39", "Coração Neon Brilhante",
     "Animação de coração neon luminoso com rastreamento de mãos."),
    ("esqueleto-laser-multicolor.html", "38", "Esqueleto Laser Multicolorido",
     "Esqueleto da mão com feixes laser neon em várias cores."),
    ("caveira-fantasma.html", "36", "Caveira Fantasma Neon",
     "Caveira 2D: ao espalhar fica dourada; ao restaurar, azul neon."),
    ("esqueleto-laser-azul.html", "28", "Esqueleto Laser Azul",
     "Esqueleto da mão com efeito laser neon azul."),
    ("fumaca-azul.html", "26", "Fumaça Azul — Uma Mão",
     "Rastro de fumaça azul realista gerado por uma mão na câmera."),
    ("saturno-3d-particulas.html", "17", "Saturno 3D — Partículas",
     "Saturno 3D com anéis e partículas de poeira interativas pelos gestos."),
    ("desenho-pontilhado.html", "14", "Desenho 3D Pontilhado",
     "Pintura pontilhada 3D brilhante controlada por uma mão."),
    ("jogo-arma.html", "13", "Jogo de Arma",
     "Jogo de tiro com mira pelas mãos; pontuação e velocidade dinâmica."),
    ("saturno-tempo-real.html", "12", "Saturno 3D — Tempo Real",
     "Planeta Saturno em 3D com controle em tempo real pelas mãos."),
    ("axtarget-fusao.html", "8", "AxtarGet — Fusão Rápida",
     "Sistema de fusão rápida de elementos com gestos."),
    ("passarinho-dedo.html", "7", "Passarinho do Dedo",
     "Jogo estilo Flappy Bird com dedo e esqueleto; bônus e recordes."),
    ("axtarget-particulas-v2.html", "2", "Axtarget Partículas 3D (v2)",
     "Partículas 3D e gestos ósseos das mãos no sistema Axtarget."),
    ("axtarget-particulas-v1.html", "1", "Axtarget Partículas 3D (v1)",
     "Versão inicial: partículas 3D e gestos ósseos com hand tracking."),
]

DEV_CSS = """
    * { box-sizing: border-box; }
    .dev-header {
      background: linear-gradient(90deg, #fff 0%, #e8f4fc 50%, #fff 100%);
      padding: 12px 24px; border-bottom: 2px solid #00b8d4;
      display: flex; align-items: center; gap: 14px; flex-shrink: 0; z-index: 500;
    }
    .dev-avatar { width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #00d4ff; flex-shrink: 0; }
    .dev-avatar-fallback {
      width: 44px; height: 44px; border-radius: 50%;
      background: linear-gradient(135deg, #0054a6, #00d4ff); color: #fff;
      font-weight: 800; font-size: 14px; display: flex; align-items: center; justify-content: center;
      border: 2px solid #00d4ff; flex-shrink: 0;
    }
    .dev-identity { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px; }
    .dev-name { color: #0d2137; font-size: 16px; font-weight: 700; }
    .dev-role { color: #007a94; font-size: 11px; line-height: 1.35; }
    .dev-back-link {
      color: #0054a6; font-size: 12px; font-weight: 600; text-decoration: none;
      padding: 6px 12px; border: 1px solid #00b8d4; border-radius: 6px; flex-shrink: 0;
    }
    .dev-back-link:hover { background: rgba(0, 184, 212, 0.12); }
    .main-stage { position: relative; flex: 1; min-height: 0; overflow: hidden; }
"""

HEADER_TMPL = """  <header class="dev-header">
    <img class="dev-avatar" src="assets/avatar.jpg" alt="Foto de Josimar Menegatt"
         onerror="this.style.display='none'; document.getElementById('avatar-fallback').style.display='flex';">
    <div id="avatar-fallback" class="dev-avatar-fallback" style="display:none;" aria-hidden="true">JM</div>
    <div class="dev-identity">
      <span class="dev-name">{name}</span>
      <span class="dev-role">{role}</span>
    </div>
    <a class="dev-back-link" href="index.html">← Início</a>
  </header>

  <div class="main-stage">
"""


def patch(path: Path, test: str, name: str, role: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "dev-header" in text:
        print(f"skip (already patched): {path.name}")
        return

    comment = f"<!-- {name} (base: smm.axtarget.xyz/test{test}.html) -->\n"
    if text.startswith("<!DOCTYPE html>"):
        text = comment + text
    text = text.replace('<html lang="az">', '<html lang="pt-BR">')
    text = text.replace('<html lang="en">', '<html lang="pt-BR">')

    text = text.replace(
        "@mediapipe/hands/hands.js\"></script>",
        "@mediapipe/hands/hands.js\" crossorigin=\"anonymous\"></script>",
    )
    text = text.replace(
        "@mediapipe/hands\"></script>",
        "@mediapipe/hands/hands.js\" crossorigin=\"anonymous\"></script>",
    )
    text = text.replace(
        "@mediapipe/camera_utils\"></script>",
        "@mediapipe/camera_utils/camera_utils.js\" crossorigin=\"anonymous\"></script>",
    )
    text = text.replace(
        "@mediapipe/drawing_utils\"></script>",
        "@mediapipe/drawing_utils/drawing_utils.js\" crossorigin=\"anonymous\"></script>",
    )

    if "<style>" in text and DEV_CSS.strip() not in text:
        text = text.replace("<style>", "<style>" + DEV_CSS, 1)

    # Layout: column body + fill stage
    if "display: flex" not in text or "flex-direction: column" not in text:
        if "body, html {" in text:
            text = text.replace(
                "body, html {",
                "html, body { display: flex; flex-direction: column; height: 100vh; }\n        body, html {",
                1,
            )
        elif "body {" in text and "body, html" not in text:
            first = text.find("body {")
            if first != -1:
                text = text[:first] + "html, body { display: flex; flex-direction: column; height: 100vh; }\n        " + text[first:]

    text = text.replace("100vw", "100%")
    text = text.replace("100vh", "100%")
    text = text.replace("h-screen", "flex-1 min-h-0")

    text = text.replace("document.body.appendChild(renderer.domElement)",
                        "document.querySelector('.main-stage').appendChild(renderer.domElement)")

    import re
    body_match = re.search(r"<body[^>]*>", text)
    if not body_match:
        raise ValueError(f"no <body> in {path.name}")
    insert_at = body_match.end()
    header = HEADER_TMPL.format(name=name, role=role)
    text = text[:insert_at] + "\n" + header + text[insert_at:]

    last_body = text.rfind("</body>")
    if last_body == -1:
        raise ValueError(f"no </body> in {path.name}")
    text = text[:last_body] + "  </div>\n" + text[last_body:]

    path.write_text(text, encoding="utf-8")
    print(f"patched: {path.name}")


def main():
    for filename, test, name, role in PROJECTS:
        patch(ROOT / filename, test, name, role)


if __name__ == "__main__":
    main()
