#Gerenciamento de cadastro de clientes e produtos 
#Cadastre varios clientes 
#1-nome do cliente 
#2- quantidade de produtos comprados 
#3-valor total gasto em reais 
#um ou mais produtos 
print("Bem- vindo!") 

def cadastro_cliente(): 
    clientes= []

    while True:
        print("--- Cadastro de cliente ---") 
        nome= input("Nome do cliente: ") 

        num_produtos = int(input("Quantos produtos o cliente comprou? "))
        produtos= [] 

        total_gasto = 0 
        for i in range (num_produtos): 
            print (f"\n Produto {i+1}: ")
            nome_produto= input("Nome do produto: ") 
            preco= float(input("Preço do produto (R$) "))
            produtos.append ({'nome': nome_produto, 'preco': preco})
            total_gasto += preco 

        clientes = {
            'nome': nome, 
            'quantidade_produto': num_produtos, 
            'total_gasto': total_gasto, 
            'produtos': produtos
        }
        clientes.append(clientes) 

        continuar= input("\n Deseja cadastrar outro cliente?") 
        if continuar == 'N': 
            break
    return clientes

def mostrar_clientes(cliente): 
    print("\n-- Lista de clientes cadastrada --") 
    for clientes in cliente:
        print(f"\n Nome: {cliente['nome']}") 
        print(f"\n Quantidade de produtos: {cliente['quantidade_produtos']}") 
        print(f"Total gasto: R$ {cliente['total_gasto']:.2f}") 
        print("Produtos:") 
        for produto in cliente['produtos']:
            print(f" -{produto['nome']}: R$ {produto['preco']:.2f}")

#executar 
clientes= cadastro_cliente
mostrar_clientes(clientes)
