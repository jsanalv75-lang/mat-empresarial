"""Tema 4. Optimización libre y con restricciones de igualdad. Problemas originales."""

TITULO = "Tema 4. Optimización"
RESUMEN = ("Puntos críticos, condiciones de primer y segundo orden, puntos de silla, Teorema de "
           "Weierstrass, Teorema local-global, método de los multiplicadores de Lagrange e "
           "interpretación del multiplicador.")

MANO = [
dict(
id="t4m1",
titulo="Maximizar el beneficio de dos productos",
enunciado=r"""
<p>Una empresa fabrica dos productos en cantidades \(x\) e \(y\) (cientos de unidades). Su beneficio, en miles de euros, es</p>
\[ B(x,y)=40x+60y-2x^2-2xy-3y^2-100. \]
<ol class="apartados">
<li>Calcule los puntos críticos de \(B\).</li>
<li>Clasifíquelos con la condición de segundo orden.</li>
<li>¿Es el óptimo global? ¿Cuál es el beneficio máximo?</li>
</ol>""",
ideas=r"""
<ul>
<li>Iguala a cero las dos derivadas parciales: sale un sistema lineal \(2\times2\).</li>
<li>La hessiana de un polinomio de grado 2 es constante: clasificarla una vez sirve para todo el plano.</li>
<li>Si \(B\) es cóncava en todo \(\mathbb R^2\), el Teorema local-global convierte el máximo local en global.</li>
</ul>""",
teoria=r"""
<p><b>Condición necesaria (1.er orden).</b> Si \(a\) es un óptimo local interior y \(f\) es diferenciable, entonces \(\nabla f(a)=0\) (punto crítico).</p>
<p><b>Condición suficiente (2.º orden).</b> En un punto crítico \(a\): \(Hf(a)\) DN \(\Rightarrow\) máximo local estricto; DP \(\Rightarrow\) mínimo local estricto; indefinida \(\Rightarrow\) punto de silla.</p>
<p><b>Teorema local-global.</b> Si \(f\) es cóncava en un conjunto convexo, todo máximo local es global. Si es convexa, todo mínimo local es global.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Puntos críticos</h5>
\[ \frac{\partial B}{\partial x}=40-4x-2y=0,\qquad \frac{\partial B}{\partial y}=60-2x-6y=0. \]
<p>De la primera, \(y=20-2x\). Sustituyendo: \(60-2x-120+12x=0\Rightarrow10x=60\Rightarrow x=6\), y entonces \(y=8\).</p>
<p class="resultado">Único punto crítico: \((6,8)\).</p></div>
<div class="paso"><h5>Paso 2. Condición de segundo orden</h5>
\[ HB(x,y)=\begin{pmatrix}-4&-2\\-2&-6\end{pmatrix},\qquad \Delta_1=-4<0,\qquad \Delta_2=24-4=20>0. \]
<p>Definida negativa: \((6,8)\) es un <b>máximo local estricto</b>.</p></div>
<div class="paso"><h5>Paso 3. Globalidad y valor</h5>
<p>La hessiana es DN en todo \(\mathbb R^2\), luego \(B\) es estrictamente cóncava en un conjunto convexo. Por el Teorema local-global, \((6,8)\) es el <b>máximo global</b>.</p>
\[ B(6,8)=240+480-72-96-192-100=260. \]
<p class="resultado">Hay que fabricar 600 unidades del primer producto y 800 del segundo. El beneficio máximo es de 260 000 €.</p>
<p class="nota">No se puede usar Weierstrass: \(\mathbb R^2\) no es acotado. No hace falta, porque basta con el Teorema local-global.</p></div>"""),

dict(
id="t4m2",
titulo="Puntos críticos, mínimo local y punto de silla",
enunciado=r"""
<p>Sea \(f(x,y)=x^3-12x+y^2-4y\).</p>
<ol class="apartados">
<li>Halle y clasifique sus puntos críticos.</li>
<li>¿Tiene \(f\) óptimos globales en \(\mathbb R^2\)? ¿Se pueden aplicar Weierstrass o el Teorema local-global?</li>
</ol>""",
ideas=r"""
<ul>
<li>Las variables están separadas: cada derivada solo depende de una variable.</li>
<li>Saldrán dos puntos críticos; la hessiana cambia de signo en el primer elemento.</li>
<li>Para ver si hay óptimo global, mira qué ocurre con \(f(x,2)\) cuando \(x\to-\infty\).</li>
</ul>""",
teoria=r"""
<p>Punto de silla: punto crítico que no es ni máximo ni mínimo local; se detecta cuando la hessiana es indefinida.</p>
<p><b>Weierstrass.</b> Si \(f\) es continua en un conjunto compacto (cerrado y acotado), alcanza máximo y mínimo globales.</p>
<p><b>Local-global.</b> Requiere que \(f\) sea cóncava (para máximos) o convexa (para mínimos) en un conjunto convexo.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Puntos críticos</h5>
\[ f_x=3x^2-12=0\Rightarrow x=\pm2,\qquad f_y=2y-4=0\Rightarrow y=2. \]
<p>Puntos críticos: \((2,2)\) y \((-2,2)\).</p></div>
<div class="paso"><h5>Paso 2. Clasificación</h5>
\[ Hf(x,y)=\begin{pmatrix}6x&0\\0&2\end{pmatrix}. \]
<p>\(Hf(2,2)=\operatorname{diag}(12,2)\): DP \(\Rightarrow\) <b>mínimo local estricto</b>, con \(f(2,2)=8-24+4-8=-20\).</p>
<p>\(Hf(-2,2)=\operatorname{diag}(-12,2)\): indefinida \(\Rightarrow\) <b>punto de silla</b>.</p></div>
<div class="paso"><h5>Paso 3. Globalidad</h5>
<p>\(f(x,2)=x^3-12x-4\to-\infty\) cuando \(x\to-\infty\), y \(f\to+\infty\) cuando \(x\to+\infty\). No hay mínimo ni máximo global.</p>
<p class="resultado">\((2,2)\) es solo un mínimo local. Weierstrass no se aplica porque \(\mathbb R^2\) no es compacto, y local-global tampoco, porque \(f\) no es convexa en todo \(\mathbb R^2\) (\(f_{xx}=6x<0\) si \(x<0\)).</p></div>"""),

dict(
id="t4m3",
titulo="Maximizar la utilidad con una restricción presupuestaria (Lagrange)",
enunciado=r"""
<p>Un consumidor tiene la utilidad \(U(x,y)=xy\). Los precios son \(p_x=2\) y \(p_y=4\) euros, y gasta toda su renta de 80 euros.</p>
<ol class="apartados">
<li>Plantee el problema y resuélvalo por el método de los multiplicadores de Lagrange.</li>
<li>Compruebe la condición de segundo orden y razone la globalidad.</li>
<li>Sin resolver de nuevo, estime la utilidad máxima si la renta fuese de 81 euros.</li>
</ol>""",
ideas=r"""
<ul>
<li>Lagrangiana: \(L=U-\lambda(g-c)\) con \(g=2x+4y\) y \(c=80\).</li>
<li>De las dos primeras ecuaciones puedes despejar \(\lambda\) y relacionar \(x\) con \(y\).</li>
<li>La hessiana de \(L\) en \((x,y)\) es indefinida: tendrás que <b>restringirla</b> al subespacio \(\nabla g\cdot h=0\).</li>
<li>El multiplicador mide cuánto cambia el óptimo por cada euro más de renta.</li>
</ul>""",
teoria=r"""
<p><b>Método de Lagrange.</b> Para optimizar \(f(x,y)\) sujeto a \(g(x,y)=c\):</p>
<ol>
<li>\(L(x,y,\lambda)=f(x,y)-\lambda\,(g(x,y)-c)\).</li>
<li>Puntos críticos: \(\nabla L=0\).</li>
<li>Segundo orden: se clasifica \(H_{(x,y)}L\) restringida al subespacio \(\{h:\nabla g(a)^t h=0\}\). DN \(\Rightarrow\) máximo local; DP \(\Rightarrow\) mínimo local.</li>
</ol>
<p><b>Interpretación.</b> Si \(f^*(c)\) es el valor óptimo, \(\dfrac{df^*}{dc}=\lambda\). Por tanto, \(f^*(c+1)\approx f^*(c)+\lambda\).</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Planteamiento</h5>
\[ \begin{cases}\text{Max. } U(x,y)=xy\\ \text{s.a. } 2x+4y=80\end{cases}\qquad L(x,y,\lambda)=xy-\lambda(2x+4y-80). \]</div>
<div class="paso"><h5>Paso 2. Puntos críticos de \(L\)</h5>
\[ L_x=y-2\lambda=0,\qquad L_y=x-4\lambda=0,\qquad L_\lambda=-(2x+4y-80)=0. \]
<p>De las dos primeras, \(y=2\lambda\) y \(x=4\lambda\), es decir, \(x=2y\). En la restricción: \(4y+4y=80\Rightarrow y=10\), \(x=20\), \(\lambda=5\).</p>
<p class="resultado">Punto crítico: \((x,y,\lambda)=(20,10,5)\).</p></div>
<div class="paso"><h5>Paso 3. Condición de segundo orden</h5>
\[ H_{(x,y)}L=\begin{pmatrix}0&1\\1&0\end{pmatrix}\quad\text{(indefinida: autovalores }\pm1). \]
<p>Subespacio: \(\nabla g=(2,4)\), así que \(2h_1+4h_2=0\Rightarrow h_2=-h_1/2\). Restringida:</p>
\[ q(h_1,h_2)=2h_1h_2 \ \Rightarrow\ q\!\left(h_1,-\tfrac{h_1}{2}\right)=-h_1^2. \]
<p>Es definida negativa: \((20,10)\) es un <b>máximo local estricto</b>.</p></div>
<div class="paso"><h5>Paso 4. Globalidad</h5>
<p>Con \(x,y\ge0\), el conjunto factible es el segmento entre \((40,0)\) y \((0,20)\): cerrado y acotado, es decir, compacto. \(U\) es continua, así que por Weierstrass existe máximo global. En los extremos \(U=0\), luego el máximo global es \((20,10)\), con \(U=200\).</p>
<figure><img src="fig/t4_U.svg" alt="Curvas de nivel xy = 100, 200 y 300 y recta 2x + 4y = 80, tangente a xy = 200 en (20,10)" width="440" height="360"></figure>
<p class="nota">La recta presupuestaria es tangente a la curva de nivel \(xy=200\) en \((20,10)\).</p></div>
<div class="paso"><h5>Paso 5. Renta de 81 euros</h5>
\[ U^*(81)\approx U^*(80)+\lambda=200+5=205. \]
<p class="resultado">Utilidad máxima aproximada: 205. (El valor exacto es \(6561/32\approx205{,}03\).)</p></div>"""),
]

