#  IMPORTAR TODAS AS PEÇAS
from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import divisao
from potencia import potencia
from raizquadrada import raiz_quadrada

def calculadora():
    """O CÉREBRO da calculadora - une todas as peças!"""
    print("\n" + "="*50)
    print(" CALCULADORA CIENTÍFICA MODULAR")
    print("="*50)
    
    while True:
        print("\nEscolha a operação:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (×)")
        print("4 - Divisão (÷)")
        print("5 - Potência (^)")
        print("6 - Raiz Quadrada (√)")
        print("0 - SAIR")
        
        opcao = input("\nDigite sua opção (0-6): ").strip()
        
        if opcao == "0":
            print(" Até logo!")
            break
        
        #  EXECUTA A OPÇÃO ESCOLHIDA (SWITCH CASE PYTHON)
        if opcao == "1":
            a = float(input("Digite o 1º número: "))
            b = float(input("Digite o 2º número: "))
            resultado = somar(a, b)
            print(f" {a} + {b} = {resultado}")
            
        elif opcao == "2":
            a = float(input("Digite o 1º número: "))
            b = float(input("Digite o 2º número: "))
            resultado = subtrair(a, b)
            print(f" {a} - {b} = {resultado}")
            
        elif opcao == "3":
            a = float(input("Digite o 1º número: "))
            b = float(input("Digite o 2º número: "))
            resultado = multiplicar(a, b)
            print(f" {a} × {b} = {resultado}")
            
        elif opcao == "4":
            a = float(input("Digite o 1º número: "))
            b = float(input("Digite o 2º número: "))
            resultado = divisao(a, b)
            print(f" {a} ÷ {b} = {resultado}")
            
        elif opcao == "5":
            a = float(input("Digite a base: "))
            b = float(input("Digite o expoente: "))
            resultado = potencia(a, b)
            print(f" {a}^{b} = {resultado}")
            
        elif opcao == "6":
            a = float(input("Digite o número: "))
            resultado = raiz_quadrada(a)
            print(f" √{a} = {resultado}")
            
        else:
            print(" Opção inválida!")
        
        input("\nPressione ENTER para continuar...")