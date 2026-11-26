"""Tema 3. Cálculo diferencial en varias variables y convexidad. Problemas originales."""

TITULO = "Tema 3. Funciones de varias variables y convexidad"
RESUMEN = ("Derivadas parciales de primer y segundo orden, vector gradiente, matriz hessiana, "
           "tasa marginal de sustitución, conjuntos convexos y funciones cóncavas y convexas.")

MANO = [
dict(
id="t3m1",
titulo="Función de producción: productividades, TMS y concavidad",
enunciado=r"""
<p>Una empresa produce según la función</p>
\[ f(K,L)=6\,K^{1/2}L^{1/3},\qquad K,L>0, \]
<p>donde \(K\) son horas de máquina y \(L\) horas de trabajo.</p>
<ol class="apartados">
<li>Calcule las productividades marginales \(f_K\) y \(f_L\) en el punto \((K,L)=(4,8)\) e interprételas.</li>
<li>Con \((K,L)=(4,8)\), ¿cuántas horas de máquina se pueden sustituir por una hora más de trabajo sin cambiar la producción? (Tasa marginal de sustitución.)</li>
<li>Calcule la matriz hessiana y estudie la concavidad de \(f\) en \((4,8)\) y en todo \(\mathbb R^2_{++}\).</li>
</ol>""",
ideas=r"""
<ul>
<li>Deriva como una potencia, tratando la otra variable como constante: \(\frac{\partial}{\partial K}K^{1/2}=\tfrac12K^{-1/2}\).</li>
<li>En \((4,8)\): \(4^{1/2}=2\), \(8^{1/3}=2\), \(8^{-2/3}=1/4\). Son números cómodos.</li>
<li>Sobre una isocuanta \(f(K,L)=\text{cte}\), la TMS es \(-\dfrac{dK}{dL}=\dfrac{f_L}{f_K}\).</li>
<li>Para la concavidad, estudia el signo de \(\Delta_1\) y \(\Delta_2\) de la hessiana.</li>
</ul>""",
teoria=r"""
<p><b>Productividad marginal.</b> \(f_K(a)\) mide, aproximadamente, cuánto aumenta la producción al usar una unidad más de \(K\), con \(L\) fijo.</p>
<p><b>Tasa marginal de sustitución.</b> A lo largo de la curva de nivel \(f(K,L)=c\), por el teorema de la función implícita:</p>
\[ \frac{dK}{dL}=-\frac{f_L}{f_K}\quad\Longrightarrow\quad \text{TMS}_{L,K}=\frac{f_L}{f_K}. \]
<p><b>Concavidad.</b> Si \(Hf(a)\) es definida negativa, \(f\) es estrictamente cóncava en \(a\); si es semidefinida negativa, cóncava. Con definida o semidefinida positiva, (estrictamente) convexa. Si lo es en todos los puntos de un conjunto convexo abierto, lo es en el conjunto.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Derivadas primeras</h5>
\[ f_K=6\cdot\tfrac12K^{-1/2}L^{1/3}=3K^{-1/2}L^{1/3},\qquad f_L=6\cdot\tfrac13K^{1/2}L^{-2/3}=2K^{1/2}L^{-2/3}. \]
<p>En \((4,8)\): \(f_K=3\cdot\tfrac12\cdot2=3\) y \(f_L=2\cdot2\cdot\tfrac14=1\). La producción es \(f(4,8)=6\cdot2\cdot2=24\).</p>
<p class="nota">Interpretación: una hora más de máquina aumenta la producción en unas 3 unidades; una hora más de trabajo, en 1 unidad.</p></div>
<div class="paso"><h5>Paso 2. Tasa marginal de sustitución</h5>
\[ \text{TMS}_{L,K}=\frac{f_L}{f_K}=\frac13. \]
<p class="resultado">Con una hora más de trabajo se pueden dejar de usar aproximadamente \(1/3\) de hora de máquina y mantener la producción en 24.</p></div>
<div class="paso"><h5>Paso 3. Derivadas segundas y hessiana</h5>
\[ f_{KK}=-\tfrac32K^{-3/2}L^{1/3},\qquad f_{LL}=-\tfrac43K^{1/2}L^{-5/3},\qquad f_{KL}=f_{LK}=K^{-1/2}L^{-2/3}. \]
<p>En \((4,8)\), con \(4^{-3/2}=\tfrac18\) y \(8^{-5/3}=\tfrac1{32}\):</p>
\[ Hf(4,8)=\begin{pmatrix} -3/8 & 1/8\\ 1/8 & -1/12\end{pmatrix}. \]</div>
<div class="paso"><h5>Paso 4. Concavidad en el punto</h5>
\[ \Delta_1=-\tfrac38<0,\qquad \Delta_2=\tfrac38\cdot\tfrac1{12}-\tfrac1{64}=\tfrac1{32}-\tfrac1{64}=\tfrac1{64}>0. \]
<p>La hessiana es definida negativa: \(f\) es <b>estrictamente cóncava en \((4,8)\)</b>.</p></div>
<div class="paso"><h5>Paso 5. Concavidad en todo \(\mathbb R^2_{++}\)</h5>
<p>En un punto cualquiera con \(K,L>0\): \(\Delta_1=f_{KK}<0\) y</p>
\[ \Delta_2=\tfrac32\cdot\tfrac43\,K^{-1}L^{-4/3}-K^{-1}L^{-4/3}=(2-1)K^{-1}L^{-4/3}>0. \]
<p class="resultado">La hessiana es definida negativa en todo punto, así que \(f\) es estrictamente cóncava en \(\mathbb R^2_{++}\). Los exponentes suman \(\tfrac12+\tfrac13<1\): rendimientos decrecientes a escala.</p></div>"""),

dict(
id="t3m2",
titulo="Zonas de convexidad de una función polinómica",
enunciado=r"""
<p>Sea \(f(x,y)=x^3-3xy+y^2\).</p>
<ol class="apartados">
<li>Calcule el gradiente y la matriz hessiana de \(f\).</li>
<li>Estudie la concavidad o convexidad de \(f\) en los puntos \((1,2)\) y \((0,0)\).</li>
<li>Determine en qué región del plano \(f\) es convexa, estrictamente convexa, cóncava o ni lo uno ni lo otro.</li>
</ol>""",
ideas=r"""
<ul>
<li>La hessiana solo depende de \(x\): los menores principales serán expresiones en \(x\).</li>
<li>El signo de \(\Delta_2\) cambia en un valor concreto de \(x\). Encuéntralo.</li>
<li>Para ser cóncava haría falta \(\Delta_1\le0\). Mira el elemento \(f_{yy}\).</li>
</ul>""",
teoria=r"""
<p>\(\nabla f=(f_x,f_y)\) y \(Hf=\begin{pmatrix}f_{xx}&f_{xy}\\f_{yx}&f_{yy}\end{pmatrix}\). Por el teorema de Schwarz, si las derivadas segundas son continuas, \(f_{xy}=f_{yx}\).</p>
<p>Clasificación de \(Hf(a)\): DP \(\Rightarrow\) estrictamente convexa; semidefinida positiva \(\Rightarrow\) convexa; DN \(\Rightarrow\) estrictamente cóncava; semidefinida negativa \(\Rightarrow\) cóncava; indefinida \(\Rightarrow\) ni cóncava ni convexa en \(a\).</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Gradiente y hessiana</h5>
\[ \nabla f(x,y)=\big(3x^2-3y,\ -3x+2y\big),\qquad Hf(x,y)=\begin{pmatrix}6x&-3\\-3&2\end{pmatrix}. \]</div>
<div class="paso"><h5>Paso 2. En \((1,2)\) y en \((0,0)\)</h5>
<p>\(Hf(1,2)=\begin{pmatrix}6&-3\\-3&2\end{pmatrix}\): \(\Delta_1=6>0\), \(\Delta_2=12-9=3>0\). Es DP: <b>estrictamente convexa</b> en \((1,2)\).</p>
<p>\(Hf(0,0)=\begin{pmatrix}0&-3\\-3&2\end{pmatrix}\): \(\Delta_2=-9<0\). Es indefinida: en \((0,0)\) <b>ni cóncava ni convexa</b>.</p></div>
<div class="paso"><h5>Paso 3. Estudio general</h5>
<p>\(\Delta_1=6x\) y \(\Delta_2=12x-9\), que se anula en \(x=3/4\).</p>
<ul>
<li>\(x>3/4\): \(\Delta_1>0,\ \Delta_2>0\Rightarrow\) DP \(\Rightarrow\) <b>estrictamente convexa</b>.</li>
<li>\(x=3/4\): \(Hf=\begin{pmatrix}4{,}5&-3\\-3&2\end{pmatrix}\), \(\Delta_2=0\), traza \(>0\). Autovalores \(0\) y \(6{,}5\): semidefinida positiva \(\Rightarrow\) <b>convexa</b>.</li>
<li>\(x<3/4\): \(\Delta_2<0\Rightarrow\) indefinida \(\Rightarrow\) <b>ni cóncava ni convexa</b>.</li>
</ul>
<p class="resultado">\(f\) nunca es cóncava (el elemento \(f_{yy}=2>0\) lo impide). Es estrictamente convexa en el semiplano abierto \(\{x>3/4\}\).</p></div>"""),

dict(
id="t3m3",
titulo="Representar conjuntos y decidir si son convexos",
enunciado=r"""
<p>Represente gráficamente los siguientes conjuntos y estudie su convexidad:</p>
\[ X=\{(x,y)\in\mathbb R^2 : y\ge x^2-4x+3,\ y\le 3\}, \]
\[ Y=\{(x,y)\in\mathbb R^2 : 1\le x^2+y^2\le 4,\ y\ge0\}, \]
\[ Z=\{(x,y)\in\mathbb R^2 : xy\ge1,\ x>0\}. \]""",
ideas=r"""
<ul>
<li>Dibuja primero la frontera de cada desigualdad (parábola, circunferencias, hipérbola) y decide qué lado vale probando un punto.</li>
<li>Para demostrar que un conjunto <b>no</b> es convexo basta un contraejemplo: dos puntos del conjunto cuyo segmento se sale.</li>
<li>Para demostrar que <b>sí</b> lo es, usa que la intersección de convexos es convexa y que el epigrafo \(\{y\ge g(x)\}\) de una función convexa es convexo.</li>
</ul>""",
teoria=r"""
<p>\(C\subseteq\mathbb R^n\) es <b>convexo</b> si para cualesquiera \(a,b\in C\) y \(t\in[0,1]\), el punto \(ta+(1-t)b\in C\): el segmento que une dos puntos del conjunto está dentro del conjunto.</p>
<ul>
<li>Los semiplanos \(\{px+qy\le r\}\) son convexos.</li>
<li>Si \(g\) es convexa, \(\{y\ge g(x)\}\) es convexo; si \(g\) es cóncava, \(\{y\le g(x)\}\) es convexo.</li>
<li>La intersección de conjuntos convexos es convexa. La unión, en general, no.</li>
</ul>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Conjunto \(X\)</h5>
<p>La parábola \(y=x^2-4x+3=(x-2)^2-1\) tiene vértice en \((2,-1)\) y corta a la recta \(y=3\) cuando \(x^2-4x=0\), es decir, en \(x=0\) y \(x=4\). \(X\) es la región entre la parábola (por encima) y la recta (por debajo).</p>
<figure><img src="fig/t3_X.svg" alt="Región entre la parábola y = x² − 4x + 3 y la recta y = 3, entre x = 0 y x = 4" width="400" height="360"></figure>
<p class="resultado">\(X\) es convexo: es la intersección del epigrafo de \(g(x)=x^2-4x+3\), que es convexa (\(g''=2>0\)), con el semiplano \(y\le3\).</p></div>
<div class="paso"><h5>Paso 2. Conjunto \(Y\)</h5>
<p>\(1\le x^2+y^2\le4\) es una corona circular de radios 1 y 2; con \(y\ge0\) nos quedamos con la mitad superior.</p>
<figure><img src="fig/t3_Y.svg" alt="Semicorona circular superior entre los radios 1 y 2" width="400" height="300"></figure>
<p>Contraejemplo: \(P=(-1{,}5;\ 0)\in Y\) y \(Q=(1{,}5;\ 0)\in Y\), pero el punto medio \((0,0)\) no cumple \(x^2+y^2\ge1\).</p>
<p class="resultado">\(Y\) no es convexo.</p></div>
<div class="paso"><h5>Paso 3. Conjunto \(Z\)</h5>
<p>Como \(x>0\), \(xy\ge1\iff y\ge\dfrac1x\). Es la región por encima de la rama de la hipérbola del primer cuadrante.</p>
<figure><img src="fig/t3_Z.svg" alt="Región por encima de la hipérbola y = 1/x en el primer cuadrante" width="400" height="360"></figure>
<p class="resultado">\(Z\) es convexo: \(g(x)=1/x\) es convexa en \(x>0\) (\(g''(x)=2/x^3>0\)) y \(Z\) es su epigrafo.</p></div>"""),
]

