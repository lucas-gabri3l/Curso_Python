pedido = int(input("O que você vai pedir hoje?\n1-Pizza\n2-Sushi\n3-Salada\nPedido: "))

match pedido:
    case 1:
        print("Hoje você pediu Pizza!")
    case 2:
        print("Hoje você pediu Sushi!")
    case 3:
        print("Hoje você pediu Salada!")
    case _:
        print("Opção Inválida.")