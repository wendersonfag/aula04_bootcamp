def cadastra_bonus(nome: str,salario: float,bonus: float) -> dict:

    CONSTANTE_BONUS = 1000

    usuario_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False
    # 1) Solicita ao usuário que digite seu nome

    while usuario_valido is not True:
        nome_usuario: str = nome

        if any(char.isdigit() for char in nome_usuario):
            print("O nome não deve conter números.")
        elif len(nome_usuario) == 0:
            print("Você não digitou nada")
            
        elif nome_usuario.isspace():
            print("Você digitou só espaço")

        else:
            usuario_valido =True
        
    # 2) Solicita ao usuário que digite o valor do seu salário
    # Converte a entrada para um número de ponto flutuante

    while salario_valido is not True:
        try:
            salario: float = salario

            salario_valido = True
        except ValueError:
            print("digite um valor de salário válido: ")
    # 3) Solicita ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante

    while bonus_valido is not True:
        try:
            bonus: float = bonus
            bonus_valido = True
        except ValueError:
            print("digite um valor de bônus válido: ")
    # 4) Calcule o valor do bônus final
    resultado_bonus = CONSTANTE_BONUS + salario * bonus
    # 5) Imprima cálculo do KPI para o usuário
    #print(resultado_bonus)
    # 6) I'mprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
    return {"nome": nome_usuario, "salario": salario, "bonus": bonus, "resultado_bonus": resultado_bonus}
    # Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

cadastro: list = []
check: bool = True

while check == True:
    
    nome_cadastro: str = input("Digite seu nome: ")
    salario_cadastro: float = float(input("Digite seu Salarioo: "))
    bonus_cadastro: float = float(input("Digite o seu bônus: "))

    cadastro.append(cadastra_bonus(nome_cadastro,salario_cadastro,bonus_cadastro))

    continuar = input("Deseja casdatra mas bonus? sim - continuar | não - cancelar ")
    for i in cadastro:
        print(i)
    
    if continuar == "não":
        check == False
        break
    