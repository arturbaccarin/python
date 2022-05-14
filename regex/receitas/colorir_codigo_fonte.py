import re

texto = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Código Fonte</title>
	<style>
		code { font-size: 26px; }
	</style>
</head>
<body>
	<h1>Código Fonte</h1>
	<pre>
		<code>
			package cod3r;

			/*
			* Imprimir a nota do aluno
			*/

			public class Nota {

			// Porta de entrada de um programa Java
			public static void main(String[] args) {
				int nota = 7;

				if (nota >= 7) {
					System.out.println("Aprovado")
				} else {
					System.out.println("Reprovado")
				}

				}
			}
		</code>
	</pre>

</body>
</html>
'''

# extrair somente o código fonte
pattern = re.compile('<code>.*<\/code>', re.DOTALL)
code_regex = pattern.findall(texto)[0]

# pegar as strings
pattern = re.compile('\".*\"')
strings_ = pattern.findall(code_regex)

# palavras reservadas
pattern = re.compile(r'\b(pacakge|public|class|static|if|else)\b')
palavras_reservadas = pattern.findall(code_regex)

# tipos
pattern = re.compile(r'\b(void|int)\b')
tipos = pattern.findall(code_regex)

# comentários de múltiplas linhas
pattern = re.compile('\/\*[\s\S]*\*\/')
comentarios_m_linhas = pattern.findall(code_regex)

# comentários de uma linha
pattern = re.compile('\/\/.*?\n')
comentarios_uma_linha = pattern.findall(code_regex)