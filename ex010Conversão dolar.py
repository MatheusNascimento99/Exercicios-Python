"dolar = 3,27"

valor = float(input('Digite o valor em reais: R$ '))

conv = (valor / 3.27)

print('Com {:.2f} reais, é possível comprar {:.2f} dolares.'.format(valor, conv))