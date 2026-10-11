opcao = int(input("Escolha uma opção (1 a 3): "))

match opcao:
    case 1:
        print("Você escolheu a opção 1!")
    case 2:
        print("Você escolheu a opção 2!")
    case 3:
        print("Você escolheu a opção 3!")
    case _:
        print(f"Você escolheu o número {opcao} ele não estava nas opções!")

nota = float(input("Digite uma nota: "))
match nota:
    case 10 | 9:
        print("Excelente!")
    case 8 | 7:
        print("Muito bom!")
    case 6 | 5:
        print("Da pra melhorar...")
    case 4 | 3 | 2 | 1:
        print("Reprovado")
    case _:
        print("Nota inválida")


