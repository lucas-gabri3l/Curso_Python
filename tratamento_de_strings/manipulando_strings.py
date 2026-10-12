
frase ="eu amo python!"

#Qual o primeiro caractere(começa no 0)
print(frase[1])

#De trás para frente
print(frase[-1])

#Do caractere 2 até o 5
print(frase[2:5])

#Caractere 2 até o final
print(frase[2:])

#vai até o 5 caractere
print(frase[:5])

#Quantos Cacteres tem
frase_tamanho = len(frase)
print(f"a frase {frase} tem {frase_tamanho} caracteres!")

#Quantas letras "o" tem
contagem = frase.count("o")
print(contagem)

#Onde ta o M
print(frase.find("m"))

#Verificar se tem trecho na String
if "python" in frase:
    print("Python está na frase")
else:
    ("Python não está na frase!")

#Deixar toda frase em minúsculo
print(frase.lower())

#Deixar toda frase maiuscula
print(frase.upper())
print(frase)

#Transforamr a variável em upper/lower
frase = frase.upper()
print(frase)

#Deixar a primeira Letra em maiúsculo
print(frase.capitalize())

frase = "          Eu amo Python!"
print(frase)
#remover espaços das laterais
print(frase.strip())
frase = frase.strip()

#Trocar um caractere por outro, o primeiro "o" pelo segundo "X"
print(frase.replace("o", "x"))

#primeira letra de cada palavra em maiusculo
print(frase.title())

