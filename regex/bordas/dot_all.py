# . dot_all é o ponto pegar qualquer coisa como o \n

import re

texto = 'Romário era um excelente jogador\n, mas hoje é um político questionador'

pattern = re.compile('^r.*r$', re.I) # o . não resolve para \n
pattern.findall(texto) # []

pattern = re.compile('^r[\s\S]*r$', re.I) # seleciona tudo que é Espaço e Não Espaço
pattern.findall(texto)

pattern = re.compile('^r.*r$', re.I | re.DOTALL) # seleciona tudo que é Espaço e Não Espaço
pattern.findall(texto)