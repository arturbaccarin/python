# /\d{1,3}\w{1,2}/gi

import re

# INTRODUÇÃO
pattern = re.compile('\d{1,3}\w{1,2}')
texto = 'Desodorande Nivea 300ml Pomada Minâncora 100g Leite Integral 1L Salgadinho Elma Chips 95g'

pattern.findall(texto)
re.findall(pattern, texto)
re.findall('\d{1,3}\w{1,2}', texto)

pattern.search(texto)

# 1 -  Entendendo as Flags
# g -> global : re.findall -> Lista de ocorrências
# i -> ignore case : re.compile('a', re.IGNORECASE)
texto = 'Carlos assinou o Abaixo-Assinado.'
pattern = re.compile('a')
pattern.findall(texto) # ['a', 'a', 'a', 'a']

pattern = re.compile('a', re.IGNORECASE)
pattern.findall(texto) # ['a', 'a', 'A', 'a', 'A', 'a']


# 2 - Caracteres -> os valores do teclado - letras (a, b, c, d...), números (0, 1, 2, 3...) e os caracteres especiais
# (, . ' ')
texto = 'Casa bonita é casa amarela da esquina com a Rua ACASALAR.'
pattern = re.compile('ab ')
pattern.findall(texto)

texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile(',')
pattern.findall(texto)
pattern.split(texto)

# 3 - Meta-Caracteres -> caracteres que irão representar algo '.' -> equivale a qualquer caracter 'wild-card'
# 3.1 Meta-Caracteres: Ponto -> Um caracter qualquer
texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile('.,.')
pattern.findall(texto)

pattern = re.compile('.\..') # escape \ -> usar o ponto como caracter \.
pattern.findall(texto)

notas = '8.3,7.1,8.8,10.0'
pattern = re.compile('...')
pattern.findall(notas) # ['8.3', ',7.', '1,8', '.8,', '10.']

pattern = re.compile('.\..')
pattern.findall(notas) # ['8.3', '7.1', '8.8', '0.0']

pattern = re.compile('\d{1,2}\.\d{1}') # guenta a emoção!
pattern.findall(notas)

# Atenção: cada espaço é um caracter também
texto = 'a   b'
pattern = re.compile('a...b')
pattern.findall(texto)


# 3.2 Meta-Caracteres: Pipe | -> Ou
texto = '1,2,3,4,5,6,a.b c!d?e'
pattern = re.compile(',|\.| |!|\?')
pattern.findall(texto)
pattern.split(texto)

texto = 'Você precisa responder sim, não ou não sei!'
pattern = re.compile('sim|não|sei')
pattern.findall(texto)

# Atenção 2: Problema com ponto
texto = 'Bom\nDia' # \n, \t -> 1 caracter
pattern = re.compile('...')
pattern.findall(texto) # ['Bom', 'Dia']

pattern = re.compile('....')
pattern.findall(texto) # o ponto não resolve \n

# DotAll -> o ponto engloba o \n
pattern = re.compile('....', re.DOTALL)
pattern.findall(texto)


# 4 Conjuntos
# para definir uma classe (ou conjunto) de caracteres usa [] -> OU
texto = '1,2,3,4,5,6,a.b c!d?e[f'
pattern = re.compile('[02458]')
pattern.findall(texto)

texto2 = 'João não vai passear na moto.'
pattern = re.compile('n[aã]')
pattern.findall(texto2)

# Intervalos [a-z]
texto = '1,2,3,4,5,6,a.b c!d?e[f'

pattern = re.compile('[a-z]')
pattern.findall(texto)

pattern = re.compile('[b-d]')
pattern.findall(texto)

pattern = re.compile('[a-z1-3]')
pattern.findall(texto)

# Alguns Cuidados com Intervalos
texto = 'ABC [abc] a-c 1234'
pattern = re.compile('a-c')
pattern.findall(texto)

pattern = re.compile('[a-c]')
pattern.findall(texto)

pattern = re.compile('[A-z]') # ['A', 'B', 'C', '[', 'a', 'b', 'c', ']', 'a', 'c']
pattern.findall(texto)

pattern = re.compile('[z-A]') # na ordem crescente da tabela UNICODE
pattern.findall(texto)

