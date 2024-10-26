import random

print('Seja bem Vindo ao jogo!')

valor_gerado = random.randint(1,100)

def jogar():
    
    acertou = False
    
    numero_de_jogadas = 0
    
    while acertou == False:
        try:
        
            chute_usuario = int(input('Digite um numero inteiro entre 1 e 100:  '))
            
            numero_de_jogadas += 1
            
            if chute_usuario < 1 or chute_usuario > 100:
                print('Digite um número entre 0 e 100.')

            elif chute_usuario > valor_gerado:
                print('Chutou alto! Tente novamente.')    
            
            elif chute_usuario < valor_gerado:
                print('Chutou baixo! Tente novamente.')
                
            elif chute_usuario == valor_gerado:
                
                acertou = True
            
                print(f'Parabéns! Você acertou após {numero_de_jogadas} tentativas.')
                
                continuar = input('Deseja continuar? (s / n) ')
                    
                
                if continuar == 's':
                    return jogar()
                    
                elif continuar == 'n':
                    break
        except:
            print('Digite apenas números!')

jogar()