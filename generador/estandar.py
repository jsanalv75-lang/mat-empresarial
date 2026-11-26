"""Ejercicios estándar por tema, del mismo tipo que los de las relaciones de la asignatura pero con datos nuevos.

Cada ejercicio lleva su resolución (pasos), su guía (una pregunta y dos pistas por paso) y su ficha.
"""


def E(id, titulo, enunciado, ideas, teoria, pasos, guia, ficha):
    """pasos: lista de (título, html, resultado o None). guia: lista de (pregunta, [p1, p2], respuesta, error)."""
    res = "".join(
        f'<div class="paso"><h5>Paso {i+1}. {t}</h5>{h}' + (f'<p class="resultado">{r}</p>' if r else "") + "</div>"
        for i, (t, h, r) in enumerate(pasos))
    g = [dict(q=q, p=p, r=r, **({"e": e} if e else {})) for q, p, r, e in guia]
    return dict(id=id, titulo=titulo, enunciado=enunciado, ideas=ideas, teoria=teoria, resolucion=res, guia=g, ficha=ficha)


T1 = [
E("t1e1", "De la matriz de Leontief a los flujos y los precios",
r"""<p>De una economía con tres sectores se conoce la matriz de Leontief</p>
\[ I-A=\begin{pmatrix} 0{,}8 & -0{,}2 & 0\\ -0{,}1 & 0{,}7 & -0{,}3\\ -0{,}2 & 0 & 0{,}9\end{pmatrix}. \]
<ol class="apartados">
<li>Obtenga la matriz tecnológica \(A\).</li>
<li>Si la producción total del sector 2 es de 60 unidades, calcule \(b_{12}\) e interprételo.</li>
<li>Calcule los valores añadidos netos unitarios si los precios son 10, 20 y 10 u.m.</li>
<li>Halle el sistema de precios que da los valores añadidos \(V=(5,5,6)\).</li>
</ol>""",
r"""<ul><li>\(A=I-(I-A)\): resta de la identidad.</li><li>\(b_{ij}=a_{ij}\,x_j\).</li><li>Precios y valores añadidos se relacionan con la traspuesta: \((I-A^t)P=V\).</li></ul>""",
r"""<p><b>Coeficientes técnicos.</b> \(a_{ij}=b_{ij}/x_j\), es decir, \(b_{ij}=a_{ij}x_j\).</p>
<p><b>Modelo de precios.</b> \((I-A^t)P=V\): para cada sector, precio menos coste unitario de los inputs intermedios.</p>""",
[("Matriz tecnológica", r"\[ A=I-(I-A)=\begin{pmatrix} 0{,}2 & 0{,}2 & 0\\ 0{,}1 & 0{,}3 & 0{,}3\\ 0{,}2 & 0 & 0{,}1\end{pmatrix}. \]", None),
 (r"Flujo \(b_{12}\)", r"<p>\(b_{12}=a_{12}\,x_2=0{,}2\cdot60=12\): el sector 2 utiliza 12 unidades del bien 1 para producir sus 60 unidades.</p>", r"\(b_{12}=12\)."),
 ("Valores añadidos", r"<p>\(v_j=p_j-\sum_i a_{ij}p_i\) (columnas de \(A\)):</p>\[ v_1=10-(0{,}2\cdot10+0{,}1\cdot20+0{,}2\cdot10)=4,\quad v_2=20-(0{,}2\cdot10+0{,}3\cdot20)=12,\quad v_3=10-(0{,}3\cdot20+0{,}1\cdot10)=3. \]", r"\(V=(4,\ 12,\ 3)\)."),
 (r"Precios para \(V=(5,5,6)\)", r"\[ \begin{cases}0{,}8p_1-0{,}1p_2-0{,}2p_3=5\\-0{,}2p_1+0{,}7p_2=5\\-0{,}3p_2+0{,}9p_3=6\end{cases} \]<p>Multiplicando por 10, de la segunda \(p_1=(7p_2-50)/2\) y de la tercera \(p_3=(60+3p_2)/9\). Sustituyendo en la primera se obtiene \(p_2=10\), y entonces \(p_1=10\), \(p_3=10\).</p>", r"\(P=(10,\ 10,\ 10)\).")],
[(r"¿Cómo recuperas \(A\) a partir de \(I-A\)?", [r"\(A=I-(I-A)\).", "En la diagonal, 1 menos el elemento; fuera de ella, cambia el signo."], r"\(A=\begin{pmatrix}0{,}2&0{,}2&0\\0{,}1&0{,}3&0{,}3\\0{,}2&0&0{,}1\end{pmatrix}\).", None),
 (r"¿Qué relación hay entre \(b_{12}\), \(a_{12}\) y \(x_2\)?", [r"\(a_{12}=b_{12}/x_2\).", r"\(a_{12}=0{,}2\) y \(x_2=60\)."], r"\(b_{12}=12\): unidades del bien 1 que usa el sector 2.", None),
 ("Para el sector 1, ¿cuánto cuestan los inputs de una unidad de su producto?", [r"Usa la columna 1 de \(A\) y los precios de cada bien.", r"\(0{,}2\cdot10+0{,}1\cdot20+0{,}2\cdot10=6\)."], r"\(V=(4,12,3)\).", r"Usar las filas de \(A\) (es decir, \(I-A\) en lugar de \(I-A^t\))."),
 (r"Escribe el sistema \((I-A^t)P=V\). ¿Qué ecuación tiene menos incógnitas?", [r"La segunda solo tiene \(p_1\) y \(p_2\), y la tercera solo \(p_2\) y \(p_3\).", r"Expresa \(p_1\) y \(p_3\) en función de \(p_2\) y sustituye en la primera."], r"\(P=(10,10,10)\).", None)],
dict(dif=1, etiqueta="Modelo de precios",
 bienvenida="Vamos a pasar de la matriz de Leontief a la tecnológica y a usarla para obtener flujos, valores añadidos y precios.",
 cierre=r"\(A\) se obtiene restando de la identidad. Los valores añadidos se calculan por columnas: \(V=(I-A^t)P\).",
 comprob=r"Con \(P=(10,10,10)\), \(V=10\,(1-s_j)\), donde \(s_j\) son las sumas por columnas de \(A\): \(10\cdot(0{,}5;\ 0{,}5;\ 0{,}4)=(5,5,6)\) ✓.",
 error=r"Confundir \(b_{12}\) (del bien 1 al sector 2) con \(b_{21}\).")),

E("t1e2", "Productividad por los tres métodos",
r"""<p>Estudie la productividad de las siguientes matrices tecnológicas mediante el Teorema de Brauer-Solow, la condición de Hawkins-Simon y la definición:</p>
\[ A=\begin{pmatrix}0{,}3&0{,}2&0{,}1\\0{,}1&0{,}4&0{,}2\\0{,}2&0{,}1&0{,}3\end{pmatrix},\quad
B=\begin{pmatrix}0{,}6&0{,}3&0{,}2\\0{,}2&0{,}5&0{,}1\\0{,}3&0{,}4&0{,}6\end{pmatrix},\quad
C=\begin{pmatrix}0{,}5&0{,}4&0{,}1\\0{,}2&0{,}3&0{,}2\\0{,}4&0{,}1&0{,}6\end{pmatrix}. \]""",
r"""<ul><li>Empieza siempre por Brauer-Solow: es el más rápido, pero solo puede dar una respuesta afirmativa.</li><li>Si no decide, calcula los menores principales de \(I-M\).</li><li>La definición exige que \((I-M)^{-1}\) exista y sea no negativa.</li></ul>""",
r"""<p><b>Definición.</b> \(M\ge0\) es productiva si \((I-M)^{-1}\) existe y es \(\ge0\).</p>
<p><b>Hawkins-Simon.</b> \(M\) es productiva \(\iff\) todos los menores principales de \(I-M\) son positivos.</p>
<p><b>Brauer-Solow.</b> Si todas las sumas por filas, o todas por columnas, son menores que 1, \(M\) es productiva. Es una condición suficiente, no necesaria.</p>""",
[(r"Matriz \(A\)", r"<p>Filas: \(0{,}6;\ 0{,}7;\ 0{,}6<1\). Por Brauer-Solow, \(A\) es productiva. Hawkins-Simon: \(\Delta=(0{,}7;\ 0{,}4;\ 0{,}245)\), todos positivos. La inversa de \(I-A\) tiene todos sus elementos positivos (el menor es \(20/49\)).</p>", r"\(A\) es productiva por los tres métodos."),
 (r"Matriz \(B\)", r"<p>Filas: \(1{,}1;\ 0{,}8;\ 1{,}3\); columnas: \(1{,}1;\ 1{,}2;\ 0{,}9\). Brauer-Solow no decide. Hawkins-Simon: \(\Delta_1=0{,}4\), \(\Delta_2=0{,}14\), \(\Delta_3=-0{,}015<0\).</p><p>La inversa existe, pero tiene elementos negativos.</p>", r"\(B\) no es productiva."),
 (r"Matriz \(C\)", r"<p>Filas: \(1;\ 0{,}7;\ 1{,}1\); columnas: \(1{,}1;\ 0{,}8;\ 0{,}9\). Brauer-Solow no decide. Hawkins-Simon: \(\Delta=(0{,}5;\ 0{,}27;\ 0{,}036)\), todos positivos, y la inversa es no negativa.</p>", r"\(C\) es productiva aunque Brauer-Solow no lo detecte.")],
[(r"Para \(A\), calcula las sumas por filas. ¿Qué concluyes? Confírmalo con los menores principales de \(I-A\).", ["Todas las sumas por filas son menores que 1.", r"\(\Delta_2=0{,}7\cdot0{,}6-0{,}1\cdot0{,}2\)."], r"Productiva: \(\Delta=(0{,}7;\ 0{,}4;\ 0{,}245)\).", None),
 (r"En \(B\), ¿decide Brauer-Solow? Calcula los menores de \(I-B\).", ["Hay sumas mayores que 1 por filas y por columnas.", r"\(\Delta_3=\det(I-B)\); desarrolla por la primera fila."], r"\(\Delta_3=-0{,}015<0\): no productiva.", "Concluir que no es productiva solo porque falla Brauer-Solow."),
 (r"En \(C\) también falla Brauer-Solow. ¿Es productiva?", [r"Calcula \(\Delta_1\), \(\Delta_2\) y \(\Delta_3\) de \(I-C\).", "Si todos son positivos, sí lo es."], r"\(\Delta=(0{,}5;\ 0{,}27;\ 0{,}036)\): productiva.", None)],
dict(dif=1, etiqueta="Productividad",
 bienvenida="Vamos a practicar los tres métodos para estudiar la productividad con tres matrices que dan resultados distintos.",
 cierre="Brauer-Solow solo puede decir «sí». Si no decide, Hawkins-Simon o la definición dan la respuesta.",
 comprob=r"Para \(B\), \(\det(I-B)=0{,}4(0{,}5\cdot0{,}4-0{,}04)+0{,}3(-0{,}08-0{,}03)-0{,}2(0{,}08+0{,}15)=0{,}064-0{,}033-0{,}046=-0{,}015\).",
 error=r"Calcular los menores de \(M\) en vez de los de \(I-M\).")),

E("t1e3", "Conjuntos autónomos y descomponibilidad",
r"""<p>Determine los conjuntos autónomos y los productos fundamentales de las siguientes matrices tecnológicas, y estudie su descomponibilidad:</p>
\[ C=\begin{pmatrix}0{,}2&0&0\\0{,}3&0{,}4&0{,}1\\0{,}1&0{,}2&0{,}5\end{pmatrix},\quad
D=\begin{pmatrix}0{,}1&0{,}2&0{,}3\\0{,}2&0{,}1&0{,}4\\0{,}3&0{,}2&0{,}1\end{pmatrix},\quad
E=\begin{pmatrix}0{,}3&0&0{,}2\\0&0{,}4&0\\0{,}1&0&0{,}2\end{pmatrix}. \]""",
r"""<ul><li>Un conjunto \(J\) es autónomo si las columnas de sus sectores tienen ceros en las filas de fuera de \(J\).</li><li>Si la matriz no tiene ceros, solo \(N\) es autónomo.</li><li>Los productos fundamentales, si existen, forman el menor conjunto autónomo; si hay dos autónomos sin elementos comunes, no hay ninguno.</li></ul>""",
r"""<p><b>Conjunto autónomo.</b> \(J\) es autónomo si \(a_{ji}=0\) para todo \(i\in J\) y \(j\notin J\).</p>
<p><b>Descomponibilidad.</b> \(A\) es descomponible si existe un conjunto autónomo distinto de \(N\).</p>
<p><b>Productos fundamentales.</b> El bien \(i\) es fundamental si se usa, directa o indirectamente, en todos los sectores. Un producto fundamental pertenece a todos los conjuntos autónomos.</p>""",
[(r"Matriz \(C\)", r"<p>\(\{2,3\}\): columnas 2 y 3 en la fila 1, \(a_{12}=a_{13}=0\), autónomo. \(\{1\}\), \(\{2\}\), \(\{3\}\), \(\{1,2\}\) y \(\{1,3\}\) no lo son (por ejemplo, \(a_{21}=0{,}3\), \(a_{32}=0{,}2\), \(a_{23}=0{,}1\)).</p><p>Los bienes 2 y 3 los usan todos los sectores (filas 2 y 3 sin ceros): son fundamentales.</p>", r"Autónomos: \(\{2,3\}\) y \(N\). Descomponible. Fundamentales: 2 y 3."),
 (r"Matriz \(D\)", r"<p>No tiene ceros: ningún subconjunto propio es autónomo.</p>", r"Solo \(N\) es autónomo. Indescomponible: los tres bienes son fundamentales."),
 (r"Matriz \(E\)", r"<p>\(\{2\}\): \(a_{12}=a_{32}=0\), autónomo. \(\{1,3\}\): \(a_{21}=a_{23}=0\), autónomo. El sector 2 solo usa el bien 2, y los sectores 1 y 3 no usan el bien 2.</p><p>Como \(\{2\}\) y \(\{1,3\}\) no tienen elementos comunes, ningún bien está en todos los conjuntos autónomos.</p>", r"Autónomos: \(\{2\}\), \(\{1,3\}\) y \(N\). Descomponible. No hay productos fundamentales.")],
[(r"En \(C\), la fila 1 tiene ceros en las columnas 2 y 3. ¿Qué conjunto autónomo sugiere?", ["Los sectores 2 y 3 no compran el bien 1.", r"Comprueba también \(\{2\}\) y \(\{3\}\): mira \(a_{32}\) y \(a_{23}\)."], r"Autónomos: \(\{2,3\}\) y \(N\); fundamentales 2 y 3.", None),
 (r"¿Qué ocurre si una matriz no tiene ningún cero?", ["Todo sector compra a todos los demás.", "Ningún subconjunto propio puede cumplir la condición."], r"\(D\) es indescomponible y todos sus bienes son fundamentales.", None),
 (r"En \(E\), ¿qué sectores compran el bien 2? ¿Y qué compra el sector 2?", ["Mira la fila 2 y la columna 2.", "Si hay dos conjuntos autónomos sin elementos comunes, ¿puede un bien estar en todos?"], r"Autónomos \(\{2\}\), \(\{1,3\}\) y \(N\); no hay productos fundamentales.", "Tomar como fundamentales los bienes del menor conjunto autónomo cuando hay dos que no se cortan.")],
dict(dif=2, etiqueta="Conjuntos autónomos",
 bienvenida="Vamos a buscar conjuntos autónomos en tres matrices con estructuras distintas: con un bloque de ceros, sin ceros y con dos bloques separados.",
 cierre="Los ceros de las columnas deciden qué conjuntos son autónomos. Sin ceros, la matriz es indescomponible; con dos bloques separados, no hay productos fundamentales.",
 comprob=r"En \(E\), reordenando los sectores como \((1,3,2)\) la matriz queda en dos bloques diagonales: \(\begin{pmatrix}0{,}3&0{,}2\\0{,}1&0{,}2\end{pmatrix}\) y \((0{,}4)\).",
 error=r"Mirar las filas de los sectores de \(J\) en lugar de sus columnas.")),

E("t1e4", "Completar una tabla input-output",
r"""<p>Complete la siguiente tabla input-output y calcule la matriz tecnológica:</p>
<div class="tabla-wrap"><table class="io">
<tr><th>Sectores</th><th>1</th><th>2</th><th>3</th><th>DI</th><th>DF</th><th>Output</th></tr>
<tr><th>1</th><td>8</td><td></td><td>4</td><td>22</td><td></td><td>40</td></tr>
<tr><th>2</th><td>12</td><td>5</td><td></td><td></td><td>25</td><td>50</td></tr>
<tr><th>3</th><td></td><td>15</td><td>8</td><td>27</td><td>13</td><td></td></tr>
<tr><th>CI</th><td></td><td></td><td></td><td colspan="3"></td></tr>
<tr><th>IP</th><td>16</td><td></td><td></td><td colspan="3"></td></tr>
<tr><th>Input total</th><td></td><td></td><td></td><td colspan="3"></td></tr>
</table></div>
<p>¿Cuántas unidades del bien 3 necesita el sector 2 por cada unidad que produce?</p>""",
r"""<ul><li>Cada fila: suma de flujos = DI, y DI + DF = output.</li><li>Cada columna: suma = CI, y CI + IP = input total = output del sector.</li><li>Empieza por las filas que tienen un solo hueco.</li></ul>""",
r"""<p><b>Relaciones de la tabla.</b> \(\text{DI}_i=\sum_j b_{ij}\), \(x_i=\text{DI}_i+d_i\), \(\text{CI}_j=\sum_i b_{ij}\), \(x_j=\text{CI}_j+\text{IP}_j\).</p>
<p><b>Coeficientes técnicos.</b> \(a_{ij}=b_{ij}/x_j\).</p>""",
[("Filas", r"<p>Fila 1: \(b_{12}=22-8-4=10\) y \(d_1=40-22=18\). Fila 2: \(\text{DI}_2=50-25=25\), así que \(b_{23}=25-12-5=8\). Fila 3: \(b_{31}=27-15-8=4\) y \(x_3=27+13=40\).</p>", None),
 ("Columnas", r"<p>\(\text{CI}=(8+12+4,\ 10+5+15,\ 4+8+8)=(24,30,20)\). Input total = output: \((40,50,40)\). Input primario: \(\text{IP}=(16,20,20)\).</p>", r"\(\text{CI}=(24,30,20)\), \(\text{IP}=(16,20,20)\)."),
 ("Matriz tecnológica", r"\[ A=\begin{pmatrix}8/40&10/50&4/40\\12/40&5/50&8/40\\4/40&15/50&8/40\end{pmatrix}=\begin{pmatrix}0{,}2&0{,}2&0{,}1\\0{,}3&0{,}1&0{,}2\\0{,}1&0{,}3&0{,}2\end{pmatrix}. \]<p>\(a_{32}=0{,}3\): el sector 2 necesita 0,3 unidades del bien 3 por unidad producida.</p>", r"\(a_{32}=0{,}3\).")],
[("¿Qué filas tienen un solo hueco? Complétalas.", ["En la fila 1 conoces la DI y dos flujos.", "En la fila 2, la DI sale de output − DF; en la fila 3, el output sale de DI + DF."], r"\(b_{12}=10\), \(d_1=18\), \(b_{23}=8\), \(b_{31}=4\), \(x_3=40\).", None),
 ("Con la parte central completa, ¿cómo obtienes CI e IP?", ["Suma cada columna.", "El input total de cada sector es su output."], r"\(\text{CI}=(24,30,20)\), \(\text{IP}=(16,20,20)\).", None),
 (r"¿Entre qué divides \(b_{32}\) para obtener \(a_{32}\)?", ["Entre el output del sector que compra, el 2.", r"\(15/50\)."], r"\(a_{32}=0{,}3\).", r"Dividir entre \(x_3\) en lugar de entre \(x_2\).")],
dict(dif=1, etiqueta="Tabla input-output",
 bienvenida="Vamos a completar una tabla con huecos usando las relaciones entre filas y columnas, y a calcular su matriz tecnológica.",
 cierre="Las filas cuadran ventas (DI + DF = output) y las columnas, compras (CI + IP = input total). Empieza siempre por donde solo falte un dato.",
 comprob=r"\(\text{IP}_1=40-24=16\), que coincide con el dato de la tabla.",
 error="Olvidar que el input total de cada sector es su output."))
]

