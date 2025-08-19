#Recebendo Dados
usuario = input('Coloque seu nome e sobrenome: ')
celular = int(input('Coloque o número do celular: '))
altura1 = float(input('Coloque sua altura(em metros): '))
altura = altura1.replace(",",".") #substitui a vírgula por ponto
peso1 = float(input('Coloque seu peso(em kg): '))
peso = peso1.replace(",",".") #substitui a vírgula por ponto

#Calculando
imc = peso /(altura*altura)
ingestao_agua = float(0.035*peso)

print('\n')

#Resultados
print(f'Paciente: {usuario}')
print(f'Número: {celular}')
print(f'Peso: {peso} kg')
print(f'Altura: {altura}m')
if imc < 18.5:
    print(f'Seu IMC é:{imc:.2f} - Muito Magro')
elif imc >= 18.5 and imc <= 24.9:
     print(f'Seu IMC é:{imc:.2f} - Normal')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu IMC é:{imc:.2f} - Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print(f'Seu IMC é:{imc:.2f} - Obeso Grau I')
elif imc >= 35 and imc <= 39.9:
    print(f'Seu IMC é:{imc:.2f} - Obeso Grau II')
else:
    print(f'Seu IMC é:{imc:.2f} - Obeso Grau III ou Mórbido')
print(f'Quantidade de água recomendada: {ingestao_agua:.2f} Listros Diários')
