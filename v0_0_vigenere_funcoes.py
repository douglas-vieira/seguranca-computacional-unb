from unidecode import unidecode
from pathlib import Path

#FUNÇÃO QUE TRATA A MENSAGEM. RETIRANDO ACENTOS
def tratar_mensagem(mensagem_bruta):
    mensagem_tratada = unidecode(mensagem_bruta).upper() #transforma todos os char com acentos em char sem acentos.
    return(mensagem_tratada)

#FUNÇÃO QUE PEGA A CHAVE E GERA A CHAVE CÍCLICA, IGUALANDO AO COMPRIMENTO DA MENSAGEM
def gerar_chave_ciclica(string, chave):
    key = list(chave)
    if len(string) == len(chave):
        return(chave)
    else:
        tamanho_loop = ((len(string) // len(chave)) + 1) #define quantas vezes é necessario repetir a chave, até alcançar o comprimento da mensagem
        chave_ciclica_cheia = ''
        for i in range(tamanho_loop):
            chave_ciclica_cheia = (chave_ciclica_cheia + chave) # repete a chave quantas vezes foram necessárias
        chave_ciclica_final = chave_ciclica_cheia[0:len(string)] # remove o excesso de char, para ficar do tamanho da mensagem. Substr
    return(chave_ciclica_final.upper()) #retorna a chave ciclica criada, maiuscula

#FUNÇÃO QUE CIFRA A MENSAGEM
def cifrar(mensagem_para_cifrar, chave, letra_para_indice, indice_para_letra, alfabeto):
    mensagem_cifrada = ''
    i = 0
    number = 0
    for letra in mensagem_para_cifrar: # loop de letra em letra da mensagem
            number = (letra_para_indice[letra] + letra_para_indice[chave[i]]) % len(alfabeto) # busca numero do indice da letra correspondente
            mensagem_cifrada += indice_para_letra[number] # appenda na mensagem cifrada, a letra correspontende ao numero do indice
            i += 1
    return mensagem_cifrada

#FUNÇÃO QUE DE-CIFRA A MENSAGEM
def decifrar(mensagem_para_descifrar, chave, letra_para_indice, indice_para_letra, alfabeto):
    mensagem_decriptada = ""
    i = 0
    for letra in mensagem_para_descifrar:
        number = (letra_para_indice[letra] - letra_para_indice[chave[i]]) % len(alfabeto)
        mensagem_decriptada += indice_para_letra[number]
        i += 1
    return mensagem_decriptada



#MAIN
def main():
    
    mensagem = "No final das contas, não são os anos de sua vida que contam. É a vida em seus anos."
    chave = "chave_poderosa".upper()
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%¨&*()_+=-,.".upper()


    #Gera indices que serão usados como base, na hora de trocar os char. Com essa abordagem de índice, consigo cifrar qualquer char, desde que esteja previsto na variavel alfabeto.
    letra_para_indice = dict(zip(alfabeto, range(len(alfabeto))))
    indice_para_letra = dict(zip(range(len(alfabeto)), alfabeto))

    #trata a mensagem, retirando acentos
    mensagem_tratada = tratar_mensagem(mensagem)
    print("\nmensagem tratada:", mensagem_tratada,"\n") 

    #gera a chave ciclica que será usada, igualando ao tamanho da mensagem
    chave_ciclica = gerar_chave_ciclica(mensagem_tratada,chave)
    print("chave cilcica   :", chave_ciclica,"\n")

    #cifra a mensagem
    mensagem_cifrada = cifrar(mensagem_tratada, chave_ciclica, letra_para_indice, indice_para_letra, alfabeto)
    print("Mensagem Cifrada:", mensagem_cifrada,"\n")

    #de-cifra a mensagem
    mensagem_descifrada = decifrar(mensagem_cifrada, chave_ciclica, letra_para_indice, indice_para_letra, alfabeto)
    print("Mensagem De-Cifrada:", mensagem_descifrada,"\n")