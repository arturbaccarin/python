import re

texto = 'supermercado hipermercado minimercado mercado'

pattern = re.compile('(super|hiper|mini)?mercado')
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)

pattern = re.compile('((su|hi)per|mini)?mercado')
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)