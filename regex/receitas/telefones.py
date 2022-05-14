import re

texto = '''
Lista telefônica:
    - (21) 12345-6789
    - (11) 62300-2234
    - 5678-7770
    - (85) 3333-7890
    - (1) 4321-1234
'''

pattern = re.compile('(\(\d{2}\)\s?)?\d{4,5}-\d{4}')
[print(i) for i in pattern.finditer(texto)]