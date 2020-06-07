from sys import argv
import os


lista_com_extensao = []

def remove_arquivos():
       
    for arquivo in os.listdir(argv[1]): # Corre em todos os arquivos do diretorio
        extensao_arquivo = os.path.splitext(arquivo)[1] # Pega a extensão do arquivo

        if extensao_arquivo in lista_com_extensao: # Caso a extensão seja igual a especificada no argumento
            os.remove(argv[1] + '/' + arquivo) # Exclui o arquivo


#------------------------------------------------------------------------------------

def mensagens(lista):
    """
    Função basica de feedback ao usuario.
    """
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
    
    for nome_arquivo in os.listdir(argv[1]): # Corre em todos os arquivos do diretorio
        extensao = os.path.splitext(nome_arquivo)[1] # Pega a extensão do arquivo

        if extensao == argv[2]: # Caso a extensão seja igual a especificada no argumento
            lista_com_extensao.append(extensao) # Adiciona na lista

    mensagens(lista_com_extensao)

main()