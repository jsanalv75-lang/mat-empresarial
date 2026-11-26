"""Tema 2. Diagonalización de matrices y formas cuadráticas. Problemas originales."""

TITULO = "Tema 2. Diagonalización y formas cuadráticas"
RESUMEN = ("Autovalores y autovectores, polinomio característico, multiplicidades, diagonalización "
           "(matriz diagonal semejante y matriz de paso), formas cuadráticas: expresión matricial, "
           "clasificación por autovalores y por menores principales, formas restringidas.")

MANO = [
dict(
id="t2m1",
titulo="Diagonalizar (o no) una matriz de orden 3",
enunciado=r"""
<p>Se consideran las matrices</p>
\[ A=\begin{pmatrix} 4 & 0 & -2\\ 1 & 2 & -1\\ 1 & 0 & 1\end{pmatrix},\qquad
B=\begin{pmatrix} 3 & 1 & 0\\ 0 & 3 & 0\\ 0 & 0 & 2\end{pmatrix}. \]
<ol class="apartados">
<li>Calcule el polinomio característico y los autovalores de \(A\), con sus multiplicidades.</li>
<li>Calcule los autovectores de \(A\). ¿Es diagonalizable? En caso afirmativo, dé una matriz diagonal semejante y una matriz de paso.</li>
<li>Razone si \(B\) es diagonalizable.</li>
</ol>""",
ideas=r"""
<ul>
<li>En \(|A-\lambda I|\), la segunda columna tiene dos ceros: desarrolla el determinante por esa columna.</li>
<li>Para cada autovalor resuelve \((A-\lambda I)v=0\). El número de parámetros es \(3-\operatorname{rg}(A-\lambda I)\).</li>
<li>Una matriz es diagonalizable si, para cada autovalor, el número de autovectores independientes coincide con su multiplicidad.</li>
<li>\(B\) es triangular: sus autovalores se leen en la diagonal.</li>
</ul>""",
teoria=r"""
<p>\(v\ne0\) es autovector de \(A\) asociado a \(\lambda\) si \(Av=\lambda v\). Los autovalores son las raíces del <b>polinomio característico</b> \(P_A(\lambda)=|A-\lambda I|\).</p>
<p>Si \(\lambda\) tiene multiplicidad algebraica \(m\), su número de autovectores linealmente independientes es \(n-\operatorname{rg}(A-\lambda I)\), que está entre 1 y \(m\).</p>
<p><b>Criterio.</b> \(A\in M_n\) es diagonalizable \(\iff\) tiene \(n\) autovectores linealmente independientes \(\iff\) para cada autovalor, \(n-\operatorname{rg}(A-\lambda I)=m\). Entonces \(P^{-1}AP=D\), con los autovalores en la diagonal de \(D\) y los autovectores, en el mismo orden, como columnas de \(P\).</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Polinomio característico de \(A\)</h5>
\[ P_A(\lambda)=\begin{vmatrix} 4-\lambda & 0 & -2\\ 1 & 2-\lambda & -1\\ 1 & 0 & 1-\lambda\end{vmatrix}. \]
<p>Desarrollamos por la segunda columna (solo queda el elemento \(2-\lambda\), en la posición (2,2), con signo +):</p>
\[ P_A(\lambda)=(2-\lambda)\begin{vmatrix} 4-\lambda & -2\\ 1 & 1-\lambda\end{vmatrix}=(2-\lambda)\big[(4-\lambda)(1-\lambda)+2\big]=(2-\lambda)(\lambda^2-5\lambda+6). \]
<p>Como \(\lambda^2-5\lambda+6=(\lambda-2)(\lambda-3)\):</p>
\[ P_A(\lambda)=-(\lambda-2)^2(\lambda-3). \]
<p class="resultado">Autovalores: \(\lambda_1=2\) con \(m_1=2\); \(\lambda_2=3\) con \(m_2=1\).</p></div>
<div class="paso"><h5>Paso 2. Autovectores de \(\lambda_1=2\)</h5>
\[ A-2I=\begin{pmatrix} 2 & 0 & -2\\ 1 & 0 & -1\\ 1 & 0 & -1\end{pmatrix}. \]
<p>Las tres filas son proporcionales: \(\operatorname{rg}(A-2I)=1\). Queda una ecuación, \(x-z=0\), y dos parámetros: \(y=\alpha\), \(z=\beta\), \(x=\beta\).</p>
\[ (\beta,\alpha,\beta)=\alpha(0,1,0)+\beta(1,0,1),\quad (\alpha,\beta)\ne(0,0). \]
<p>Tomamos \(v_1=(0,1,0)\) y \(v_2=(1,0,1)\): hay 2 autovectores independientes, igual que \(m_1=2\).</p></div>
<div class="paso"><h5>Paso 3. Autovectores de \(\lambda_2=3\)</h5>
\[ A-3I=\begin{pmatrix} 1 & 0 & -2\\ 1 & -1 & -1\\ 1 & 0 & -2\end{pmatrix},\qquad \operatorname{rg}(A-3I)=2. \]
<p>Usamos las dos primeras ecuaciones: \(x=2z\) y \(y=x-z=z\). Con \(z=\alpha\): \((2\alpha,\alpha,\alpha)\), \(\alpha\ne0\). Tomamos \(v_3=(2,1,1)\).</p></div>
<div class="paso"><h5>Paso 4. Diagonalización de \(A\)</h5>
<p>Tenemos 3 autovectores independientes, así que \(A\) <b>es diagonalizable</b>:</p>
\[ D=\begin{pmatrix} 2&0&0\\0&2&0\\0&0&3\end{pmatrix},\qquad P=\begin{pmatrix} 0&1&2\\1&0&1\\0&1&1\end{pmatrix}. \]
<p class="nota">Comprobación: \(\det P=1\ne0\) y \(AP=PD\). Por ejemplo, \(Av_3=(8-2,\ 2+2-1,\ 2+1)=(6,3,3)=3v_3\) ✓.</p></div>
<div class="paso"><h5>Paso 5. La matriz \(B\)</h5>
<p>Es triangular: autovalores \(3\) (doble) y \(2\) (simple). Para \(\lambda=3\):</p>
\[ B-3I=\begin{pmatrix} 0&1&0\\0&0&0\\0&0&-1\end{pmatrix},\qquad \operatorname{rg}(B-3I)=2. \]
<p>Solo hay \(3-2=1\) autovector independiente para un autovalor de multiplicidad 2.</p>
<p class="resultado">\(B\) no es diagonalizable.</p></div>"""),

dict(
id="t2m2",
titulo="Clasificar formas cuadráticas, libres y restringidas",
enunciado=r"""
<p>Se consideran las formas cuadráticas</p>
\[ q_1(x,y,z)=2x^2+y^2+3z^2+2xy-2yz,\qquad q_2(x,y,z)=x^2+y^2+2z^2-4xy. \]
<ol class="apartados">
<li>Escriba la matriz simétrica asociada a cada una y su expresión matricial.</li>
<li>Clasifique \(q_1\) por menores principales.</li>
<li>Clasifique \(q_2\) por menores principales y por autovalores.</li>
<li>Clasifique \(q_2\) restringida a \(x=y\) y restringida a \(x+y=0\).</li>
</ol>""",
ideas=r"""
<ul>
<li>En la matriz simétrica, la diagonal lleva los coeficientes de los cuadrados y cada término cruzado se <b>reparte a medias</b>: \(2xy\to1\) en las posiciones (1,2) y (2,1).</li>
<li>En \(q_2\) la variable \(z\) va sola: la matriz tiene un bloque \(2\times2\) y un 2 aislado, lo que simplifica los autovalores.</li>
<li>Para restringir, despeja una variable de la restricción y sustitúyela en \(q\).</li>
</ul>""",
teoria=r"""
<p><b>Expresión matricial.</b> \(q(X)=X^tAX\) con \(A\) simétrica (\(a_{ij}=a_{ji}\)).</p>
<p><b>Por autovalores.</b> Todos \(>0\): definida positiva (DP). Todos \(<0\): definida negativa (DN). \(\ge0\) con algún 0: semidefinida positiva. \(\le0\) con algún 0: semidefinida negativa. De signos opuestos: indefinida.</p>
<p><b>Por menores principales</b> \(\Delta_1,\dots,\Delta_n\):</p>
<ul>
<li>Todos \(>0\) \(\Rightarrow\) DP.</li>
<li>Signos alternos empezando por negativo (\(\Delta_1<0,\ \Delta_2>0,\ \Delta_3<0,\dots\)) \(\Rightarrow\) DN.</li>
<li>\(\Delta_n\ne0\) y no se da ninguno de los anteriores \(\Rightarrow\) indefinida.</li>
<li>Si \(\Delta_n=0\), el criterio puede no decidir y conviene usar autovalores.</li>
</ul>
<p><b>Restricción.</b> Para clasificar \(q\) sobre un subespacio, se expresan unas variables en función de otras y se clasifica la nueva forma, con menos variables. Si \(q\) es DP (o DN), lo sigue siendo restringida; si es indefinida, la restringida puede ser de cualquier tipo.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Matrices simétricas</h5>
\[ q_1:\ A_1=\begin{pmatrix} 2&1&0\\1&1&-1\\0&-1&3\end{pmatrix},\qquad q_2:\ A_2=\begin{pmatrix} 1&-2&0\\-2&1&0\\0&0&2\end{pmatrix}. \]
<p>La expresión matricial es \(q_i(x,y,z)=(x\ y\ z)\,A_i\,(x\ y\ z)^t\).</p>
<p class="nota">El término \(-2yz\) de \(q_1\) da \(-1\) en (2,3) y (3,2); el \(-4xy\) de \(q_2\) da \(-2\) en (1,2) y (2,1).</p></div>
<div class="paso"><h5>Paso 2. Menores principales de \(q_1\)</h5>
\[ \Delta_1=2>0,\qquad \Delta_2=\begin{vmatrix}2&1\\1&1\end{vmatrix}=1>0, \]
\[ \Delta_3=\det A_1=2(3-1)-1(3-0)+0=4-3=1>0. \]
<p class="resultado">\(q_1\) es definida positiva.</p></div>
<div class="paso"><h5>Paso 3. Clasificación de \(q_2\)</h5>
<p>Menores: \(\Delta_1=1>0\), \(\Delta_2=1-4=-3<0\). Con \(\Delta_2<0\) ya no puede ser DP ni DN, y \(\Delta_3=2\cdot(-3)=-6\ne0\): <b>indefinida</b>.</p>
<p>Por autovalores: \(|A_2-\lambda I|=(2-\lambda)\big[(1-\lambda)^2-4\big]=(2-\lambda)(\lambda-3)(\lambda+1)\). Autovalores \(3,\ 2,\ -1\): hay positivos y negativos, <b>indefinida</b>.</p></div>
<div class="paso"><h5>Paso 4. Restricción a \(x=y\)</h5>
\[ q_2(x,x,z)=x^2+x^2+2z^2-4x^2=-2x^2+2z^2. \]
<p>En las variables \((x,z)\) la matriz es \(\operatorname{diag}(-2,2)\): <b>indefinida</b>.</p></div>
<div class="paso"><h5>Paso 5. Restricción a \(x+y=0\)</h5>
<p>Con \(y=-x\): \(q_2(x,-x,z)=x^2+x^2+2z^2+4x^2=6x^2+2z^2\).</p>
<p class="resultado">Restringida a \(x+y=0\), \(q_2\) es definida positiva. Una forma indefinida puede pasar a ser definida al restringirla.</p></div>"""),

dict(
id="t2m3",
titulo="Beneficios con un parámetro: ¿habrá siempre ganancias?",
enunciado=r"""
<p>El beneficio de una empresa que fabrica dos productos en cantidades \(x,y\) se aproxima por</p>
\[ B(x,y)=x^2+2a\,xy+4y^2,\qquad a\in\mathbb R. \]
<ol class="apartados">
<li>Clasifique la forma cuadrática según los valores de \(a\).</li>
<li>¿Para qué valores de \(a\) se asegura beneficio positivo con cualquier producción no nula?</li>
<li>Si \(a=-3\) y la empresa fabrica la misma cantidad de ambos productos, ¿obtiene beneficios?</li>
</ol>""",
ideas=r"""
<ul>
<li>Escribe la matriz simétrica: el parámetro aparece fuera de la diagonal.</li>
<li>Con una matriz \(2\times2\), el signo de \(\Delta_1\) y de \(\Delta_2\) lo decide casi todo; estudia cuándo \(\Delta_2\) es positivo, cero o negativo.</li>
<li>“La misma cantidad” es la restricción \(y=x\): sustitúyela.</li>
</ul>""",
teoria=r"""
<p>Para \(A=\begin{pmatrix}p&r\\r&s\end{pmatrix}\): si \(\Delta_1=p>0\) y \(\Delta_2=ps-r^2>0\), DP; si \(\Delta_1>0\) y \(\Delta_2=0\), semidefinida positiva; si \(\Delta_2<0\), indefinida.</p>
<p>“Beneficio positivo siempre” equivale a \(B(x,y)>0\) para todo \((x,y)\ne(0,0)\), es decir, a que \(B\) sea definida positiva.</p>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Matriz y menores</h5>
\[ A=\begin{pmatrix}1&a\\a&4\end{pmatrix},\qquad \Delta_1=1>0,\qquad \Delta_2=4-a^2. \]</div>
<div class="paso"><h5>Paso 2. Discusión según \(a\)</h5>
<ul>
<li>\(-2\lt a\lt 2\): \(\Delta_2>0\Rightarrow\) <b>definida positiva</b>.</li>
<li>\(a=\pm2\): \(\Delta_1>0,\ \Delta_2=0\Rightarrow\) <b>semidefinida positiva</b> (autovalores 0 y 5).</li>
<li>\(|a|>2\): \(\Delta_2<0\Rightarrow\) <b>indefinida</b>.</li>
</ul>
<p class="nota">Con \(a=2\), \(B=(x+2y)^2\), que vale 0 en \((2,-1)\ne(0,0)\): por eso es solo semidefinida.</p></div>
<div class="paso"><h5>Paso 3. Beneficio siempre positivo</h5>
<p class="resultado">Solo cuando \(-2\lt a\lt 2\).</p></div>
<div class="paso"><h5>Paso 4. \(a=-3\) con \(y=x\)</h5>
\[ B(x,x)=x^2-6x^2+4x^2=-x^2<0\quad\text{para todo }x\ne0. \]
<p class="resultado">La forma restringida es definida negativa: fabricando lo mismo de ambos productos, la empresa tiene <b>pérdidas</b> para cualquier producción no nula.</p></div>"""),
]

