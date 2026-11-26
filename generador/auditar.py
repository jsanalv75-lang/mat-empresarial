"""Auditoría de lo que ve el alumno, siguiendo las reglas del formato «paso a paso».

Uso: python3 auditar.py  (lee public/index.html)
Busca: $ sueltos, \\comandos fuera de las fórmulas, referencias a otros problemas o cuadros por número,
puntuaciones y restos de fuentes. Las fórmulas \\( \\) y \\[ \\] y el código de Mathematica se excluyen.
"""
import html, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent
s = (RAIZ.parent / "public" / "index.html").read_text(encoding="utf-8")
s = s[s.index("<main"):s.index("</main>")]
s = re.sub(r"<(pre|code|script|style)\b.*?</\1>", " ", s, flags=re.S)
t = html.unescape(re.sub(r"<[^>]+>", " ", s))
sin_formulas = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)", " ", t, flags=re.S)

PATRONES = {
    "dolar": (r"\$", sin_formulas),
    "barra_tex": (r"\\[a-zA-Z]{2,}", sin_formulas),
    "problema_N": (r"\bproblemas?\s+(con\s+Mathematica\s+)?\d", t),
    "otro_problema": (r"(problema anterior|otro problema|este bloque|siguiente problema)", t),
    "apartado": (r"apartado\s+(anterior|\(?\d)", t),
    "cuadro_N": (r"\bcuadros?\s+(T?\d)", t),
    "puntuacion": (r"\(\s*\d+([.,]\d+)?\s*(puntos?|ptos?)\s*\)|puntuaci[oó]n", t),
    "fuente": (r"\b(OCR|escane|copia digital|\(sic\)|editorial)\b", t),
}
total = 0
for nombre, (rx, texto) in PATRONES.items():
    hall = [texto[max(0, m.start() - 50):m.end() + 50].replace("\n", " ") for m in re.finditer(rx, texto, re.I)]
    total += len(hall)
    print(f"== {nombre}: {len(hall)}")
    for h in hall[:5]:
        print("   |", h)
print("Total:", total)
sys.exit(1 if total else 0)
