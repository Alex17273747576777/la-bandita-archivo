# -*- coding: utf-8 -*-
import json, re, statistics, datetime, pathlib
RAIZ=pathlib.Path(__file__).resolve().parents[3]
M=json.load(open(str(RAIZ/'docs/MEDICION-16-noche-2026-11-04.json'),encoding='utf-8'))
E={f['repo']:f for f in json.load(open(str(RAIZ/'docs/ESCRUTINIO-2026-11-04.json'),encoding='utf-8'))['fichas']}
R=M['repos']; HOY=datetime.date(2026,11,4); HORA=M['medido_a_las']
for _r in R.values():
    if isinstance(_r.get('dias_push'),int) and _r['dias_push']<0: _r['dias_push']=0
LISTA=re.findall(r'^- (\S+/\S+)$',open(str(RAIZ/'docs/LOTE-16-recursos-2026-11-04.md'),encoding='utf-8').read(),re.M)
VIVOS=[r for r in LISTA if R.get(r,{}).get('estado')=='vivo']
NUM={0:'cero',1:'uno',2:'dos',3:'tres',4:'cuatro',5:'cinco',6:'seis',7:'siete',8:'ocho',9:'nueve',10:'diez',
     11:'once',12:'doce',13:'trece',14:'catorce',15:'quince',16:'dieciséis',17:'diecisiete',18:'dieciocho',
     19:'diecinueve',20:'veinte',21:'veintiuno',22:'veintidós',23:'veintitrés',24:'veinticuatro',25:'veinticinco',
     26:'veintiséis',27:'veintisiete',28:'veintiocho',29:'veintinueve',30:'treinta',31:'treinta y uno',
     32:'treinta y dos',33:'treinta y tres',34:'treinta y cuatro',35:'treinta y cinco',36:'treinta y seis',
     37:'treinta y siete',38:'treinta y ocho',39:'treinta y nueve',40:'cuarenta',41:'cuarenta y uno',
     42:'cuarenta y dos',43:'cuarenta y tres',44:'cuarenta y cuatro',45:'cuarenta y cinco',46:'cuarenta y seis',
     47:'cuarenta y siete',48:'cuarenta y ocho',49:'cuarenta y nueve',50:'cincuenta',51:'cincuenta y uno',
     52:'cincuenta y dos'}
def num(n): return f"{n:,}".replace(",", ".")
def palabras(n):
    if n in NUM: return NUM[n]
    if n<100:
        d,r=divmod(n,10)
        base={3:'treinta',4:'cuarenta',5:'cincuenta',6:'sesenta',7:'setenta',8:'ochenta',9:'noventa'}[d]
        return base if r==0 else f"{base} y {NUM[r]}"
    if n<1000:
        c,r=divmod(n,100)
        base={1:'ciento',2:'doscientos',3:'trescientos',4:'cuatrocientos',5:'quinientos',6:'seiscientos',7:'setecientos',8:'ochocientos',9:'novecientos'}[c]
        return base if r==0 else f"{base} {palabras(r)}"
    miles,resto=divmod(n,1000)
    pre='mil' if miles==1 else f"{palabras(miles)} mil"
    return pre if resto==0 else f"{pre} {palabras(resto)}"
def cuando(r):
    d=R[r]['dias_push']
    return '**hoy**' if d==0 else ('ayer' if d==1 else f"hace {d} días")
def estrella(r): return f"★{num(R[r]['stars'])}"
def lic(r):
    l=R[r]['licencia']
    return l if l and l!='NOASSERTION' else 'sin licencia legible'
def adjuntos(r):
    e=E[r]
    if not e['adjuntos']: return "sin adjuntos"
    return f"**{num(e['adjuntos'])} adjuntos · {num(e['con_huella'])} con suma**"
def ficha(r, texto):
    e=E[r]; Rr=R[r]
    edad=f" · madurez {num(Rr['dias_nace'])} d" if Rr['stars']<200 or Rr['dias_nace']<120 else ""
    return (f"**{texto}** — {estrella(r)} · {lic(r)} · empujón {cuando(r)} · {num(Rr['entregas'])} entregas · "
            f"{adjuntos(r)} · nota **{e['puntos']}**{edad} · `{r}`")
def ficha_sin(r, texto):
    e=E[r]; Rr=R[r]
    edad=f" · madurez {num(Rr['dias_nace'])} d" if Rr['stars']<200 or Rr['dias_nace']<120 else ""
    return (f"**{texto}** — {estrella(r)} · {lic(r)} · empujón {cuando(r)} · {num(Rr['entregas'])} entregas · "
            f"{adjuntos(r)} · nota **{e['puntos']}**{edad}")
AGG=dict(vivos=len(VIVOS), estrellas=sum(R[r]['stars'] for r in VIVOS),
         descargas=sum(R[r]['descargas'] for r in VIVOS),
         adjuntos=sum(E[r]['adjuntos'] for r in VIVOS), con_huella=sum(E[r]['con_huella'] for r in VIVOS),
         con_huella_repos=sum(1 for r in VIVOS if E[r]['con_huella']),
         sin_lic=sum(1 for r in VIVOS if not R[r]['licencia'] or R[r]['licencia']=='NOASSERTION'),
         arch=sum(1 for r in VIVOS if R[r]['archivado']),
         push7=sum(1 for r in VIVOS if R[r]['dias_push']<=7), push_hoy=sum(1 for r in VIVOS if R[r]['dias_push']==0),
         sin_entrega=sum(1 for r in VIVOS if R[r]['entregas']==0),
         ci=sum(len(E[r]['flujos_ci']) for r in VIVOS), sin_ci=sum(1 for r in VIVOS if not E[r]['flujos_ci']),
         chicas=sum(1 for r in VIVOS if R[r]['stars']<500),
         nuevas=sum(1 for r in VIVOS if R[r]['dias_nace']<=90),
         mediana_puntos=statistics.median(E[r]['puntos'] for r in VIVOS),
         mediana_dias=statistics.median(R[r]['dias_nace'] for r in VIVOS),
         security=sum(1 for r in VIVOS if E[r]['security_md']),
         nuevas2026=sum(1 for r in VIVOS if R[r]['dias_nace']<=300))