# Conjunto negado
texto = 'ABC [abc] a-c 1234'
pattern = re.compile('[^0-9]') # ['A', 'B', 'C', '[', 'a', 'b', 'c', ']', 'a', 'c']
pattern.findall(texto)

pattern = re.compile('[^a-c]', re.I)
pattern.findall(texto)

# Usando Shorthands -> caracateres que representam um grupo
# \d -> números [0-9]
# \D -> não números [^0-9]
# \w ->  caracteres [a-zA-Z0-9_] -> não é só letra e número. É letra, número e o UNDERLINE
# \W -> não caracteres [^a-zA-Z0-9_]
# \s -> espaço [ \t\n\r\f]
# \S -> não espaço [^ \t\n\r\f]

texto = '1 2 3 _ a b c'
pattern = re.compile('\w')
pattern.findall(texto)

texto = '1 2 3 _ a b c'
pattern = re.compile('\S')
pattern.findall(texto)

texto = '1 2 3 _ a b c'
pattern = re.compile('[\s\S]')
pattern.findall(texto)


# 5 Quantificadores
# Quantificador: ? (Zero-Um)
texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

pattern = re.compile('fogo?', re.I)
pattern.findall(texto1) # ['fogo', 'FOGO']
pattern.findall(texto2) # ['fog']

# Quantificador: + (Um-Mais)
pattern = re.compile('fogo+', re.IGNORECASE)
pattern.findall(texto1) # ['fogo', 'FOGOOOOOO']
pattern.findall(texto2) # []

# Quantificador: * (Zero-Mais)
pattern = re.compile('fogo*', re.IGNORECASE)
pattern.findall(texto1) # ['fogo', 'FOGOOOOOO']
pattern.findall(texto2) # ['fog']

# Quantificador: {n, m}
texto = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46.'
pattern = re.compile('\d{1,2}') # 1 ou 2 dígitos
pattern.findall(texto) # ['fog']

pattern = re.compile('\d{1,}') # 1 ou mais dígitos
pattern.findall(texto) # ['120', '6', '9', '21', '23', '45', '46']

pattern = re.compile('\d{2}') # 1 ou mais dígitos
pattern.findall(texto) # ['12', '21', '23', '45', '46']

pattern = re.compile('\d{1,3}') # 1, 2 ou 3 dígitos
pattern.findall(texto) # ['120', '6', '9', '21', '23', '45', '46']

texto = '''
CPF dos aprovados:
    - 600.567.890-12
    - 765.998.345-23
    - 454.674.333-21
    - 678.987.123-87
    - 789.112.543-00
'''

pattern = re.compile('\d{3}\.\d{3}\.\d{3}-\d{2}') # 1 ou mais dígitos
pattern.findall(texto)



# 6. Grupos
texto1 = 'O José Simão é muito engraçado... hehehehehehe'
pattern = re.compile('(he)+')
iter = pattern.finditer(texto1)
[print(i) for i in iter]

texto = 'supermercado hipermercado minimercado mercado'
pattern = re.compile('(super|hiper|mini)?mercado')
iter = pattern.finditer(texto)
[print(i) for i in iter]

texto = 'supermercado hipermercado minimercado mercado'
pattern = re.compile('((hi|su)per|mini)?mercado')
iter = pattern.finditer(texto)
[print(i) for i in iter]


texto = 'Pedrinho (filho do Pedro Silva) é doutor do ABCabc!'
pattern = re.compile('[(abc)]') # não é um grupo
iter = pattern.finditer(texto)
[print(i) for i in iter]

pattern = re.compile('[abc]') # conjunto
iter = pattern.finditer(texto)
[print(i) for i in iter]

pattern = re.compile('(abc)') # grupo
iter = pattern.finditer(texto)
[print(i) for i in iter]


# 7. Bordas
texto = 'Romário era um excelente jogador\n, mas hoje é um político questionador'

pattern = re.compile('r')
pattern.findall(texto)

pattern = re.compile('^r', re.I) # ^ inicio da linha/string
pattern.findall(texto)

pattern = re.compile('r$', re.I) # $ fim da linha/string
pattern.findall(texto)

# Bordas de Palavras
texto = 'dia diatonico diafragma media wikipedia bom_dia melodia radial'
pattern = re.compile(r'\bdia\w+') # padrão raw -> cru
pattern.findall(texto)

pattern = re.compile(r'\w+gma\b') # padrão raw -> cru
pattern.findall(texto)
