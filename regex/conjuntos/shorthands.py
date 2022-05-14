# shorthands: grupo de atalhos para ter um grupo de caracteres
# shorthand character classes match a single character from a predefined set of characters.
# forma reduzida de ter um grupo de caracteres
# /w serve para agrupar do A-Z a-z 0-9 e o _
# /d - 0-9
# /D - não números

import re

texto = '1,2,3,4,5,6,a.b c!d?e\t-\nf_g'

pattern = re.compile('\d') # números [0-9]
pattern.findall(texto)

pattern = re.compile('\D') # não números [^0-9]
pattern.findall(texto)

pattern = re.compile('\w') # caracteres [a-zA-Z0-9_] - uderline também
pattern.findall(texto)

pattern = re.compile('\W') # não caracteres [a-zA-Z0-9_]
pattern.findall(texto)

pattern = re.compile('\s') # espaço em branco [' ', \t, \n, \r, \f]
pattern.findall(texto)

pattern = re.compile('\S') # não espaço em branco [' ', \t, \n, \r, \f]
pattern.findall(texto)