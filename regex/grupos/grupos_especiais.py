import re

texto = 'João é calmo, mas no transito fica nervoso.'

pattern = re.compile('[\wÀ-ú]+', re.IGNORECASE) # [\wÀ-ú]+ -> todas as palavras
pattern.findall(texto)

# Positive Lookahead
pattern = re.compile('[\wÀ-ú]+(?=,)', re.IGNORECASE) # única palavra que tem um vírgula na frente
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)

pattern = re.compile('[\wÀ-ú]+(?=\.)', re.IGNORECASE)
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)

pattern = re.compile('[\wÀ-ú]+(?=, mas)', re.IGNORECASE)
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)


# Negative Lookahed
pattern = re.compile(r"[\wÀ-ú]+\b(?!,)", re.IGNORECASE) # palavras que não estejam na frente de vírgula
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)

pattern = re.compile(r"[\wÀ-ú]+\b(?!.)", re.IGNORECASE) # palavras que não estejam na frente de vírgula
iter_ = pattern.finditer(texto)
for i in iter_:
    print(i)