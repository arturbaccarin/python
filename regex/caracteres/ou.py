import re

texto = 'Você precisa responder sim, não ou não sei!'

pattern = re.compile('sim|não sei|não')
pattern.findall(texto)