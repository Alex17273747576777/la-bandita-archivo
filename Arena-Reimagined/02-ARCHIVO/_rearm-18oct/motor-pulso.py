# -*- coding: utf-8 -*-
"""Motor de cirugía de pulso 18-oct-tarde: parcha estrellas/restas/sumas/fechas/push-HOY en piezas nacidas."""
import re,glob,json,sys
def fmt(n): return f"{n:,}".replace(",",".")
MODO=sys.argv[1] if len(sys.argv)>1 else "dry"
fresh={}
for ln in open('/tmp/rearm/censo-fresco-18oct-tarde.tsv',encoding='utf-8').read().splitlines():
    c=ln.split('\t')
    if len(c)>=5:
        try: fresh[c[0]]={'s':int(c[1]),'push':c[3]}
        except: pass
# mapa repo→valores viejos (censo15 + placas actas 16/18-oct-mañana)
olds={
 'ollama/ollama':[183717],'huggingface/transformers':[167814],'open-webui/open-webui':[156064],
 'localsend/localsend':[94549],'louislam/uptime-kuma':[92557],'home-assistant/core':[91562],
 'modelcontextprotocol/servers':[91285,91349],'syncthing/syncthing':[89412],
 'ChatGPTNextWeb/NextChat':[88852,88861],'unslothai/unsloth':[78217],'Mintplex-Labs/anything-llm':[67275],
 'topjohnwu/Magisk':[63273,63307],'termux/termux-app':[62686,62753],'moeru-ai/airi':[50409],
 'team-spotube/spotube':[49956],'Crosstalk-Solutions/project-nomad':[40252],'TeamNewPipe/NewPipe':[40148],
 'yuliskov/SmartTube':[34998],'RikkaApps/Shizuku':[31555],'Johnshall/Shadowrocket-ADBlock-Rules-Forever':[31221],
 'koreader/koreader':[30341],'koodo-reader/koodo-reader':[28513],'GopeedLab/gopeed':[26936],
 'mihonapp/mihon':[24400,24385],'open-ani/animeko':[20948],'ImranR98/Obtainium':[20433],
 'simplex-chat/simplex-chat':[19567],'brunodev85/winlator':[19519],'getlantern/lantern':[16300],
 'organicmaps/organicmaps':[15685],'dolphin-emu/dolphin':[15681],'hrydgard/ppsspp':[14680],
 'libretro/RetroArch':[14367],'LawnchairLauncher/lawnchair':[13713],'MetrolistGroup/Metrolist':[13520],
 'libre-tube/LibreTube':[12823],'maxrave-dev/SimpMusic':[12068],'recloudstream/cloudstream':[10968],
 'TeamPiped/Piped':[10283],'MuntashirAkon/AppManager':[9241],'MorpheApp/morphe-manager':[8995],
 'KotatsuApp/Kotatsu':[8923],'bmax121/APatch':[8050],'aniyomiorg/aniyomi':[7801],
 'j-hc/revanced-magisk-module':[7684],'Droid-ify/client':[7592],'Moriafly/SaltPlayerSource':[7488],
 'mgba-emu/mgba':[7507],'Kunzisoft/KeePassDX':[7480],'rukamori/ArchiveTune':[7167],
 'smuyyh/BookReader':[6953],'shiaho777/web-to-app':[6811],'PixelPlayerHQ/PixelPlayer':[6711],
 'namidaco/namida':[6646],'TeamAmaze/AmazeFileManager':[6429],'bromite/bromite':[6324],
 'gsantner/markor':[6295],'z-huang/InnerTune':[6122],'MorpheApp/MicroG-RE':[5775],
 'fcitx5-android/fcitx5-android':[5761],'miru-project/miru-app':[5757],'OuterTune/OuterTune':[5428],
 'RetroMusicPlayer/RetroMusicPlayer':[5351],'zfdang/Android-Touch-Helper':[5321],'MM2-0/Kvaesitso':[5268],
 'awesome-android-root/awesome-android-root':[5182,5226],'melonDS-emu/melonDS':[5122],
 'komikku-app/komikku':[4873],'keiyoushi/extensions-source':[4792],'gokadzev/Musify':[4330],
 'syncthing/syncthing-android':[4286],'jobobby04/TachiyomiSY':[4177],'libredirect/browser_extension':[4079],
 'PerformanC/ReZygisk':[4060],'proninyaroslav/libretorrent':[3951],'cwuom/NeriPlayer':[3783],
 'FossifyOrg/Gallery':[3801],'futo-org/android-keyboard':[3355],'PaulWoitaschek/Voice':[3180],
 'researchxxl/syncthing-android':[3068],'lnreader/lnreader':[2909],'scummvm/scummvm':[2858],
 'mytv-android/mytv-android':[2804],'nekomangaorg/Neko':[2814],'MeowDump/Integrity-Box':[2747],
 'xoureldeen/Vectras-VM-Android':[2711],'snake-4/Zygisk-Assistant':[2641],'siavash79/PixelXpert':[2449],
 'Leviidev/Husk':[1974],'VegaBobo/DSU-Sideloader':[2324],'staniel359/muffon':[2244],
 'MMRLApp/MMRL':[2206],'sonorahq/sonora':[2052],'null2264/yokai':[1906],
 'kitsumed/ShizuCallRecorder':[1755],'flectar/mail':[1366],'horsemail/yourtv':[1355],
 'oxyroid/M3UAndroid':[1281],'animiruorg/Animiru':[893],'Riteshp2001/mpvRx':[790],
 'Kototoro-app/Kototoro':[625],'yuzono/anime-extensions':[485],'aayush2622/Dartotsu':[479],
 'AppFuton/Futon':[449],'SysAdminDoc/HushFacebook':[288],'AnBui2004/Vectras-VM-Emu-Android':[299],
 'andarcanum/Tadami-Aniyomi-fork':[279],'UsagiApp/Usagi':[273],'SysAdminDoc/HushFeed':[226],

 'Noirero/Miyorare':[13],'Dr-TSNG/ZygiskNext':[10606,10634],'ptitSeb/box64':[5679],
 'dosbox-staging/dosbox-staging':[1815],'Flavor-Z/flavor':[1129],'Noirero/Miyorare-Source-Packs':[8],
}
# ★token_old → (repo, ★token_new)
tok2repo={}
for r,ol in olds.items():
    if r not in fresh: continue
    for o in ol:
        if o>=100 and o!=fresh[r]['s']: tok2repo["★"+fmt(o)]=(r,"★"+fmt(fresh[r]['s']))
