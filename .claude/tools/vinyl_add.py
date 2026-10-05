#!/usr/bin/env python3
"""Добавляет релиз в раздел «Винил» по номеру издания на Discogs.

Запуск из корня репозитория:
    python3 .claude/tools/vinyl_add.py <release_id>[:<год альбома>][:<имя-файла>] ...

Номер издания — из адреса https://www.discogs.com/release/<release_id>. Адрес вида /master/<id> не подходит:
у альбома много изданий, нужно выбрать конкретное. Скрипт создаёт _vinyl/<имя>.md, скачивает обложку
в assets/img/vinyl/, делает уменьшенную копию в assets/img/vinyl/thumbs/ и превью ссылки
в assets/img/vinyl/og/ (нужны sips и Google Chrome, macOS).
Ответы Discogs кэшируются во временной папке. После запуска файл нужно просмотреть глазами.
"""
import json,re,os,sys,urllib.request,time,tempfile
D=os.path.join(tempfile.gettempdir(),'bukatchuk-vinyl-discogs')+'/'
os.makedirs(D,exist_ok=True)
UA={"User-Agent":"bukatchuk.ru-vinyl/1.0 +https://bukatchuk.ru"}
def get(url,cache):
    if os.path.exists(cache): return json.load(open(cache))
    for a in range(8):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=30)
            d=json.load(r); json.dump(d,open(cache,'w')); time.sleep(2.6); return d
        except Exception as e: time.sleep(25)
    raise SystemExit('fail '+url)
