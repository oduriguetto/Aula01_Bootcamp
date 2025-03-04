# O programa deve começar solicitando ao usuário que insira seu nome.
CONTANTE_BONUS = 1000

nome_usuario = input("Digite seu nome: ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.

salario_usuario = float(input("Informe seu salário: "))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.

bonus_usuario = float(input("Digite o percentual do seu bônus: "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

valor_do_bonus = CONTANTE_BONUS + salario_usuario * bonus_usuario

# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

print(f'O usuario {nome_usuario} possui o bonus de {valor_do_bonus}')

# Salve esse script python como kpi.py
# Faça uma documentação simples de como executar esse programa, utilize o README
# Salve no Git e no Github