# sumas de fila (recalcular)
def S(*rs): return sum(fresh[r]['s'] for r in rs if r in fresh)
fila7180=['brunodev85/winlator','dolphin-emu/dolphin','hrydgard/ppsspp','libretro/RetroArch','stenzek/duckstation','mgba-emu/mgba','ptitSeb/box64','melonDS-emu/melonDS','scummvm/scummvm']
sum7180=S(*fila7180); sum7180h=sum7180+fresh.get('dosbox-staging/dosbox-staging',{}).get('s',0)
sumroot=S('Dr-TSNG/ZygiskNext','bmax121/APatch','j-hc/revanced-magisk-module','awesome-android-root/awesome-android-root','PerformanC/ReZygisk','snake-4/Zygisk-Assistant','siavash79/PixelXpert','MMRLApp/MMRL')
SUMAS={"96.269":fmt(sum7180),"98.084":fmt(sum7180h),"96.319":fmt(sum7180),"43.291":fmt(sumroot),"6.168.116":None}
FECHAS=["(pulso 15-oct-2026)","(pulso 16-oct-2026)","(pulso 17-oct-2026)","(censo 15-oct-2026)","(censo 16-oct-2026)","(censo 17-oct-2026)","(pulso 18-oct-2026)","(censo 18-oct-2026)"]
resumen=[]
files=sorted(glob.glob('01-PUBLICACIONES/WhatsApp-dominicano-ES/2[1-9]-*.md'))+sorted(glob.glob('01-PUBLICACIONES/WhatsApp-dominicano-ES/[3-8][0-9]-*.md'))+sorted(glob.glob('02-ARCHIVO/_fuentes-serie/pack-*.txt'))
for f in files:
    t0=open(f,encoding='utf-8').read()
    lineas=t0.split("\n"); tocadas=set(); cambios=[]
    for i,ln in enumerate(lineas):
        ln0=ln
        # 1) estrellas cambiantes
        for tok,(r,new) in sorted(tok2repo.items(), key=lambda x:-len(x[0])):
            if tok in ln:
                ln=ln.replace(tok,new)
        # 2) sumas de fila
        for old,new in SUMAS.items():
            if new and old in ln: ln=ln.replace(old,new)
        # 3) restas: recompute RHS si ambos operandos son estrellas del mapa nuevo
        def fixresta(m):
            a,b,c=m.group(1),m.group(2),m.group(3)
            try: d=abs(int(a.replace('.',''))-int(b.replace('.','')))
            except: return m.group(0)
            return f"{a}−{b}={fmt(d)}"
        ln=re.sub(r"(\d[\d.]*)−(\d[\d.]*)=(\d[\d.]*)", fixresta, ln)
        # 3b) prosa "por D" entre dos estrellas (guarda: D debe ser resta vieja REAL del par)
        stars_ln=set(re.findall(r"★(\d[\d.]*)", ln))
        if len(stars_ln)==2 and "por " in ln:
            vals=[int(s.replace('.','')) for s in stars_ln]
            new2repo={fmt(v['s']):r for r,v in fresh.items()}
            r1,r2=new2repo.get(stars_ln.__iter__().__next__()),None
            sl=sorted(stars_ln)
            r1=new2repo.get(sl[0]); r2=new2repo.get(sl[1])
            if r1 and r2:
                cands=set()
                for o1 in olds.get(r1,[fresh[r1]['s']]):
                    for o2 in olds.get(r2,[fresh[r2]['s']]):
                        cands.add(abs(o1-o2))
                def fixpor(m):
                    try: d=int(m.group(1).replace('.',''))
                    except: return m.group(0)
                    if d in cands:
                        return "por "+fmt(abs(vals[0]-vals[1]))
                    return m.group(0)
                ln=re.sub(r"por (\d[\d.]*)", fixpor, ln)
        # 4) fechas de pulso/censo en líneas tocadas → 18-oct
        if ln!=ln0:
            for fe in ["15-oct-2026","16-oct-2026","17-oct-2026"]:
                ln=ln.replace("(pulso "+fe+")","(pulso 18-oct-2026)").replace("(censo "+fe+")","(censo 18-oct-2026)")
                ln=ln.replace("pulso "+fe,"pulso 18-oct-2026").replace("censo "+fe,"censo 18-oct-2026")
        # 5) claims push de HOY: si línea tocada y push del repo citado != 18-oct → fecha real
        if ln!=ln0 and re.search(r"push de HOY|push de hoy|empuje de HOY|empuje de hoy|push HOY", ln):
            for tok,(r,new) in tok2repo.items():
                if tok in ln or new in ln:
                    pass
            # buscar repos presentes por valores nuevos/viejos
            for r,fd in fresh.items():
                if fmt(fd['s']) in ln and fd['push']!="2026-10-18":
                    dia={"10":"10-","11":"11-","12":"12-","13":"13-","14":"14-","15":"15-","16":"16-","17":"17-"}.get(fd['push'][5:7],"")+fd['push'][8:10]+"-oct"
                    if fd['push'][:7]=="2026-10":
                        ln=re.sub(r"push de HOY","push "+dia,ln,count=1)
                        ln=re.sub(r"push de hoy","push "+dia,ln,count=1)
                        ln=re.sub(r"empuje de HOY","empuje "+dia,ln,count=1)
                        ln=re.sub(r"empuje de hoy","empuje "+dia,ln,count=1)
        if ln!=ln0:
            cambios.append(i+1); lineas[i]=ln
    t1="\n".join(lineas)
    if cambios:
        resumen.append((f.split('/')[-1][:50],len(cambios)))
        if MODO=="aplicar":
            open(f,'w',encoding='utf-8').write(t1)
print("suma 71-80:",fmt(sum7180),"| con horno:",fmt(sum7180h),"| root II:",fmt(sumroot))
for r,c in resumen: print(f"  {r}: {c} líneas")
print("PIEZAS CON DELTA:",len(resumen))
if MODO=="aplicar": print("APLICADO")
