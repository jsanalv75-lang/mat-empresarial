# Matemática Empresarial II · Prácticas

Web de prácticas de Matemática Empresarial II (Grado en ADE): ejercicios estándar, problemas sin software
y con Mathematica con resolución guiada, test de autoevaluación y glosario de comandos.

- Web pública: https://mat-empresarial.pages.dev (Cloudflare Pages, se publica sola desde `main`; directorio de salida `public`)
- Web en Claude: https://claude.ai/artifact/McDR19e2hRRguVEJbfL5nv

## Estructura

```
public/          la web generada (index.html, fig/, katex/): es lo que publica Cloudflare
generador/       contenido y generador
  tema1-4.py     problemas sin software y con Mathematica, y test
  estandar.py    ejercicios estándar
  guias.py       resolución guiada (preguntas, pistas) y pistas de comandos
  formato.py     fichas: dificultad, etiquetas, bienvenida, cierre, comprobación
  glosario.py    glosario de Mathematica
  plantilla.html diseño de la página
  montar.py      construye public/index.html
  comprobar.py   recalcula con sympy todos los resultados
  auditar.py     reglas de limpieza (sin $, sin \comandos, sin referencias a otros problemas)
wrangler.jsonc   configuración para publicar como Worker (no se usa con Cloudflare Pages)
```

## Cambiar algo

```bash
python3 generador/montar.py
python3 generador/comprobar.py   # «Fallos: 0»
python3 generador/auditar.py     # «Total: 0»
git add -A && git commit -m "…" && git push
```

Cada push a `main` actualiza la web pública.