MMA = [
dict(
id="t2w1",
titulo="Diagonalización de matrices de orden 4 y 3",
enunciado=r"""
<p>Se consideran las matrices</p>
\[ M=\begin{pmatrix} 5&-1&-1&-1\\-1&5&-1&-1\\-1&-1&5&-1\\-1&-1&-1&5\end{pmatrix},\qquad
N=\begin{pmatrix} 3&1&0\\0&3&0\\0&0&2\end{pmatrix}. \]
<ol class="apartados">
<li>Obtenga con Mathematica el polinomio característico, los autovalores y los autovectores de \(M\).</li>
<li>Compruebe que \(M\) es diagonalizable: construya \(P\) y \(D\) y verifique \(P^{-1}MP=D\).</li>
<li>Repita el estudio con \(N\) e interprete la lista de autovectores que devuelve Mathematica.</li>
</ol>""",
ideas=r"""
<ul>
<li>Pide a Mathematica los autovalores y los autovectores a la vez: así salen emparejados en el mismo orden.</li>
<li>La matriz de paso tiene los autovectores en <b>columnas</b>, pero Mathematica los da en filas: habrá que trasponer.</li>
<li>Cuando una matriz no es diagonalizable, Mathematica completa la lista de autovectores con vectores nulos.</li>
</ul>""",
teoria=r"""
<p>\(M\) es simétrica, así que es diagonalizable (todas las matrices simétricas reales lo son). Un autovalor triple necesita 3 autovectores independientes, es decir, \(\operatorname{rg}(M-\lambda I)=4-3=1\).</p>
<p>Mathematica calcula \(P_M(\lambda)=\det(M-\lambda I)\), con el mismo convenio que en clase.</p>""",
comandos=r"""
<pre class="mma"><code>M = {{5,-1,-1,-1},{-1,5,-1,-1},{-1,-1,5,-1},{-1,-1,-1,5}};
CharacteristicPolynomial[M, λ] // Factor   (* λ: escribe Esc l Esc *)
{vals, vecs} = Eigensystem[M]
P = Transpose[vecs];
D1 = DiagonalMatrix[vals];      (* no uses D: es la orden de derivar *)
Inverse[P] . M . P == D1
MatrixRank[M - 6 IdentityMatrix[4]]
N1 = {{3,1,0},{0,3,0},{0,0,2}};
Eigenvectors[N1]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Polinomio característico</h5>
<pre class="mma"><code>CharacteristicPolynomial[M, λ] // Factor
<span class="out">(-6 + λ)^3 (-2 + λ)</span></code></pre>
<p>\(P_M(\lambda)=(\lambda-6)^3(\lambda-2)\): \(\lambda=6\) triple y \(\lambda=2\) simple.</p></div>
<div class="paso"><h5>Paso 2. Autovalores y autovectores</h5>
<pre class="mma"><code>{vals, vecs} = Eigensystem[M]
<span class="out">{{6, 6, 6, 2}, {{-1,0,0,1}, {-1,0,1,0}, {-1,1,0,0}, {1,1,1,1}}}</span></code></pre>
<p class="nota">El orden o la escala de los autovectores puede cambiar según la versión; lo importante es el subespacio que generan.</p>
<pre class="mma"><code>MatrixRank[M - 6 IdentityMatrix[4]]
<span class="out">1</span></code></pre>
<p>\(4-1=3\) autovectores independientes para \(\lambda=6\), igual que su multiplicidad.</p></div>
<div class="paso"><h5>Paso 3. Matrices \(P\) y \(D\)</h5>
<pre class="mma"><code>P = Transpose[vecs]; D1 = DiagonalMatrix[vals];
Inverse[P] . M . P == D1
<span class="out">True</span></code></pre>
\[ P=\begin{pmatrix}-1&-1&-1&1\\0&0&1&1\\0&1&0&1\\1&0&0&1\end{pmatrix},\qquad D=\begin{pmatrix}6&0&0&0\\0&6&0&0\\0&0&6&0\\0&0&0&2\end{pmatrix}. \]</div>
<div class="paso"><h5>Paso 4. La matriz \(N\)</h5>
<pre class="mma"><code>Eigenvalues[N1]
<span class="out">{3, 3, 2}</span>
Eigenvectors[N1]
<span class="out">{{1,0,0}, {0,0,0}, {0,0,1}}</span></code></pre>
<p class="resultado">El vector nulo \(\{0,0,0\}\) indica que falta un autovector: \(\lambda=3\) es doble pero solo tiene uno independiente. \(N\) no es diagonalizable.</p>
<p class="nota">No llames <code>N</code> a una matriz: <code>N</code> es la orden que da valores decimales. Por eso usamos <code>N1</code>.</p></div>"""),

dict(
id="t2w2",
titulo="Forma cuadrática de cuatro variables restringida a un subespacio",
enunciado=r"""
<p>Se considera la forma cuadrática</p>
\[ q(x,y,z,t)=x^2+2y^2-z^2+t^2+2xy+4zt. \]
<ol class="apartados">
<li>Obtenga su matriz simétrica y clasifíquela por menores principales y por autovalores.</li>
<li>Clasifíquela restringida al subespacio \(\{x-t=0,\ x-y-z=0\}\).</li>
</ol>""",
ideas=r"""
<ul>
<li>La matriz simétrica de la forma cuadrática es la mitad de su hessiana: no hace falta escribirla a mano.</li>
<li>Despeja dos variables de las restricciones (aquí \(z\) y \(t\)) y sustitúyelas en \(q\).</li>
<li>La forma restringida solo depende de \(x,y\): vuelve a calcular su matriz y clasifícala.</li>
</ul>""",
teoria=r"""
<p>Si \(q\) es indefinida, su restricción a un subespacio puede ser de cualquier tipo, así que hay que calcularla. Tras sustituir, la forma restringida es una forma cuadrática en las variables libres y se clasifica con los criterios habituales.</p>""",
comandos=r"""
<pre class="mma"><code>q = x^2 + 2 y^2 - z^2 + t^2 + 2 x y + 4 z t;
A = D[q, {{x,y,z,t}, 2}]/2;  MatrixForm[A]
Table[Det[A[[1;;k,1;;k]]], {k,1,4}]
Eigenvalues[A] // N
sol = Solve[{x - t == 0, x - y - z == 0}, {z, t}]
qr = Expand[q /. sol[[1]]]
Ar = D[qr, {{x,y}, 2}]/2
Eigenvalues[Ar]
PositiveDefiniteMatrixQ[Ar]</code></pre>""",
resolucion=r"""
<div class="paso"><h5>Paso 1. Matriz simétrica</h5>
<pre class="mma"><code>A = D[q, {{x,y,z,t}, 2}]/2
<span class="out">{{1,1,0,0}, {1,2,0,0}, {0,0,-1,2}, {0,0,2,1}}</span></code></pre></div>
<div class="paso"><h5>Paso 2. Menores y autovalores</h5>
<pre class="mma"><code>Table[Det[A[[1;;k,1;;k]]], {k,1,4}]
<span class="out">{1, 1, -1, -5}</span>
Eigenvalues[A] // N
<span class="out">{2.61803, 2.23607, -2.23607, 0.381966}</span></code></pre>
<p>\(\Delta_1=1>0,\ \Delta_2=1>0,\ \Delta_3=-1<0\) y \(\Delta_4=-5\ne0\): no es DP ni DN, así que es <b>indefinida</b>. Los autovalores tienen signos distintos, lo que lo confirma.</p></div>
<div class="paso"><h5>Paso 3. Restricción</h5>
<pre class="mma"><code>sol = Solve[{x - t == 0, x - y - z == 0}, {z, t}]
<span class="out">{{z -> x - y, t -> x}}</span>
qr = Expand[q /. sol[[1]]]
<span class="out">5 x^2 + y^2</span></code></pre>
<p class="nota">A mano: \(x^2+2y^2-(x-y)^2+x^2+2xy+4(x-y)x=5x^2+y^2\) ✓.</p></div>
<div class="paso"><h5>Paso 4. Clasificación de la restringida</h5>
<pre class="mma"><code>Ar = D[qr, {{x,y}, 2}]/2
<span class="out">{{5, 0}, {0, 1}}</span>
PositiveDefiniteMatrixQ[Ar]
<span class="out">True</span></code></pre>
<p class="resultado">\(q\) es indefinida, pero restringida a \(\{x=t,\ z=x-y\}\) es <b>definida positiva</b> (autovalores 5 y 1).</p></div>"""),
]

