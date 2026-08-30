def calcular_imc(peso, altura):
# Correção: altura deve ser elevada ao quadrado
imc = peso / (altura ** 2)
return imc

def classificar_imc(imc):
# Correção: faixas ajustadas para não deixar valores de fora
if imc < 18.5:
return "Abaixo do peso"
elif imc < 25.0:
return "Peso normal"
elif imc < 30.0:
return "Sobrepeso"
else:
return "Obesidade"

def calcular_agua_diaria(peso):
# Correção: recomendação de 35 ml por kg
# Divide por 1000 para converter ml em litros
litros = (peso * 35) / 1000
return litros

def calcular_frequencia_cardiaca_maxima(idade):
# Correção: FC máxima estimada = 220 - idade
fc_max = 220 - idade
return fc_max

def menu():
print("\n" + "=" * 30)
print(" SISTEMA DE SAÚDE E BEM-ESTAR ")
print("=" * 30)
print("1. Calcular IMC")
print("2. Calcular Recomendação de Água")
print("3. Calcular Frequência Cardíaca Máxima")
print("4. Sair")

# Correção: input convertido para inteiro
opcao = int(input("Escolha uma opção (1-4): "))
return opcao

def main():
while True:
opcao = menu()

    if opcao == 1:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        imc = calcular_imc(peso, altura)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificar_imc(imc)}")

    elif opcao == 2:
        peso = float(input("Digite seu peso (kg): "))

        qtd_agua = calcular_agua_diaria(peso)

        print(f"Sua meta diária de água é: {qtd_agua:.2f} Litros")

    elif opcao == 3:
        idade = int(input("Digite sua idade: "))

        fc = calcular_frequencia_cardiaca_maxima(idade)

        print(f"Sua Frequência Cardíaca Máxima estimada é: {fc} bpm")

    elif opcao == 4:
        print("Encerrando o sistema...")
        print("Obrigado por usar nosso sistema!")

        # Correção: encerra o while
        break

    else:
        print("Opção inválida! Tente novamente.")

if name == "main":
main()
