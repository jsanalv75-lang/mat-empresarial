"""Tema 1. El modelo input-output de Leontief. Problemas originales (no son los de la relación)."""

TITULO = "Tema 1. Modelo input-output de Leontief"
RESUMEN = ("Tablas input-output, matriz tecnológica, matriz de Leontief, productividad "
           "(definición, Hawkins-Simon, Brauer-Solow), modelo de precios, conjuntos autónomos, "
           "productos fundamentales y descomponibilidad.")

MANO = [
dict(
id="t1m1",
titulo="Una economía de tres sectores: de la tabla a la matriz tecnológica",
enunciado=r"""
<p>Una comarca tiene tres sectores productivos (1: agroalimentario, 2: industria, 3: servicios). Su tabla
input-output, en millones de euros, es:</p>
<div class="tabla-wrap"><table class="io">
<tr><th>Sectores</th><th>1</th><th>2</th><th>3</th><th>Demanda final</th><th>Output total</th></tr>
<tr><th>1</th><td>10</td><td>16</td><td>15</td><td></td><td>100</td></tr>
<tr><th>2</th><td>20</td><td>8</td><td>45</td><td></td><td>80</td></tr>
<tr><th>3</th><td>30</td><td>24</td><td>30</td><td></td><td>150</td></tr>
</table></div>
<ol class="apartados">
<li>Calcule la demanda intermedia y la demanda final de cada bien, y el consumo intermedio, el input primario y el input total de cada sector.</li>
<li>Obtenga la matriz tecnológica \(A\) e interprete el elemento \(a_{23}\).</li>
<li>Estudie si \(A\) es productiva mediante el Teorema de Brauer-Solow y la condición de Hawkins-Simon.</li>
<li>¿Qué demanda final se podría satisfacer con una producción de 200, 150 y 250 unidades?</li>
<li>Si los precios unitarios son \(p=(10,12,8)\), calcule el valor añadido neto unitario de cada sector.</li>
</ol>""",
ideas=r"""
<ul>
<li>Las <b>filas</b> de la tabla cuentan lo que <b>vende</b> cada sector (demanda intermedia + demanda final = output).</li>
<li>Las <b>columnas</b> cuentan lo que <b>compra</b> cada sector (consumo intermedio + input primario = input total).</li>
<li>En una tabla equilibrada, el input total de cada sector coincide con su output total.</li>
<li>Para la matriz tecnológica divide <b>cada columna</b> entre el output total de ese sector.</li>
<li>Para Brauer-Solow basta con que <b>todas</b> las sumas por filas, o <b>todas</b> las sumas por columnas, sean menores que 1.</li>
</ul>""",
teoria=r"""
<p><b>Relaciones de la tabla.</b> Si \(b_{ij}\) es la cantidad del bien \(i\) que usa el sector \(j\), \(d_i\) la demanda final y \(x_i\) el output total:</p>
\[ \text{DI}_i=\sum_{j=1}^n b_{ij},\qquad x_i=\sum_{j=1}^n b_{ij}+d_i,\qquad \text{CI}_j=\sum_{i=1}^n b_{ij},\qquad \text{IP}_j = x_j-\text{CI}_j. \]
<p><b>Coeficientes técnicos.</b> \(a_{ij}=\dfrac{b_{ij}}{x_j}\): unidades del bien \(i\) necesarias para producir una unidad del bien \(j\).</p>
<p><b>Modelo de producción.</b> \((I-A)X=D\). La matriz \(I-A\) es la <b>matriz de Leontief</b>.</p>
<p><b>Productividad.</b> \(A\ge 0\) es productiva si \((I-A)^{-1}\) existe y es no negativa. Equivale a que todos los menores principales \(\Delta_1,\dots,\Delta_n\) de \(I-A\) sean positivos (<b>Hawkins-Simon</b>). <b>Brauer-Solow</b> (condición suficiente): si todas las sumas por filas \(r_i<1\) o todas las sumas por columnas \(s_j<1\), \(A\) es productiva.</p>
<p><b>Modelo de precios.</b> \((I-A^t)P=V\), donde \(V\) es el vector de valores añadidos netos unitarios.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Leemos la tabla por filas</h5>
<p>La demanda intermedia de cada bien es la suma de su fila dentro de la parte intersectorial:</p>
\[ \text{DI}_1=10+16+15=41,\quad \text{DI}_2=20+8+45=73,\quad \text{DI}_3=30+24+30=84. \]
<p>La demanda final es lo que falta para llegar al output: \(d_i=x_i-\text{DI}_i\).</p>
\[ d_1=100-41=59,\quad d_2=80-73=7,\quad d_3=150-84=66. \]
<p class="nota">Interpretación: de los 100 millones que produce el sector 1, 41 los compran otros sectores para producir y 59 van al consumo final.</p></div>
<div class="paso"><h5>Paso 2. Leemos la tabla por columnas</h5>
\[ \text{CI}_1=10+20+30=60,\quad \text{CI}_2=16+8+24=48,\quad \text{CI}_3=15+45+30=90. \]
<p>El input total coincide con el output (tabla equilibrada): \(100,\ 80,\ 150\). El input primario (valor añadido: salarios, beneficios…) es la diferencia:</p>
\[ \text{IP}_1=100-60=40,\quad \text{IP}_2=80-48=32,\quad \text{IP}_3=150-90=60. \]</div>
<div class="paso"><h5>Paso 3. Matriz tecnológica</h5>
<p>Dividimos la columna 1 entre 100, la columna 2 entre 80 y la columna 3 entre 150:</p>
\[ A=\begin{pmatrix} 10/100 & 16/80 & 15/150\\ 20/100 & 8/80 & 45/150\\ 30/100 & 24/80 & 30/150\end{pmatrix}
=\begin{pmatrix} 0{,}1 & 0{,}2 & 0{,}1\\ 0{,}2 & 0{,}1 & 0{,}3\\ 0{,}3 & 0{,}3 & 0{,}2\end{pmatrix}. \]
<p>\(a_{23}=0{,}3\): el sector 3 (servicios) necesita 0,3 unidades del bien 2 (industria) para producir una unidad de su bien.</p></div>
<div class="paso"><h5>Paso 4. ¿Es productiva? Brauer-Solow</h5>
<p>Sumas por columnas: \(s_1=0{,}6,\ s_2=0{,}6,\ s_3=0{,}6\), todas menores que 1. (También por filas: \(r_1=0{,}4,\ r_2=0{,}6,\ r_3=0{,}8\).) Por Brauer-Solow, \(I-A\) cumple Hawkins-Simon y \(A\) es productiva.</p>
<p>Comprobación con Hawkins-Simon sobre \(I-A=\begin{pmatrix} 0{,}9 & -0{,}2 & -0{,}1\\ -0{,}2 & 0{,}9 & -0{,}3\\ -0{,}3 & -0{,}3 & 0{,}8\end{pmatrix}\):</p>
\[ \Delta_1=0{,}9>0,\qquad \Delta_2=0{,}81-0{,}04=0{,}77>0,\qquad \Delta_3=\det(I-A)=\tfrac{121}{250}=0{,}484>0. \]
<p class="nota">Interpretación: para cualquier demanda final \(D\ge 0\) existe una producción \(X\ge 0\) que la satisface.</p></div>
<div class="paso"><h5>Paso 5. Demanda final para \(X=(200,150,250)\)</h5>
\[ D=(I-A)X=\begin{pmatrix} 0{,}9\cdot200-0{,}2\cdot150-0{,}1\cdot250\\ -0{,}2\cdot200+0{,}9\cdot150-0{,}3\cdot250\\ -0{,}3\cdot200-0{,}3\cdot150+0{,}8\cdot250\end{pmatrix}
=\begin{pmatrix} 180-30-25\\ -40+135-75\\ -60-45+200\end{pmatrix}=\begin{pmatrix}125\\20\\95\end{pmatrix}. \]</div>
<div class="paso"><h5>Paso 6. Valores añadidos con \(p=(10,12,8)\)</h5>
<p>Usamos \(V=(I-A^t)P\): cada sector cobra su precio y paga los inputs que usa (su <b>columna</b> de \(A\)).</p>
\[ v_1=10-(0{,}1\cdot10+0{,}2\cdot12+0{,}3\cdot8)=10-5{,}8=4{,}2, \]
\[ v_2=12-(0{,}2\cdot10+0{,}1\cdot12+0{,}3\cdot8)=12-5{,}6=6{,}4, \]
\[ v_3=8-(0{,}1\cdot10+0{,}3\cdot12+0{,}2\cdot8)=8-6{,}2=1{,}8. \]
<p class="resultado">Solución: \(V=(4{,}2;\ 6{,}4;\ 1{,}8)\) u.m. por unidad producida.</p></div>"""),

dict(
id="t1m2",
titulo="Producciones y precios resolviendo sistemas",
enunciado=r"""
<p>La matriz tecnológica de una economía con tres sectores es</p>
\[ A=\begin{pmatrix} 0{,}2 & 0{,}2 & 0{,}1\\ 0{,}3 & 0{,}1 & 0{,}2\\ 0 & 0{,}4 & 0{,}2\end{pmatrix}. \]
<ol class="apartados">
<li>Interprete \(a_{31}=0\) y \(a_{32}=0{,}4\).</li>
<li>Justifique que se puede satisfacer cualquier demanda final no negativa.</li>
<li>Calcule la producción necesaria para atender una demanda final \(D=(40,85,20)\).</li>
<li>Halle los precios que permiten obtener unos valores añadidos netos unitarios \(V=(7,13,12)\).</li>
</ol>""",
ideas=r"""
<ul>
<li>“Cualquier demanda final” = la matriz es productiva. Prueba Brauer-Solow primero: es lo más rápido.</li>
<li>Para resolver \((I-A)X=D\) a mano, multiplica cada ecuación por 10 para quitar decimales.</li>
<li>La tercera ecuación tiene solo dos incógnitas: despeja una de ellas y sustituye.</li>
<li>Para los precios, el sistema usa la <b>traspuesta</b>: \((I-A^t)P=V\).</li>
<li>Comprueba siempre el resultado sustituyendo en el sistema original.</li>
</ul>""",
teoria=r"""
<p>Si \(A\) es productiva, el sistema \((I-A)X=D\) tiene solución única \(X=(I-A)^{-1}D\ge0\) para todo \(D\ge0\).</p>
<p>Además, \(A\) productiva \(\Rightarrow\) \(A^t\) productiva, así que también existe un sistema de precios \(P=(I-A^t)^{-1}V\ge0\) para cualquier \(V\ge0\).</p>
<p>En el modelo de precios, la ecuación del sector \(j\) es</p>
\[ p_j-\sum_{i=1}^n a_{ij}\,p_i=v_j, \]
<p>es decir, precio menos coste de los inputs intermedios por unidad = valor añadido unitario.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Interpretación</h5>
<p>\(a_{31}=0\): el sector 1 no utiliza el bien 3 en su producción. \(a_{32}=0{,}4\): por cada unidad que produce el sector 2 necesita 0,4 unidades del bien 3.</p></div>
<div class="paso"><h5>Paso 2. Productividad</h5>
<p>Sumas por columnas: \(s_1=0{,}5,\ s_2=0{,}7,\ s_3=0{,}5\), todas \(<1\). Por Brauer-Solow, \(A\) es productiva, luego cualquier \(D\ge0\) se puede satisfacer con una producción \(X\ge0\).</p>
<p class="nota">Por filas: \(r_1=0{,}5,\ r_2=0{,}6,\ r_3=0{,}6\); también valdría.</p></div>
<div class="paso"><h5>Paso 3. Planteamos \((I-A)X=D\) y quitamos decimales</h5>
\[ \begin{cases} 0{,}8x_1-0{,}2x_2-0{,}1x_3=40\\ -0{,}3x_1+0{,}9x_2-0{,}2x_3=85\\ -0{,}4x_2+0{,}8x_3=20\end{cases}
\ \Longrightarrow\ \begin{cases} 8x_1-2x_2-x_3=400\\ -3x_1+9x_2-2x_3=850\\ -4x_2+8x_3=200\end{cases} \]</div>
<div class="paso"><h5>Paso 4. Resolvemos por sustitución</h5>
<p>De la tercera: \(x_2=2x_3-50\). Sustituimos en las otras dos:</p>
\[ 8x_1-2(2x_3-50)-x_3=400 \ \Rightarrow\ 8x_1-5x_3=300, \]
\[ -3x_1+9(2x_3-50)-2x_3=850 \ \Rightarrow\ -3x_1+16x_3=1300. \]
<p>De la primera, \(x_1=\dfrac{300+5x_3}{8}\). Llevándolo a la segunda y multiplicando por 8:</p>
\[ -900-15x_3+128x_3=10400 \ \Rightarrow\ 113x_3=11300 \ \Rightarrow\ x_3=100. \]
<p>Entonces \(x_1=\dfrac{300+500}{8}=100\) y \(x_2=2\cdot100-50=150\).</p>
<p class="resultado">Producción necesaria: \(X=(100,\ 150,\ 100)\).</p>
<p class="nota">Comprobación: \(0{,}8\cdot100-0{,}2\cdot150-0{,}1\cdot100=80-30-10=40\) ✓.</p></div>
<div class="paso"><h5>Paso 5. Sistema de precios \((I-A^t)P=V\)</h5>
\[ I-A^t=\begin{pmatrix} 0{,}8 & -0{,}3 & 0\\ -0{,}2 & 0{,}9 & -0{,}4\\ -0{,}1 & -0{,}2 & 0{,}8\end{pmatrix}
\ \Longrightarrow\ \begin{cases} 8p_1-3p_2=70\\ -2p_1+9p_2-4p_3=130\\ -p_1-2p_2+8p_3=120\end{cases} \]
<p>De la tercera, \(8p_3=120+p_1+2p_2\). Multiplicando la segunda por 2 y sustituyendo \(8p_3\):</p>
\[ -4p_1+18p_2-(120+p_1+2p_2)=260 \ \Rightarrow\ -5p_1+16p_2=380. \]
<p>Con \(p_1=\dfrac{70+3p_2}{8}\): \(-5(70+3p_2)+128p_2=3040\Rightarrow 113p_2=3390\Rightarrow p_2=30\).</p>
<p>Luego \(p_1=\dfrac{70+90}{8}=20\) y \(p_3=\dfrac{120+20+60}{8}=25\).</p>
<p class="resultado">Precios: \(P=(20,\ 30,\ 25)\) u.m.</p>
<p class="nota">Comprobación del sector 2: \(30-(0{,}2\cdot20+0{,}1\cdot30+0{,}4\cdot25)=30-17=13\) ✓.</p></div>"""),

dict(
id="t1m3",
titulo="Conjuntos autónomos, productos fundamentales y tabla a completar",
enunciado=r"""
<p>Una economía de tres sectores tiene por matriz tecnológica</p>
\[ A=\begin{pmatrix} 0{,}2 & 0 & 0{,}1\\ 0{,}3 & 0{,}4 & 0{,}2\\ 0{,}1 & 0 & 0{,}3\end{pmatrix}. \]
<ol class="apartados">
<li>Determine todos los conjuntos autónomos y estudie la descomponibilidad de \(A\).</li>
<li>¿Qué productos son fundamentales? Razone la relación (directa o indirecta) de cada bien con los sectores.</li>
<li>Complete la tabla input-output sabiendo que los outputs totales son \(x_1=50,\ x_2=100,\ x_3=40\).</li>
</ol>""",
ideas=r"""
<ul>
<li>Un conjunto \(J\) es autónomo si sus sectores <b>no compran</b> nada fuera de \(J\): mira las <b>columnas</b> de los sectores de \(J\), en las filas que no están en \(J\).</li>
<li>Haz una tabla con los 7 subconjuntos no vacíos de \(\{1,2,3\}\).</li>
<li>Los productos fundamentales, si existen, forman el <b>menor</b> conjunto autónomo.</li>
<li>Para completar la tabla, usa \(b_{ij}=a_{ij}\,x_j\) (multiplica cada columna por su output).</li>
</ul>""",
teoria=r"""
<p><b>Conjunto autónomo.</b> \(J\subseteq N=\{1,\dots,n\}\), \(J\ne\varnothing\), es autónomo si \(a_{ji}=0\) para todo \(i\in J\) y todo \(j\notin J\). Los sectores de \(J\) pueden producir usando solo bienes de \(J\). \(N\) siempre es autónomo.</p>
<p><b>Descomponibilidad.</b> \(A\) es descomponible si existe algún conjunto autónomo distinto de \(N\); en caso contrario es indescomponible.</p>
<p><b>Producto fundamental.</b> El bien \(i\) es fundamental si se usa, directa o indirectamente, en la producción de todos los sectores. Si existen, el conjunto de productos fundamentales es el menor conjunto autónomo. Si \(A\) es indescomponible, todos los bienes son fundamentales.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Revisamos cada subconjunto</h5>
<p>Para cada \(J\) miramos los elementos \(a_{ji}\) con \(i\in J\) (columna) y \(j\notin J\) (fila):</p>
<div class="tabla-wrap"><table class="io">
<tr><th>\(J\)</th><th>Elementos a revisar</th><th>¿Autónomo?</th></tr>
<tr><td>\(\{1,2,3\}\)</td><td>ninguno</td><td>Sí</td></tr>
<tr><td>\(\{1,2\}\)</td><td>\(a_{31}=0{,}1\ne0\)</td><td>No</td></tr>
<tr><td>\(\{1,3\}\)</td><td>\(a_{21}=0{,}3\ne0\)</td><td>No</td></tr>
<tr><td>\(\{2,3\}\)</td><td>\(a_{12}=0,\ a_{13}=0{,}1\ne0\)</td><td>No</td></tr>
<tr><td>\(\{1\}\)</td><td>\(a_{21}=0{,}3\ne0\)</td><td>No</td></tr>
<tr><td>\(\{2\}\)</td><td>\(a_{12}=0,\ a_{32}=0\)</td><td>Sí</td></tr>
<tr><td>\(\{3\}\)</td><td>\(a_{13}=0{,}1\ne0\)</td><td>No</td></tr>
</table></div>
<p>Conjuntos autónomos: \(N=\{1,2,3\}\) y \(\{2\}\). Como existe uno distinto de \(N\), <b>\(A\) es descomponible</b>.</p></div>
<div class="paso"><h5>Paso 2. Productos fundamentales</h5>
<p>El menor conjunto autónomo es \(\{2\}\), así que el único candidato es el bien 2. La fila 2 de \(A\) no tiene ceros (\(a_{21},a_{22},a_{23}\ne0\)): el bien 2 se usa <b>directamente</b> en todos los sectores. Es fundamental.</p>
<p>El bien 1 no es fundamental: el sector 2 solo usa el bien 2, así que no lo necesita ni directa ni indirectamente. Lo mismo ocurre con el bien 3.</p></div>
<div class="paso"><h5>Paso 3. Completamos la tabla con \(b_{ij}=a_{ij}x_j\)</h5>
<p>Columna 1 (\(x_1=50\)): \(10,\ 15,\ 5\). Columna 2 (\(x_2=100\)): \(0,\ 40,\ 0\). Columna 3 (\(x_3=40\)): \(4,\ 8,\ 12\).</p>
<div class="tabla-wrap"><table class="io">
<tr><th>Sectores</th><th>1</th><th>2</th><th>3</th><th>DI</th><th>DF</th><th>Output</th></tr>
<tr><th>1</th><td>10</td><td>0</td><td>4</td><td>14</td><td>36</td><td>50</td></tr>
<tr><th>2</th><td>15</td><td>40</td><td>8</td><td>63</td><td>37</td><td>100</td></tr>
<tr><th>3</th><td>5</td><td>0</td><td>12</td><td>17</td><td>23</td><td>40</td></tr>
<tr><th>CI</th><td>30</td><td>40</td><td>24</td><td colspan="3"></td></tr>
<tr><th>IP</th><td>20</td><td>60</td><td>16</td><td colspan="3"></td></tr>
<tr><th>Input total</th><td>50</td><td>100</td><td>40</td><td colspan="3"></td></tr>
</table></div>
<p class="nota">Comprobación: en cada fila, \(\text{DI}+\text{DF}=\text{output}\); en cada columna, \(\text{CI}+\text{IP}=\text{input total}=\text{output}\).</p></div>"""),
]

