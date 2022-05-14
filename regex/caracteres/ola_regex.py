import re

texto = 'Casa bonita é casa amarela da esquina com a Rua ACASALAR'

pattern = re.compile('casa', re.I) # valores literais

match = re.search(pattern, texto)
match_all = re.findall(pattern, texto)

re.search('a b', texto)
re.findall('a b', texto)


prog = pattern.match(texto)
result = re.match(pattern, texto)

'''
re.search(pattern, string, flags=0)
Scan through string looking for the first location where the regular expression
pattern produces a match, and return a corresponding match object.
'''

'''
re.match(pattern, string, flags=0)
If zero or more characters at the beginning of string match the regular
expression pattern, return a corresponding match object
'''

# https://docs.python.org/3/library/re.html


texto = 'Olá, como vai você?'
pattern = re.compile('a')
re.search(pattern, texto)
re.search('o', texto)

re.findall('o', texto)

pattern = re.compile('como', re.IGNORECASE)
pattern.search(texto)