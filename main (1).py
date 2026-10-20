# main.py - tela inicial (menu principal)
# Para rodar o programa: python main.py

import agenda


def mostrar_regras():
    print()
    print("===== REGRAS DE NEGÓCIO =====")
    print("RN01 - O título é obrigatório.")
    print("RN02 - A data é obrigatória.")
    print("RN03 - A hora é obrigatória.")
    print("RN04 - Não pode ter dois compromissos na mesma data e hora.")
    print("RN05 - A agenda aceita no máximo 10 compromissos.")
    print("RN06 - Para remover, o programa pede confirmação.")


def main():
    while True:
        print()
        print("===== MENU PRINCIPAL =====")
        print("1 - Abrir agenda")
        print("2 - Ver regras de negócio")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            agenda.tela_agenda()
        elif opcao == "2":
            mostrar_regras()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


main()
