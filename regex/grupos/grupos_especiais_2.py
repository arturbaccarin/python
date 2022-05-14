import re

texto = 'supermercado superação hiperMERCADO'

pattern = re.compile('(?:super)[\wÀ-ú]+') # + -> uma ou mais ocorrências
[print(i) for i in pattern.finditer(texto)]


# Positive Lookbehind
pattern = re.compile('(?<=super)[\wÀ-ú]+', re.I)
[print(i) for i in pattern.finditer(texto)]

# Negative Lookbehind
pattern = re.compile('(?<!super)[\wÀ-ú]+', re.I)
[print(i) for i in pattern.finditer(texto)]
