from calculadora_funcoes import Calculadora

if __name__ == "__main__":
    calc = Calculadora()

    while True:
        print("\n Operações disponíveis: somar, subtrair, multiplicar e dividir.")
        operacao = input("Escolha a operação ou digite 'sair' para encerrar: ").strip().lower()

        if operacao == 'sair':
            print("Calculadora foi encerrada;")
            break

        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if operacao == 'somar':
            resultado = calc.somar(x, y)
        elif operacao == 'subtrair':
            resultado = calc.subtrair(x, y)
        elif operacao == 'multiplicar':
            resultado = calc.multiplicar(x, y)
        elif operacao == 'dividir':
            resultado = calc.dividir(x, y)
        else:
            print("A operação digitada está inválida.")
            continue

        print(f"Resultado é: {resultado}")
