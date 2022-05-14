import re

texto = '''
123456
cod3r
QUASE123!
#OpA1
#essaSenhaEGrande1234

#OpA1?
Foi123!
'''

pattern = re.compile('^.{6,20}$', re.MULTILINE)
pattern.findall(texto)

pattern = re.compile('^(?=.*[A-Z]).{6,20}$', re.MULTILINE)
pattern.findall(texto)

pattern = re.compile('^(?=.*[A-Z]).{6,20}$', re.MULTILINE)
pattern.findall(texto)

pattern = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%!^&*]).{6,20}$', re.MULTILINE)
pattern.findall(texto)