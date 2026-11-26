"""Construye public/index.html a partir de tema1..4.py y glosario.py.

Uso:  python3 montar.py
"""
import html, json, re, shutil, pathlib
import tema1, tema2, tema3, tema4, glosario, guias, formato, estandar

RAIZ = pathlib.Path(__file__).resolve().parent
SALIDA = RAIZ.parent / "public"
TEMAS = [tema1, tema2, tema3, tema4]
LETRAS = "abcdefgh"


ICONO = {
    "ideas": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.6 10.8c.7.6 1.1 1.3 1.1 2.2h5c0-.9.4-1.6 1.1-2.2A6 6 0 0 0 12 3Z"/></svg>',
    "teoria": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M8 8h8M8 12h5"/></svg>',
    "comandos": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="4" width="19" height="16" rx="2.5"/><path d="m6.5 9 3 3-3 3M12 15h5"/></svg>',
    "solucion": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h3M4 12h3M4 18h3"/><path d="M11 6h9M11 12h9M11 18h5"/><path d="m16.5 17.5 1.5 1.5 3-3"/></svg>',
    "profe": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="7" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M14 4h7v6h-4l-2 2v-2"/></svg>',
}
PUERTAS = {"ideas": "Ideas previas", "teoria": "Resultados teóricos", "comandos": "Comandos", "solucion": "Solución"}


def burbuja(html, quien="Profesor"):
    return (f'<div class="burbuja"><div class="avatar" aria-hidden="true">{ICONO["profe"]}</div>'
            f'<div class="globo"><div class="quien">{quien}</div><div>{html}</div></div></div>')


def partir_pasos(res):
    """Divide la resolución en pasos [(título, html)] a partir de los <div class="paso">."""
    trozos = res.split('<div class="paso">')[1:]
    pasos = []
    for t in trozos:
        t = t.strip()
        t = t[: t.rfind("</div>")]
        m = re.match(r"<h5>(.*?)</h5>(.*)", t, re.S)
        titulo = re.sub(r"^Paso \d+\.\s*", "", m.group(1))
        pasos.append((titulo, m.group(2).strip()))
    return pasos


def cuadros_teoria(pid, h):
    """Parte la teoría en cuadros con título (cada <p><b>Título.</b> abre uno) y añade un índice."""
    trozos = re.split(r'(?=<p><b>)', h.strip())
    cuadros = []
    for t in trozos:
        m = re.match(r'<p><b>(.*?)</b>\s*(.*)', t, re.S)
        if m:
            cuadros.append([m.group(1).rstrip('. '), '<p>' + m.group(2)])
        elif t.strip():
            if cuadros: cuadros[-1][1] += t
            else: cuadros.append(["Resultado", t])
    if len(cuadros) < 2:
        return h
    idx = "".join(f'<li><a href="#{pid}-c{i}" class="ir-cuadro">{tit}</a></li>' for i, (tit, _) in enumerate(cuadros))
    cajas = "".join(f'<section class="cuadro" id="{pid}-c{i}"><h6>{tit}</h6>{cu}</section>' for i, (tit, cu) in enumerate(cuadros))
    return f'<ul class="idx-teoria limpia">{idx}</ul>{cajas}'


def zona(pid, clave, cuerpo):
    return (f'<section class="zona z-{clave}" data-zona="{clave}" hidden>'
            f'<header class="zona-cab">{ICONO[clave]}<h5>{PUERTAS[clave]}</h5></header>'
            f'<div class="zona-cuerpo">{cuerpo}</div></section>')


def comandos_html(pid):
    items = []
    for i, (nec, pista, orden) in enumerate(guias.COMANDOS[pid]):
        items.append(f'<li class="cmd"><span class="cmd-nec">{html.escape(nec)}</span>'
                     f'<span class="cmd-bot"><button type="button" class="mini revelar" data-revela="{pid}-cp{i}">Pista</button>'
                     f'<button type="button" class="mini revelar" data-revela="{pid}-co{i}">Ver la orden</button></span>'
                     f'<span class="cmd-pista" id="{pid}-cp{i}" hidden>{html.escape(pista)}</span>'
                     f'<code class="cmd-orden" id="{pid}-co{i}" hidden>{html.escape(orden)}</code></li>')
    return ('<p class="nota">Antes de mirar la orden, intenta recordarla o búscala en el glosario. Abre primero la pista.</p>'
            f'<ol class="cmds">{"".join(items)}</ol>')


