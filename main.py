import funcoes

while True:
    print("\n Agenda de Contatos")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desamarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    try:
        opcao = int(input("\nQual é a opção desejada? "))

        if opcao == 1:
            funcoes.adicionar_contato()
        elif opcao == 2:
            funcoes.visualizar_lista_contatos()
        elif opcao == 3:
            funcoes.visualizar_lista_contatos()
            escolha = int(input("Qual contato deseja editar? ")) - 1
            funcoes.editar_contato(escolha)
        elif opcao == 4:
            funcoes.visualizar_lista_contatos()
            escolha = int(input("Qual contato deseja editar? ")) - 1
            funcoes.editar_favorito(escolha)
        elif opcao == 5:
            funcoes.visualizar_favoritos()
        elif opcao == 6:
            funcoes.visualizar_lista_contatos()
            escolha = int(input("Qual contato deseja apagar? ")) - 1
            funcoes.apagar_contato(escolha)
        elif opcao == 7:
            print("Fechando agenda!")
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Por favor, digite uma opção válida!")