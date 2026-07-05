"""
Script para gerar uma versão estática do site Flask para deploy no GitHub Pages.
Copia os arquivos estáticos e renderiza os templates HTML substituindo url_for()
por caminhos relativos.
"""
import shutil
import json
from pathlib import Path

ROOT = Path(__file__).parent
APP_DIR = ROOT / "app"
OUTPUT_DIR = ROOT / "docs"  # GitHub Pages usa /docs por padrão


def build():
    # Limpa a pasta de saída
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    # 1. Copiar arquivos estáticos (css, js, imagens)
    src_static = APP_DIR / "static"
    dst_static = OUTPUT_DIR / "static"
    shutil.copytree(src_static, dst_static)

    # 2. Copiar dados JSON (ajustando caminhos de imagens)
    dst_data = OUTPUT_DIR / "data"
    dst_data.mkdir()
    with open(APP_DIR / "data" / "info.json", "r", encoding="utf-8") as f:
        info = json.load(f)
    # Remover a barra inicial dos caminhos de imagem para funcionar como relativo
    for author in info:
        if "image" in author and author["image"].startswith("/"):
            author["image"] = author["image"].lstrip("/")
    with open(dst_data / "info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    # 3. Copiar o SVG do mapa (se existir nos templates)
    map_svg = APP_DIR / "templates" / "map.svg"
    if map_svg.exists():
        shutil.copy2(map_svg, OUTPUT_DIR / "map.svg")

    # 4. Renderizar index.html substituindo url_for
    index_template = (APP_DIR / "templates" / "index.html").read_text(encoding="utf-8")

    # Substituir {{ url_for('static', filename='...') }} por caminhos relativos
    import re
    def replace_url_for(match):
        filename = match.group(1)
        return f"static/{filename}"

    index_html = re.sub(
        r"\{\{\s*url_for\s*\(\s*'static'\s*,\s*filename\s*=\s*'([^']+)'\s*\)\s*\}\}",
        replace_url_for,
        index_template
    )

    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # 5. Renderizar cards HTML
    cards_src = APP_DIR / "templates" / "cards"
    if cards_src.exists():
        cards_dst = OUTPUT_DIR / "cards"
        cards_dst.mkdir()
        for card_file in cards_src.glob("*.html"):
            card_content = card_file.read_text(encoding="utf-8")
            card_content = re.sub(
                r"\{\{\s*url_for\s*\(\s*'static'\s*,\s*filename\s*=\s*'([^']+)'\s*\)\s*\}\}",
                lambda m: f"../static/{m.group(1)}",
                card_content
            )
            (cards_dst / card_file.name).write_text(card_content, encoding="utf-8")

    # 6. Criar .nojekyll para o GitHub Pages não processar com Jekyll
    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"✅ Build estático gerado em: {OUTPUT_DIR}")
    print(f"   - index.html")
    print(f"   - static/ (css, js, imagens)")
    print(f"   - data/info.json")
    if cards_src.exists():
        print(f"   - cards/ ({len(list(cards_dst.glob('*.html')))} páginas)")


if __name__ == "__main__":
    build()
