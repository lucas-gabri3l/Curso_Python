frase = str(input("Escreva uma mensagem (Se tiver bomba o sistema alerta!): "))
if "bomba".lower() in frase.lower():
    print("Alerta!!!!")
else:
    print("Mensagem Segura!")