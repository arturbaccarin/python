import re

texto = 'Pedrinho (filho de Pedro Silva) é doutor do ABC!'

# dentro de um grupo, o conjunto não existe
pattern = re.compile('[(abc)]', re.I)
pattern.findall(texto)

# o conjunto sobrevive dentro de um grupo
pattern = re.compile('[abc]', re.I)
pattern.findall(texto)

pattern = re.compile('(abc)', re.I)
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)
