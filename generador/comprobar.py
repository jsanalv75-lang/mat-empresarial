"""Recalcula con sympy los resultados que aparecen en la página. Uso: python3 comprobar.py"""
from sympy import *

R = Rational
x, y, z, t, l, K, L = symbols("x y z t lambda K L")
fallos = 0


def ok(nombre, valor, esperado):
    global fallos
    bien = simplify(Matrix([valor]) - Matrix([esperado])) == zeros(*Matrix([valor]).shape) if isinstance(valor, (list, tuple)) else simplify(valor - esperado) == 0
    if not bien:
        fallos += 1
    print(("OK   " if bien else "FALLO"), nombre, valor if not bien else "")


def d(*v):  # decimales exactos
    return [R(str(a)) for a in v]


I3, I4 = eye(3), eye(4)
# ---------- Tema 1 ----------
B = Matrix([[10, 16, 15], [20, 8, 45], [30, 24, 30]]); X = [100, 80, 150]
A = B * diag(*[R(1, a) for a in X])
ok("t1m1 DI", list(B * ones(3, 1)), [41, 73, 84]); ok("t1m1 DF", list(Matrix(X) - B * ones(3, 1)), [59, 7, 66])
ok("t1m1 CI", list(ones(1, 3) * B), [60, 48, 90]); ok("t1m1 A", list(A), d(.1, .2, .1, .2, .1, .3, .3, .3, .2))
ok("t1m1 menores", [(I3 - A)[:k, :k].det() for k in (1, 2, 3)], [R(9, 10), R(77, 100), R(121, 250)])
ok("t1m1 D", list((I3 - A) * Matrix([200, 150, 250])), [125, 20, 95])
ok("t1m1 V", list((I3 - A.T) * Matrix([10, 12, 8])), d(4.2, 6.4, 1.8))
A = Matrix(3, 3, d(.2, .2, .1, .3, .1, .2, 0, .4, .2))
ok("t1m2 X", list((I3 - A).solve(Matrix([40, 85, 20]))), [100, 150, 100])
ok("t1m2 P", list((I3 - A.T).solve(Matrix([7, 13, 12]))), [20, 30, 25])
A = Matrix(3, 3, d(.2, 0, .1, .3, .4, .2, .1, 0, .3)); Bt = A * diag(50, 100, 40)
ok("t1m3 tabla", list(Bt), [10, 0, 4, 15, 40, 8, 5, 0, 12]); ok("t1m3 DF", list(Matrix([50, 100, 40]) - Bt * ones(3, 1)), [36, 37, 23])
A = Matrix(4, 4, d(.1, .2, 0, .1, .2, .1, .3, 0, .1, .3, .1, .2, 0, .1, .2, .3)); Lt = I4 - A
ok("t1w1 menores", [Lt[:k, :k].det() for k in range(1, 5)], [R(9, 10), R(77, 100), R(303, 500), R(3829, 10000)])
print("     t1w1 inversa", [round(float(v), 6) for v in Lt.inv()])
ok("t1w1 D", list(Lt * Matrix([100, 120, 150, 80])), [58, 43, 73, 14])
ok("t1w1 X", list(Lt.solve(Matrix([30, 40, 50, 20]))), [R(34300, 547), R(364800, 3829), R(423800, 3829), R(282600, 3829)])
ok("t1w1 V", list((I4 - A.T) * Matrix([5, 4, 6, 3])), d(3.1, .5, 3.6, .4))
print("     t1w1 P", [round(float(v), 5) for v in (I4 - A.T).solve(Matrix([2, 2, 2, 2]))])
A = Matrix(3, 3, d(.5, .1, .2, .3, .6, .1, .3, .2, .4)); Bb = Matrix(3, 3, d(.5, .4, .2, .3, .6, .1, .3, .2, .4))
ok("t1w2 HS A", [(I3 - A)[:k, :k].det() for k in (1, 2, 3)], [R(1, 2), R(17, 100), R(53, 1000)])
ok("t1w2 HS B", [(I3 - Bb)[:k, :k].det() for k in (1, 2, 3)], [R(1, 2), R(2, 25), R(-1, 100)])
ok("t1w2 inv B", list((I3 - Bb).inv()), [-22, -28, -12, -21, -24, -11, -18, -22, -8])
print("     t1w2 X, dX", [round(float(v), 3) for v in (I3 - A).solve(Matrix([10, 20, 15]))], [round(float(v), 4) for v in (I3 - A).inv() * Matrix([0, 10, 0])])
A2 = Matrix(2, 2, d(.2, .3, .4, .1))
ok("t1 test4", list((eye(2) - A2) * Matrix([50, 40])), [28, 16]); ok("t1 test10", list((eye(2) - A2.T) * Matrix([10, 20])), [0, 15])
# ---------- Tema 2 ----------
A = Matrix([[4, 0, -2], [1, 2, -1], [1, 0, 1]]); P = Matrix([[0, 1, 2], [1, 0, 1], [0, 1, 1]])
ok("t2m1 pol", factor((A - l * I3).det()), -(l - 2) ** 2 * (l - 3)); ok("t2m1 PinvAP", list(P.inv() * A * P), list(diag(2, 2, 3)))
ok("t2m1 rg B-3I", Matrix([[0, 1, 0], [0, 0, 0], [0, 0, -1]]).rank(), 2)
Q1 = Matrix([[2, 1, 0], [1, 1, -1], [0, -1, 3]]); ok("t2m2 q1", [Q1[:k, :k].det() for k in (1, 2, 3)], [2, 1, 1])
ok("t2m2 q1 matriz", expand((Matrix([[x, y, z]]) * Q1 * Matrix([x, y, z]))[0]), 2*x**2 + y**2 + 3*z**2 + 2*x*y - 2*y*z)
q2 = x**2 + y**2 + 2*z**2 - 4*x*y
ok("t2m2 q2 autov", sorted(Matrix([[1, -2, 0], [-2, 1, 0], [0, 0, 2]]).eigenvals()), [-1, 2, 3])
ok("t2m2 x=y", expand(q2.subs(y, x)), -2*x**2 + 2*z**2); ok("t2m2 x+y=0", expand(q2.subs(y, -x)), 6*x**2 + 2*z**2)
ok("t2m3 a=-3,y=x", expand((x**2 - 6*x*y + 4*y**2).subs(y, x)), -x**2)
M = Matrix(4, 4, lambda i, j: 5 if i == j else -1)
ok("t2w1 pol", factor((M - l * I4).det()), (l - 6) ** 3 * (l - 2))
Pm = Matrix([[-1, -1, -1, 1], [0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 1]]); ok("t2w1 PinvMP", list(Pm.inv() * M * Pm), list(diag(6, 6, 6, 2)))
q = x**2 + 2*y**2 - z**2 + t**2 + 2*x*y + 4*z*t; Aq = hessian(q, (x, y, z, t)) / 2
ok("t2w2 menores", [Aq[:k, :k].det() for k in range(1, 5)], [1, 1, -1, -5])
print("     t2w2 autov", sorted([round(float(N(v)), 6) for v in Aq.eigenvals()]))
ok("t2w2 restringida", expand(q.subs({z: x - y, t: x})), 5*x**2 + y**2)
ok("t2 test11", [Matrix([[2, 5, 1], [0, -1, 4], [0, 0, 3]]).det()], [-6])
# ---------- Tema 3 ----------
f = 6 * K**R(1, 2) * L**R(1, 3); pt = {K: 4, L: 8}
ok("t3m1 f,fK,fL", [f.subs(pt), diff(f, K).subs(pt), diff(f, L).subs(pt)], [24, 3, 1])
ok("t3m1 H", list(hessian(f, (K, L)).subs(pt)), [R(-3, 8), R(1, 8), R(1, 8), R(-1, 12)])
ok("t3m1 det H", simplify(hessian(f, (K, L)).det() - 1 / (K * L**R(4, 3))), 0)
g = x**3 - 3*x*y + y**2; ok("t3m2 H", list(hessian(g, (x, y))), [6*x, -3, -3, 2])
ok("t3m2 autov x=3/4", sorted(hessian(g, (x, y)).subs(x, R(3, 4)).eigenvals()), [0, R(13, 2)])
h = x**2*y + y*z**2 - 2*x*z; Hh = hessian(h, (x, y, z))
ok("t3w1 autov (1,1,1)", sorted(Hh.subs({x: 1, y: 1, z: 1}).eigenvals(), key=lambda v: float(v)), [-2*sqrt(2), 2*sqrt(2), 4])
ok("t3w1 autov (0,1,0)", sorted(Hh.subs({x: 0, y: 1, z: 0}).eigenvals()), [0, 4])
gg = -x**2 - 2*y**2 - 3*z**2 + x*y + y*z + 4*x + 2*z; Hg = hessian(gg, (x, y, z))
ok("t3w1 menores g", [Hg[:k, :k].det() for k in (1, 2, 3)], [-2, 7, -40])
s = solve([diff(gg, v) for v in (x, y, z)], [x, y, z]); ok("t3w1 crit g", [s[x], s[y], s[z]], [R(47, 20), R(7, 10), R(9, 20)])
u = x**R(1, 3) * y**R(2, 3); ok("t3w2 TMS", simplify(diff(u, x) / diff(u, y)), y / (2*x))
print("     t3w2 cortes", solve([x + 2*y - 10, x*y - 8], [x, y]))
ok("t3 test TMS", (y / x).subs({x: 2, y: 8}), 4)
# ---------- Tema 4 ----------
Bf = 40*x + 60*y - 2*x**2 - 2*x*y - 3*y**2 - 100; s = solve([diff(Bf, x), diff(Bf, y)])
ok("t4m1", [s[x], s[y], Bf.subs(s)], [6, 8, 260])
f4 = x**3 - 12*x + y**2 - 4*y; ok("t4m2 f(2,2)", f4.subs({x: 2, y: 2}), -20)
s = solve([diff(x*y - l*(2*x + 4*y - 80), v) for v in (x, y, l)], dict=True)[0]; ok("t4m3", [s[x], s[y], s[l]], [20, 10, 5])
s81 = solve([diff(x*y - l*(2*x + 4*y - 81), v) for v in (x, y, l)], dict=True)[0]; ok("t4m3 U(81)", (x*y).subs(s81), R(6561, 32))
c = x**2 + 2*y**2 + 3*z**2
s = solve([diff(c - l*(x + y + z - 110), v) for v in (x, y, z, l)], dict=True)[0]; ok("t4w1", [s[x], s[y], s[z], s[l], c.subs(s)], [60, 30, 20, 120, 6600])
s = solve([diff(c - l*(x + y + z - 111), v) for v in (x, y, z, l)], dict=True)[0]; print("     t4w1 con 111", round(float(c.subs(s)), 2), [round(float(s[v]), 4) for v in (x, y, z)])
f5 = x**3 - 3*x + y**2 + z**2 + y*z - 3*z; sols = solve([diff(f5, v) for v in (x, y, z)], dict=True)
for s in sols:
    print("     t4w2", s, f5.subs(s), sorted(hessian(f5, (x, y, z)).subs(s).eigenvals()))