MMA = [
dict(
id="t1w1",
titulo="Economía de cuatro sectores con Mathematica",
enunciado=r"""
<p>Una economía regional tiene cuatro sectores y su matriz tecnológica es</p>
\[ A=\begin{pmatrix} 0{,}1 & 0{,}2 & 0 & 0{,}1\\ 0{,}2 & 0{,}1 & 0{,}3 & 0\\ 0{,}1 & 0{,}3 & 0{,}1 & 0{,}2\\ 0 & 0{,}1 & 0{,}2 & 0{,}3\end{pmatrix}. \]
<ol class="apartados">
<li>Compruebe que \(A\) es productiva con la definición y con Hawkins-Simon.</li>
<li>Calcule la demanda final que se atiende con \(X=(100,120,150,80)\).</li>
<li>Calcule la producción necesaria para \(D=(30,40,50,20)\).</li>
<li>Calcule los valores añadidos netos con precios \(p=(5,4,6,3)\) y los precios que dan \(V=(2,2,2,2)\).</li>
</ol>""",
ideas=r"""
<ul>
<li>Introduce la matriz de forma que Mathematica trabaje con fracciones exactas, no con decimales.</li>
<li>Para la definición, calcula la inversa de la matriz de Leontief y mira si algún elemento es negativo.</li>
<li>Para Hawkins-Simon necesitas los determinantes de las submatrices superiores izquierdas: piensa cómo obtenerlos todos de una vez.</li>
<li>Cuando solo quieras resolver un sistema, no hace falta calcular la inversa: hay una orden que resuelve sistemas lineales.</li>
</ul>""",
teoria=r"""
<p>\(A\) productiva \(\iff (I-A)^{-1}\) existe y es \(\ge0\) \(\iff\) \(\Delta_k(I-A)>0\) para \(k=1,\dots,n\).</p>
<p>Producción: \(D=(I-A)X\), \(X=(I-A)^{-1}D\). Precios: \(V=(I-A^t)P\), \(P=(I-A^t)^{-1}V\).</p>
<p>Aquí Brauer-Solow también funciona (filas: 0,4; 0,6; 0,7; 0,6), pero se pide usar los otros métodos.</p>""",
comandos=r"""
<pre class="mma"><code>A = {{1,2,0,1},{2,1,3,0},{1,3,1,2},{0,1,2,3}}/10;   (* fracciones exactas *)
id = IdentityMatrix[4];
leo = id - A;                    (* matriz de Leontief *)
MatrixForm[leo]
Inverse[leo] // N                (* // N: valor decimal *)
Table[Det[leo[[1;;k, 1;;k]]], {k, 1, 4}]   (* menores principales *)
leo . {100,120,150,80}           (* el punto . es el producto matricial *)
LinearSolve[leo, {30,40,50,20}]
(id - Transpose[A]) . {5,4,6,3}
LinearSolve[id - Transpose[A], {2,2,2,2}]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Definimos la matriz y la de Leontief</h5>
<pre class="mma"><code>A = {{1,2,0,1},{2,1,3,0},{1,3,1,2},{0,1,2,3}}/10;
leo = IdentityMatrix[4] - A;</code></pre>
<p class="nota">El punto y coma final evita que Mathematica muestre la salida.</p></div>
<div class="paso"><h5>Paso 2. Productividad por la definición</h5>
<pre class="mma"><code>Inverse[leo] // N
<span class="out">{{1.20658, 0.347349, 0.164534, 0.219378},
 {0.363019, 1.38156, 0.504048, 0.195874},
 {0.28467, 0.579786, 1.40245, 0.441369},
 {0.133194, 0.363019, 0.472708, 1.58266}}</span></code></pre>
<p>La inversa existe y todos sus elementos son positivos: \(A\) es productiva.</p></div>
<div class="paso"><h5>Paso 3. Hawkins-Simon</h5>
<pre class="mma"><code>Table[Det[leo[[1;;k, 1;;k]]], {k, 1, 4}]
<span class="out">{9/10, 77/100, 303/500, 3829/10000}</span></code></pre>
<p>\(\Delta_1=0{,}9;\ \Delta_2=0{,}77;\ \Delta_3=0{,}606;\ \Delta_4=0{,}3829\): todos positivos, se confirma que \(A\) es productiva.</p></div>
<div class="paso"><h5>Paso 4. Demanda final con \(X=(100,120,150,80)\)</h5>
<pre class="mma"><code>leo . {100,120,150,80}
<span class="out">{58, 43, 73, 14}</span></code></pre>
<p class="nota">Comprobación del primer sector a mano: \(0{,}9\cdot100-0{,}2\cdot120-0\cdot150-0{,}1\cdot80=90-24-8=58\) ✓.</p></div>
<div class="paso"><h5>Paso 5. Producción para \(D=(30,40,50,20)\)</h5>
<pre class="mma"><code>LinearSolve[leo, {30,40,50,20}] // N
<span class="out">{62.7057, 95.2729, 110.682, 73.8052}</span></code></pre>
<p>Sin <code>// N</code> sale la solución exacta \(\left(\tfrac{34300}{547},\tfrac{364800}{3829},\tfrac{423800}{3829},\tfrac{282600}{3829}\right)\).</p></div>
<div class="paso"><h5>Paso 6. Precios y valores añadidos</h5>
<pre class="mma"><code>(IdentityMatrix[4] - Transpose[A]) . {5,4,6,3}
<span class="out">{31/10, 1/2, 18/5, 2/5}</span>
LinearSolve[IdentityMatrix[4] - Transpose[A], {2,2,2,2}] // N
<span class="out">{3.97493, 5.34343, 5.08749, 4.87856}</span></code></pre>
<p class="resultado">Con \(p=(5,4,6,3)\): \(V=(3{,}1;\ 0{,}5;\ 3{,}6;\ 0{,}4)\). Para \(V=(2,2,2,2)\): \(P\approx(3{,}97;\ 5{,}34;\ 5{,}09;\ 4{,}88)\).</p></div>"""),

dict(
id="t1w2",
titulo="Cuando Brauer-Solow no decide: productividad y multiplicadores",
enunciado=r"""
<p>Se comparan dos economías de tres sectores que solo se diferencian en el coeficiente \(a_{12}\):</p>
\[ A=\begin{pmatrix} 0{,}5 & 0{,}1 & 0{,}2\\ 0{,}3 & 0{,}6 & 0{,}1\\ 0{,}3 & 0{,}2 & 0{,}4\end{pmatrix},\qquad
B=\begin{pmatrix} 0{,}5 & 0{,}4 & 0{,}2\\ 0{,}3 & 0{,}6 & 0{,}1\\ 0{,}3 & 0{,}2 & 0{,}4\end{pmatrix}. \]
<ol class="apartados">
<li>Compruebe que el Teorema de Brauer-Solow no permite concluir nada en ninguna de las dos.</li>
<li>Estudie la productividad de cada una con Hawkins-Simon y con la inversa de Leontief.</li>
<li>Para la economía productiva, calcule la producción necesaria para \(D=(10,20,15)\) y cuánto debe aumentar la producción de cada sector si la demanda final del bien 2 crece en 10 unidades.</li>
</ol>""",
ideas=r"""
<ul>
<li>Calcula las sumas por filas y por columnas: si hay alguna \(\ge1\) en filas <b>y</b> alguna \(\ge1\) en columnas, Brauer-Solow no sirve.</li>
<li>Una inversa con elementos negativos (o un menor principal \(\le0\)) indica que la matriz <b>no</b> es productiva.</li>
<li>Un aumento \(\Delta D\) provoca \(\Delta X=(I-A)^{-1}\Delta D\): solo interviene la columna 2 de la inversa.</li>
</ul>""",
teoria=r"""
<p>Brauer-Solow es una condición <b>suficiente</b>, no necesaria: si falla, hay que usar Hawkins-Simon o la definición.</p>
<p>El elemento \(c_{ij}\) de \((I-A)^{-1}\) indica cuánto debe producir el sector \(i\) para atender una unidad adicional de demanda final del bien \(j\) (efectos directos e indirectos). Por eso</p>
\[ \Delta X=(I-A)^{-1}\Delta D. \]""",
comandos=r"""
<pre class="mma"><code>A = {{5,1,2},{3,6,1},{3,2,4}}/10;
B = {{5,4,2},{3,6,1},{3,2,4}}/10;
Total[A, {2}]        (* sumas por filas *)
Total[A]             (* sumas por columnas *)
Table[Det[(IdentityMatrix[3]-A)[[1;;k,1;;k]]], {k,1,3}]
Inverse[IdentityMatrix[3]-A]
LinearSolve[IdentityMatrix[3]-A, {10,20,15}] // N
Inverse[IdentityMatrix[3]-A] . {0,10,0} // N</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Brauer-Solow</h5>
<pre class="mma"><code>Total[A, {2}]
<span class="out">{4/5, 1, 9/10}</span>
Total[A]
<span class="out">{11/10, 9/10, 7/10}</span></code></pre>
<p>En \(A\): \(r_2=1\) no es menor que 1 y \(s_1=1{,}1>1\). No se cumple ni por filas ni por columnas. En \(B\) las sumas son aún mayores (\(r_1=1{,}1\), \(s_1=1{,}1\), \(s_2=1{,}2\)). Brauer-Solow no decide en ningún caso.</p></div>
<div class="paso"><h5>Paso 2. Hawkins-Simon</h5>
<pre class="mma"><code>Table[Det[(IdentityMatrix[3]-A)[[1;;k,1;;k]]], {k,1,3}]
<span class="out">{1/2, 17/100, 53/1000}</span>
Table[Det[(IdentityMatrix[3]-B)[[1;;k,1;;k]]], {k,1,3}]
<span class="out">{1/2, 2/25, -1/100}</span></code></pre>
<p>\(A\): todos los menores positivos \(\Rightarrow\) <b>productiva</b>. \(B\): \(\Delta_3=-0{,}01<0\Rightarrow\) <b>no productiva</b>.</p></div>
<div class="paso"><h5>Paso 3. Confirmación con la inversa</h5>
<pre class="mma"><code>Inverse[IdentityMatrix[3]-A]
<span class="out">{{220/53, 100/53, 90/53}, {210/53, 240/53, 110/53}, {180/53, 130/53, 170/53}}</span>
Inverse[IdentityMatrix[3]-B]
<span class="out">{{-22, -28, -12}, {-21, -24, -11}, {-18, -22, -8}}</span></code></pre>
<p>La inversa de \(I-A\) es positiva; la de \(I-B\) es negativa. En la economía \(B\), una demanda final positiva exigiría producciones negativas.</p></div>
<div class="paso"><h5>Paso 4. Producción y efecto de \(\Delta D=(0,10,0)\) en la economía \(A\)</h5>
<pre class="mma"><code>LinearSolve[IdentityMatrix[3]-A, {10,20,15}] // N
<span class="out">{104.717, 161.321, 131.132}</span>
Inverse[IdentityMatrix[3]-A] . {0,10,0} // N
<span class="out">{18.8679, 45.283, 24.5283}</span></code></pre>
<p class="resultado">Para \(D=(10,20,15)\): \(X\approx(104{,}72;\ 161{,}32;\ 131{,}13)\). Si la demanda final del bien 2 sube 10 unidades, las producciones deben subir \(\approx18{,}87\), \(45{,}28\) y \(24{,}53\) unidades: el aumento llega a todos los sectores por las relaciones intersectoriales.</p></div>"""),
]

