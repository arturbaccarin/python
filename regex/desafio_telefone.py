import re

texto = '''
Lista Telefônica
    - (11) 98756-1212
    - 98765-4321
    - (85) 99988-7766
    - (21) 3216-8899
'''

pattern = re.compile('\(?\d{0,2}\)?\s?\d{4,5}-\d{4}') # ? - é o opcional, pode ter ou não
# {0,2} - pode ter de 0 a 2 dígitos
pattern.findall(texto)

pattern = re.compile('\d+-\d+')
pattern.findall(texto)