MMA = [
dict(
id="t3w1",
titulo="Gradiente, hessiana y concavidad de funciones de tres variables",
enunciado=r"""
<p>Se consideran las funciones</p>
\[ h(x,y,z)=x^2y+yz^2-2xz,\qquad g(x,y,z)=-x^2-2y^2-3z^2+xy+yz+4x+2z. \]
<ol class="apartados">
<li>Calcule con Mathematica el gradiente y la hessiana de \(h\), y estudie su concavidad o convexidad en \((1,1,1)\) y en \((0,1,0)\).</li>
<li>Demuestre que \(g\) es estrictamente cóncava en \(\mathbb R^3\) y obtenga el punto donde su gradiente se anula.</li>
</ol>""",
ideas=r"""
<ul>
<li>La orden de derivar admite una lista de variables: con ella obtienes el gradiente y la hessiana de una vez.</li>
<li>Para estudiar un punto, sustituye sus coordenadas en la hessiana y calcula los autovalores.</li>
<li>Si la hessiana de \(g\) es constante, su clasificación vale para todo \(\mathbb R^3\).</li>
</ul>""",
teoria=r"""
<p>Hessiana DP en \(a\) \(\Rightarrow\) estrictamente convexa en \(a\); DN \(\Rightarrow\) estrictamente cóncava; semidefinida \(\Rightarrow\) convexa o cóncava (no estrictamente según este criterio); indefinida \(\Rightarrow\) ni una cosa ni otra.</p>
<p>Si \(f\) tiene hessiana DN en todo un conjunto convexo abierto, \(f\) es estrictamente cóncava en él.</p>""",
comandos=r"""
<pre class="mma"><code>h = x^2 y + y z^2 - 2 x z;
grad = D[h, {{x,y,z}}]
H = D[h, {{x,y,z}, 2}];  MatrixForm[H]
H1 = H /. {x->1, y->1, z->1};  Eigenvalues[H1]
H0 = H /. {x->0, y->1, z->0};  Eigenvalues[H0]
g = -x^2 - 2 y^2 - 3 z^2 + x y + y z + 4 x + 2 z;
Hg = D[g, {{x,y,z}, 2}]
Table[Det[Hg[[1;;k,1;;k]]], {k,1,3}]
NegativeDefiniteMatrixQ[Hg]
Solve[D[g, {{x,y,z}}] == {0,0,0}, {x,y,z}]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Gradiente y hessiana de \(h\)</h5>
<pre class="mma"><code>grad = D[h, {{x,y,z}}]
<span class="out">{2 x y - 2 z, x^2 + z^2, -2 x + 2 y z}</span>
H = D[h, {{x,y,z}, 2}]
<span class="out">{{2 y, 2 x, -2}, {2 x, 0, 2 z}, {-2, 2 z, 2 y}}</span></code></pre></div>
<div class="paso"><h5>Paso 2. En \((1,1,1)\)</h5>
<pre class="mma"><code>H1 = H /. {x->1, y->1, z->1}
<span class="out">{{2, 2, -2}, {2, 0, 2}, {-2, 2, 2}}</span>
Eigenvalues[H1]
<span class="out">{4, 2 Sqrt[2], -2 Sqrt[2]}</span></code></pre>
<p>Hay autovalores positivos y negativos: indefinida. \(h\) <b>no es cóncava ni convexa</b> en \((1,1,1)\). (Con menores: \(\Delta_2=-4<0\).)</p></div>
<div class="paso"><h5>Paso 3. En \((0,1,0)\)</h5>
<pre class="mma"><code>H0 = H /. {x->0, y->1, z->0}
<span class="out">{{2, 0, -2}, {0, 0, 0}, {-2, 0, 2}}</span>
Eigenvalues[H0]
<span class="out">{4, 0, 0}</span></code></pre>
<p>Autovalores \(\ge0\) con algún cero: semidefinida positiva. \(h\) es <b>convexa</b> (no estrictamente según el criterio) en \((0,1,0)\).</p>
<p class="nota">Aquí los menores principales no deciden (\(\Delta_2=\Delta_3=0\)): por eso conviene usar autovalores.</p></div>
<div class="paso"><h5>Paso 4. Concavidad de \(g\)</h5>
<pre class="mma"><code>Hg = D[g, {{x,y,z}, 2}]
<span class="out">{{-2, 1, 0}, {1, -4, 1}, {0, 1, -6}}</span>
Table[Det[Hg[[1;;k,1;;k]]], {k,1,3}]
<span class="out">{-2, 7, -40}</span>
NegativeDefiniteMatrixQ[Hg]
<span class="out">True</span></code></pre>
<p>Signos \(-,+,-\): definida negativa en todo \(\mathbb R^3\), porque la hessiana no depende del punto.</p>
<pre class="mma"><code>Solve[D[g, {{x,y,z}}] == {0,0,0}, {x,y,z}]
<span class="out">{{x -> 47/20, y -> 7/10, z -> 9/20}}</span></code></pre>
<p class="resultado">\(g\) es estrictamente cóncava en \(\mathbb R^3\) y su gradiente se anula en \((47/20,\ 7/10,\ 9/20)=(2{,}35;\ 0{,}7;\ 0{,}45)\). (Por ser estrictamente cóncava, ese punto es su máximo global.)</p></div>"""),

dict(
id="t3w2",
titulo="Curvas de nivel, TMS y regiones con gráficos",
enunciado=r"""
<p>Un consumidor tiene la función de utilidad \(u(x,y)=x^{1/3}y^{2/3}\), con \(x,y>0\).</p>
<ol class="apartados">
<li>Obtenga la TMS de \(y\) por \(x\) (unidades de \(y\) que cede por una unidad más de \(x\)) y evalúela en \((4,2)\).</li>
<li>Represente las curvas de nivel 1, 2 y 3 de \(u\).</li>
<li>Represente el conjunto \(S=\{(x,y): x+2y\le10,\ xy\ge8,\ x\ge0,\ y\ge0\}\) y razone si es convexo.</li>
</ol>""",
ideas=r"""
<ul>
<li>La TMS es el cociente de utilidades marginales \(u_x/u_y\): calcúlalo y simplifícalo.</li>
<li>Para las curvas de nivel hay un tipo de gráfico específico en el que puedes elegir los niveles.</li>
<li>Para la región, otro tipo de gráfico sombrea los puntos que cumplen varias desigualdades a la vez.</li>
</ul>""",
teoria=r"""
<p>Sobre una curva de indiferencia \(u(x,y)=c\): \(\dfrac{dy}{dx}=-\dfrac{u_x}{u_y}\), así que \(\text{TMS}_{x,y}=\dfrac{u_x}{u_y}\).</p>
<p>\(\{x+2y\le10\}\) es un semiplano (convexo) y \(\{xy\ge8,\ x>0\}=\{y\ge8/x,\ x>0\}\) es el epigrafo de una función convexa (convexo). La intersección de convexos es convexa.</p>""",
comandos=r"""
<pre class="mma"><code>u = x^(1/3) y^(2/3);
tms = Simplify[D[u, x]/D[u, y]]
tms /. {x->4, y->2}
ContourPlot[u, {x,0,10}, {y,0,10}, Contours -> {1,2,3},
  ContourShading -> None, FrameLabel -> {"x","y"}]
RegionPlot[x + 2 y <= 10 && x y >= 8 && x >= 0 && y >= 0,
  {x,0,11}, {y,0,6}, PlotPoints -> 60]
Solve[{x + 2 y == 10, x y == 8}, {x,y}]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. TMS</h5>
<pre class="mma"><code>tms = Simplify[D[u, x]/D[u, y]]
<span class="out">y/(2 x)</span>
tms /. {x->4, y->2}
<span class="out">1/4</span></code></pre>
<p class="resultado">\(\text{TMS}=\dfrac{y}{2x}\). En \((4,2)\) vale \(1/4\): por una unidad más del bien \(x\), el consumidor cedería unas 0,25 unidades de \(y\) sin cambiar su utilidad.</p></div>
<div class="paso"><h5>Paso 2. Curvas de nivel</h5>
<p>El <code>ContourPlot</code> muestra tres curvas decrecientes y convexas hacia el origen (\(y=c^{3/2}x^{-1/2}\)); cuanto mayor es el nivel, más alejadas del origen están.</p>
<p class="nota">Si Mathematica avisa de valores complejos, restringe el dominio a \(x,y>0\), por ejemplo <code>{x,0.01,10}</code>.</p></div>
<div class="paso"><h5>Paso 3. Región \(S\)</h5>
<pre class="mma"><code>Solve[{x + 2 y == 10, x y == 8}, {x,y}]
<span class="out">{{x -> 2, y -> 4}, {x -> 8, y -> 1}}</span></code></pre>
<p>La región queda por encima de la hipérbola \(y=8/x\) y por debajo de la recta \(y=(10-x)/2\), para \(2\le x\le8\). El <code>RegionPlot</code> muestra una “lente” cerrada sin entrantes.</p>
<p class="resultado">\(S\) es convexo: es la intersección del semiplano \(x+2y\le10\) con el epigrafo de \(8/x\), que es convexo en \(x>0\). Además, es cerrado y acotado, es decir, compacto (útil para Weierstrass en el Tema 4).</p></div>"""),
]