TEST = [
dict(q=r"¿Cuáles de los siguientes vectores son autovectores de \(A=\begin{pmatrix}2&1\\1&2\end{pmatrix}\)?",
 o=[r"\((1,1)\)", r"\((1,-1)\)", r"\((1,0)\)", r"\((2,2)\)"], c=[0,1,3],
 e=r"\(A(1,1)=(3,3)=3(1,1)\); \(A(1,-1)=(1,-1)\), autovalor 1; \(A(1,0)=(2,1)\), que no es múltiplo de \((1,0)\); \((2,2)\) es múltiplo de \((1,1)\)."),
dict(q=r"Una matriz \(3\times3\) con tres autovalores reales distintos:",
 o=["Siempre es diagonalizable.", "Nunca es diagonalizable.", "Es diagonalizable solo si es simétrica.", "Tiene determinante nulo."],
 c=[0], e="A autovalores distintos les corresponden autovectores linealmente independientes, así que hay 3."),
dict(q=r"El autovalor \(\lambda=2\) de una matriz \(3\times3\) tiene multiplicidad 2 y \(\operatorname{rg}(A-2I)=2\). Entonces:",
 o=["La matriz no es diagonalizable.", "La matriz es diagonalizable.", r"\(\lambda=2\) tiene 2 autovectores independientes.", "No se puede saber."],
 c=[0], e=r"Autovectores independientes de \(\lambda=2\): \(3-2=1<2\). Falta uno, así que la matriz no es diagonalizable."),
dict(q="Sobre una matriz simétrica real, son ciertas:",
 o=["Siempre es diagonalizable.", "Todos sus autovalores son reales.", "Puede tener autovalores complejos no reales.", "Autovectores de autovalores distintos son ortogonales."],
 c=[0,1,3], e="Es el teorema espectral. Una matriz simétrica real nunca tiene autovalores complejos no reales."),
dict(q=r"La matriz simétrica asociada a \(q(x,y)=3x^2-4xy+y^2\) es:",
 o=[r"\(\begin{pmatrix}3&-2\\-2&1\end{pmatrix}\)", r"\(\begin{pmatrix}3&-4\\0&1\end{pmatrix}\)", r"\(\begin{pmatrix}3&-4\\-4&1\end{pmatrix}\)", r"\(\begin{pmatrix}3&2\\2&1\end{pmatrix}\)"],
 c=[0], e=r"El término cruzado \(-4xy\) se reparte a medias: \(-2\) en cada posición fuera de la diagonal. La segunda matriz también da \(q\), pero no es simétrica."),
dict(q=r"La forma cuadrática \(q(x,y)=3x^2-4xy+y^2\) es:",
 o=["Definida positiva", "Semidefinida positiva", "Indefinida", "Definida negativa"], c=[2],
 e=r"\(\Delta_1=3>0\) y \(\Delta_2=3\cdot1-(-2)^2=-1<0\): indefinida. Por ejemplo, \(q(1,1)=0\), \(q(1,0)=3\) y \(q(1,2)=-1\)."),
dict(q=r"En \(\mathbb R^3\), la forma \(q(x,y,z)=x^2+2y^2\) es:",
 o=["Definida positiva", "Semidefinida positiva", "Indefinida", "Semidefinida negativa"], c=[1],
 e=r"Autovalores 1, 2 y 0. Vale 0 en \((0,0,1)\ne0\), así que no es definida."),
dict(q=r"Los menores principales de la matriz de una forma cuadrática de 3 variables son \(\Delta_1<0,\ \Delta_2>0,\ \Delta_3<0\). La forma es:",
 o=["Definida positiva", "Definida negativa", "Indefinida", "No se puede clasificar"], c=[1],
 e="Signos alternos empezando por negativo: definida negativa."),
dict(q=r"Una forma cuadrática de 2 variables tiene \(\Delta_1>0\) y \(\Delta_2=0\). Es:",
 o=["Definida positiva", "Semidefinida positiva", "Indefinida", "Definida negativa"], c=[1],
 e=r"Con \(\Delta_2=\det=0\), un autovalor es 0. Como \(\Delta_1>0\) y la traza es positiva, el otro autovalor es positivo: semidefinida positiva."),
dict(q=r"Para \(A=\begin{pmatrix}2&5&1\\0&-1&4\\0&0&3\end{pmatrix}\), son ciertas:",
 o=[r"Sus autovalores son \(2,\ -1\) y \(3\).", r"\(\det A=-6\).", "No es diagonalizable.", "Su traza vale 4."],
 c=[0,1,3], e=r"Es triangular: los autovalores son los de la diagonal. Son distintos, así que es diagonalizable. \(\det=2\cdot(-1)\cdot3=-6\) y traza \(=2-1+3=4\)."),
]
