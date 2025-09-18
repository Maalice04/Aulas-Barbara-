def jogo_do_sapo (): 
    pedra_atual = 1 
    print("Bem vindo ao jogo do sapo!\n") 

    while pedra_atual <4:
        print(f"O sapo está na {pedra_atual} .") 

        try: 
            proxima_pedra= int(input("Digite o número da proxima pedra onde o sapo deve pular:"))
        except ValueError: 
            print("Entrada inválida!O sapo caiu na água. Fim de jogo.")
            return  #para retornar ao inicio novamente 
        
        #verificar entrada válida (entre 1 e 9) 
        if proxima_pedra < 1 or proxima_pedra > 9:
            print("Entrada inválida! O sapo caiu na água. Fim de jogo") 
            return
        #verificar se o pulo e correto(apenas para a próxima pedra imediata) 
        if proxima_pedra == pedra_atual + 1: 
            print("Pulo correto!\n") 
            pedra_atual = proxima_pedra
        else: 
            print("Pulo errado! O sapo caiu na água. Fim de jogo") 
            return
    
    print("Parabéns!O sapo atravesssou o rio com sucesso!") 
     
#executar o jogo
jogo_do_sapo() 



