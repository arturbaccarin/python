import re

texto = 'O João recebeu 120 milhões apostando 6 9 21 23 45 46.'

# {} - quantificador
pattern = re.compile('\d{1,2}') # pega primeiro pelo máximo e depois pelo mínimo
pattern.findall(texto)

pattern = re.compile('[0-9]{2}')
pattern.findall(texto)

pattern = re.compile('\d{1,}')
pattern.findall(texto)

pattern = re.compile('\w{7}') # ['recebeu', 'milhões', 'apostan'] - talvez o milhões não venha
pattern.findall(texto)

pattern = re.compile('[\wõ]{7}')
pattern.findall(texto)

pattern = re.compile('[\wõ\s]{7}') # ['O João ', 'recebeu', ' 120 mi', 'lhões a', 'postand', 'o 6 9 2', '1 23 45']
pattern.findall(texto)

pattern = re.compile('[\wõ\s]{7,}')
pattern.findall(texto)


# no futuro
# You should be using raw strings in your code
pattern = re.compile(r'\b\d{1,2}\b')
pattern.findall(texto)