T2 = [
E("t2e1", "Comprobar autovectores",
r"""<p>Dada \(A=\begin{pmatrix}2&0&1\\0&3&0\\1&0&2\end{pmatrix}\), compruebe cuáles de los vectores \((1,0,-1)\), \((0,2,0)\), \((1,1,1)\), \((1,0,0)\) y \((2,0,2)\) son autovectores de \(A\), indicando el autovalor asociado.</p>""",
r"""<ul><li>Multiplica \(A\) por cada vector.</li><li>Es autovector si el resultado es un múltiplo del vector (y el vector no es nulo).</li></ul>""",
r"""<p><b>Autovector.</b> \(v\ne0\) es autovector de \(A\) si existe \(\lambda\in\mathbb R\) con \(Av=\lambda v\); \(\lambda\) es el autovalor asociado.</p>""",
[("Productos", r"\[ A(1,0,-1)=(1,0,-1),\ A(0,2,0)=(0,6,0),\ A(1,1,1)=(3,3,3),\ A(1,0,0)=(2,0,1),\ A(2,0,2)=(6,0,6). \]", None),
 ("Conclusión", r"<p>\((1,0,-1)\) con \(\lambda=1\); \((0,2,0)\), \((1,1,1)\) y \((2,0,2)\) con \(\lambda=3\). \((1,0,0)\) no es autovector: \((2,0,1)\) no es múltiplo de \((1,0,0)\).</p>", r"Autovectores: \((1,0,-1)\) (\(\lambda=1\)), \((0,2,0)\), \((1,1,1)\), \((2,0,2)\) (\(\lambda=3\)).")],
[(r"Calcula \(Av\) para cada vector.", ["Multiplica fila por columna.", r"Por ejemplo, \(A(1,1,1)=(2+1,\ 3,\ 1+2)\)."], r"\((1,0,-1)\), \((0,6,0)\), \((3,3,3)\), \((2,0,1)\), \((6,0,6)\).", None),
 ("¿Qué resultados son múltiplos del vector de partida?", ["Compara componente a componente.", r"\((2,0,1)\) no es múltiplo de \((1,0,0)\): la tercera componente no es 0."], r"Cuatro autovectores: uno con \(\lambda=1\) y tres con \(\lambda=3\).", r"Olvidar que \((2,0,2)\) es autovector por ser múltiplo de \((1,0,1)\).")],
dict(dif=1, etiqueta="Autovectores",
 bienvenida="Vamos a aplicar la definición de autovector: multiplicar y comparar.",
 cierre=r"Para comprobar si \(v\) es autovector basta un producto: no hace falta calcular los autovalores.",
 comprob=r"La traza de \(A\) es \(7=1+3+3\), la suma de sus autovalores.",
 error="Considerar autovector cualquier vector cuya imagen tenga alguna componente proporcional.")),

E("t2e2", "Parámetros para que un vector sea autovector",
r"""<p>Calcule los parámetros para que, en cada caso, el vector dado sea autovector de la matriz, e indique el autovalor asociado:</p>
\[ \text{(a) } A=\begin{pmatrix}a&1&0\\1&2&1\\0&1&a\end{pmatrix},\ v=(1,1,1);\qquad
\text{(b) } B=\begin{pmatrix}2&b&1\\0&3&b\\1&0&c\end{pmatrix},\ w=(1,0,1). \]""",
r"""<ul><li>Calcula \(Av\) en función de los parámetros.</li><li>Iguala a \(\lambda v\) componente a componente: sale un sistema en los parámetros y \(\lambda\).</li></ul>""",
r"""<p>\(v\) es autovector asociado a \(\lambda\) \(\iff (A-\lambda I)v=0\iff Av=\lambda v\).</p>""",
[("Apartado (a)", r"<p>\(Av=(a+1,\ 4,\ a+1)=\lambda(1,1,1)\). La segunda componente da \(\lambda=4\), y entonces \(a+1=4\).</p>", r"\(a=3\), \(\lambda=4\)."),
 ("Apartado (b)", r"<p>\(Bw=(3,\ b,\ 1+c)=\lambda(1,0,1)\). Entonces \(\lambda=3\), \(b=0\) y \(1+c=3\).</p>", r"\(b=0\), \(c=2\), \(\lambda=3\).")],
[(r"Calcula \(Av\) con \(v=(1,1,1)\). ¿Qué componente fija \(\lambda\)?", [r"Suma cada fila de \(A\).", r"La segunda componente no depende de \(a\)."], r"\(\lambda=4\) y \(a=3\).", None),
 (r"Calcula \(Bw\). ¿Qué te dice la componente que debe ser 0?", [r"La segunda componente de \(w\) es 0, luego la de \(Bw\) también.", r"La primera componente da \(\lambda\); la tercera, \(c\)."], r"\(b=0\), \(c=2\), \(\lambda=3\).", None)],
dict(dif=1, etiqueta="Autovectores con parámetros",
 bienvenida="Vamos a imponer que un vector sea autovector y despejar los parámetros.",
 cierre=r"Imponer \(Av=\lambda v\) da un sistema; casi siempre una componente sin parámetros fija \(\lambda\).",
 comprob=r"Con \(a=3\): \(A(1,1,1)=(4,4,4)\) ✓. Con \(b=0\), \(c=2\): \(B(1,0,1)=(3,0,3)\) ✓.",
 error=r"Olvidar que \(\lambda\) también es una incógnita.")),

E("t2e3", "Diagonalización según un parámetro",
r"""<p>Estudie para qué valores de \(a\in\mathbb R\) es diagonalizable la matriz \(A=\begin{pmatrix}1&a&0\\0&1&0\\0&0&2\end{pmatrix}\). Cuando lo sea, dé una matriz diagonal semejante y una matriz de paso.</p>""",
r"""<ul><li>Es triangular: los autovalores están en la diagonal.</li><li>El autovalor doble decide: estudia el rango de \(A-I\) según \(a\).</li></ul>""",
r"""<p>\(A\) es diagonalizable \(\iff\) para cada autovalor \(\lambda\) de multiplicidad \(m\), \(n-\operatorname{rg}(A-\lambda I)=m\).</p>""",
[("Autovalores", r"<p>\(\lambda=1\) doble y \(\lambda=2\) simple.</p>", None),
 (r"Rango de \(A-I\)", r"\[ A-I=\begin{pmatrix}0&a&0\\0&0&0\\0&0&1\end{pmatrix}. \]<p>Si \(a\ne0\), rango 2: un solo autovector para \(\lambda=1\), no diagonalizable. Si \(a=0\), rango 1: dos autovectores.</p>", r"Diagonalizable solo si \(a=0\)."),
 (r"Caso \(a=0\)", r"<p>\(A\) ya es diagonal: \(D=A=\operatorname{diag}(1,1,2)\) y \(P=I\).</p>", r"Con \(a=0\): \(D=\operatorname{diag}(1,1,2)\), \(P=I\).")],
[("¿Cuáles son los autovalores y sus multiplicidades?", ["La matriz es triangular.", "Lee la diagonal."], r"\(\lambda=1\) (doble), \(\lambda=2\) (simple).", None),
 (r"¿Cómo depende de \(a\) el rango de \(A-I\)?", [r"Si \(a\ne0\), hay dos filas no nulas independientes.", r"Autovectores \(=3-\text{rango}\)."], r"Diagonalizable \(\iff a=0\).", r"Olvidar el caso \(a=0\)."),
 (r"Para \(a=0\), ¿qué forma tiene \(A\)?", ["Fíjate en los elementos fuera de la diagonal.", "Una matriz diagonal es su propia forma diagonal."], r"\(D=A\), \(P=I\).", None)],
dict(dif=2, etiqueta="Diagonalización con parámetro",
 bienvenida="Vamos a discutir la diagonalización de una matriz según un parámetro, fijándonos en el autovalor doble.",
 cierre=r"Con autovalores múltiples, el rango de \(A-\lambda I\) decide; cualquier parámetro que lo cambie cambia la respuesta.",
 comprob=r"Con \(a=1\), \(A-I\) tiene rango 2: solo el autovector \((1,0,0)\) para \(\lambda=1\).",
 error="Pensar que una matriz triangular siempre es diagonalizable.")),

E("t2e4", "Clasificar formas cuadráticas",
r"""<p>Halle la matriz simétrica y clasifique, por menores principales y por autovalores, las formas cuadráticas</p>
\[ q_1=x^2+2y^2+3z^2+2xy,\qquad q_2=-x^2-2y^2-z^2+2xz,\qquad q_3=x^2-y^2+4yz. \]
<p>Clasifique además \(q_3\) restringida al subespacio \(z=y\).</p>""",
r"""<ul><li>Términos cruzados a medias fuera de la diagonal.</li><li>Si el último menor principal es 0, usa autovalores.</li><li>Para restringir, sustituye \(z=y\).</li></ul>""",
r"""<p><b>Menores principales.</b> Todos \(>0\): DP. Alternados empezando por negativo: DN. \(\Delta_n\ne0\) en otro caso: indefinida. Si \(\Delta_n=0\), pueden no decidir.</p>
<p><b>Autovalores.</b> Signos de los autovalores: todos positivos DP, todos negativos DN, positivos y ceros semidefinida positiva, negativos y ceros semidefinida negativa, de distinto signo indefinida.</p>""",
[(r"Forma \(q_1\)", r"<p>\(A_1=\begin{pmatrix}1&1&0\\1&2&0\\0&0&3\end{pmatrix}\), \(\Delta=(1,1,3)\).</p>", r"\(q_1\) definida positiva."),
 (r"Forma \(q_2\)", r"<p>\(A_2=\begin{pmatrix}-1&0&1\\0&-2&0\\1&0&-1\end{pmatrix}\), \(\Delta=(-1,2,0)\): los menores no deciden. Autovalores: \(-2\) (doble) y \(0\).</p>", r"\(q_2\) semidefinida negativa."),
 (r"Forma \(q_3\) y su restricción", r"<p>\(A_3=\begin{pmatrix}1&0&0\\0&-1&2\\0&2&0\end{pmatrix}\), \(\Delta=(1,-1,-4)\): indefinida. Con \(z=y\): \(q_3=x^2-y^2+4y^2=x^2+3y^2\).</p>", r"\(q_3\) indefinida; restringida a \(z=y\), definida positiva.")],
[(r"Escribe \(A_1\) y calcula sus menores. ¿Qué patrón ves?", [r"El término \(2xy\) da 1 en las posiciones \((1,2)\) y \((2,1)\).", "Todos positivos."], r"DP.", None),
 (r"En \(A_2\), \(\Delta_3=0\). ¿Qué haces entonces?", ["Calcula los autovalores.", r"\(y\) va sola: un autovalor es \(-2\); el bloque de \(x,z\) da \(-2\) y \(0\)."], r"Autovalores \(-2,-2,0\): semidefinida negativa.", r"Declararla definida negativa por los signos de \(\Delta_1\) y \(\Delta_2\)."),
 (r"Clasifica \(q_3\) y después sustituye \(z=y\).", [r"\(\Delta_2=-1<0\).", r"\(4yz\) pasa a ser \(4y^2\)."], r"Indefinida; restringida, \(x^2+3y^2\), DP.", None)],
dict(dif=2, etiqueta="Clasificación de formas cuadráticas",
 bienvenida="Vamos a clasificar tres formas cuadráticas, una de ellas con un caso que los menores principales no resuelven.",
 cierre=r"Si \(\Delta_n=0\), los menores principales no bastan: pasa a los autovalores.",
 comprob=r"\(q_2=-(x-z)^2-2y^2\le0\), y vale 0 en \((1,0,1)\): semidefinida negativa.",
 error=r"Clasificar una forma con \(\Delta_n=0\) solo por los primeros menores.")),
]