def solucion_html(p, pasos, tipo):
    pid, guia = p["id"], p.get("guia") or guias.GUIA[p["id"]]
    assert len(guia) == len(pasos), f"{pid}: {len(guia)} preguntas para {len(pasos)} pasos"
    n = len(pasos)
    resultados = re.findall(r'<p class="resultado">(.*?)</p>', p["resolucion"], re.S)
    final = "".join(f"<p>{r}</p>" for r in resultados)
    g, d = [], []
    f = p.get("ficha") or formato.FICHA[pid]
    obs = (f'<ul class="limpia obs"><li><b>Comprobación.</b> {f["comprob"]}</li>'
           f'<li><b>Error frecuente.</b> {f["error"]}</li></ul>')
    for i, ((tit, cuerpo), q) in enumerate(zip(pasos, guia)):
        q = dict(q, p=list(q["p"]) + ([formato.PISTA2[(pid, i)]] if (pid, i) in formato.PISTA2 else []))
        assert len(q["p"]) == 2, f"{pid} paso {i+1}: {len(q['p'])} pistas"
        pistas = "".join(
            f'<div class="ayuda-g" {"hidden" if j else ""}><button type="button" class="mini revelar" data-revela="{pid}-g{i}p{j}" data-siguiente="1">Pista {j+1}</button>'
            f'<div class="revelado" id="{pid}-g{i}p{j}" hidden>{burbuja(t, f"Pista {j+1}")}</div></div>'
            for j, t in enumerate(q["p"]))
        error = f'<div class="aviso"><div class="eti">Cuidado</div>{q["e"]}</div>' if q.get("e") else ""
        g.append(f'<section class="pantalla" data-k="{i+1}" hidden>'
                 f'<div class="tipo">Resolución guiada · paso {i+1} de {n}</div><h5>{tit}</h5>'
                 f'{burbuja(q["q"])}'
                 f'<label class="borrador" for="{pid}-b{i}"><span>Tus cuentas (no se guardan)</span>'
                 f'<textarea id="{pid}-b{i}" rows="3" placeholder="Escribe aquí tu idea o tu cálculo…"></textarea></label>'
                 f'<div class="ayudas-g">{pistas}'
                 f'<div class="ayuda-g"><button type="button" class="mini revelar" data-revela="{pid}-g{i}r">Comprobar mi respuesta</button>'
                 f'<div class="revelado" id="{pid}-g{i}r" hidden><div class="caja-sol"><div class="eti">Deberías haber llegado a</div>{q["r"]}</div>{error}</div></div>'
                 f'<div class="ayuda-g"><button type="button" class="mini revelar" data-revela="{pid}-g{i}c">Ver el paso resuelto</button>'
                 f'<div class="revelado" id="{pid}-g{i}c" hidden><div class="paso-completo"><div class="eti">Resolución del paso</div>{cuerpo}</div></div></div>'
                 f'</div></section>')
        d.append(f'<section class="pantalla" data-k="{i}" {"hidden" if i else ""}>'
                 f'<div class="tipo">Resolución directa · paso {i+1} de {n}</div><h5>{tit}</h5>{cuerpo}</section>')
    g.insert(0, f'<section class="pantalla" data-k="0"><div class="tipo">Resolución guiada</div><h5>Empezamos</h5>'
                f'{burbuja(f["bienvenida"])}<p class="nota">En cada paso te haré una pregunta. Piensa y escribe tus cuentas en papel o en el recuadro. '
                f'Pide pistas solo si te atascas, comprueba tu respuesta y, si quieres, mira el paso resuelto.</p></section>')
    g.append(f'<section class="pantalla" data-k="{n+1}" hidden><div class="tipo">Resolución guiada</div><h5>Resultado</h5>'
             f'<div class="caja-sol"><div class="eti">Respuesta</div>{final}</div>{burbuja(f["cierre"])}'
             f'<details class="recordatorio"><summary>Comprobación y observaciones</summary>{obs}</details></section>')
    d.append(f'<section class="pantalla" data-k="{n}" hidden><div class="tipo">Resolución directa</div><h5>Resultado</h5>'
             f'<div class="caja-sol"><div class="eti">Respuesta</div>{final}</div></section>')
    d.append(f'<section class="pantalla" data-k="{n+1}" hidden><div class="tipo">Para terminar</div><h5>Comprobación y observaciones</h5>{obs}</section>')
    return (f'<div class="solucion" data-k="0" data-n="{n+2}" data-modo="g">'
            '<div class="modo" role="group" aria-label="Formato de la solución">'
            '<button type="button" class="activo" data-modo="g">Resolución guiada</button>'
            '<button type="button" data-modo="d">Resolución directa</button></div>'
            f'<div class="barra-prog" aria-hidden="true"><div style="width:0%"></div></div>'
            f'<div class="pasos" data-pasos="g">{"".join(g)}</div>'
            f'<div class="pasos" data-pasos="d" hidden>{"".join(d)}</div>'
            '<footer class="nav"><button type="button" class="btn btn-sec" data-mover="-1" disabled>← Anterior</button>'
            f'<span class="cuenta">1 / {n+2}</span>'
            '<button type="button" class="btn" data-mover="1">Empezar →</button></footer></div>')


