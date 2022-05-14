# também conhecido como classe de caracteres

import re

texto = '1,2,3,4,5,6,a.b c!d?e'

# Para definir uma classe (ou conjunto) de caracteres usa []
regex_pares = '[02468]' # 0 ou 2 ou 4 ou 6 ou 8 ele vai achar
    # é diferente de '02468' que é uma string só
pattern = re.compile(regex_pares)
pattern.findall(texto)

texto2 = 'João não vai passear na moto.'
regex_com_e_sem_acento = '[aã]'
pattern = re.compile(regex_com_e_sem_acento)
pattern.findall(texto2)


regex_grupo_caracter = 'n[aã]'
pattern = re.compile(regex_grupo_caracter)
pattern.findall(texto2)