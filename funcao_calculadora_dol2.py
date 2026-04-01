# 📥 IMPORTAR TODAS AS PEÇAS
from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import divisao
from potencia import potencia
from raizquadrada import raiz_quadrada
from cotacao_dolar import cotacao_dolar  # 🔥 NOVO!

def calculadora():
    """🧠 CÉREBRO da calculadora com DÓLAR!"""
    # 🔥 BUSCA COTAÇÃO NA INICIALIZAÇÃO
    print("⏳ Buscando cotação do dólar...")
    cotacao_atual = cotacao_dolar()
    print(f"💰 Dólar hoje: R$ {cotacao_atual:.4f}")
    print("="*60)
    
    while True:
        print("\n🧮 CALCULADORA CIENTÍFICA + DÓLAR")
        print("1 - Soma (+)          7 - Dólar → Real")
        print("2 - Subtração (-)     8 - Real → Dólar")
        print("3 - Multiplicação (×)")
        print("4 - Divisão (÷)")
        print("5 - Potência (^)")
        print("6 - Raiz Quadrada (√)")
        print("0 - SAIR")
        
        opcao = input("\nDigite sua opção (0-8): ").strip()
        
        try:
            if opcao == "0":
                print("👋 Até logo!")
                break
                
            elif opcao == "1":
                a = float(input("1º número: "))
                b = float(input("2º número: "))
                resultado = somar(a, b)
                print(f"✅ {a} + {b} = {resultado}")
                
            elif opcao == "2":
                a = float(input("1º número: "))
                b = float(input("2º número: "))
                resultado = subtrair(a, b)
                print(f"✅ {a} - {b} = {resultado}")
                
            elif opcao == "3":
                a = float(input("1º número: "))
                b = float(input("2º número: "))
                resultado = multiplicar(a, b)
                print(f"✅ {a} × {b} = {resultado}")
                
            elif opcao == "4":
                a = float(input("1º número: "))
                b = float(input("2º número: "))
                resultado = divisao(a, b)
                print(f"✅ {a} ÷ {b} = {resultado}")
                
            elif opcao == "5":
                a = float(input("Base: "))
                b = float(input("Expoente: "))
                resultado = potencia(a, b)
                print(f"✅ {a}^{b} = {resultado}")
                
            elif opcao == "6":
                a = float(input("Número: "))
                resultado = raiz_quadrada(a)
                print(f"✅ √{a} = {resultado}")
                
            # 🔥 OPÇÕES DÓLAR!
            elif opcao == "7":  # Dólar → Real
                valor_dolar = float(input("Valor em US$: "))
                resultado = valor_dolar * cotacao_atual
                print(f"✅ US$ {valor_dolar:,.2f} = R$ {resultado:,.2f}")
                print(f"📊 Cotação usada: R$ {cotacao_atual:.4f}")
                
            elif opcao == "8":  # Real → Dólar
                valor_real = float(input("Valor em R$: "))
                resultado = valor_real / cotacao_atual
                print(f"✅ R$ {valor_real:,.2f} = US$ {resultado:,.2f}")
                print(f"📊 Cotação usada: R$ {cotacao_atual:.4f}")
                
            else:
                print("❌ Opção inválida! Escolha 0-8")
                
        except ValueError:
            print("❌ Digite apenas números!")
        except Exception as e:
            print(f"❌ Erro: {e}")
        
        input("\n🔄 Pressione ENTER para continuar...")
