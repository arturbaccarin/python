import re

texto = 'O José Simão é muito engraçado... hehehehehe'

pattern = re.compile('(he)+')
pattern.findall(texto)

result = re.search(pattern, texto)
result.group(0)

pattern.findall(texto)
a = pattern.finditer(texto)
for i in a:
    print(i)



texto2 = 'http://www.site.info www.escola.ninja.br google.com.ag'
pattern = re.compile('(http:\/\/)?(www\.)?\w+\.\w+\.\w{2,}(\.\w{2})?') # ? opcional

result = re.search(pattern, texto2)
result.group(0)

pattern.findall(texto2)
a = pattern.finditer(texto2)
for i in a:
    print(i)