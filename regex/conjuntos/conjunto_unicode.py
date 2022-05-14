import re

texto = 'áéíóú àèìòù âêîôû ç ãõ ü'

pattern = re.compile('[À-ü]')
pattern.findall(texto)