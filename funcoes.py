import listas

def nome_contato():
    nome = input("Digite o nome: ")
    return nome

def telefone_contato():
    telefone = int(input("Digite o telefone(Sem espaços, traços ou parênteses): "))
    return telefone

def email_contato():
    email = input("Digite o email: ")
    return email

def favoritar_contato():
    fav = input("Deseja adicionar contato como favorito ☆ ?(S/N) ").upper()
    if fav == "S":
        favorito = True
    else: 
        favorito = False
    return favorito

def adicionar_contato():
    nome, telefone, email, favorito = nome_contato(), telefone_contato(), email_contato(), favoritar_contato()
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    listas.contatos.append(contato)
    print("Contato adicionado com sucesso!")
    return

def visualizar_unico_contato(indice):
    contato = listas.contatos[indice]
    print(f"1.Nome: {contato["nome"]:^15} 2.Telefone: {contato["telefone"]:^15} 3.Email: {contato["email"]:^15} ")
    return

def visualizar_lista_contatos():
    for indice, contato in enumerate(listas.contatos, start=1):
        favorito = "☆" if contato["favorito"] else " "
        print(f"{indice}. {favorito} {contato["nome"]:^15} {contato["telefone"]:^15} {contato["email"]:^15}")
    return

def editar_contato(indice):
    while True:
        visualizar_unico_contato(indice)
        opcao = input("Qual campo deseja editar? (1, 2, 3 ou 0 para sair)").strip()
        if opcao == "0":
            break
        elif opcao == "1":
            novo_nome = nome_contato()
            listas.contatos[indice]["nome"] = novo_nome
            print("Nome atualizado!\n")
        elif opcao == "2":
            novo_telefone = telefone_contato()
            listas.contatos[indice]["telefone"] = novo_telefone
            print("Telefone atualizado!\n")
        elif opcao == "3":
            novo_email = email_contato()
            listas.contatos[indice]["email"] = novo_email
            print("Email atualizado!\n")
        else:
            print("Opção inválida!\n")
    return

def editar_favorito(indice):
    favorito = favoritar_contato()
    listas.contatos[indice]["favorito"] = favorito
    return

def visualizar_favoritos():
    for indice, contato in enumerate(listas.contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. ☆ {contato["nome"]:^15} {contato["telefone"]:^15} {contato["email"]:^15}")
    return

def apagar_contato(indice):
    listas.contatos.pop(indice)
    print("Contato apagado!")
    return