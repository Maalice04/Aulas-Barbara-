#cadastro de cidades para pesquiss populacional 
print("Bem-vindo ao nosso site de pesquisas!")

total= 0 
soma= 0 
nome_cidade= "" 
populaçao_estimada = -1

#inicoo do loop 
while True:
    #NOME DA CIDADE 
    cidade= input("\n Digite o nome da sua cidade:") 
#NUMERO DA POULAÇÃO 
    populaçao_str= input("Digite o número da população da cidade:") 
    
    if populaçao_str.isdigit(): #isdigit() PARA ACEITAR APENAS NUMEROS 
        populaçao = int(populaçao_str) #APENAS NUMEROS INTEIROS 
    else: 
        print("População inválida. Digite apenas números inteiros") 
        continue
    #atualiza o nome da cidade e o total da população 
    total +=1 
    soma += populaçao
    
    if populaçao > populaçao_estimada: 
        populaçao_estimada = populaçao #atualiza o numero da população 
        nome_cidade= cidade #atualiza o nome da cidade 

        continuar= input("Deseja continuar a pesquisa? (s/n):").strip().upper()

    if continuar =='N': #se for S, loop termina
        break

#resultado e mensagens finais 
print("\nResultado final") 
print(f"Total de cidades cadastradas: {total}") 
print(f"Média de população: {soma / total:.1f} das cidades") 
print(f"Nome da {cidade} mais populosa {nome_cidade} ({populaçao_estimada})") 

#SALVAR NO GITHUB