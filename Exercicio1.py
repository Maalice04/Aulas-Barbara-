#FOR PARA VERIFICAR E EXIBIR NUMEROS DE 1 A 100 
# AO FINAL, MOSTRAR QUANTOS NUMEROS PRIMOS FORAM ENCONTRADOS 

#LISTA PARA ARMAZENAR 
primos =[] 
#laço de 1 a 100
for num in range (1, 101): 
    if num > 1:    # 0 e 1 não são primos 
        e_primo = True 
        for i in range (2, int(num ** 0.5) +2): 
            if num % i == 0:
                e_primo = False 
                break
            if e_primo: 
               primos.append(num) 

#EXIBIR NÚMEROS PRIMOS 
print("Números primos entre 1 e 100:") 
for p in primos: 
    print(p, end=' ') 

#MOSTRAR QUANTIDADES DE NÚMEROS PRIMOS 
print(f"\n\nQuantidade de números primos encontrados: {len(primos)}") 
