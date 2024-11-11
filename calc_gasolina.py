import time
import os

distancia_trajeto = None

while distancia_trajeto is None:
    entrada = input('Digite a distância do trajeto. (OBS: SOMENTE NÚMEROS): ')
    if entrada.strip() == '' or entrada.strip() == ' ':
        print('Por favor, digite algo válido.')
    else:
        try:
            distancia_trajeto = float(entrada)
        except ValueError:
            print('Por favor, digite um número válido.')
print(f'Trajeto de {distancia_trajeto} KM')
print('Carregando...')
time.sleep(3)
os.system('cls')

carro_km = None

while carro_km is None:
    entrada_carro = input('Digite quantos KM por litro o carro roda. (OBS: SOMENTE NÚMEROS): ')
    if entrada_carro.strip() == '' or entrada_carro.strip() == ' ':
        print('Por favor, digite algo válido.')
    else:
        try:
            carro_km = float(entrada_carro)
        except ValueError:
            print('Por favor, digite um km válido.')

print(f'Carro com {carro_km} KM/L')
print('Carregando volume necessário de gasolina...')
time.sleep(5)
os.system('cls')

volume_gasolina_necessario = distancia_trajeto / carro_km
print(f'Para um trajeto de {distancia_trajeto}. Vai precisar de {volume_gasolina_necessario:.2f} litros de gasolina')

gasolina = None
while gasolina is None:
    entrada_gasolina = input('Quanto custa a gasolina. (OBS: SOMENTE NÚMEROS): ')
    if entrada_gasolina.strip() == '' or entrada_gasolina.strip() == ' ':
        print('Por favor, digite algo válido.')
    else:
        try:
            gasolina = float(entrada_gasolina)
        except ValueError:
            print('Por favor, digite um valor válido.')

print(f'Gasolina com preço de {gasolina} o litro')
print('Carregando custo...')
time.sleep(5)
os.system('cls')

custo_gasolina = volume_gasolina_necessario * gasolina
print(f'O custo para por a gasolina a {gasolina}. Vai ser de R${custo_gasolina:.2f}')

detalhado = input('Deseja saber os valores detalhados (s/n): ')
os.system('cls')
if detalhado == 's':
    print(f'TRAJETO => {distancia_trajeto}')
    print(f'KM/L CARRO => {carro_km}')
    print(f'GASOLINA NECESSÁRIA => {volume_gasolina_necessario:.2f}')
    print(f'GASOLINA => R${gasolina}')
    print(f'CUSTO TOTAL => R$ {custo_gasolina:.2f}')
else:
    print('Obrigado por usar!')