import re

texto = '.$+*?-'

pattern = re.compile('[.$+*?-]') # dentro de um conjunto são elementos literais
# por isso não precisa de escape (barra) dentro do conjunto
pattern.findall(texto)

pattern = re.compile('[.]')

pattern = re.compile('[.$+*?-].')
pattern.findall(texto)

pattern = re.compile('[$-?]') # aqui o - é visto como metacaracter e não como literal
# isso é um intervalo (range)
pattern.findall(texto)

# Não é um intervalo...
pattern = re.compile('[$\-?]')
pattern.findall(texto)

pattern = re.compile('[-?#]')
pattern.findall(texto)

# Pode precisar de escape dentro do conjunto: - [ ] ^ 