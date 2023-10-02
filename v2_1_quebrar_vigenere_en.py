tamanho_tentativa = 30
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# frequencias
frequencia_en = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# Retorna o índice de coincidência para a "seção" do texto cifrado 
def indice_auxiliar(texto_cifrado):
	
	N = float(len(texto_cifrado))
	soma_frequencia = 0.0

	# formula de coincidencia
	for letra in alfabeto:
		soma_frequencia+= texto_cifrado.count(letra) * (texto_cifrado.count(letra)-1)

	# formula de coincidencia
	ic = soma_frequencia/(N*(N-1))
	return ic

# Retorna o comprimento da chave com o índice médio de coincidência mais alto
def get_comprimento_chave(texto_cifrado):
	tabela_auxiliar=[]
	# Divide o texto cifrado em sequências com base no comprimento da chave adivinhada de 0 até o comprimento máximo da chave estimado (20)
	for comprimento_tentativa in range(tamanho_tentativa):
		soma_auxiliar=0.0
		media_auxilia=0.0
		for i in range(comprimento_tentativa):
			sequence=""
			# quebra em sequencias 
			for j in range(0, len(texto_cifrado[i:]), comprimento_tentativa):
				sequence += texto_cifrado[i+j]
			soma_auxiliar+=indice_auxiliar(sequence)
		# evitar divisão por zero
		if not comprimento_tentativa==0:
			media_auxilia=soma_auxiliar/comprimento_tentativa
		tabela_auxiliar.append(media_auxilia)

		# retorna o índice do índice de coincidência mais alto (comprimento de chave mais provável)
	melhor_tentativa = tabela_auxiliar.index(sorted(tabela_auxiliar, reverse = True)[0])
	segunda_melhor_tentativa = tabela_auxiliar.index(sorted(tabela_auxiliar, reverse = True)[1])
	# Como este programa pode retornar que a chave é  duas vezes ela mesma, ou três vezes ela mesma, manter valores menores
	# A distribuição de frequência para a chave "chave" vs "chavechave" seria muito parecida
	if melhor_tentativa % segunda_melhor_tentativa == 0:
		return segunda_melhor_tentativa
	else:
		return melhor_tentativa


#utiliza o metodo de chi-quadrado, para medir a semelhança entre as distribuições
def contar_frequencia(sequence):
	todos_chi_quad = [0] * 26

	for i in range(26):

		soma_chi_quadrado = 0.0
		sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26
		# contando a frequencia de cada letra 
		for l in sequence_offset:
			v[ord(l) - ord('a')] += 1
		# dividindo o array pelo comprimento da sequência para obter as porcentagens de frequência
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))

		# comparando com as frequencias declaradas em cima
		for j in range(26):
			soma_chi_quadrado+=((v[j] - float(frequencia_en[j]))**2)/float(frequencia_en[j])
		# adicionando na tabela de chi quadrado
		todos_chi_quad[i] = soma_chi_quadrado

	# retorna a letra da chave, com a menor estatística qui-quadrado (menor diferença entre distribuição de sequência e distribuição em do idioma)
	shift = todos_chi_quad.index(min(todos_chi_quad))
	# retorna a letra
	return chr(shift+97)

def get_key(texto_cifrado, comprimento_chave):
	key = ''
	# Calcula a tabela de frequência de letras para cada letra da chave
	for i in range(comprimento_chave):
		sequence=""
		# quebrando a sequencia em pedaços
		for j in range(0,len(texto_cifrado[i:]), comprimento_chave):
			sequence+=texto_cifrado[i+j]
		key+=contar_frequencia(sequence)
	return key

from pathlib import Path
def main():
	#lendo dados arquivo texto
	texto_cifrado_bruto = Path('desafio1.txt').read_text()
	print("texto bruto:\n", texto_cifrado_bruto,"\n")

	# Mnatendo somente char que sejam numeros ou letras  
	texto_cifrado = ''
	for x in texto_cifrado_bruto:
		if x.isalpha():
			texto_cifrado += x.lower()
	print("texto tratado:\n", texto_cifrado,"\n")

	# Inferindo o tamanho da chave
	comprimento_chave=get_comprimento_chave(texto_cifrado)
	print("Comprimento provavel da chave {}".format(comprimento_chave))

	# Inferindo a chave em si
	key = get_key(texto_cifrado, comprimento_chave)
	print("chave: {}".format(key))

main()