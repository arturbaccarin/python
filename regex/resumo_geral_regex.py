from importlib.abc import PathEntryFinder
import re

texto = 'Carlos assinou o Abaixo-Assinado.'

pattern = re.compile('a')

pattern.search(texto)
pattern.findall(texto)

re.findall('a', texto)

pattern_insesitive = re.compile('a', re.IGNORECASE)
pattern_insesitive.findall(texto)


# Meta Caracteres
# . - Ponto -> um caracter qualquer
texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile('.,.')
pattern.findall(texto)

# \ -> escape
pattern = re.compile('.\..')
pattern.findall(texto)

# \s -> space
texto = 'a   b'
pattern = re.compile('a   b')
pattern.findall(texto)

pattern = re.compile('a\s\s\sb')
pattern.findall(texto)

pattern = re.compile('a\s{3}b') # {} -> quantificador
pattern.findall(texto)

# | -> Pipe -> Ou
texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile('e|.,.|\sc')
pattern.findall(texto)

# . -> Problema com o Ponto - ele não identifica o \n
# DOTALL -> o ponto identificar qualquer coisa \t e o \n
texto = 'Bom\nDia'
pattern = re.compile('....', re.DOTALL)
pattern.findall(texto)

# [] -> Conjuntos
texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile('[123abc]')
re.findall(pattern, texto)

pattern = re.compile('[12],')
re.findall(pattern, texto)

texto2 = 'João não vai passear na moto.'
pattern = re.compile('n[aã].')
re.findall(pattern, texto2)

# [123456789] -> [1-9]
texto = '1,2,3,4,5,6,a.b c!d?e F G H'
pattern = re.compile('[1-9]')
re.findall(pattern, texto)

pattern = re.compile('[1-9a-z]')
re.findall(pattern, texto)

pattern = re.compile('[A-z]')
re.findall(pattern, texto)


pattern = re.compile('[a-Z]')
re.findall(pattern, texto)

texto = '1,2,3,4,5,6,a.b c!d?e F G H_'
pattern = re.compile('[A-z]')
re.findall(pattern, texto)

pattern = re.compile('[A-Za-z]')
re.findall(pattern, texto)

pattern = re.compile('a-c') # não é um conjunto
re.findall(pattern, texto)

pattern = re.compile('[a-c]')
re.findall(pattern, texto)

# /[A-Z1-3]/gi -> '[A-Z1-3]' -> '\b[A-Z1-3]' -> r'/[A-Z1-3]/gi'


# Shorthands -> alguns caracteres que representam um conjunto
texto = '1,2,3,4,5,6,a.b c!d?e\n  - f_g'
pattern = re.compile('\d') # todos os números [0-9]
pattern.findall(texto)

pattern = re.compile('\D') # não números [^0-9]
pattern.findall(texto)

pattern = re.compile('\w') # caracteres [a-zA-Z0-9_]
pattern.findall(texto)

pattern = re.compile('\W') # não caracteres [^a-zA-Z0-9_]
pattern.findall(texto)

pattern = re.compile('\s') # espaço  [ \t\n\r\f]
pattern.findall(texto)

pattern = re.compile('\S') # não espaço [^ \t\n\r\f]
pattern.findall(texto)

# Conjunto negado
texto = '1,2,3,4,5,6,a.b c!d?e F G H_'
pattern = re.compile('[^a-c]')
re.findall(pattern, texto)

pattern = re.compile('[^2,36. ]')
re.findall(pattern, texto)

pattern = re.compile('\d{1,3}')

# Selecionando intervalors unicode
texto = 'áéíóú àèìòù âêîôû ç ãõ ü'
pattern = re.compile('[À-ü]')
re.findall(pattern, texto)

texto = 'áéíóú àèìòù âêîôû ç ãõ ü'
pattern = re.compile('[A-z]')
re.findall(pattern, texto)


# Quantificadores
# ? -> zero ou um (opcional)
texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

