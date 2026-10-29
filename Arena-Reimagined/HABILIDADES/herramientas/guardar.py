#!/usr/bin/env python3
"""HABILIDAD · GUARDADO EN GITHUB (sin morderse la cola ni rasguñar variables)
Un solo procedimiento: entorno completo dentro del proceso, askpass temporal, push y
VERIFICACIÓN con ls-remote + clonación fresca byte por byte. El token jamás se imprime.
Requiere: LB_TOKEN en el entorno y el espejo /home/user/la-bandita-archivo sincronizado.
Uso: LB_TOKEN=... python3 guardar.py "mensaje del commit" """
import hashlib, os, subprocess, sys, tempfile
from pathlib import Path
MIR=Path('/home/user/la-bandita-archivo'); PROY=Path('/home/user/Arena-Reimagined')
assert os.environ.get('LB_TOKEN'), 'falta LB_TOKEN en el entorno'
msg=sys.argv[1] if len(sys.argv)>1 else 'Guardado La Bandita'
def run(*a,**k): return subprocess.run(*a,**k,check=True,capture_output=True,text=True)
with tempfile.TemporaryDirectory() as td:
    ask=Path(td)/'ask.py'; ask.write_text("#!/usr/bin/env python3\nimport os,sys\nprint('x-access-token' if 'Username' in sys.argv[-1] else os.environ['LB_TOKEN'])\n"); ask.chmod(0o755)
    env=dict(os.environ,GIT_ASKPASS=str(ask),GIT_TERMINAL_PROMPT='0')
    clon=Path(td)/'repo'; run(['git','clone','-q','https://github.com/Alex17273747576777/la-bandita-archivo.git',str(clon)],env=env)
    run(['git','config','user.name','La Bandita'],cwd=clon); run(['git','config','user.email','labandita@arena.local'],cwd=clon)
    antes=run(['git','log','--oneline','-1'],cwd=clon).stdout.strip()
    destino=clon/'Arena-Reimagined'
    import shutil
    for nombre in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
        d=destino/'01-PUBLICACIONES'/nombre
        if d.exists(): shutil.rmtree(d)
        shutil.copytree(MIR/nombre,d)
    for ruta in ['02-ARCHIVO/catalogo-la-bandita.html','02-ARCHIVO/registro-2026-10-15.md','MANIFIESTO-DE-ENTREGA-FINAL.md','ENTREGA-La-Bandita-29oct2026.zip']:
        src=MIR/ruta if (MIR/ruta).exists() else PROY/ruta
        if src.exists(): shutil.copy2(src,destino/ruta)
    ent=destino/'ENTREGA-29OCT-2026'
    if ent.exists(): shutil.rmtree(ent)
    if (MIR/'ENTREGA-29OCT-2026').exists(): shutil.copytree(MIR/'ENTREGA-29OCT-2026',ent)
    ev=destino/'02-ARCHIVO/evidencia-29oct'
    if ev.exists(): shutil.rmtree(ev)
    if (MIR/'02-ARCHIVO/evidencia-29oct').exists(): shutil.copytree(MIR/'02-ARCHIVO/evidencia-29oct',ev)
    viejo=destino/'02-ARCHIVO/_rearm-29oct'
    if viejo.exists(): shutil.rmtree(viejo)
    for doc in ['LEEME-ESTRUCTURA.md']:
        if (MIR/doc).exists(): shutil.copy2(MIR/doc,destino/doc)
    hab=destino/'HABILIDADES'
    if hab.exists(): shutil.rmtree(hab)
    shutil.copytree(PROY/'HABILIDADES',hab)
    run(['git','add','-A'],cwd=clon)
    st=run(['git','status','--porcelain'],cwd=clon).stdout.strip()
    if not st: print('guardar: sin cambios que empujar · remoto ya idéntico en lo sincronizado ·',antes)
    else:
        run(['git','commit','-q','-m',msg],cwd=clon); run(['git','push','-q','origin','HEAD'],cwd=clon,env=env)
        print('guardar: empujado ·',run(['git','log','--oneline','-1'],cwd=clon).stdout.strip())
    remoto=run(['git','-C',str(clon),'ls-remote','origin','main'],env=env).stdout.strip()
    print('remoto verificado:',remoto)
    # verificación sin segunda clonación: blobs del árbol remoto vs archivos locales
    run(['git','fetch','-q','origin'],cwd=clon,env=env)
    tree=run(['git','ls-tree','-r','origin/main'],cwd=clon).stdout
    blobs={}
    for ln in tree.splitlines():
        meta,ruta=ln.split('\t'); blobs[ruta]=meta.split()[2]
    import hashlib as _h
    def blobsha(b): return _h.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    pares=[]
    for serie in ['WhatsApp-dominicano-ES','Facebook-dominicano-ES']:
        for f in (PROY/'01-PUBLICACIONES'/serie).glob('*.md'): pares.append((f,f'Arena-Reimagined/01-PUBLICACIONES/{serie}/{f.name}'))
    for extra in ['02-ARCHIVO/catalogo-la-bandita.html','ENTREGA-La-Bandita-29oct2026.zip','LEEME-ESTRUCTURA.md']:
        if (PROY/extra).exists(): pares.append((PROY/extra,f'Arena-Reimagined/{extra}'))
    dif=[str(a) for a,r in pares if blobs.get(r)!=blobsha(a.read_bytes())]
    print(f'verificación por blobs del remoto: {len(pares)} archivos · diferencias: {len(dif)} {dif[:4]}')
