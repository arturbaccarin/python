import re


texto = '\nca\tr\nr\to s!'

# espaço em branco: tab, pula linha e o \s - shorthand

pattern = re.compile('ca\t') # \t - tab | \n - pulando espaço | \s - espaço
pattern.findall(texto)

pattern = re.compile('\n')
pattern.split(texto)