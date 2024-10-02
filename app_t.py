'''
Crie um programa que possa:
- Inserir o nome de um usuário em uma lista
- Exibir a lista de nomes
- Ordenar os nomes
- Alterar um nome da lista
- Excluir um nome da lista
- Sair do programa
O programa deverá  exibir um menu, e o usuário irá escolher a opção desejada do menu.
Ao terminar, enviar para o GitHub e poste o link do repositório no Classroom.
'''

print("1. Inserir nome")
print("2. Exibir lista de nomes")
print("3. Ordenar nomes")
print("4. Alterar nome")
print("5. Excluir nome")
print("6. Sair")
print("--------------")

lista_nomes = []

while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome a ser inserido: ")
            lista_nomes.append(nome)
            print(f"{nome} adicionado à lista.")

        elif opcao == "2":
            if lista_nomes:
                print("Lista de nomes:")
                for nome in lista_nomes:
                    print(nome)
            else:
                print("A lista está vazia.")

        elif opcao == "3":
            lista_nomes.sort()
            print("Nomes ordenados.")

        elif opcao == "4":
            nome_antigo = input("Digite o nome a ser alterado: ")
            if nome_antigo in lista_nomes:
                novo_nome = input("Digite o novo nome: ")
                indice = lista_nomes.index(nome_antigo)
                lista_nomes[indice] = novo_nome
                print(f"{nome_antigo} alterado para {novo_nome}.")
            else:
                print(f"{nome_antigo} não encontrado na lista.")

        elif opcao == "5":
            nome_a_excluir = input("Digite o nome a ser excluído: ")
            if nome_a_excluir in lista_nomes:
                lista_nomes.remove(nome_a_excluir)
                print(f"{nome_a_excluir} excluído da lista.")
            else:
                print(f"{nome_a_excluir} não encontrado na lista.")

        elif opcao == "6":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


