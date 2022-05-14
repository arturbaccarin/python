import re

texto = 'a   b'

pattern = re.compile('a   b')
pattern.search(texto)

pattern = re.compile('a\s\s\sb')
pattern.search(texto)

pattern = re.compile('a\s \sb')
pattern.search(texto)

# no futuro
pattern = re.compile('a\s+b') # quantos espaços estiverem entre as letras
pattern.search(texto)

pattern = re.compile('a {3}b') # exatamente 3 espaços
pattern.search(texto)

pattern = re.compile('a\s{3}b')
pattern.search(texto)