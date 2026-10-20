# agenda.py - tela da agenda
# Aqui ficam as funções da agenda e as regras de negócio

compromissos = []   # lista onde ficam guardados os compromissos


def adicionar():
    # RN05: a agenda aceita no máximo 10 compromissos
    if len(compromissos) >= 10:
        print("A agenda está cheia! (máximo de 10 compromissos)")
        return

    titulo = input("Título: ").strip()
    data = input("Data (exemplo: 25/10/2026): ").strip()
    hora = input("Hora (exemplo: 14:30): ").strip()

    # RN01: o título é obrigatório
    if titulo == "":
        print("Erro: você precisa digitar um título!")
        return

    # RN02: a data é obrigatória
    if data == "":
        print("Erro: você precisa digitar a data!")
        return

    # RN03: a hora é obrigatória
    if hora == "":
        print("Erro: você precisa digitar a hora!")
        return

    # RN04: não pode ter dois compromissos na mesma data e hora
    for c in compromissos:
        if c["data"] == data and c["hora"] == hora:
            print("Erro: já existe um compromisso nesse horário!")
            return

    compromisso = {"titulo": titulo, "data": data, "hora": hora}
    compromissos.append(compromisso)
    print("Compromisso adicionado!")


def listar():
    if len(compromissos) == 0:
        print("Ainda não tem nenhum compromisso.")
    else:
        numero = 1
        for c in compromissos:
            print(numero, "-", c["data"], "às", c["hora"], "-", c["titulo"])
            numero = numero + 1


def remover():
    if len(compromissos) == 0:
        print("Não tem nenhum compromisso para remover.")
        return

    listar()
    escolha = input("Qual número você quer remover? ")

    if not escolha.isdigit():
        print("Digite só o número!")
        return

    escolha = int(escolha)
    if escolha < 1 or escolha > len(compromissos):
        print("Esse número não existe na lista!")
        return

    # RN06: pedir confirmação antes de remover
    resposta = input("Tem certeza? (s/n): ")
    if resposta == "s":
        compromissos.pop(escolha - 1)
        print("Compromisso removido!")
    else:
        print("Remoção cancelada.")


def tela_agenda():
    while True:
        print()
        print("===== TELA DA AGENDA =====")
        print("1 - Adicionar compromisso")
        print("2 - Ver compromissos")
        print("3 - Remover compromisso")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
