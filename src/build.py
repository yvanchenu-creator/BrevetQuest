import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d=open(os.path.join(ROOT,'questions.json')).read()
t=open(os.path.join(ROOT,'src','app_template.html')).read().replace('__DATA__', d.replace('</','<\\/'))
head='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0F1426">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='6' fill='%230F1426'/%3E%3Cpath d='M12 4c1 3 4 5 4 9a4 4 0 0 1-8 0c0-2 1-3 1-5 2 1 2 2 2 4 1-2 1-4 1-8z' fill='%23D4FF3A'/%3E%3C/svg%3E">
<script src="config.js"></script>
'''
# move <title>,<meta>,<link>,<style> from template top into head
m=re.match(r'(.*?</style>)(.*)', t, re.S)
out=head+m.group(1)+'\n<style>body{margin:0}*{-webkit-tap-highlight-color:transparent}</style>\n</head>\n<body>'+m.group(2)+'\n</body>\n</html>\n'
open(os.path.join(ROOT,'index.html'),'w').write(out)

