from sys import argv
import os


lista_com_extensao = []

def remove_arquivos():

    for arquivo in os.listdir(argv[1]):
        extensao_arquivo = os.path.splitext(arquivo)[1]

        if extensao_arquivo in lista_com_extensao:
            os.remove(argv[1] + '/' + arquivo)


#------------------------------------------------------------------------------------

def mensagens(lista):

    tamanho = len(lista)

    resposta = input(f"Existem {tamanho} arquivos repetidos a serem apagados, continuar(y/n):\n >>> ").lower()

    if resposta == "y":
        remove_arquivos()
        print("Arquivos apagados com sucesso!")

    elif resposta == "n":
        print("Entendido, saindo do programa!")

    else:
        print("Opção invalida! Saindo do programa, nenhuma ação foi executada.")

#-------------------------------------------------------------------------------------

def main():
    
    for nome_arquivo in os.listdir(argv[1]):
        extensao = os.path.splitext(nome_arquivo)[1]

        if extensao == argv[2]:
            lista_com_extensao.append(extensao)

    mensagens(lista_com_extensao)

main()