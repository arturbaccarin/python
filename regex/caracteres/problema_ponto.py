import re

texto = 'Bom\tdia'

pattern = re.compile('.')
pattern.findall(texto) # ['B', 'o', 'm', '\t', 'd', 'i', 'a']


texto = 'Bom\ndia'
pattern = re.compile('.') # ['B', 'o', 'm', 'd', 'i', 'a']
pattern.findall(texto)

# o \n não é resolvido pelo . (ponto)
# dot all - algumas linguagens tem um flag /exp/s, mas JS não

texto = 'Bom\ndia'
pattern = re.compile('...') # ['Bom', 'dia']
pattern.findall(texto)

texto = 'Bom\tdia'
pattern = re.compile('...') # ['Bom', '\tdi']
pattern.findall(texto)