def problema(p, n, tipo):
    etiqueta = {"mano": "Sin software", "mma": "Mathematica", "est": "Ejercicio estándar"}[tipo]
    claves = ["ideas", "teoria"] + (["comandos"] if tipo == "mma" else []) + ["solucion"]
    pasos = partir_pasos(p["resolucion"])
    f = p.get("ficha") or formato.FICHA[p["id"]]
    cuerpos = {"ideas": p["ideas"], "teoria": cuadros_teoria(p["id"], p["teoria"]),
               "comandos": comandos_html(p["id"]) if tipo == "mma" else "",
               "solucion": solucion_html(p, pasos, tipo)}
    puertas = "".join(
        f'<button type="button" class="puerta p-{c}" data-abre="{c}" aria-expanded="false">{ICONO[c]}<span>{PUERTAS[c]}</span></button>'
        for c in claves)
    return (f'<article class="problema" id="{p["id"]}">'
            f'<header><span class="prob-n">{n}</span><div class="prob-tit"><h4>{p["titulo"]}</h4>'
            f'<div class="ficha"><span class="chip chip-{tipo}">{etiqueta}</span><span class="etq"><b>Tema</b> {p["id"][1]}</span>'
            f'<span class="etq"><b>Contenido</b> {f["etiqueta"]}</span><span class="etq"><b>Curso</b> 2023-24</span></div></div>'
            f'<span class="estrellas" title="Dificultad {f["dif"]} de 3" aria-label="Dificultad {f["dif"]} de 3">{"★"*f["dif"]}<span>{"★"*(3-f["dif"])}</span></span></header>'
            f'<div class="enunciado">{p["enunciado"]}</div>'
            f'<nav class="puertas n{len(claves)}" aria-label="Ayudas del problema {n}">{puertas}</nav>'
            f'{"".join(zona(p["id"], c, cuerpos[c]) for c in claves)}</article>')


def test(t, tid):
    out = []
    for k, q in enumerate(t, 1):
        varias = len(q["c"]) > 1
        tipo = "checkbox" if varias else "radio"
        aviso = "Varias respuestas correctas" if varias else "Una respuesta correcta"
        ops = "".join(
            f'<label class="op"><input type="{tipo}" name="{tid}-{k}" value="{i}"><span class="letra">{LETRAS[i]})</span><span>{o}</span></label>'
            for i, o in enumerate(q["o"]))
        out.append(f'<fieldset class="pregunta" data-correctas="{",".join(map(str, q["c"]))}">'
                   f'<legend><span class="num">{k}.</span> {q["q"]} <span class="tipo-p">{aviso}</span></legend>'
                   f'<div class="ops">{ops}</div><div class="explica" hidden><p class="veredicto"></p><p>{q["e"]}</p></div></fieldset>')
    return (f'<form class="test" id="{tid}" onsubmit="return false">{"".join(out)}'
            f'<div class="test-barra"><button type="button" class="btn" data-accion="corregir">Corregir test</button>'
            f'<button type="button" class="btn btn-sec" data-accion="reiniciar">Volver a empezar</button>'
            f'<p class="nota-test" aria-live="polite"></p></div></form>')