TEST = [
dict(q=r"Para \(f(x,y)=x^2y^3\), la derivada parcial \(\dfrac{\partial f}{\partial x}\) es:",
 o=[r"\(2xy^3\)", r"\(3x^2y^2\)", r"\(2xy^3+3x^2y^2\)", r"\(6xy^2\)"], c=[0],
 e=r"Se deriva respecto de \(x\) con \(y\) constante. \(6xy^2\) es la derivada cruzada \(f_{xy}\)."),
dict(q=r"La matriz hessiana de \(f(x,y)=x^2+xy+2y^2\) es:",
 o=[r"\(\begin{pmatrix}2&1\\1&4\end{pmatrix}\)", r"\(\begin{pmatrix}2&1\\1&2\end{pmatrix}\)", r"\(\begin{pmatrix}2x&1\\1&4y\end{pmatrix}\)", r"\(\begin{pmatrix}1&1/2\\1/2&2\end{pmatrix}\)"], c=[0],
 e=r"\(f_{xx}=2,\ f_{xy}=1,\ f_{yy}=4\). La última opción es la matriz de la forma cuadrática, que es la mitad de la hessiana."),
dict(q="Sobre conjuntos convexos, son ciertas:",
 o=["Un conjunto es convexo si contiene el segmento que une dos cualesquiera de sus puntos.", "La intersección de dos conjuntos convexos es convexa.", "La unión de dos conjuntos convexos es convexa.", r"La circunferencia \(\{x^2+y^2=1\}\) es un conjunto convexo."],
 c=[0,1], e=r"La unión de dos discos separados no es convexa. La circunferencia tampoco (el círculo \(x^2+y^2\le1\) sí lo es)."),
dict(q=r"Sobre \(f(x,y)=x^2+y^2\) en \(\mathbb R^2\), son ciertas:",
 o=["Es estrictamente convexa.", "Es convexa.", "Es cóncava.", "Su hessiana es definida positiva en todo punto."],
 c=[0,1,3], e=r"\(Hf=\begin{pmatrix}2&0\\0&2\end{pmatrix}\), DP en todo punto. Toda función estrictamente convexa es convexa."),
dict(q=r"La función \(f(x,y)=\ln x+\ln y\) en \(\mathbb R^2_{++}\) es:",
 o=["Estrictamente cóncava", "Estrictamente convexa", "Ni cóncava ni convexa", "Lineal"], c=[0],
 e=r"\(Hf=\begin{pmatrix}-1/x^2&0\\0&-1/y^2\end{pmatrix}\): definida negativa en todo punto."),
dict(q=r"Si \(Hf(a)\) es indefinida, entonces en \(a\):",
 o=[r"\(f\) no es ni cóncava ni convexa.", r"\(f\) es convexa.", r"\(f\) es cóncava.", r"\(f\) tiene un mínimo."], c=[0],
 e="Una hessiana indefinida indica que la curvatura cambia de signo según la dirección."),
dict(q=r"Con \(u(x,y)=xy\) y consumo \((2,8)\), ¿cuántas unidades de \(y\) cedería el consumidor por una unidad más de \(x\), manteniendo la utilidad?",
 o=["4", "1/4", "16", "8"], c=[0],
 e=r"\(\text{TMS}=u_x/u_y=y/x=8/2=4\)."),
dict(q=r"Sobre \(f(K,L)=K^{0{,}3}L^{0{,}5}\) en \(\mathbb R^2_{++}\), son ciertas:",
 o=[r"\(f_K>0\)", r"\(f_{KK}<0\)", r"\(f\) es convexa.", r"\(f\) es estrictamente cóncava."], c=[0,1,3],
 e=r"\(f_K=0{,}3K^{-0{,}7}L^{0{,}5}>0\) y \(f_{KK}=-0{,}21K^{-1{,}7}L^{0{,}5}<0\). \(\Delta_2=\alpha\beta(1-\alpha-\beta)K^{2\alpha-2}L^{2\beta-2}>0\) porque \(0{,}3+0{,}5<1\): DN."),
dict(q="¿Cuál de estos conjuntos es convexo?",
 o=[r"\(\{(x,y): y\ge x^2\}\)", r"\(\{(x,y): y\le x^2\}\)", r"\(\{(x,y): x^2+y^2\ge1\}\)", r"\(\{(x,y): xy\ge1\}\)"], c=[0],
 e=r"Es el epigrafo de \(x^2\), que es convexa. \(\{xy\ge1\}\) tiene dos ramas (primer y tercer cuadrante): no es convexo, aunque cada rama por separado sí lo es."),
dict(q=r"El teorema de Schwarz garantiza que \(f_{xy}=f_{yx}\) cuando:",
 o=["Las derivadas parciales segundas son continuas.", "La función es polinómica de grado 2.", "La función es cóncava.", "Siempre, sin condiciones."], c=[0],
 e="Con derivadas segundas continuas, la hessiana es simétrica."),
]
