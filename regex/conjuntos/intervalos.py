import re

texto = '1,2,3,4,5,6,a.b c!d?e'

pattern = re.compile('[a-z]')
pattern.findall(texto)

pattern = re.compile('[b-d]')
pattern.findall(texto)

pattern = re.compile('[2-4]')
pattern.findall(texto)

pattern = re.compile('[A-Z2-4]', re.I)
pattern.findall(texto)