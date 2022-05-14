import re

texto = '1,2,3,4,5,6,a.b c!d?e'

pattern = re.compile(',')

pattern.findall(texto)
pattern.split(texto)

re.search('b c!d', texto)