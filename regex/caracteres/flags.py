'''
A flag is an optional parameter to a regex that modifies its behavior of searching.
A flag changes the default searching behaviour of a regular expression.
It makes a regex search in a different way.

A flag is denoted using a single lowercase alphabetic character.

In JavaScript regex, we have a total of 6 flags, each serving a different purpose.

Flag	Name	Modification
i	Ignore Casing	Makes the expression search case-insensitively.
g	Global	Makes the expression search for all occurrences.

'''


# g - global: vai achar o primeiro 'a' e parar
# i - ignore case: 

'''
re.match always starts at the beginning of the string.

re.search steps through the string from the start looking for the first match. It stops when it finds a match.

re.findall returns a list of all the search matches.
'''

import re

texto = 'Carlos assinou o abaixo-assinado.'

pattern = re.compile('a')
match = re.search(pattern, texto)
print(match)
print(match.start())
print(match.end())
print(match.group(0))

valores = re.findall('[a-f]', texto)

# i - ignore case
pattern2 = re.compile('c', re.IGNORECASE) # or re.I
re.search(pattern2, texto)

'''
How to obtain g global search behavior?

The findall in Python will get you matched texts in case you have no capturing groups.
So, for r"somestring", findall is sufficient.

'''

