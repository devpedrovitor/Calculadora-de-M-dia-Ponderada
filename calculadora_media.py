def notas_invalidas(nota_1: float,  nota_2: float, nota_3: float):

    err = [] # Acumulador de error

    if nota_1 < 0.0 or nota_1 > 10.0:
        err.append(f"- Primeira nota: {nota_1} (deve ser entre 0 e 10)")
    if nota_2 < 0.0 or nota_2 > 10.0:
        err.append(f"- Segunda nota: {nota_2} (deve ser entre 0 e 10)")
    if nota_3 < 0.0 or nota_3 > 10.0:
        err.append(f"- Terceira nota: {nota_3} (deve ser entre 0 e 10)")

    if err:
        print("Notas inválidas encontradas:")
        for erro in err:
            print(f"  - {erro}")
        return False
    else:
        print("Todas as notas são válidas!")
        print(f"Notas registradas: {nota_1}, {nota_2}, {nota_3}")
        return True

while True:
    try:
        nota_1 = float(input("Digite sua primeira nota: "))
        nota_2 = float(input("Digite sua segunda nota: "))
        nota_3 = float(input("Digite sua terceira nota: "))

        if notas_invalidas(nota_1, nota_2, nota_3):
            break;
        else:
            print("\nTente Novamente")
    except ValueError:
        print("Um dos valores inseridos não é um número.")

media = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / (2 +  3 + 5)
print(f"Sua media final: {media:.1f}")

if media >= 7 :
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
 