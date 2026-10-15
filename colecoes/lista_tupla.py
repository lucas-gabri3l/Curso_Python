frutas = ['maça', 'banana', 'laranja']

#Append adiciona na lista
frutas.append('melancia')

#Remove remove da lista
frutas.remove('banana')

#Trocar o item do número - maça por uva
frutas[0] = "uva"

#len para contar quantos itens tem dentro da lista
print(len(frutas))

#Adiciona na lista, porém escolhe onde vai adicionar 
frutas.insert(1, 'kiwi')
print(frutas)

#Serve pra remover o item do lugar que você escolhe(index)
fruta_removida = frutas.pop(1)
print (fruta_removida)
print(frutas)

#Organiza em ordem alfabética
frutas.sort()
print(frutas)

#Retorna o Index do valor, onde está a palavra(index.)
print(frutas.index('melancia'))

#Quantas vezes aparece na lista o valor
print(frutas.count('laranja'))

#Como criar cópia de lista, jeito errado
frutas2 = frutas
frutas2.append('Melancia')
frutas2.append('Uva')

print(frutas2)
print(frutas)

#Jeito certo
frutas2 = frutas.copy()
print(frutas2)


#limpa lista
frutas.clear()
print(frutas)


#TUPLASS

#Tupla é Inalterável, usar quando dados não vão mudar
cores =('vermelho', 'verde', 'azul')
cores[1] = "amarelo"