FEAT={'Limited Edition':'лимитированное издание','Numbered':'нумерованное','Remastered':'ремастер','Reissue':'переиздание','Repress':'допечатка','Mixed':'треки сведены','Partially Mixed':'треки частично сведены','Compilation':'сборник','Record Store Day':'Record Store Day','Picture Disc':'пикчер-диск'}
COUNTRY={'Germany':'Германия','Europe':'Европа','Worldwide':'весь мир','UK, Europe & US':'Великобритания, Европа и США','USA & Europe':'США и Европа','UK & Europe':'Великобритания и Европа','US':'США','UK':'Великобритания','France':'Франция','Japan':'Япония'}
def slugify(s):
    s=s.lower().replace('ö','o').replace('ü','u').replace('ä','a').replace('ß','ss')
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def clean(n): return re.sub(r'\s*\(\d+\)$','',n).strip()
made=[]
for arg in sys.argv[1:]:
    p=arg.split(':'); rid=int(p[0]); oy_override=int(p[1]) if len(p)>1 and p[1] else None; slug_override=p[2] if len(p)>2 else None
    d=get(f"https://api.discogs.com/releases/{rid}",D+f'r_{rid}.json')
    artist=clean(d['artists'][0]['name']); title=d['title'].strip()
    slug=slug_override or slugify(artist+' '+title)
    vin=[f for f in d['formats'] if f['name']=='Vinyl']
    qty=sum(int(f.get('qty') or 1) for f in vin)
    colors=[]; feats=[]; weight=''
    for f in d['formats']:
        for x in f.get('descriptions',[]):
            if x in FEAT and FEAT[x] not in feats: feats.append(FEAT[x])
        t=f.get('text') or ''
        if f['name']=='Vinyl' and t:
            if re.search(r'180\s*(gram|gr|g)',t,re.I): weight='180 г'
            c=re.sub(r',?\s*180\s*(gram|gr\.?|g\b)\s*(pressing)?','',t,flags=re.I)
            c=re.sub(r',?\s*(DMM|Gatefold)','',c); c=c.replace(' Vinyl','').strip(' ,')
            if c and c not in colors: colors.append(c)
    notes=d.get('notes') or ''
    if not weight and re.search(r'180\s*g',notes,re.I): weight='180 г'
    m=re.search(r'Limited to (\d[\d.,]*) copies',notes); limited=m.group(1).replace('.','').replace(',','') if m else ''
    lab=d['labels'][0]
    year=(d.get('released') or str(d.get('year')))[:4]
    oy=oy_override
    if not oy and d.get('master_id'):
        oy=get(f"https://api.discogs.com/masters/{d['master_id']}",D+f"m_{d['master_id']}.json").get('year')
    oy=oy or year
    tracks=[]
    flat=[]
    for t in d['tracklist']:
        if t.get('type_')=='index':
            for st in t.get('sub_tracks',[]):
                st=dict(st); st['title']=t['title'].strip()+': '+st['title'].strip(); flat.append(st)
        elif t.get('type_')=='track': flat.append(t)
    for t in flat:
        feat=[clean(a['name']) for a in t.get('artists',[]) if clean(a['name'])!=artist]
        tracks.append((t.get('position','').strip(),t['title'].strip(),(t.get('duration') or '').strip(),feat))
    img=[i for i in d.get('images',[]) if i['type']=='primary'] or d.get('images',[])
    cover=f'/assets/img/vinyl/{slug}.jpg'
    if img and not os.path.exists('.'+cover):
        r=urllib.request.urlopen(urllib.request.Request(img[0]['uri'],headers=UA),timeout=30)
        open('.'+cover,'wb').write(r.read()); time.sleep(1.2)
    thumb='./assets/img/vinyl/thumbs/'+slug+'.jpg'
    if os.path.exists('.'+cover) and not os.path.exists(thumb):
        os.makedirs(os.path.dirname(thumb),exist_ok=True)
        os.system(f'sips -Z 400 -s format jpeg -s formatOptions 78 ".{cover}" --out "{thumb}" >/dev/null 2>&1')
    fmt=(f'{qty}×LP' if qty>1 else 'LP')
    barcode=''
    for i in d.get('identifiers',[]):
        x=re.sub(r'\D','',i.get('value') or '')
        if i.get('type')=='Barcode' and len(x) in (12,13): barcode=x; break
    L=['---','layout: release',f'artist: {q(artist)}',f'title: {q(title)}',f'year: {year}',f'original_year: {oy}',f'released: {d.get("released") or year}',
       f'label: {q(clean(lab["name"]))}',f'catno: {q(lab["catno"].strip())}',f'barcode: {q(barcode)}' if barcode else None,f'country: {q(COUNTRY.get(d.get("country"),d.get("country") or ""))}',
       f'format: {q(fmt)}',f'discs: {qty}']
    # на Discogs цвет указывают, только если он не чёрный; пустое поле означает обычный чёрный винил
    L.append(f'color: {q(" / ".join(colors) if colors else "Black")}')
    if weight: L.append(f'weight: {q(weight)}')
    if limited: L.append(f'limited: {limited}')
    if feats: L.append('features: ['+', '.join(q(x) for x in feats)+']')
    L.append('genres: ['+', '.join(q(x) for x in d.get('genres',[]))+']')
    L.append('styles: ['+', '.join(q(x) for x in d.get('styles',[]))+']')
    L.append(f'discogs: {q("https://www.discogs.com/release/"+str(rid))}')
    L.append(f'cover: {cover}'); L.append(f'image: {cover}')
    L.append(f'description: {q(f"{artist} — {title}: {fmt}, {clean(lab["name"])}, {year}.")}')
    L.append('tracklist:')
    for pos,t,dur,feat in tracks:
        row=f'  - {{pos: {q(pos)}, title: {q(t)}'
        if dur: row+=f', duration: {q(dur)}'
        if feat: row+=', feat: ['+', '.join(q(x) for x in feat)+']'
        L.append(row+'}')
    L.append('---'); L.append('')
    L=[x for x in L if x is not None]
    open(f'_vinyl/{slug}.md','w',encoding='utf-8').write('\n'.join(L))
    print(slug,'|',fmt,'|',' / '.join(colors) or '-','|',weight or '-','|',limited or '-','|',d.get('country'),'|',oy,'→',year,'|',clean(lab['name']),lab['catno'],'|',len(tracks),'tr | first',tracks[0][:3] if tracks else '','| cover',os.path.getsize('.'+cover) if os.path.exists('.'+cover) else 'NONE')
    made.append(slug)

# превью ссылок 1200×630 для новых релизов и общей страницы
if made:
    os.system('python3 "'+os.path.join(os.path.dirname(os.path.abspath(__file__)),'vinyl_og.py')+'" '+' '.join(made))
