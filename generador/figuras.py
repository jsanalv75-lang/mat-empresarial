"""Genera las figuras SVG de la página (Tema 3, conjuntos; Tema 4, curvas de nivel)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "svg.fonttype": "none", "font.family": "sans-serif"})
V="#0f3966"; G="#8a8f98"
def ejes(ax, xl, yl):
    ax.axhline(0,color=G,lw=.8); ax.axvline(0,color=G,lw=.8)
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect("equal"); ax.grid(alpha=.25)
    for s in ax.spines.values(): s.set_visible(False)
def guardar(fig,n):
    fig.tight_layout(); fig.savefig(f"fig/{n}.svg",transparent=False,facecolor="white"); plt.close(fig)

# a) X = {y >= x^2-4x+3, y <= 3}
fig,ax=plt.subplots(figsize=(4,3.6)); x=np.linspace(-1,5,400)
ax.plot(x,x**2-4*x+3,color=V,lw=2,label="y = x²−4x+3"); ax.axhline(3,color="#e8890c",lw=2,label="y = 3")
xx=np.linspace(0,4,200); ax.fill_between(xx,xx**2-4*xx+3,3,color=V,alpha=.25)
ax.plot([0,4],[3,3],"ko",ms=4); ax.annotate("(0,3)",(0,3),(-.9,3.4)); ax.annotate("(4,3)",(4,3),(3.6,3.4)); ax.annotate("(2,-1)",(2,-1),(2.2,-1.6))
ejes(ax,(-1,5),(-2,5)); ax.legend(loc="lower left",fontsize=9); ax.set_title("Conjunto X: convexo"); guardar(fig,"t3_X")
# b) semicorona
fig,ax=plt.subplots(figsize=(4,3.0)); th=np.linspace(0,np.pi,200)
ax.fill(np.r_[2*np.cos(th),np.cos(th[::-1])],np.r_[2*np.sin(th),np.sin(th[::-1])],color=V,alpha=.25)
ax.plot(2*np.cos(th),2*np.sin(th),color=V,lw=2); ax.plot(np.cos(th),np.sin(th),color=V,lw=2)
ax.plot([-1.5,1.5],[0,0],"--",color="#e8890c",lw=2); ax.plot([-1.5,1.5],[0,0],"o",color="#e8890c",ms=5)
ax.annotate("P=(-1.5,0)",(-1.5,0),(-2.4,-.5),fontsize=9); ax.annotate("Q=(1.5,0)",(1.5,0),(1.0,-.5),fontsize=9)
ejes(ax,(-2.5,2.5),(-.8,2.3)); ax.set_title("Conjunto Y: no convexo"); guardar(fig,"t3_Y")
# c) xy>=1, x>0
fig,ax=plt.subplots(figsize=(4,3.6)); x=np.linspace(.2,4,300)
ax.plot(x,1/x,color=V,lw=2,label="y = 1/x"); ax.fill_between(x,1/x,5,color=V,alpha=.25)
ejes(ax,(-.5,4),(-.5,4.5)); ax.legend(loc="upper right",fontsize=9); ax.set_title("Conjunto Z: convexo"); guardar(fig,"t3_Z")
# Tema 4: U=xy con 2x+4y=80
fig,ax=plt.subplots(figsize=(4.4,3.6)); x=np.linspace(.5,45,400)
for k in (100,200,300):
    ax.plot(x,k/x,color=G if k!=200 else V,lw=1.2 if k!=200 else 2.2,label=f"xy={k}")
ax.plot(x,(80-2*x)/4,color="#e8890c",lw=2,label="2x+4y=80"); ax.plot(20,10,"ko",ms=5); ax.annotate("(20,10)",(20,10),(22,12))
ax.set_xlim(0,45); ax.set_ylim(0,25); ax.grid(alpha=.25); ax.legend(fontsize=8)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_title("Curvas de nivel y restricción"); guardar(fig,"t4_U")
