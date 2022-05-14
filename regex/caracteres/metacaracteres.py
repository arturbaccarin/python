'''
Representantes:
. -> Ponto -> um caractere qualquer
[] -> Conjunto -> conjunto de caracteres permitidos
[^] -> Conjunto Negado -> conjunto de caracteres proibidos

Quantificadores
? -> Opcional -> Zero ou um
* -> Asterisco -> Zero ou mais
+ -> Mais -> Um ou mais
{n, m} -> Chaves -> De n até m

Âncoras
^ -> Circunflexo -> Início de linha
$ -> Cifrão -> Fim da Linha
\b -> Borda -> Início ou fim da palavra

Outros Metacaracteres
\\ -> Escape -> Uso de metacaracteres como literal
| -> Ou -> Operação de Ou
( ) -> Grupo -> Define um grupo
\1... \9 -> Retrovisor -> Resgata grupos já definidos
'''

import re

texto = '1,2,3,4,5,6,a.b c!d?e'

pattern = re.compile('\.') # para mostrar que é o valor literal do ponto
# quando você trabalha com símbolo que é metacaracter e quer usar como literal precisa do escape (barra)
pattern.split(texto)

pattern_2 = re.compile(',|\.|\?|!| ')
pattern_2.findall(texto)
pattern_2.split(texto)




texto = '1,2,3,4,5,6,a.b c!d?e'

pattern = re.compile('.,.')
pattern.findall(texto)
pattern.split(texto)