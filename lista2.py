Feminino = []
Masculino = []
respostaSimTotal = 0
respostaNaoTotal = 0
simFeminino = 0
simMasculino = 0

def gostarDoProduto():
    gostouDoProduto = input("Gostou do produto? [Sim/Nao]: ")
    return gostouDoProduto.upper()

while True:
    sexo = input("Qual é seu sexo?\nM - Masulino\nF - Feminino\nEscolha [M/F]: ")
    if sexo.upper() == "M":
        print("Masculino")
        resposta = gostarDoProduto()

        if resposta == 'SIM':
            respostaSimTotal += 1
        elif resposta == 'NAO':
            respostaNaoTotal += 1

        Masculino.append(resposta)
    elif sexo.upper() == "F":
        print("Feminino")
        resposta = gostarDoProduto()

        if resposta == 'SIM':
            respostaSimTotal += 1
        elif resposta == 'NAO':
            respostaNaoTotal += 1

        Feminino.append(resposta)
    else:
        break

for x in Feminino:
    if x == "SIM":
        simFeminino += 1
porcentagemSimFeminino = simFeminino*100 / len(Feminino)

for x in Masculino:
    if x == "NAO":
        simMasculino += 1
porcentagemSimMasculino = simMasculino*100 / len(Masculino)

print(f'Numeros de entrevistados que disseram sim: {respostaSimTotal}')
print(f'Numeros de entrevistados que disseram nao: {respostaNaoTotal}')
print(f'A porcentagem de entrevistados do sexo feminino que responderam sim: {porcentagemSimFeminino:.2f} %')
print(f'A porcentagem de entrevistados do sexo masculino que responderam nao: {porcentagemSimMasculino:.2f} %')