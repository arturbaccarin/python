import re


texto = 'lista de arquivos mp3: jazz.mp3,rock.mp3,podcast.mp3,blues.mp3'

pattern = re.compile('\.mp3')
pattern.findall(texto)

# no futuro
pattern = re.compile('\w+\.mp3')
pattern.findall(texto)