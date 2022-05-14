import re

texto = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOO'
texto_2 = 'There is a big fog in NYC'

# * -> zero ou mais
pattern = re.compile('fogo*', re.I)
pattern.findall(texto) # ['fogo', 'FOGOOOO']

pattern.findall(texto_2) # [fog]