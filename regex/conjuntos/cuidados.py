import re

texto = 'ABC [abc] a-c 1234'

pattern = re.compile('[a-c]')
pattern.findall(texto)

pattern = re.compile('a-c') # não define um range
pattern.findall(texto)

pattern = re.compile('[A-z]') # o intervalo usam a ordem da tabela UNICODE / ASCII
pattern.findall(texto)


# tem que respeitar a ordem da tabela UNICODE 
pattern = re.compile('[a-Z]') # error: bad character range a-Z at position 1
pattern.findall(texto)

pattern = re.compile('[4-1]') # error: bad character range 4-1 at position 1
pattern.findall(texto)