MMA = [
dict(
id="t4w1",
titulo="Minimizar costes con tres bienes (Lagrange con Mathematica)",
enunciado=r"""
<p>El coste de una empresa que fabrica tres bienes es \(C(x,y,z)=x^2+2y^2+3z^2\) (euros), y debe producir en total 110 unidades.</p>
<ol class="apartados">
<li>Plantee la función de Lagrange y obtenga sus puntos críticos con Mathematica.</li>
<li>Clasifique el punto con la condición de segundo orden y razone si es global.</li>
<li>Compruebe el resultado calculando directamente el mínimo global con Mathematica y verifique la interpretación del multiplicador cuando la producción total es de 111 unidades.</li>
</ol>""",
ideas=r"""
<ul>
<li>Define la función de Lagrange y anula sus derivadas respecto de \(x,y,z,\lambda\).</li>
<li>La hessiana de \(L\) respecto de \((x,y,z)\) es diagonal y positiva: si es DP sin restringir, también lo es restringida.</li>
<li>Para comprobar el resultado, Mathematica puede calcular directamente el mínimo global con la restricción.</li>
</ul>""",
teoria=r"""
<p>Si \(H_{(x,y,z)}L\) es DP en el punto crítico, es DP restringida a cualquier subespacio: mínimo local estricto.</p>
<p>Si la función objetivo es convexa y la restricción es lineal (conjunto factible convexo), el Teorema local-global garantiza que el mínimo es global.</p>
<p>\(\lambda\approx\) coste marginal de producir una unidad más en total.</p>""",
comandos=r"""
<pre class="mma"><code>c = x^2 + 2 y^2 + 3 z^2;
lag = c - λ (x + y + z - 110);
sol = Solve[D[lag, {{x,y,z,λ}}] == {0,0,0,0}, {x,y,z,λ}]
c /. sol[[1]]
HL = D[lag, {{x,y,z}, 2}]
PositiveDefiniteMatrixQ[HL]
Minimize[{c, x + y + z == 110}, {x,y,z}]
Minimize[{c, x + y + z == 111}, {x,y,z}] // N</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Puntos críticos de la lagrangiana</h5>
<pre class="mma"><code>lag = c - λ (x + y + z - 110);
sol = Solve[D[lag, {{x,y,z,λ}}] == {0,0,0,0}, {x,y,z,λ}]
<span class="out">{{x -> 60, y -> 30, z -> 20, λ -> 120}}</span>
c /. sol[[1]]
<span class="out">6600</span></code></pre>
<p class="nota">A mano: \(2x=4y=6z=\lambda\Rightarrow x=\lambda/2,\ y=\lambda/4,\ z=\lambda/6\), y \(\tfrac{11}{12}\lambda=110\Rightarrow\lambda=120\) ✓.</p></div>
<div class="paso"><h5>Paso 2. Segundo orden</h5>
<pre class="mma"><code>HL = D[lag, {{x,y,z}, 2}]
<span class="out">{{2, 0, 0}, {0, 4, 0}, {0, 0, 6}}</span>
PositiveDefiniteMatrixQ[HL]
<span class="out">True</span></code></pre>
<p>DP sin restringir, luego DP restringida: \((60,30,20)\) es un <b>mínimo local estricto</b>. Como \(C\) es convexa y la restricción es lineal, por el Teorema local-global es <b>global</b>.</p></div>
<div class="paso"><h5>Paso 3. Comprobación directa del mínimo global</h5>
<pre class="mma"><code>Minimize[{c, x + y + z == 110}, {x,y,z}]
<span class="out">{6600, {x -> 60, y -> 30, z -> 20}}</span>
Minimize[{c, x + y + z == 111}, {x,y,z}] // N
<span class="out">{6720.55, {x -> 60.5455, y -> 30.2727, z -> 20.1818}}</span></code></pre>
<p class="resultado">Coste mínimo: 6600 € con \((60,30,20)\). Con 111 unidades, el coste pasa a 6720,55 €: sube 120,55 €, muy cerca de \(\lambda=120\), el coste marginal.</p></div>"""),

dict(
id="t4w2",
titulo="Optimización libre en tres variables: mínimo y punto de silla",
enunciado=r"""
<p>Sea \(f(x,y,z)=x^3-3x+y^2+z^2+yz-3z\).</p>
<ol class="apartados">
<li>Obtenga con Mathematica los puntos críticos de \(f\).</li>
<li>Clasifíquelos mediante los autovalores de la hessiana.</li>
<li>Estudie si los óptimos locales son globales y compruébelo con una búsqueda numérica de mínimos.</li>
</ol>""",
ideas=r"""
<ul>
<li>Resuelve el sistema \(\nabla f=0\) para obtener todos los puntos críticos.</li>
<li>Evalúa la hessiana en cada punto crítico sin repetir las órdenes a mano, por ejemplo con una tabla.</li>
<li>Para ver si un óptimo es global, estudia \(f(x,0,0)\) cuando \(x\to\pm\infty\).</li>
</ul>""",
teoria=r"""
<p>Hessiana DP en el punto crítico: mínimo local estricto. DN: máximo local estricto. Indefinida: punto de silla. Si es semidefinida, el criterio no decide.</p>
<p>Las búsquedas numéricas de mínimos parten de un punto inicial y encuentran un mínimo <b>local</b>; no garantizan que sea global.</p>""",
comandos=r"""
<pre class="mma"><code>f = x^3 - 3 x + y^2 + z^2 + y z - 3 z;
crit = Solve[D[f, {{x,y,z}}] == {0,0,0}, {x,y,z}]
H = D[f, {{x,y,z}, 2}];
Table[{p, Eigenvalues[H /. p], f /. p}, {p, crit}]
Limit[f /. {y->0, z->0}, x -> -Infinity]
FindMinimum[f, {{x,0.5}, {y,0}, {z,0}}]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Puntos críticos</h5>
<pre class="mma"><code>crit = Solve[D[f, {{x,y,z}}] == {0,0,0}, {x,y,z}]
<span class="out">{{x -> -1, y -> -1, z -> 2}, {x -> 1, y -> -1, z -> 2}}</span></code></pre>
<p class="nota">A mano: \(3x^2-3=0\Rightarrow x=\pm1\); \(2y+z=0\) y \(y+2z-3=0\Rightarrow y=-1,\ z=2\) ✓.</p></div>
<div class="paso"><h5>Paso 2. Clasificación</h5>
<pre class="mma"><code>H = D[f, {{x,y,z}, 2}]
<span class="out">{{6 x, 0, 0}, {0, 2, 1}, {0, 1, 2}}</span>
Table[{p, Eigenvalues[H /. p], f /. p}, {p, crit}]
<span class="out">{{{x -> -1, y -> -1, z -> 2}, {-6, 3, 1}, -1},
 {{x -> 1, y -> -1, z -> 2}, {6, 3, 1}, -5}}</span></code></pre>
<p>\((-1,-1,2)\): autovalores de distinto signo \(\Rightarrow\) <b>punto de silla</b>.</p>
<p>\((1,-1,2)\): todos positivos \(\Rightarrow\) <b>mínimo local estricto</b>, con \(f=-5\).</p></div>
<div class="paso"><h5>Paso 3. Globalidad</h5>
<pre class="mma"><code>Limit[f /. {y->0, z->0}, x -> -Infinity]
<span class="out">-Infinity</span>
FindMinimum[f, {{x,0.5}, {y,0}, {z,0}}]
<span class="out">{-5., {x -> 1., y -> -1., z -> 2.}}</span></code></pre>
<p class="resultado">\((1,-1,2)\) es un mínimo local, pero no global: \(f\) no está acotada inferiormente. <code>FindMinimum</code> encuentra el mínimo local partiendo de un punto cercano.</p></div>"""),
]

