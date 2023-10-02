from v0_0_vigenere_funcoes import *

#MAIN
def main():
    mensagem = "PV 1MHPZ#HR7BCQUTVW(,2DSA7SO@VSEEH47#HV- UC&V4H_,5XIAQ7NVHMU$,,O#ZZRS GT #IO8-DR67R"
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

    #de-cifra a mensagem
    mensagem_descifrada = decifrar(mensagem_tratada, chave_ciclica, letra_para_indice, indice_para_letra, alfabeto)
    print("Mensagem De-Cifrada:", mensagem_descifrada,"\n")

main()