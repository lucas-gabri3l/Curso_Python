print("ENTRADA EVENTO!")

idademinima = 15

idade = int(input("Qual sua idade?: "))

if idade >= idademinima:
    print("Você pode participar do Evento!")
else:
    diferenca = idademinima - idade
    print(f"Faltam {diferenca} anos para você acessar a festa!")