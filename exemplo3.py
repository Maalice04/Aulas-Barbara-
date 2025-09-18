#mensagem de boas vindas 
print("Bem-vindo ao Caixa Eletrônico!") 

#saldo disponivel em conta do usuario
saldo = 1000

#inicio do loop q vai parar quando o usuário digitar um valor válido para saque  
while True: #LOOP
    #solicita ao usuário o valor do saque (como string) 
    valor_str= input("Digite o valor que deseja sacar(em reais): ") 

#(isdigit():) usado para identificar digitos 
    if valor_str.isdigit(): #verifica se p string contém apenas números 
        valor= int(valor_str) #converta a string para um número inteiro 
    else: 
        #caso o valor digitado não seja um número válido, exibe uma mensagem de erro e reinicia o loop
        print("entrada inválida. digite apenas números inteiros. ")
        continue

#verifica se o valor e maior do que o saldo disponível 
    if valor > saldo: 
        print("Saldo insuficiente! tente um valor menor ou igual a R$", saldo)
#verifica se o valor do saque e menor que o mínimo perimitido(R$2) 
    elif valor < 2: 
        print("Valor mínimo para saque é R$ 2.")
    else:
        #se o valor for válido, sai do loop 
        break
#lista de valores disponiveis pra saque 
notas= [100, 50, 20, 10, 5, 2 ]

#exibe mensagem informando o valor do saque 
print(f"\n Contando notas para R$ {valor}: ") 
#para cada tipo de nota, calcula quantas podem ser usadas 
for nota in notas: 
    quantidade = valor // notas #divide o valor restante pelo valor da nota, pegando a parte inteira 
    valor = valor % nota   #atualiza o valor restante após retirar as notas dessa denominação 
    if quantidade > 0: 
        #exibe apenas as notas que estão sendo usadas(maior que 0) 
        print(f"{quantidade} nota(s) de R$ {nota}") 
    
#mensagem final, indicando sucesso 
print("\n Retire seu dinheiro. Obrigado por usar o nosso caixa eletrônico!") 