T3 = [
E("t3e1", "Derivadas parciales y matriz hessiana",
r"""<p>Calcule, sin ayuda de software, las derivadas parciales de primer y segundo orden y la matriz hessiana de</p>
\[ f(x,y)=x^3y^2-4xy,\qquad g(x,y)=\ln(x^2+y),\qquad h(x,y,z)=x\,e^{yz}. \]
<p>Evalúe la hessiana de \(f\) en \((1,2)\).</p>""",
r"""<ul><li>Deriva respecto de una variable tratando las demás como constantes.</li><li>En \(g\), aplica la regla de la cadena para el logaritmo.</li><li>Las derivadas cruzadas coinciden (Schwarz): sirve de comprobación.</li></ul>""",
r"""<p><b>Hessiana.</b> \(Hf=\left(\dfrac{\partial^2 f}{\partial x_i\partial x_j}\right)\); si las derivadas segundas son continuas, es simétrica.</p>
<p><b>Regla de la cadena.</b> \(\dfrac{\partial}{\partial x}\ln u=\dfrac{u_x}{u}\).</p>""",
[(r"Función \(f\)", r"\[ f_x=3x^2y^2-4y,\quad f_y=2x^3y-4x,\quad Hf=\begin{pmatrix}6xy^2&6x^2y-4\\6x^2y-4&2x^3\end{pmatrix},\quad Hf(1,2)=\begin{pmatrix}24&8\\8&2\end{pmatrix}. \]", r"\(Hf(1,2)=\begin{pmatrix}24&8\\8&2\end{pmatrix}\)."),
 (r"Función \(g\)", r"\[ g_x=\frac{2x}{x^2+y},\quad g_y=\frac{1}{x^2+y},\quad Hg=\frac{1}{(x^2+y)^2}\begin{pmatrix}2(y-x^2)&-2x\\-2x&-1\end{pmatrix},\quad x^2+y>0. \]", None),
 (r"Función \(h\)", r"\[ \nabla h=(e^{yz},\ xze^{yz},\ xye^{yz}),\quad Hh=e^{yz}\begin{pmatrix}0&z&y\\z&xz^2&x(1+yz)\\y&x(1+yz)&xy^2\end{pmatrix}. \]", None)],
[(r"Deriva \(f\) respecto de \(x\) y de \(y\), y después otra vez. Evalúa en \((1,2)\).", [r"\(f_{xx}=6xy^2\), \(f_{yy}=2x^3\).", r"\(f_{xy}=6x^2y-4\); en \((1,2)\) vale 8."], r"\(Hf(1,2)=\begin{pmatrix}24&8\\8&2\end{pmatrix}\).", None),
 (r"Deriva \(g=\ln(x^2+y)\). ¿Qué regla necesitas?", [r"La derivada de \(\ln u\) es \(u'/u\).", r"Para \(g_{xx}\), usa la regla del cociente con \(2x/(x^2+y)\)."], r"\(g_{xx}=\dfrac{2(y-x^2)}{(x^2+y)^2}\), \(g_{xy}=\dfrac{-2x}{(x^2+y)^2}\), \(g_{yy}=\dfrac{-1}{(x^2+y)^2}\).", r"Olvidar que \(g\) solo existe si \(x^2+y>0\)."),
 (r"Deriva \(h=xe^{yz}\). ¿Cuál es \(h_{yz}\)?", [r"\(h_y=xze^{yz}\).", r"Deriva \(xz\,e^{yz}\) respecto de \(z\) como un producto."], r"\(h_{yz}=x(1+yz)e^{yz}\).", None)],
dict(dif=1, etiqueta="Derivadas parciales",
 bienvenida="Vamos a practicar derivadas parciales y hessianas con tres funciones de tipo distinto: polinómica, logarítmica y exponencial.",
 cierre="Las derivadas cruzadas deben coincidir: es la mejor comprobación de que la hessiana está bien.",
 comprob=r"En \(f\), \(f_{xy}\) y \(f_{yx}\) dan las dos \(6x^2y-4\).",
 error=r"En \(h\), derivar \(e^{yz}\) respecto de \(y\) y olvidar el factor \(z\).")),

E("t3e2", "Tasas marginales de sustitución",
r"""<ol class="apartados">
<li>La utilidad de un consumidor es \(u(x,y,z)=x^2yz\) y consume \((2,3,1)\). ¿A qué cantidad del bien 1 renunciaría por una unidad más del bien 3, manteniendo la utilidad?</li>
<li>La producción de una empresa es \(f(K,L)=10\sqrt{K}\sqrt{L}\). Con \(K=9\) y \(L=4\), calcule la tasa marginal de sustitución de trabajo por capital e interprétela.</li>
</ol>""",
r"""<ul><li>La cantidad que se cede de un bien por una unidad más de otro es el cociente de utilidades marginales: la del bien que se gana entre la del que se cede.</li><li>Simplifica el cociente antes de sustituir.</li></ul>""",
r"""<p>Sobre una curva de nivel \(u=\text{cte}\), con las demás variables fijas: \(-\dfrac{dx}{dz}=\dfrac{u_z}{u_x}\).</p>""",
[("Utilidad", r"<p>\(u_x=2xyz\) y \(u_z=x^2y\), así que \(\dfrac{u_z}{u_x}=\dfrac{x}{2z}=\dfrac{2}{2}=1\).</p>", r"Renunciaría a 1 unidad del bien 1."),
 ("Producción", r"<p>\(f_K=5\sqrt{L/K}\) y \(f_L=5\sqrt{K/L}\), así que \(\text{TMS}=\dfrac{f_L}{f_K}=\dfrac{K}{L}=\dfrac94\).</p>", r"\(\text{TMS}=9/4\): una hora más de trabajo sustituye a 2,25 horas de máquina.")],
[(r"¿Qué utilidades marginales necesitas? ¿En qué orden las divides?", [r"La del bien que se gana (\(z\)) entre la del que se cede (\(x\)).", r"\(u_z/u_x=x^2y/(2xyz)\)."], "1 unidad del bien 1.", "Invertir el cociente."),
 (r"Calcula \(f_K\) y \(f_L\). ¿Qué queda al dividir?", [r"\(f=10K^{1/2}L^{1/2}\).", r"El cociente se simplifica a \(K/L\)."], r"\(\text{TMS}=9/4\).", None)],
dict(dif=1, etiqueta="Tasa marginal de sustitución",
 bienvenida="Vamos a calcular tasas marginales de sustitución en una utilidad y en una producción, y a interpretarlas.",
 cierre="La TMS es un cociente de derivadas parciales: arriba, la del bien que se gana; abajo, la del que se cede.",
 comprob=r"\(u(2,3,1)=12\). Cediendo 0,1 del bien 1 a cambio de 0,1 del bien 3: \(u(1{,}9;\ 3;\ 1{,}1)=1{,}9^2\cdot3\cdot1{,}1\approx11{,}91\), casi igual.",
 error="Sustituir los valores antes de derivar.")),

E("t3e3", "Convexidad de conjuntos",
r"""<p>Represente y estudie la convexidad de los conjuntos</p>
\[ A=\{(x,y): x+y\le6,\ y\ge x^2\},\quad B=\{(x,y): xy\le1,\ x>0,\ y>0\},\quad C=\{(x,y): x^2+y^2\le9,\ y\ge|x|\}. \]""",
r"""<ul><li>Escribe cada conjunto como intersección de conjuntos sencillos.</li><li>Epigrafo de una función convexa: convexo. Hipografo de una convexa: no tiene por qué serlo.</li><li>Si sospechas que no es convexo, busca dos puntos cuyo segmento se salga.</li></ul>""",
r"""<p>La intersección de convexos es convexa. Si \(g\) es convexa, \(\{y\ge g(x)\}\) es convexo. Un disco es convexo.</p>""",
[(r"Conjunto \(A\)", r"<p>Semiplano \(x+y\le6\) intersecado con el epigrafo de \(x^2\) (convexa). La parábola y la recta se cortan en \(x=-3\) y \(x=2\).</p>", r"\(A\) es convexo."),
 (r"Conjunto \(B\)", r"<p>Región bajo la hipérbola \(y=1/x\) en el primer cuadrante. Contraejemplo: \((4;\ 0{,}2)\) y \((0{,}2;\ 4)\) están en \(B\), pero su punto medio \((2{,}1;\ 2{,}1)\) cumple \(xy=4{,}41>1\).</p>", r"\(B\) no es convexo."),
 (r"Conjunto \(C\)", r"<p>Disco de radio 3 intersecado con el epigrafo de \(|x|\), que es convexa: un sector circular de 90°.</p>", r"\(C\) es convexo.")],
[(r"¿De qué dos conjuntos es intersección \(A\)? ¿Son convexos?", [r"\(y\ge x^2\) es el epigrafo de una parábola.", "Un semiplano siempre es convexo."], r"\(A\) es convexo.", None),
 (r"En \(B\), toma dos puntos cerca de los ejes. ¿Está su punto medio en \(B\)?", [r"Prueba con \((4;\ 0{,}2)\) y \((0{,}2;\ 4)\).", r"Calcula \(xy\) en el punto medio."], r"No: \(B\) no es convexo.", "Pensar que la región bajo una curva convexa es convexa."),
 (r"¿Qué figura es \(C\)?", [r"\(y\ge|x|\) es una región en forma de V.", "Cortada con el disco, queda un sector."], r"\(C\) es convexo.", None)],
dict(dif=1, etiqueta="Conjuntos convexos",
 bienvenida="Vamos a estudiar la convexidad de tres conjuntos: dos convexos y uno que no lo es.",
 cierre="Epigrafo de convexa: convexo. La región bajo una curva convexa normalmente no lo es; un contraejemplo lo demuestra.",
 comprob=r"En \(A\), el punto medio de \((-3,9)\) y \((2,4)\) es \((-0{,}5;\ 6{,}5)\): cumple \(x+y=6\) y \(6{,}5\ge0{,}25\).",
 error="Confundir el epigrafo con el hipografo.")),

E("t3e4", "Concavidad y convexidad de funciones",
r"""<p>Estudie la concavidad o convexidad de</p>
<ol class="apartados">
<li>\(f(x,y)=x^2+xy+y^2-3x\) en \(\mathbb R^2\);</li>
<li>\(g(x,y)=x^3-6xy+3y^2\) en los puntos \((2,0)\) y \((0,0)\), y en general;</li>
<li>\(h(x,y)=\ln x+2\ln y-x\) en \(\mathbb R^2_{++}\).</li>
</ol>""",
r"""<ul><li>Calcula la hessiana; si es constante, la clasificación vale en todo el plano.</li><li>Si depende del punto, estudia el signo de los menores en función de \(x,y\).</li></ul>""",
r"""<p>\(Hf(a)\) DP: estrictamente convexa en \(a\). DN: estrictamente cóncava. Semidefinida positiva o negativa: convexa o cóncava. Indefinida: ninguna de las dos.</p>""",
[(r"Función \(f\)", r"<p>\(Hf=\begin{pmatrix}2&1\\1&2\end{pmatrix}\), \(\Delta=(2,3)\): DP en todo punto.</p>", r"\(f\) estrictamente convexa en \(\mathbb R^2\)."),
 (r"Función \(g\)", r"<p>\(Hg=\begin{pmatrix}6x&-6\\-6&6\end{pmatrix}\), \(\Delta_2=36x-36\). En \((2,0)\): \(\Delta=(12,36)\), DP. En \((0,0)\): \(\Delta_2=-36\), indefinida. En general: estrictamente convexa si \(x>1\), convexa si \(x=1\), ni cóncava ni convexa si \(x<1\).</p>", r"Estrictamente convexa en \((2,0)\); ni cóncava ni convexa en \((0,0)\)."),
 (r"Función \(h\)", r"<p>\(Hh=\begin{pmatrix}-1/x^2&0\\0&-2/y^2\end{pmatrix}\): DN en todo \(\mathbb R^2_{++}\).</p>", r"\(h\) estrictamente cóncava en \(\mathbb R^2_{++}\).")],
[(r"Calcula la hessiana de \(f\). ¿Depende del punto?", ["Es un polinomio de grado 2.", r"\(\Delta_2=4-1\)."], r"Estrictamente convexa en \(\mathbb R^2\).", None),
 (r"¿Para qué valores de \(x\) es \(\Delta_2=36x-36\) positivo?", [r"\(x>1\).", r"En \((0,0)\), \(\Delta_2<0\)."], r"DP en \((2,0)\); indefinida en \((0,0)\).", r"Concluir que \(g\) es convexa en todo el plano por un solo punto."),
 (r"La hessiana de \(h\) es diagonal. ¿Qué signo tienen sus elementos?", [r"\(-1/x^2<0\) y \(-2/y^2<0\).", "Diagonal con elementos negativos: definida negativa."], "Estrictamente cóncava.", None)],
dict(dif=2, etiqueta="Concavidad y convexidad",
 bienvenida="Vamos a clasificar la hessiana de tres funciones: una con hessiana constante, otra que cambia de zona y otra cóncava en todo su dominio.",
 cierre="Hessiana constante: un solo cálculo. Si depende del punto, la respuesta depende de la zona.",
 comprob=r"\(f=\left(x+\tfrac y2\right)^2+\tfrac34y^2-3x\): parte cuadrática definida positiva.",
 error=r"Estudiar \(h\) fuera de su dominio \(x,y>0\).")),
]

