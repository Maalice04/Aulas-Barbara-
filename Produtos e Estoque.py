#cadastro de produtos e estoque 
print("Seja bem-vindo. Cadastre o seu produto e organize o seu estoque aqui!") 

total=0 
soma=0 
nome_produto= ""
estoque_quant= -1

while True:
    #identificação do produto no estoque 
    produto= input("Digite o nome do produto que voçê procura: ") 
#quantidade do produto em estoque 
    estoque_str= input("Digite a quantidade do produto em estoque: ") 

    if estoque_str.isdigit(): #isdigit() para aceitar apenas numeros 
        estoque= int(estoque_str) #apenas numeros inteiros válidos 

    else: 
        print("Quantidade invalida. Tente novamente usando apenas números.") 
        continue
    #atualiza o nome e quantidade 
    total +=1 
    soma += estoque 

    if estoque > estoque_quant: 
        estoque_quant = estoque
        nome_produto= produto 

        continuar= input("Deseja continuar organizando o estoque? (S/N):").strip().upper()

        if continuar == 'S': #se for S, o loop termina 
            break

        print("\nResultado Final!") 
        print(f"Total de produtos cadastrados: {total}")
        print(f"Media de estoque: {soma/total:.1f} por produtos")
        print(f"O {produto} com maior quantidade {nome_produto} ({estoque_quant})")
    #SALVAR NO GITHUB