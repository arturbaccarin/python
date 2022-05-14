import re

texto = '1,2,3,a.b c!d?e[f'

pattern = re.compile('\D')
pattern.findall(texto)

pattern = re.compile('[^0-9]') # ^ dentro do conjunto [] ele tem um significado e fora tem outro.
pattern.findall(texto)

pattern = re.compile('[^\d!\?\[\s,\.]')
pattern.findall(texto)

texto_2 = '1: 1"#$%/()*+,-./ 2: :;<==>?@'
pattern = re.compile('[^!-/:-@\s]') # tem dois intervalos
pattern.findall(texto_2)
