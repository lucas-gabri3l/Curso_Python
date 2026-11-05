pessoa = {
    "nome":"Júlio",
    "idade":25,
    "cidade":"São Paulo",
    "profissoes":['Programador','Designer','Pintor']
}
# pessoa["idade"] = 26
# print(pessoa["idade"])

# del pessoa["cidade"]
# print(pessoa["profissoes"][1])

# valores = list(pessoa.values())
# print(valores[2])

# print(pessoa.get('telefone', 'Não Existe'))

# itemremovido = pessoa.pop('profissoes')
# print(f"item Removido: {itemremovido}")
# print(pessoa)

produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 12
}
print(f"Ainda restam {produto['estoque']} unidades do produto {produto['nome']}")