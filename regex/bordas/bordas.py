import re

texto = 'Romário era um excelente jogador\n, mas hoje é um político questionador'
texto_2 = 'Romário era um excelente jogador, mas hoje é um político questionador'

pattern = re.compile('r', re.I) # ['R', 'r', 'r', 'r', 'r']
pattern.findall(texto)

# [^] -> dentro de um conjunto significa que é um conjunto negado
# ^ -> fora significa início de linha/string
pattern = re.compile('^r', re.I) # ['R']
pattern.findall(texto)

# $ -> fim da linha ou string
pattern = re.compile('r$', re.I) # ['R']
pattern.findall(texto)

pattern = re.compile('^r.*r$', re.I) # o . não resolve para \n
pattern.findall(texto_2)