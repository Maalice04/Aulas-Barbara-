#Quantos itens deseja colocar na lista de compra 
#A) LISTA COMPLETA DE ITENS 
#B) QUANTOS ITENS A LISTA POSSUI
#C) A LISTA EM ORDEM ALFABETICA 
Lista_compras = []
quantidade = int(input("Digite quantos itens voçê deseja ter na sua lista de compras: "))

for i in range (quantidade):
    item = input(f"Digite o {i + 1}° iten da lista:")
    Lista_compras.append(item) 

#exibindo os itens da lista
#A)EXIIBIR A LISTA COMPLETA DE ITENS 
print("\nLista completa de itens: ") 
for item in Lista_compras: 
    print(f"-{item}") 

#B)MOSTRAR QUANTOS ITENS A LISTA POSSUI 
print(f"\n A lista possui{len(Lista_compras)} item(ns).") 
#F= para armazenar e imprimir informaçoes do banco de dados 

#C)MOSTRAR A LISTA EM ORDEM ALFABETICA 
lista_ordenada = sorted(Lista_compras)

print("\n Lista em ordem alfabética:")
for item in lista_ordenada: 
    print(f"- {item}") 