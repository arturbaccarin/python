import re

texto = '<div>Conteudo 01</div><div>Conteudo 02</div>'

# quantificadores SÂO gulosos (greedy)...
pattern = re.compile('<div>.+<\/div>')
pattern.findall(texto)

pattern = re.compile('<div>.*<\/div>')
pattern.findall(texto)

pattern = re.compile('<div>.{0,100}<\/div>')
pattern.findall(texto)


# quantificadores NÃO gulosos (lazy)...
pattern = re.compile('<div>.+?<\/div>')
pattern.findall(texto)

pattern = re.compile('<div>.*?<\/div>')
pattern.findall(texto)

pattern = re.compile('<div>.{0,100}?<\/div>')
pattern.findall(texto)