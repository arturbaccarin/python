import re

texto = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOO'
texto_2 = 'There is a big fog in NYC'

# + -> um ou mais
pattern = re.compile('fogo+', re.I)
pattern.findall(texto) # ['fogo', 'FOGOOOO']

pattern.findall(texto_2) # []


texto_3 = 'Os números: 0123456789.'
pattern = re.compile('[0-9]') # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pattern.findall(texto_3)

pattern = re.compile('[0-9]+') # ['0123456789']
pattern.findall(texto_3)

pattern = re.compile('\d') # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pattern.findall(texto_3)

pattern = re.compile('\d+') # ['0123456789']
pattern.findall(texto_3)