s = solve([diff(x**2 + 2*y**2 - l*(x + y - 30), v) for v in (x, y, l)], dict=True)[0]; ok("t4 test7", [s[x], s[y], s[l]], [20, 10, 40])
ok("t4 test5", (x**2 + y**2 - 2*x - 4*y).subs({x: 1, y: 2}), -5)

# ---------- Ejercicios estándar ----------
A = I3 - Matrix(3, 3, d(.8, -.2, 0, -.1, .7, -.3, -.2, 0, .9))
ok("t1e1 A", list(A), d(.2, .2, 0, .1, .3, .3, .2, 0, .1)); ok("t1e1 b12", A[0, 1] * 60, 12)
ok("t1e1 V", list((I3 - A.T) * Matrix([10, 20, 10])), [4, 12, 3]); ok("t1e1 P", list((I3 - A.T).solve(Matrix([5, 5, 6]))), [10, 10, 10])
for nom, v, esp in [("A", (.3, .2, .1, .1, .4, .2, .2, .1, .3), d(.7, .4, .245)), ("B", (.6, .3, .2, .2, .5, .1, .3, .4, .6), d(.4, .14, -.015)), ("C", (.5, .4, .1, .2, .3, .2, .4, .1, .6), d(.5, .27, .036))]:
    Lm = I3 - Matrix(3, 3, d(*v)); ok("t1e2 HS " + nom, [Lm[:k, :k].det() for k in (1, 2, 3)], esp)
