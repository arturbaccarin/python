# . é um coringa, válido para uma posição somente

import re

texto = '1,2,3,4,5,6,7,8,9,0'
texto = '1X2,3,4,5,6,7,8,9,0'

pattern = re.compile('1.2')
pattern.match(texto)

pattern = re.compile('1..2')
pattern.match(texto) # não retorna nada porque o ponto retorna um caracter só

pattern = re.compile('1..,')
pattern.match(texto)


notas = '8.3,7.1,8.8,10.0'
pattern = re.compile('8..')
re.findall(pattern, notas)

pattern = re.compile('.\..')
re.findall(pattern, notas)