pattern = re.compile('fogo?') # verifica se o 'o' é opcional é não a palavra 'fogo'
pattern.findall(texto1) # fogo

pattern.findall(texto2) # fog


# + -> um ou mais 
texto3 = 'Os números: 0123456789.'
pattern = re.compile('[0-9]')
pattern.findall(texto3) 

texto3 = 'Os números: 012 34567 89.'
pattern = re.compile('[0-9]+')
pattern.findall(texto3) 


# * -> zero ou mais
texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

pattern = re.compile('fogo*', re.IGNORECASE)
pattern.findall(texto1) # fogo -> ['fogo', 'FOGOOOOOO']

pattern.findall(texto2) # fog


# Quantificadores fixos {3}, {1,6}, {2,}
texto = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46.'

pattern = re.compile('\d{2}')
pattern.findall(texto)

pattern = re.compile('\d{3}')
pattern.findall(texto)

pattern = re.compile('\d{2,}')
pattern.findall(texto)

pattern = re.compile('\d{1,2}')
pattern.findall(texto)


# Grupos -> (1234) (and) -> [1234] (or)
texto1 = 'O José Simão é muito engraçado... hehehehehehe hehe he'
pattern = re.compile('(he)+')
pattern.findall(texto1)

pattern.finditer(texto1)
[print(i) for i in pattern.finditer(texto1)]


# Grupos & Retrovisores
texto2 = 'Lentamente é mente muito lenta.'
pattern = re.compile('(lenta)(mente)', re.IGNORECASE)
[print(i) for i in pattern.finditer(texto2)]

pattern = re.compile('(lenta)(mente)?', re.IGNORECASE)
[print(i) for i in pattern.finditer(texto2)]

pattern = re.compile(r'(lenta)(mente).*\2.*\1', re.IGNORECASE)
[print(i) for i in pattern.finditer(texto2)]


# Grupos aninhados
texto = 'supermercado hipermercado minimercado mercado'
pattern = re.compile('(super|hiper|mini)?mercado') # ? -> 0 ou 1 
[print(i) for i in pattern.finditer(texto)]

pattern = re.compile('((su|hi)per|mini)?mercado') # ? -> 0 ou 1 
[print(i) for i in pattern.finditer(texto)]


# Alguns cuidados com grupos
texto = 'Pedrinho (filho do Pedro Silva) é doutor do ABCabc!'

pattern = re.compile('[(abc)]', re.I)
pattern.findall(texto)

pattern = re.compile('(abc)+', re.I)
[print(i) for i in pattern.finditer(texto)]


# Bordas
texto = 'Romário era um excelente jogador\n, mas hoje é um político\nquestionadoR'
pattern = re.compile('r', re.I)
pattern.findall(texto)

pattern = re.compile('^r', re.I) # ^ -> início de linha/string
pattern.findall(texto)

pattern = re.compile('r$', re.MULTILINE | re.IGNORECASE) # ^ -> início de linha/string
pattern.findall(texto)

pattern = re.compile('^r.*r$', re.MULTILINE | re.IGNORECASE) # . -> não pega \n -> problema do Dotall
pattern.findall(texto) 

pattern = re.compile('^r.*r$', re.MULTILINE | re.IGNORECASE | re.DOTALL) # . -> não pega \n 
pattern.findall(texto) 

pattern = re.compile('^r[\s\S]*r$', re.MULTILINE | re.IGNORECASE | re.DOTALL) # . -> não pega \n 
pattern.findall(texto)  # \s -> ' '\t\r\n


# Bordas de Palavras -> \b
texto1 = 'dia diatonico diafragma media wikipedia bom_dia melodia radial'

pattern = re.compile(r'\bdia\w*')
pattern.findall(texto1)

pattern = re.compile(r'\w*dia\b')
pattern.findall(texto1)

pattern = re.compile(r'\bdia\b')
pattern.findall(texto1)


texto = '1,2,3,4,5,6,a.b c!d?e F G H_'
pattern = re.compile('[,. !?_]')
pattern.split(texto)