def seccion_tema(i, t):
    n = i + 1
    dif = lambda p: (p.get("ficha") or formato.FICHA[p["id"]])["dif"]
    est = "".join(problema(p, f"E{k}", "est") for k, p in enumerate(sorted(estandar.POR_TEMA[n], key=dif), 1))
    mano = "".join(problema(p, k, "mano") for k, p in enumerate(sorted(t.MANO, key=dif), 1))
    mma = "".join(problema(p, k + len(t.MANO), "mma") for k, p in enumerate(sorted(t.MMA, key=dif), 1))
    return f'''
<section class="vista" id="tema{n}" data-titulo="{html.escape(t.TITULO)}" hidden>
  <h2>{t.TITULO}</h2>
  <p class="entradilla">{t.RESUMEN}</p>
  <div class="pestanas" role="tablist">
    <button role="tab" class="pestana activa" data-panel="t{n}-est" aria-selected="true">Ejercicios estándar</button>
    <button role="tab" class="pestana" data-panel="t{n}-mano" aria-selected="false">Problemas sin software</button>
    <button role="tab" class="pestana" data-panel="t{n}-mma" aria-selected="false">Problemas con Mathematica</button>
    <button role="tab" class="pestana" data-panel="t{n}-test" aria-selected="false">Test de autoevaluación</button>
  </div>
  <div class="panel" id="t{n}-est">
    <p class="intro-panel">Ejercicios del mismo tipo que los de la relación del tema, con datos nuevos, para practicar la técnica básica sin software. Cada uno tiene ideas previas, resultados teóricos y solución guiada o directa.</p>
    {est}
  </div>
  <div class="panel" id="t{n}-mano" hidden>
    <p class="intro-panel">Problemas para resolver sin software, con lápiz y papel. Intenta cada uno antes de abrir las ayudas. En «Solución» puedes elegir la resolución guiada, en la que un profesor te pregunta y te da pistas, o la directa, paso a paso.</p>
    {mano}
  </div>
  <div class="panel" id="t{n}-mma" hidden>
    <p class="intro-panel">Problemas para resolver con Mathematica. Las órdenes no se dan de entrada: en «Comandos» y en la resolución guiada tienes pistas para encontrarlas. Las salidas pueden cambiar ligeramente de orden o de formato según la versión.</p>
    {mma}
  </div>
  <div class="panel" id="t{n}-test" hidden>
    <p class="intro-panel">Cada pregunta indica si tiene una o varias respuestas correctas. En las de varias, solo cuenta como acierto si marcas todas las correctas y ninguna incorrecta.</p>
    {test(t.TEST, f"test{n}")}
  </div>
</section>'''


def glosario_html():
    filas = []
    for cat, items in glosario.GLOSARIO:
        filas.append(f'<tr class="cat"><th colspan="4">{html.escape(cat)}</th></tr>')
        for orden, sint, desc, ej, temas in items:
            filas.append(f'<tr data-buscar="{html.escape((orden+" "+sint+" "+desc).lower())}">'
                         f'<td><code>{html.escape(orden)}</code></td><td><code>{html.escape(sint)}</code></td>'
                         f'<td>{html.escape(desc)}<div class="ej">Ejemplo: <code>{html.escape(ej)}</code></div></td>'
                         f'<td class="temas">{html.escape(temas)}</td></tr>')
    consejos = "".join(f"<li>{c}</li>" for c in glosario.CONSEJOS)
    return f'''
<section class="vista" id="glosario" data-titulo="Glosario de Mathematica" hidden>
  <h2>Glosario de comandos de Mathematica</h2>
  <p class="entradilla">Órdenes que se usan en las prácticas de la asignatura, agrupadas por tipo. Usa el buscador para filtrar.</p>
  <div class="buscador"><label for="buscar">Buscar comando</label><input id="buscar" type="search" placeholder="Por ejemplo: Eigenvalues, hessiana, Solve…"></div>
  <div class="tabla-wrap"><table class="glosario">
    <thead><tr><th>Orden</th><th>Sintaxis</th><th>Para qué sirve</th><th>Temas</th></tr></thead>
    <tbody>{"".join(filas)}</tbody>
  </table></div>
  <div class="caja-consejos"><h3>Errores frecuentes y consejos</h3><ul>{consejos}</ul></div>
</section>'''