T4 = [
E("t4e1", "Parámetros para que un punto sea crítico",
r"""<p>Halle el valor de \(a\) para el que el punto indicado es crítico:</p>
<ol class="apartados">
<li>\(f(x)=x^3+ax^2+3\), en \(x=2\);</li>
<li>\(f(x)=x\,e^{ax}\), en \(x=1/2\);</li>
<li>\(f(x,y)=x^2+ay^2+xy-5x\), en \((2,1)\).</li>
</ol>""",
r"""<ul><li>Un punto es crítico si se anulan todas las derivadas primeras.</li><li>Sustituye el punto en la derivada y despeja \(a\).</li></ul>""",
r"""<p>\(a\) es punto crítico de \(f\) si \(\nabla f(a)=0\) (en una variable, \(f'(a)=0\)).</p>""",
[("Apartado (a)", r"<p>\(f'(x)=3x^2+2ax\); \(f'(2)=12+4a=0\).</p>", r"\(a=-3\)."),
 ("Apartado (b)", r"<p>\(f'(x)=e^{ax}(1+ax)\); como \(e^{ax}>0\), \(1+a/2=0\).</p>", r"\(a=-2\)."),
 ("Apartado (c)", r"<p>\(f_x=2x+y-5\), que en \((2,1)\) vale 0 para cualquier \(a\). \(f_y=2ay+x\), que en \((2,1)\) vale \(2a+2=0\).</p>", r"\(a=-1\).")],
[(r"Deriva y sustituye \(x=2\).", [r"\(f'(x)=3x^2+2ax\).", r"\(12+4a=0\)."], r"\(a=-3\).", None),
 (r"Deriva \(xe^{ax}\) como un producto. ¿Puede anularse la exponencial?", [r"\(f'=e^{ax}+axe^{ax}\).", r"\(e^{ax}\ne0\): solo puede anularse \(1+ax\)."], r"\(a=-2\).", None),
 (r"Calcula las dos parciales en \((2,1)\). ¿Cuál depende de \(a\)?", [r"\(f_x(2,1)=4+1-5\).", r"\(f_y(2,1)=2a+2\)."], r"\(a=-1\).", "Imponer solo una de las dos derivadas.")],
dict(dif=1, etiqueta="Puntos críticos",
 bienvenida="Vamos a imponer que un punto sea crítico y despejar el parámetro.",
 cierre="Punto crítico significa todas las derivadas primeras nulas a la vez.",
 comprob=r"Con \(a=-3\), \(f'(x)=3x(x-2)\), que se anula en \(x=2\) ✓.",
 error="Olvidar que la exponencial nunca se anula.")),

E("t4e2", "Puntos críticos en dos y tres variables",
r"""<p>Halle y clasifique los puntos críticos de</p>
\[ f(x,y)=x^3+y^3-3x-12y,\qquad g(x,y,z)=x^2+y^2+z^2-xy+x-2z. \]
<p>¿Tiene \(g\) un mínimo global?</p>""",
r"""<ul><li>En \(f\) las variables están separadas: hay cuatro puntos críticos.</li><li>En \(g\) el sistema es lineal y la hessiana, constante.</li></ul>""",
r"""<p>Hessiana DP: mínimo local; DN: máximo local; indefinida: silla. Si la función es convexa en \(\mathbb R^n\), el mínimo local es global.</p>""",
[(r"Puntos críticos de \(f\)", r"<p>\(3x^2-3=0\Rightarrow x=\pm1\); \(3y^2-12=0\Rightarrow y=\pm2\). Cuatro puntos: \((\pm1,\pm2)\).</p>", None),
 (r"Clasificación de \(f\)", r"<p>\(Hf=\operatorname{diag}(6x,6y)\). \((1,2)\): DP, mínimo local, \(f=-18\). \((-1,-2)\): DN, máximo local, \(f=18\). \((1,-2)\) y \((-1,2)\): sillas.</p>", r"Mínimo local \((1,2)\), máximo local \((-1,-2)\), dos puntos de silla."),
 (r"Función \(g\)", r"<p>\(2x-y+1=0\), \(2y-x=0\), \(2z-2=0\Rightarrow(-2/3,\ -1/3,\ 1)\). \(Hg=\begin{pmatrix}2&-1&0\\-1&2&0\\0&0&2\end{pmatrix}\), \(\Delta=(2,3,6)\): DP en todo punto, \(g\) convexa.</p>", r"Mínimo global en \((-2/3,-1/3,1)\), con \(g=-4/3\).")],
[(r"Iguala a cero \(f_x\) y \(f_y\). ¿Cuántos puntos salen?", [r"\(x^2=1\) e \(y^2=4\).", r"Combina los dos valores de \(x\) con los dos de \(y\)."], r"Cuatro: \((\pm1,\pm2)\).", "Olvidar las combinaciones de signos."),
 ("La hessiana es diagonal. ¿Qué signos tiene en cada punto?", [r"\(\operatorname{diag}(6x,6y)\).", "Signos iguales positivos: mínimo; iguales negativos: máximo; distintos: silla."], r"Mínimo \((1,2)\), máximo \((-1,-2)\), dos sillas.", None),
 (r"Resuelve el sistema lineal de \(g\) y clasifica. ¿Puedes asegurar que el mínimo es global?", [r"De la segunda ecuación, \(x=2y\).", r"Si la hessiana es DP en todo punto, \(g\) es convexa."], r"Mínimo global \((-2/3,-1/3,1)\), \(g=-4/3\).", None)],
dict(dif=2, etiqueta="Optimización libre",
 bienvenida="Vamos a encontrar y clasificar puntos críticos en una función con cuatro de ellos y en otra de tres variables con un mínimo global.",
 cierre="Si la hessiana no depende del punto y es DP, el mínimo es global por el Teorema local-global.",
 comprob=r"\(g(-2/3,-1/3,1)=\tfrac49+\tfrac19+1-\tfrac29-\tfrac23-2=-\tfrac43\).",
 error=r"Decir que \(f\) tiene mínimo global: \(f\to-\infty\) cuando \(x\to-\infty\).")),

E("t4e3", "Coste mínimo de una empresa",
r"""<p>El coste total de una empresa, en miles de euros, en función de las cantidades \(x\) e \(y\) (en miles de unidades) de dos productos es</p>
\[ C(x,y)=3x^2+2y^2-2xy-20x-10y+100. \]
<p>¿Qué cantidades minimizan el coste? ¿Cuál es el coste mínimo?</p>""",
r"""<ul><li>Iguala a cero las derivadas parciales.</li><li>Comprueba que la hessiana es DP para asegurar un mínimo, y razona la globalidad.</li></ul>""",
r"""<p>Si \(HC\) es DP en todo \(\mathbb R^2\), \(C\) es convexa y su punto crítico es mínimo global (Teorema local-global).</p>""",
[("Punto crítico", r"<p>\(6x-2y-20=0\) y \(4y-2x-10=0\). De la segunda, \(x=2y-5\); en la primera, \(10y=50\Rightarrow y=5\), \(x=5\).</p>", None),
 ("Segundo orden y globalidad", r"<p>\(HC=\begin{pmatrix}6&-2\\-2&4\end{pmatrix}\), \(\Delta=(6,20)\): DP en todo punto. Mínimo global.</p>", None),
 ("Coste mínimo", r"<p>\(C(5,5)=75+50-50-100-50+100=25\).</p>", r"5000 unidades de cada producto, con un coste mínimo de 25 000 €.")],
[("Iguala a cero las dos derivadas y resuelve.", [r"\(C_x=6x-2y-20\), \(C_y=4y-2x-10\).", r"Despeja \(x\) de la segunda."], r"\((5,5)\).", None),
 ("¿Es un mínimo? ¿Es global?", ["Calcula los menores de la hessiana.", "Hessiana constante y DP: función convexa."], "Mínimo global.", None),
 (r"Sustituye en \(C\). ¿En qué unidades está el resultado?", [r"\(3\cdot25+2\cdot25-2\cdot25-100-50+100\).", "El coste está en miles de euros."], "25 000 €.", "Olvidar las unidades.")],
dict(dif=1, etiqueta="Coste mínimo",
 bienvenida="Vamos a minimizar el coste de una empresa con dos productos.",
 cierre="Función convexa en todo el plano: el punto crítico es el mínimo global.",
 comprob=r"\(C(6,5)=108+50-60-120-50+100=28>25\).",
 error="Dar el resultado en unidades sin tener en cuenta que están en miles.")),

E("t4e4", "Dos problemas con restricción de igualdad",
r"""<ol class="apartados">
<li>Minimice \(f(x,y)=x^2+y^2\) sujeto a \(2x+y=10\). Estime el valor mínimo si la restricción fuera \(2x+y=11\).</li>
<li>Halle los óptimos de \(f(x,y)=xy\) sujeto a \(x^2+y^2=8\).</li>
</ol>""",
r"""<ul><li>Lagrangiana \(L=f-\lambda(g-c)\) y \(\nabla L=0\).</li><li>En (a), \(f\) es convexa y la restricción lineal: local-global. En (b), la circunferencia es compacta: Weierstrass.</li></ul>""",
r"""<p><b>Interpretación del multiplicador.</b> \(f^*(c+1)\approx f^*(c)+\lambda\).</p>
<p><b>Weierstrass.</b> Una función continua en un compacto alcanza máximo y mínimo globales.</p>""",
[("Apartado (a)", r"<p>\(2x=2\lambda\), \(2y=\lambda\Rightarrow x=\lambda\), \(y=\lambda/2\). En la restricción, \(2\lambda+\lambda/2=10\Rightarrow\lambda=4\): \((4,2)\), \(f=20\). Mínimo global (convexa y restricción lineal).</p><p>Con \(c=11\): \(f^*\approx20+4=24\) (exacto: 24,2).</p>", r"Mínimo en \((4,2)\), \(f=20\), \(\lambda=4\); con 11, \(\approx24\)."),
 ("Apartado (b): puntos críticos", r"<p>\(y=2\lambda x\), \(x=2\lambda y\Rightarrow\lambda=\pm\tfrac12\). Con \(\lambda=\tfrac12\): \(x=y=\pm2\). Con \(\lambda=-\tfrac12\): \(x=-y=\pm2\).</p>", None),
 ("Apartado (b): óptimos", r"<p>La circunferencia es compacta y \(f\) continua: hay máximo y mínimo globales. Comparando valores: \(f(2,2)=f(-2,-2)=4\) y \(f(2,-2)=f(-2,2)=-4\).</p>", r"Máximos globales \((2,2)\) y \((-2,-2)\), con valor 4; mínimos globales \((2,-2)\) y \((-2,2)\), con valor \(-4\).")],
[(r"Plantea la lagrangiana de (a). ¿Qué relación hay entre \(x\) e \(y\)?", [r"\(L=x^2+y^2-\lambda(2x+y-10)\).", r"\(x=2y\)."], r"\((4,2)\), \(\lambda=4\), \(f=20\); con 11, \(\approx24\).", None),
 (r"En (b), de \(y=2\lambda x\) y \(x=2\lambda y\), ¿qué valores puede tomar \(\lambda\)?", [r"Sustituye una en la otra: \(x=4\lambda^2x\).", r"\(x\ne0\) (si no, \(y=0\) y no se cumple la restricción)."], r"\(\lambda=\pm\tfrac12\): cuatro puntos.", "Perder soluciones al dividir sin comprobar que el divisor no es 0."),
 ("¿Cómo decides cuáles son máximos y cuáles mínimos?", ["La circunferencia es cerrada y acotada.", r"Compara los valores de \(f\) en los cuatro puntos."], r"Máximo 4 en \((\pm2,\pm2)\) con el mismo signo; mínimo \(-4\) con signos opuestos.", None)],
dict(dif=2, etiqueta="Lagrange",
 bienvenida="Vamos a resolver dos problemas con restricción: uno con restricción lineal y otro sobre una circunferencia.",
 cierre="Con restricción lineal y función convexa, local-global; sobre un compacto, Weierstrass y comparar valores.",
 comprob=r"\(2\cdot4+2=10\) ✓ y \(2^2+2^2=8\) ✓.",
 error="En (b), quedarse solo con las soluciones positivas.")),
]

POR_TEMA = {1: T1, 2: T2, 3: T3, 4: T4}
