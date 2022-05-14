import re

texto = '''
    Leo é muito legal
    Emanuel foi jogar em Sergipe
    Bianca é casa com Habib
'''

pattern = re.compile('\n')
pattern.findall(texto)

pattern = re.compile(r'^(\w).+\1$', re.IGNORECASE)
[print(i) for i in pattern.finditer(texto)]

pattern = re.compile(r'^(\w).+\1$', re.IGNORECASE | re.DOTALL | re.MULTILINE)
[print(i) for i in pattern.finditer(texto)]