def inicio_html():
    tarjetas = "".join(
        f'<a class="tarjeta" href="#tema{i+1}"><span class="t-num">Tema {i+1}</span>'
        f'<strong>{t.TITULO.split(". ",1)[1]}</strong><span class="ver">VER +</span><span>{len(estandar.POR_TEMA[i+1])} estándar · {len(t.MANO)} sin software · {len(t.MMA)} con Mathematica · {len(t.TEST)} preguntas</span></a>'
        for i, t in enumerate(TEMAS))
    formas = "".join(
        f'<span style="left:{x}%;top:{y}%;width:{w}px;height:{w}px;background:{c};opacity:{o}"></span>'
        for x, y, w, c, o in [(58, 12, 70, "#fda231", .95), (66, 30, 46, "#9cc4ea", .9), (74, 8, 90, "#ffffff", .12),
                              (82, 34, 60, "#fda231", .55), (90, 10, 40, "#9cc4ea", .7), (63, 52, 34, "#ffffff", .25),
                              (86, 56, 28, "#ffffff", .35), (52, 40, 22, "#9cc4ea", .5)])
    return f'''
<section class="vista" id="inicio" data-titulo="Presentación">
  <div class="banner" role="img" aria-label="Portada de Matemática Empresarial II">
    <div class="formas" aria-hidden="true">{formas}</div>
    <div class="rotulo" aria-hidden="true"><span class="r1">Grado en ADE</span><span class="r2">Matemática</span><span class="r3">Empresarial II</span></div>
    <div class="titulo-banner">Espacio de prácticas</div>
    <div class="texto-banner">Practicar Matemática Empresarial II es mucho más que repetir ejercicios: aquí encontrarás <b>problemas nuevos con ayudas guiadas</b>, prácticas con <b>Mathematica</b> y <b>test de autoevaluación</b> para cada tema.</div>
  </div>
  <h2>Presentación</h2>
  <p class="entradilla">Espacio de prácticas de <b>Matemática Empresarial II</b> (Grado en Administración y Dirección de Empresas). Los problemas son nuevos y siguen los contenidos de las relaciones de ejercicios de los Temas 1 a 4.</p>
  <div class="tarjetas">{tarjetas}
    <a class="tarjeta tarjeta-glos" href="#glosario"><span class="t-num">Recurso</span><strong>Glosario de comandos de Mathematica</strong><span class="ver">VER +</span><span>{sum(len(x[1]) for x in glosario.GLOSARIO)} órdenes con ejemplos</span></a>
  </div>
  <div class="caja-info">
    <h3>Cómo usar este espacio</h3>
    <ul>
      <li><b>Ejercicios estándar:</b> del mismo tipo que los de las relaciones de cada tema, con datos nuevos.</li>
      <li><b>Problemas sin software:</b> bajo cada enunciado hay tres botones: <b>Ideas previas</b>, <b>Resultados teóricos</b> y <b>Solución</b>. La solución puede ser guiada (un profesor te pregunta, te da pistas y te deja comprobar) o directa (paso a paso).</li>
      <li><b>Problemas con Mathematica:</b> tienen además el botón <b>Comandos</b>, con pistas para encontrar cada orden antes de verla.</li>
      <li><b>Test:</b> preguntas con una o varias respuestas correctas, que se corrigen al momento y explican la respuesta.</li>
    </ul>
  </div>
</section>'''


def pie_html():
    cols = []
    for i, t in enumerate(TEMAS):
        n = i + 1
        enlaces = "".join(f'<li><a href="#{p["id"]}">{p["titulo"]}</a></li>' for p in (t.MANO + t.MMA)[:3])
        cols.append(f'<div class="col"><h3>Tema {n}</h3><ul>{enlaces}<li><a href="#t{n}-test">Test del tema {n}</a></li></ul></div>')
    cats = "".join(f'<li><a href="#glosario">{c}</a></li>' for c, _ in glosario.GLOSARIO)
    cols.append(f'<div class="col"><h3>Glosario</h3><ul>{cats}</ul></div>')
    return "".join(cols)


def main():
    plantilla = (RAIZ / "plantilla.html").read_text(encoding="utf-8")
    menu = "".join(f'<li><a href="#tema{i+1}" data-vista="tema{i+1}">Tema {i+1}</a></li>' for i in range(4))
    lateral = "".join(
        f'<li><a href="#tema{i+1}" data-vista="tema{i+1}">Tema {i+1}. {t.TITULO.split(". ",1)[1]}</a></li>'
        for i, t in enumerate(TEMAS))
    lat_test = "".join(f'<li><a href="#t{i+1}-test">Test de autoevaluación del Tema {i+1}</a></li>' for i in range(4))
    cuerpo = inicio_html() + "".join(seccion_tema(i, t) for i, t in enumerate(TEMAS)) + glosario_html()
    pagina = (plantilla.replace("{{MENU}}", menu).replace("{{LATERAL}}", lateral).replace("{{LATERAL_TEST}}", lat_test)
              .replace("{{PIE}}", pie_html()).replace("{{CONTENIDO}}", cuerpo))
    SALIDA.mkdir(exist_ok=True)
    (SALIDA / "index.html").write_text(pagina, encoding="utf-8")
    shutil.copytree(RAIZ / "fig", SALIDA / "fig", dirs_exist_ok=True)
    print("Escrito", SALIDA / "index.html", len(pagina) // 1024, "KB")


if __name__ == "__main__":
    main()