import itertools
def autonomos(B):
    n = B.shape[0]
    return [J for r in range(1, n + 1) for J in itertools.combinations(range(1, n + 1), r)
            if all(B[j - 1, i - 1] == 0 for i in J for j in range(1, n + 1) if j not in J)]
print("     t1e3", autonomos(Matrix(3, 3, d(.2, 0, 0, .3, .4, .1, .1, .2, .5))), autonomos(Matrix(3, 3, d(.1, .2, .3, .2, .1, .4, .3, .2, .1))), autonomos(Matrix(3, 3, d(.3, 0, .2, 0, .4, 0, .1, 0, .2))))
Bt = Matrix([[8, 10, 4], [12, 5, 8], [4, 15, 8]]); X = [40, 50, 40]
ok("t1e4 DI/DF", list(Bt * ones(3, 1)) + list(Matrix(X) - Bt * ones(3, 1)), [22, 25, 27, 18, 25, 13])
ok("t1e4 IP", list(Matrix([X]) - ones(1, 3) * Bt), [16, 20, 20]); ok("t1e4 a32", Bt[2, 1] / R(50), R(3, 10))
A = Matrix([[2, 0, 1], [0, 3, 0], [1, 0, 2]])
ok("t2e1", sum([list(A * Matrix(v)) for v in [(1, 0, -1), (0, 2, 0), (1, 1, 1), (2, 0, 2)]], []), [1, 0, -1, 0, 6, 0, 3, 3, 3, 6, 0, 6])
a_, b_, c_ = symbols("a b c")
ok("t2e2 a", list(Matrix([[3, 1, 0], [1, 2, 1], [0, 1, 3]]) * Matrix([1, 1, 1])), [4, 4, 4])
ok("t2e2 b", list(Matrix([[2, 0, 1], [0, 3, 0], [1, 0, 2]]) * Matrix([1, 0, 1])), [3, 0, 3])
ok("t2e3", [(Matrix([[1, av, 0], [0, 1, 0], [0, 0, 2]]) - I3).rank() for av in (0, 1)], [1, 2])
for nom, qq, esp in [("q1", x**2 + 2*y**2 + 3*z**2 + 2*x*y, [1, 1, 3]), ("q2", -x**2 - 2*y**2 - z**2 + 2*x*z, [-1, 2, 0]), ("q3", x**2 - y**2 + 4*y*z, [1, -1, -4])]:
    H = hessian(qq, (x, y, z)) / 2; ok("t2e4 " + nom, [H[:k, :k].det() for k in (1, 2, 3)], esp)
