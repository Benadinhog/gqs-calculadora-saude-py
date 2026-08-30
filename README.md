# Sistema de Saúde e Bem-Estar

## Descrição do Projeto

O **Sistema de Saúde e Bem-Estar** é um programa desenvolvido em Python para realizar alguns cálculos básicos relacionados à saúde.

O sistema possui um menu interativo com três funcionalidades principais:

1. **Cálculo do IMC** — calcula o Índice de Massa Corporal com base no peso e na altura e informa sua classificação.
2. **Recomendação de água** — estima a quantidade diária de água recomendada considerando 35 ml por quilograma de peso.
3. **Frequência cardíaca máxima** — calcula uma estimativa da frequência cardíaca máxima utilizando a fórmula `220 - idade`.

Também existe uma opção para encerrar o programa.

---

## Relatório de Bugs Encontrados

Durante a análise do código original, foram identificados **7 bugs**, envolvendo erros de lógica matemática, tipos de dados e fluxo de execução.

| Local do Bug | Comportamento Incorreto Observado | Solução Aplicada |
|---|---|---|
| `calcular_imc()` | O cálculo utilizava `altura * 2` em vez de elevar a altura ao quadrado. | Alterado para `peso / (altura ** 2)`. |
| `classificar_imc()` | As condições utilizavam comparações estritas (`>` e `<`), deixando valores como 18.5, 25.0 e 30.0 sem classificação. | As faixas foram reorganizadas usando limites adequados, garantindo que todos os valores sejam classificados. |
| `calcular_agua_diaria()` | A fórmula utilizava `peso / 35`, produzindo um resultado incorreto. | Alterado para `peso * 35 / 1000`, considerando 35 ml por kg e convertendo o resultado para litros. |
| `calcular_frequencia_cardiaca_maxima()` | A idade era somada a 220 (`220 + idade`). | Alterado para `220 - idade`. |
| `menu()` | `input()` retorna uma `string`, enquanto as opções eram posteriormente comparadas com números inteiros. | O valor recebido foi convertido para inteiro utilizando `int(input(...))`. |
| `main()` | As comparações `opcao == 1`, `opcao == 2`, etc. não funcionavam corretamente porque `opcao` era uma string. | A conversão da opção para `int` no `menu()` resolveu o problema de comparação de tipos. |
| `main()` — opção 4 | Ao selecionar a opção 4, o programa imprimia a mensagem de encerramento, mas continuava no `while True`. | Adicionado `break` após as mensagens de encerramento para finalizar o loop. |

### Exemplos dos problemas corrigidos

**Cálculo do IMC:**

Antes:
```python
imc = peso / (altura * 2)
```

Depois:
```python
imc = peso / (altura ** 2)
```

**Cálculo da água:**

Antes:
```python
litros = peso / 35
```

Depois:
```python
litros = (peso * 35) / 1000
```

**Frequência cardíaca máxima:**

Antes:
```python
fc_max = 220 + idade
```

Depois:
```python
fc_max = 220 - idade
```

**Opção do menu:**

Antes:
```python
opcao = input("Escolha uma opção (1-4): ")
```

Depois:
```python
opcao = int(input("Escolha uma opção (1-4): "))
```

**Encerramento do programa:**

Foi adicionado:
```python
break
```

para interromper o `while True` quando a opção 4 for selecionada.

---

## Como Executar

### Pré-requisitos

É necessário ter o **Python 3** instalado no computador.

Para verificar se o Python está instalado, abra o terminal ou prompt de comando e execute:

```bash
python --version
```

ou, em alguns sistemas:

```bash
python3 --version
```

### Passo 1 — Salvar os arquivos

Certifique-se de que o arquivo do programa esteja salvo com o nome:

```text
calculadora_saude.py
```

E que o arquivo `README.md` esteja no mesmo diretório.

Estrutura esperada:

```text
projeto/
├── calculadora_saude.py
└── README.md
```

### Passo 2 — Abrir o terminal na pasta do projeto

Navegue até a pasta onde o arquivo `calculadora_saude.py` está salvo.

### Passo 3 — Executar o programa

No Windows:

```bash
python calculadora_saude.py
```

Caso o comando `python` não funcione, tente:

```bash
py calculadora_saude.py
```

No Linux ou macOS:

```bash
python3 calculadora_saude.py
```

### Passo 4 — Utilizar o menu

Após executar o programa, será apresentado um menu semelhante a:

```text
==============================
  SISTEMA DE SAÚDE E BEM-ESTAR
==============================
1. Calcular IMC
2. Calcular Recomendação de Água
3. Calcular Frequência Cardíaca Máxima
4. Sair
Escolha uma opção (1-4):
```

Digite o número correspondente à funcionalidade desejada.

Para encerrar o sistema, selecione:

```text
4
```

O programa exibirá a mensagem de encerramento e finalizará sua execução.

---

## Testes de Exemplo

### IMC

Entrada:

```text
Peso: 70 kg
Altura: 1.75 m
```

Resultado esperado:

```text
Seu IMC é: 22.86
Classificação: Peso normal
```

### Recomendação de água

Entrada:

```text
Peso: 70 kg
```

Resultado esperado:

```text
Sua meta diária de água é: 2.45 Litros
```

### Frequência cardíaca máxima

Entrada:

```text
Idade: 30
```

Resultado esperado:

```text
Sua Frequência Cardíaca Máxima estimada é: 190 bpm
```

---

## Observação

Os cálculos apresentados são **estimativas** e não substituem avaliação ou orientação de profissionais de saúde.
