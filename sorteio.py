import random

if __name__ == '__main__':
    
    num = 0
    
    sorteado = random.randrange(1, 100)

    print(sorteado)
    while num != sorteado:
        num = int(input(f"Adivinhe o número:"))

        if num == sorteado:
            print("Parabéns! Você acertou!")   
        elif sorteado > num:
            print("Quase lá, o número é maior")
        elif sorteado < num:
            print("Quase lá, o número é menor")       