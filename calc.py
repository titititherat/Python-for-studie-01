#calculadora para aprendizado de python
#tititiorato

print("┈╭━━╮╭━━╮┈┈┈┈┈ ")
print("┈┃╭╮┗┻━━┻━╮┈┈┈  Pratica de python 1.0 - Calculadora")
print("┈┃╰┓╭━╮╭━╮┃┈┈┈         Discord tititi#6447")
print("┈╰━┓┃▇┃┃▇┃┃┈┈┈             ʕ•̫͡•ʔ ")
print("┈┈┈┃╱▔▔▔▔▔▔▔▇┈    Respeita o Rato")
print("┈┈┈┃▏┏┳┳┳┳┳━┛┈             Caralho")
print("┈┈┈┃╲╰┻┻┻┻┻┓┈┈")
print(" ")

#inicio do programa
operation_list = {"soma", "subtração", "divisão", "multiplicação", "sair"}
repeat = 24 #quantidade de vezes que irá repetir o ■
#repetição e "design"
while True:
	operation = str(input('escolha qual operação deseja fazer(soma,subtração,divisão,multiplicação ou digite "sair" para sair):'))
	if operation == "sair":
		break
	if operation not in operation_list:
	    print("escolha inválida")
	elif operation in operation_list:
	    print(repeat * "■")
	    print("\t", operation.upper())
	    print(repeat * "■")
#escolhas
	    number1 = int(input("Digite o primeiro número"))
	    number2 = int(input("Digite o segundo número"))
#operações
	    if operation == "soma":
	    	print(number1+number2)
	    elif operation == "subtração":
	    	print(number1-number2)
	    elif operation == "divisão":
	    	print(number1/number2)
	    elif operation == "multiplicação":
	    	print(number1*number2)	
#fim	    	