# -*- coding: utf-8 -*-
"""mapa-completo.py — canon nacido de la cicatriz 03 (15-oct-2026).
Reconstruye el mapa de una pieza: TODAS las secciones reales (header = *EMOJI …* línea-bold completa),
minutos medidos (1.100 c/min, mínimo 1), Σ honesta y ⏱️ actualizado.
Uso: python3 _herramientas/mapa-completo.py PIEZA.md [--dry]"""
import re, sys, hashlib
EMO=r"[\U0001F300-\U0001FAFF\u2600-\u27BF\U0001F1E6-\U0001F1FF]"
HDR=re.compile(r"^\*%s \S.*\*\s*$"%EMO)   # una sola línea-bold que abre con emoji y CIERRA al final
def main():
    F=sys.argv[1]; dry="--dry" in sys.argv
    d=open(F,encoding="utf-8").read(); PRE=len(d); L=d.split("\n")
    hdrs=[l for l in L if HDR.match(l) and "MAPA DE ESTA GUÍA" not in l]
    # localizar el bloque de vallas que contiene la primera rama
    try: i0=next(i for i,l in enumerate(L) if l.strip().startswith(("├──","└──")))
    except StopIteration:
        print("SIN ÁRBOL previo: se requiere inserción manual (abortado)"); return
    a=next(i for i in range(i0,-1,-1) if L[i].strip()=="```")
    b=next(i for i in range(i0,len(L)) if L[i].strip()=="```")
    idx=[L.index(h) for h in hdrs]
    def corto(h):
        t=h.strip("*").strip()
        while len(t)>48 and "(" in t: t=re.sub(r"\s*\([^()]*\)\s*$","",t).rstrip()
        if len(t)>48:
            t=t[:48].rsplit(" ",1)[0].rstrip(":,;")
        return t
    n=len(hdrs)
    mins=[max(1,round(sum(len(x) for x in L[idx[k]:(idx[k+1] if k+1<n else len(L))])/1100)) for k in range(n)]
    tot=sum(mins)
    ramas=[("%s %s  · ~%d min"%("└──" if k==n-1 else "├──",corto(h),mins[k])) for k,h in enumerate(hdrs)]
    print("secciones: %d · Σ=%d min · árbol previo: %d ramas"%(n,tot,b-a-1))
    for k in range(n): print("   %-3d %s"%(mins[k],ramas[k][4:56]))
    if dry: return
    d2="\n".join(L[:a+1]+ramas+L[b:])
    d2=re.sub(r"⏱️ \*?Lectura total: \d+ min\*","⏱️ *Lectura total: %d min*"%tot,d2,count=1)
    open(F,"w",encoding="utf-8").write(d2)
    print("PRE %d → POST %d · %s · sello %s"%(PRE,len(d2),"DENTRO ✓" if 62000<=len(d2)<=64000 else "FUERA",hashlib.sha256(d2.encode()).hexdigest()[:16]))
main()
