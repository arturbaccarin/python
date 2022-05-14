import re

# O grupo além de agrupar o número de caracteres, ele captura aquilo que deu match
# quando ele encontra a letra 'b', ele armazenou a letra b
# quando ele controu a palavra 'strong', ele armazenou a palavra 'strong'
# os retrovisores é uma forma de você referenciar aquilo que foi armazenado
# em um determinado grupo. Se tem 1 grupo, vai ter 1 retrovisor. 2 grupos, 2 retrovisores.

texto = '<b>Destaque</b><strong>Frote</strong><div>Conteudo</div>'

pattern = re.compile(r'<(\w+)>.*<\/\1>') # .* -> qualquer coisa 
# o \1 é a forma de referenciar aquilo que foi capturado no grupo
pattern.findall(texto)

iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)


texto2 = 'Lentamente é mente muito lenta.'
pattern = re.compile(r'(lenta)(mente).*\2.*\1\.', re.I)
iter_ = pattern.finditer(texto2)
for i in iter_:
    print(i)

# como não armazenar o valor do grupo ?:
pattern = re.compile(r'(?:lenta)(mente).*\1', re.I) # ?: não captura a informação
iter_ = pattern.finditer(texto2)
for i in iter_:
    print(i)


pattern = re.compile(r'(lenta)(mente)', re.I)
iter_ = pattern.finditer(texto2)
for i in iter_:
    print(i)

pattern = re.compile(r'(lenta)?(mente)', re.I)
iter_ = pattern.finditer(texto2)
for i in iter_:
    print(i)

# trocar um valor pelo retrovisor em JS
# console.log(texto2.replace(/(lenta)(mente)/gi, $2))

# suporta uma quantidade maior do que 9 de retrovisores
texto3 = 'abcdefghijkll'
pattern = re.compile(r'(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)\12')
iter_ = pattern.finditer(texto3)
for i in iter_:
    print(i)