TEST = [
dict(q=r"En la matriz tecnológica \(A\), el coeficiente \(a_{ij}\) representa:",
 o=[r"Las unidades del bien \(i\) necesarias para producir una unidad del bien \(j\).",
    r"Las unidades del bien \(j\) necesarias para producir una unidad del bien \(i\).",
    r"La cantidad total del bien \(i\) que vende el sector \(i\) al sector \(j\).",
    r"La demanda final del bien \(i\)."],
 c=[0], e=r"\(a_{ij}=b_{ij}/x_j\): se divide lo que el sector \(j\) compra del bien \(i\) entre lo que produce \(j\). La tercera opción describe \(b_{ij}\), no \(a_{ij}\)."),
dict(q=r"Si una matriz tecnológica no cumple la condición de Brauer-Solow ni por filas ni por columnas:",
 o=["La matriz no es productiva.", "No se puede concluir nada solo con ese teorema.",
    r"La matriz \(I-A\) no es invertible.", "Hay que estudiarla con Hawkins-Simon o con la definición."],
 c=[1,3], e="Brauer-Solow es condición suficiente pero no necesaria. Si falla, la matriz puede ser productiva o no; hay que usar otro método."),
dict(q=r"¿Cuáles de las siguientes afirmaciones son equivalentes a que \(A\ge0\) sea productiva?",
 o=[r"\((I-A)^{-1}\) existe y es no negativa.", r"Todos los menores principales de \(I-A\) son positivos.",
    r"Todos los elementos de \(A\) son menores que 1.", r"\((I-A)X=D\) tiene solución \(X\ge0\) para todo \(D\ge0\)."],
 c=[0,1,3], e=r"Son la definición, la condición de Hawkins-Simon y la interpretación económica. Que cada \(a_{ij}<1\) no basta: \(B=\begin{pmatrix}0{,}5&0{,}4&0{,}2\\0{,}3&0{,}6&0{,}1\\0{,}3&0{,}2&0{,}4\end{pmatrix}\) tiene todos sus elementos menores que 1 y no es productiva, porque \(\det(I-B)=-0{,}01<0\)."),
dict(q=r"Con \(A=\begin{pmatrix}0{,}2&0{,}3\\0{,}4&0{,}1\end{pmatrix}\) y una producción \(X=(50,40)\), la demanda final que se satisface es:",
 o=[r"\(D=(28,\,16)\)", r"\(D=(22,\,24)\)", r"\(D=(40,\,36)\)", r"\(D=(28,\,24)\)"],
 c=[0], e=r"\(d_1=50-0{,}2\cdot50-0{,}3\cdot40=50-10-12=28\); \(d_2=40-0{,}4\cdot50-0{,}1\cdot40=40-20-4=16\)."),
dict(q=r"El input primario del sector \(j\):",
 o=[r"Es \(x_j-\sum_i b_{ij}\).", r"Es \(x_j-\sum_k b_{jk}\).",
    "Representa el valor añadido (pago a factores primarios: trabajo, capital…).", r"Coincide con la demanda final del bien \(j\)."],
 c=[0,2], e="Input primario = input total − consumo intermedio (suma de la columna). La segunda expresión es la demanda final (se resta la fila)."),
dict(q="Sobre los conjuntos autónomos, son correctas:",
 o=[r"Los sectores de un conjunto autónomo \(J\) no utilizan bienes producidos fuera de \(J\).",
    r"\(J\) es autónomo si \(a_{ji}=0\) para todo \(i\in J\) y \(j\notin J\).",
    r"Los sectores de \(J\) no venden nada a sectores de fuera de \(J\).",
    r"El conjunto \(N=\{1,\dots,n\}\) siempre es autónomo."],
 c=[0,1,3], e=r"La condición se refiere a lo que compran (columnas de \(J\)), no a lo que venden."),
dict(q=r"Una matriz tecnológica \(A\) es descomponible cuando:",
 o=["Todos sus elementos son positivos.", r"Existe algún conjunto autónomo distinto de \(N\).",
    "No es productiva.", "Todos los bienes son fundamentales."],
 c=[1], e="Esa es la definición. Si todos los elementos son positivos, ningún subconjunto propio es autónomo y la matriz es indescomponible."),
dict(q=r"Si \(A\) es productiva, entonces \(A^t\):",
 o=["También es productiva.", "Puede no ser productiva.", r"Tiene \(\det(I-A^t)=0\).", "Es descomponible."],
 c=[0], e=r"\(\det\) y menores principales de \(I-A^t\) coinciden con los de \(I-A\). Por eso se pueden fijar precios para cualquier \(V\ge0\)."),
dict(q=r"Sea \(A=\begin{pmatrix}0{,}1&0\\0{,}3&0{,}2\end{pmatrix}\). Señale las afirmaciones correctas:",
 o=[r"\(\{2\}\) es un conjunto autónomo.", r"\(\{1\}\) es un conjunto autónomo.", "El bien 2 es un producto fundamental.", "A es indescomponible."],
 c=[0,2], e=r"\(\{2\}\): \(a_{12}=0\) ✓. \(\{1\}\): \(a_{21}=0{,}3\ne0\) ✗. El bien 2 lo usan los dos sectores (\(a_{21},a_{22}\ne0\)), así que es fundamental. Como \(\{2\}\ne N\) es autónomo, \(A\) es descomponible."),
dict(q=r"Con \(A=\begin{pmatrix}0{,}2&0{,}3\\0{,}4&0{,}1\end{pmatrix}\) y precios \(p=(10,20)\), los valores añadidos netos unitarios son:",
 o=[r"\(V=(0,\,15)\)", r"\(V=(2,\,14)\)", r"\(V=(8,\,18)\)", r"\(V=(10,\,5)\)"],
 c=[0], e=r"\(V=(I-A^t)p\): \(v_1=10-(0{,}2\cdot10+0{,}4\cdot20)=0\); \(v_2=20-(0{,}3\cdot10+0{,}1\cdot20)=15\). La opción \((2,14)\) es el error de usar \(I-A\) en vez de \(I-A^t\)."),
]
