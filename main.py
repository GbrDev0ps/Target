def pergunta1():
    num = int(input("Digite um numero positivo para analisarmos se existe na sequência de fibonacci:"))
    fibonacci = [0, 1]
    
    while fibonacci [-1] < num:
        fibonacci.append(fibonacci [-1] + fibonacci [-2]) 
    print(fibonacci)

    if num in fibonacci:
        print(f"O numero {num} está presente na sequencia de Fibonacci")
    else:
        print(f"O numero {num} não está presente na sequencia de fibonacci")       
            

def pergunta2():
    palavra = input('Digite uma palavra:')
    quantidade = palavra.count('a') + palavra.count('A')
    
    if quantidade > 0:
        print(f"A letra 'a' está presente e aparece {quantidade} vezes.")
    else:
        print("A letra 'a' não está presente")




def pergunta3():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k +=1
        soma += k
        
   
    print(soma)
    