TEST = [
dict(q=r"Si \(a\) es un óptimo local interior de una función diferenciable \(f\), entonces:",
 o=[r"\(\nabla f(a)=0\)", r"\(Hf(a)\) es definida positiva", r"\(f(a)=0\)", r"\(Hf(a)\) es indefinida"], c=[0],
 e="Es la condición necesaria de primer orden. La hessiana sirve para clasificar después."),
dict(q="En un punto crítico, la hessiana es indefinida. El punto es:",
 o=["Un punto de silla", "Un máximo local", "Un mínimo local", "Un óptimo global"], c=[0],
 e="Hessiana indefinida: en unas direcciones la función crece y en otras decrece."),
dict(q="El Teorema de Weierstrass asegura la existencia de máximo y mínimo globales si:",
 o=["La función es continua y el conjunto es compacto.", "La función es cóncava.", "El conjunto es convexo.", "La función es derivable en todo el conjunto."], c=[0],
 e="Las hipótesis son continuidad y conjunto compacto (cerrado y acotado)."),
dict(q="Sobre el Teorema local-global, son ciertas:",
 o=[r"Si \(f\) es convexa en un conjunto convexo, todo mínimo local es global.", r"Si \(f\) es cóncava en un conjunto convexo, todo máximo local es global.", r"Si \(f\) es convexa, todo máximo local es global.", "Exige que el conjunto sea compacto."],
 c=[0,1], e="Asocia convexidad con mínimos y concavidad con máximos. La compacidad es una hipótesis de Weierstrass."),
dict(q=r"Para \(f(x,y)=x^2+y^2-2x-4y\):",
 o=[r"\((1,2)\) es mínimo global y \(f(1,2)=-5\).", r"\((1,2)\) es máximo global.", r"\((-1,-2)\) es mínimo global.", r"\((2,4)\) es punto crítico."], c=[0],
 e=r"\(\nabla f=(2x-2,\ 2y-4)=0\Rightarrow(1,2)\). \(Hf=2I\) es DP y \(f\) es convexa en \(\mathbb R^2\): mínimo global. \(f(1,2)=1+4-2-8=-5\)."),
dict(q=r"En el método de Lagrange con \(L=f-\lambda(g-c)\), el multiplicador \(\lambda\) en el óptimo indica:",
 o=[r"La variación aproximada del valor óptimo de \(f\) si \(c\) aumenta en una unidad.", r"El valor de \(f\) en el óptimo.", "La pendiente de la restricción.", "Si el punto es máximo o mínimo."], c=[0],
 e=r"\(df^*/dc=\lambda\). Por eso se llama precio sombra o valor marginal de la restricción."),
dict(q=r"Para \(\min\ x^2+2y^2\) s.a. \(x+y=30\), son ciertas:",
 o=[r"El óptimo está en \((20,10)\).", r"\(\lambda=40\).", r"Si la restricción fuera \(x+y=31\), el coste mínimo aumentaría unas 40 unidades.", "El punto es un máximo."],
 c=[0,1,2], e=r"\(2x=\lambda,\ 4y=\lambda\Rightarrow x=2y\Rightarrow y=10,\ x=20,\ \lambda=40\). \(H_{(x,y)}L=\operatorname{diag}(2,4)\) es DP: mínimo. \(C^*=600\); con 31, \(C^*\approx640\) (exacto: \(640{,}67\))."),
dict(q=r"En un problema con restricción, \(H_{(x,y)}L(a,\lambda)\) restringida al subespacio \(\nabla g(a)^t h=0\) es definida positiva. Entonces \(a\) es:",
 o=["Un mínimo local estricto del problema", "Un máximo local estricto del problema", "Un punto de silla", "No se puede saber"], c=[0],
 e="Es la condición suficiente de segundo orden para problemas con restricciones de igualdad."),
dict(q=r"Sobre \(f(x)=x^3-3x\) en \(\mathbb R\), son ciertas:",
 o=[r"\(x=1\) es un mínimo local.", r"\(x=-1\) es un máximo local.", r"\(x=1\) es un mínimo global.", r"Se puede aplicar Weierstrass en \(\mathbb R\)."],
 c=[0,1], e=r"\(f''(1)=6>0\) y \(f''(-1)=-6<0\). No hay óptimos globales: \(f\to\pm\infty\). \(\mathbb R\) no es compacto."),
dict(q=r"El valor máximo de \(xy\) sujeto a \(x+y=10\) es:",
 o=["25", "10", "50", "20"], c=[0],
 e=r"\(y=\lambda,\ x=\lambda\Rightarrow x=y=5\), \(\lambda=5\). Valor: \(5\cdot5=25\)."),
]
