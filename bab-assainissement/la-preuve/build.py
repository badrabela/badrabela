import re,base64,os
from io import BytesIO
from PIL import Image
def b64(path,mime): return f'data:{mime};base64,'+base64.b64encode(open(path,'rb').read()).decode()
def imgb64(path,maxw):
    im=Image.open(path).convert('RGB')
    if im.size[0]>maxw: im=im.resize((maxw,int(im.size[1]*maxw/im.size[0])),Image.LANCZOS)
    b=BytesIO(); im.save(b,'JPEG',quality=72); return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
s=open('dossier.src.html').read()
s=re.sub(r'\{\{font:([^}]+)\}\}',lambda m:b64(m.group(1),'font/woff2'),s)
s=re.sub(r'\{\{img:([^}]+)\}\}',lambda m:imgb64(m.group(1),1100),s)
open('dossier.html','w').write(s); print('dossier',os.path.getsize('dossier.html')//1024,'ko')
h=open('index.html').read()
h=re.sub(r'<link rel="preload"[^>]*>\n','',h)
h=re.sub(r'<source media="\(min-width:700px\)" srcset="img/(allee-\d)\.webp">',r'',h)
h=h.replace('img/allee-1-s.webp','img/allee-1.webp').replace('img/allee-4-s.webp','img/allee-4.webp')
h=re.sub(r'url\((fonts/[^)]+)\)',lambda m:'url('+b64(m.group(1),'font/woff2')+')',h)
cache={}
def im(m):
    p=m.group(0)
    if p not in cache: cache[p]=b64(p,'image/webp')
    return cache[p]
h=re.sub(r'img/[a-z0-9\-]+\.webp',im,h)
open('BAB-la-preuve-autonome.html','w').write(h); print('autonome',os.path.getsize('BAB-la-preuve-autonome.html')//1024,'ko',len(cache),'images')
