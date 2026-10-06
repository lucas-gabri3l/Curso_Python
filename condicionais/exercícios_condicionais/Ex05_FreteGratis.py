valor_compra = float(input("Qual foi o valor da compra?: "))

cadastrado_programa = str(input("Você está cadastrado no programa de fidelidade? (Sim/Não): "))

if valor_compra >= 100 and cadastrado_programa == "Sim":
    print("Frete grátis aplicado!")
else:
    print("Frete não disponível gratuitamente!")