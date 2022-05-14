import re

texto = '''
Os e-mails dos convidados são:
    - fulano@cod3r.com.br
    - xico@gmail.com
    - joao@empresa.info.br
    - maria_silva@registro.br
    - rafa.sampaio@yahoo.com
    - fulano+de+tal@escola.ninja.br
'''

pattern = re.compile('\S+@\w+\.\w{2,6}(\.\w{2})?')

[print(i) for i in pattern.finditer(texto)]