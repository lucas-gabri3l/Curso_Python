meiodetransporte = str(input("Escolha um meio de transporte(Avião, Bicicleta, Carro, Helicóptero): "))

match meiodetransporte:
    case "Avião" | "Helicóptero":
        print("Transporte Aéreo")
    case "Bicicleta":
        print("Transporte Sustentável")
    case "Carro":
        print("Transporte Terrestre")
    case _:
        print("Transporte não cadastrado!")