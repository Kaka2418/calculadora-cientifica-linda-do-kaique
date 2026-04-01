#  IMPORTAR TODAS AS PEÇAS
from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import divisao
from potencia import potencia
from raizquadrada import raiz_quadrada
from cotacao_dolar import cotacao_dolar  # NOVO!

def calculadora():
    """ CÉREBRO da calculadora com DÓLAR!"""
    #  BUSCA COTAÇÃO NA INICIALIZAÇÃO
    print(" Buscando cotação do dólar...")
    cotacao_atual = cotacao_dolar()
    print(f" Dólar hoje: R$ {cotacao_atual:.4f}")
    print("="*60)
    
    while True:
        print("\n CALCULADORA CIENTÍFICA + DÓLAR")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (×)")
        print("4 - Divisão (÷)")
        print("5 - Potência (^)")
        print("6 - Raiz Quadrada (√)")
        print("7 - Dólar → Real (US$ → R$)")      #  NOVO!
        print("8 - Real → Dólar (R$ → US$)")      #  NOVO!
        print("0 - SAIR")
        
        opcao = input("\nDigite sua opção (0-8): ").strip()
        
        #  SWITCH CASE PYTHON (if/elif)
        if opcao == "0":
            print(" Até logo!")
            break
            
        elif opcao == "1":
            a, b = self.get_numeros()
            print(f" {a} + {b} = {somar(a, b)}")
        
        elif opcao == "2":
            a, b = self.get_numeros()
            print(f" {a} - {b} = {subtrair(a, b)}")
            
        elif opcao == "3":
            a, b = self.get_numeros()
            print(f" {a} × {b} = {multiplicar(a, b)}")
            
        elif opcao == "4":
            a, b = self.get_numeros()
            print(f" {a} ÷ {b} = {divisao(a, b)}")
            
        elif opcao == "5":
            a = float(input("Base: "))
            b = float(input("Expoente: "))
            print(f" {a}^{b} = {potencia(a, b)}")
            
        elif opcao == "6":
            a = float(input("Número: "))
            print(f" √{a} = {raiz_quadrada(a)}")
            
        #  NOVAS OPÇÕES DÓLAR!
        elif opcao == "7":  # Dólar → Real
            valor_dolar = float(input("Valor em US$: "))
            resultado = valor_dolar * cotacao_atual
            print(f" US$ {valor_dolar:,.2f} = R$ {resultado:,.2f}")
            print(f"   (cotação: R$ {cotacao_atual:.4f})")
            
        elif opcao == "8":  # Real → Dólar
            valor_real = float(input("Valor em R$: "))
            resultado = valor_real / cotacao_atual
            print(f" R$ {valor_real:,.2f} = US$ {resultado:,.2f}")
            print(f"   (cotação: R$ {cotacao_atual:.4f})")
            
        else:
            print(" Opção inválida!")
        
        input("\nPressione ENTER para continuar...")
    
    def get_numeros(self):
        """Auxiliar para pegar 2 números"""
        a = float(input("1º número: "))
        b = float(input("2º número: "))
        return a, b