ok("t2e4 q2 autov", sorted((hessian(-x**2 - 2*y**2 - z**2 + 2*x*z, (x, y, z)) / 2).eigenvals()), [-2, 0])
ok("t2e4 q3 z=y", expand((x**2 - y**2 + 4*y*z).subs(z, y)), x**2 + 3*y**2)
ok("t3e1 Hf(1,2)", list(hessian(x**3*y**2 - 4*x*y, (x, y)).subs({x: 1, y: 2})), [24, 8, 8, 2])
ok("t3e1 g_xx", simplify(diff(log(x**2 + y), x, 2) - 2*(y - x**2)/(x**2 + y)**2), 0)
ok("t3e1 h_yz", simplify(diff(x*exp(y*z), y, z) - x*(1 + y*z)*exp(y*z)), 0)
u = x**2*y*z; ok("t3e2 u", (diff(u, z)/diff(u, x)).subs({x: 2, y: 3, z: 1}), 1)
F = 10*sqrt(K)*sqrt(L); ok("t3e2 f", (diff(F, L)/diff(F, K)).subs({K: 9, L: 4}), R(9, 4))
ok("t3e4 g", hessian(x**3 - 6*x*y + 3*y**2, (x, y)).det(), 36*x - 36)
ok("t4e1", [solve(diff(x**3 + a_*x**2 + 3, x).subs(x, 2), a_)[0], solve(diff(x*exp(a_*x), x).subs(x, R(1, 2)), a_)[0], solve(diff(x**2 + a_*y**2 + x*y - 5*x, y).subs({x: 2, y: 1}), a_)[0]], [-3, -2, -1])
g4 = x**2 + y**2 + z**2 - x*y + x - 2*z; s = solve([diff(g4, v) for v in (x, y, z)])
ok("t4e2 g", [s[x], s[y], s[z], g4.subs(s)], [R(-2, 3), R(-1, 3), 1, R(-4, 3)])
ok("t4e2 f", [(x**3 + y**3 - 3*x - 12*y).subs({x: 1, y: 2}), (x**3 + y**3 - 3*x - 12*y).subs({x: -1, y: -2})], [-18, 18])
Cc = 3*x**2 + 2*y**2 - 2*x*y - 20*x - 10*y + 100; s = solve([diff(Cc, x), diff(Cc, y)]); ok("t4e3", [s[x], s[y], Cc.subs(s)], [5, 5, 25])
s = solve([diff(x**2 + y**2 - l*(2*x + y - 10), v) for v in (x, y, l)], dict=True)[0]; ok("t4e4 a", [s[x], s[y], s[l]], [4, 2, 4])
s11 = solve([diff(x**2 + y**2 - l*(2*x + y - 11), v) for v in (x, y, l)], dict=True)[0]; ok("t4e4 a 11", (x**2 + y**2).subs(s11), R(121, 5))
ok("t4e4 b", sorted(set((x*y).subs(dd) for dd in solve([diff(x*y - l*(x**2 + y**2 - 8), v) for v in (x, y, l)], dict=True))), [-4, 4])
print("\nFallos:", fallos)
