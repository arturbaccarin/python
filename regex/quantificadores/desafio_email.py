import re

texto = '''
Os e-mails dos convidados são:
    - fulano@cod3r.com.br
    - xico@gmail.com
    - joao@empresa.info.br
    - maria_silva@registro.br
    - rafa.sampaio@yahoo.com
'''

pattern = re.compile('\w+@\w+\.\w{2,4}')
pattern.findall(texto)

pattern = re.compile('[\w.]+@\w+\.\w{2,4}')
pattern.findall(texto)

pattern = re.compile('[\w.]+@\w+\.\w{2,4}\.?\w{0,2}')
pattern.findall(texto)


# no futuro ...
pattern = re.compile('[\w.]+@\w+\.\w{2,4}(\.\w{2})?')
pattern.findall(texto)