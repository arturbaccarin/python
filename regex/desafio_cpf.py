import re

texto = '''
CPF dos aprovados:
    - 600.567.890-12
    - 765.998.345-23
    - 454.674.333-21
    - 678.987.153-07
    - 789.112.543-00
'''
pattern = re.compile('\d{3}\.\d{3}\.\d{3}-\d{2}')
pattern.findall(texto)


pattern = re.compile('\d+\.\d+\.\d+-\d+')
pattern.findall(texto)


