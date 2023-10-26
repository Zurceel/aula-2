def boasVindas(nome):
    print(f'Seja muito bem-vindo(a) {nome}')

if __name__ == '__main__':
    palavra = "devaria"
    for letra in palavra:
        print(f'A letra é {letra}')


    contador = 0

    while contador <= 3:
        print(f'Lavando carro na posição {contador}')
        contador += 1
    else:
        print('Terminou de lavar os carros')

    pessoas = ["Gabriel", "Gael", "Geovanna"]
    for p in pessoas:
            boasVindas(p)


    for n in range(0, 10, 2):
        print(f'O número é: {n}')