import re

texto1 = 'dia diatonico diafragma media wikipedia bom_dia melodia radial'

# palavras que começam com DIA
pattern = re.compile(r"\bdia\w+", re.IGNORECASE)
pattern.findall(texto1)

# palavras que terminam com DIA
pattern = re.compile(r"\w+dia\b", re.IGNORECASE)
pattern.findall(texto1)

# palavras com dia no meio
pattern = re.compile('\w+dia\w+', re.IGNORECASE) 
pattern.findall(texto1)

# seleciona todas do grupo
pattern = re.compile('\w*dia\w*', re.IGNORECASE) 
pattern.findall(texto1)

# trazer apenas a palavra dia
pattern = re.compile(r'\bdia\b', re.IGNORECASE) 
pattern.findall(texto1)

# borda é não \w, que é [^A-Za-z0-9_]... temos problemas com acentos!
# o espaço e acentos são bordas
texto2 = 'dia diatônico diafragma, média wikipédia bom-dia melodia radial'
pattern = re.compile(r'\bdia\b', re.IGNORECASE) 
pattern.findall(texto1)

pattern = re.compile('(\S*)?dia(\S*)?') # a vírgula entra
[print(i) for i in pattern.finditer(texto2)]

pattern = re.compile('([\wÀ-ú-]*)?dia([\wÀ-ú-]*)?') # a vírgula entra
[print(i) for i in pattern.finditer(texto2)] 