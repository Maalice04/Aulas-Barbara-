#quantos quilos deseja doar 
# doação aceita de 1kg ou mais 
#não deve aceitar entradas inválidas(letras, simbolos ou números negativos)
#1,2 e 5kg 
#quantos pacotes de cada tipo será usado
#mensagem de agradecimento no final 

#mensagem de boas vindas 
print(" Bem-vindo! Fique a vontade para participar da nossa Caixa de Doaçao de Alimentos!")

doação= [1, 2, 5 ]
#inicio do loop 
while True: 
    quilos_str= ("Digite quantos quilos de alimentos voçê deseja doar (em kg): ")
    
    if quilos_str.isdigit(): #verifica se todos os caracteres da string são digitos 0-9 
        quilo = int(quilos_str) #converte a string para um numero inteiro 
    else: 
        #caso a quantidade de quilos não for digitada em numeros, exibe uma mensagem de erro 
        print("Quantidade inválida. Digite apenas números inteiros.")
        continue
    #verifica se a quantidade de kg está entre as pedidas 
    if quilo > doação: 
        print("Doação não autorizada. Tente uma quantidade entre 1kg, 2kg e/ou 5kg!").strip().upper()
    #verifica se o valor do kg é menos que o minimo desejavel
    elif quilo < 1: 
        print("Quantidade de kg mimina para a doação.") 
    else: 
        #se o kg for válido, sair do loop
        break 
#mensagem indentificando se a doação foi permitida
print(f"\n Contando quantidade de kg {quilo}") 
    
for doação in quilo: 
    quantidade = quilo // doação 
    quilo = quilo % doação
    if quantidade > 0: 
        print(f"{quantidade} de kg {doação}:") 

print("\n Doação realizada. Agradecemos pela sua colaboração!")

#SALVAR NO GITHUB