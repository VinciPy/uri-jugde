quantidade_moedas = int(input())
moedas = []
soma = 0
number = -1
cont_salto = 0

def Primo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        return True
    else:
        return False


for x in range(quantidade_moedas):
    valor = int(input())
    moedas.append(valor)


salto = int(input())
moedas = list(reversed(moedas))


for x in moedas:
    number += 1
    cont_salto += 1

    if cont_salto == salto or number == 0:
        soma = soma + moedas[number]
        cont_salto = 0
        
resposta = Primo(soma)

if resposta == True:
    print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    
else:
    print("Bad boy! I’ll hit you.")

    