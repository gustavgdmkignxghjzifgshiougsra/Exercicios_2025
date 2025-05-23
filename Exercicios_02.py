#Exercicio1
numero1 = int(input("digite o primeiro numero: ")
numero2 = int(input("digite o segundo numero: ")
numero3 = int(input("digite o terceiro numero: ")
numero4 = int(input("digite o quarto numero: ")
numero5 = int(input("digite o quinto numero: ")

soma = numero1 + numero2 + numero3 + numero4 + numero5

print(f" O resultado é: {soma}") 

#Exericio2


#Exercicio3
palavra = input("Digite uma palavra: ")
vogais = ["a","e","i","o","u"]
contador_vogais = 0

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

print(f"A quantidade de vogais na palavra {palavra} e de: {contador_vogais}")

#Exercicio4
numero1 = int(input("digite o primeiro número:"))
numero2 = int(input("digite o segundo número:" ))
numero3 = int(input("digite o terceiro número:"))
numero4 = int(input("digite o quarto número:"))
numero5 = int( input("digite o quinto número:"))
numero6 = int(input("digite o sexto número:"))

numeros = [numero1, numero2, numero3, numero4, numero5, numero6]

for numero in numeros:
    if numero %2==0:
        print(f"Número par:{numero}")
#Exercio5
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 

print(f" A média das notas é: {media}") 

#Exercio6
n = int(input("Digite um número: "))

for n in range(1, n + 1):
 print(f'{n}')


#Exercicio7
palavraDigitada = input('digite uma palavra: ')


palavraReserva = palavraDigitada [::-1]

print (f'O contrário da palavra {palavraDigitada} é: {palavraReserva}')

#Exercicio8
digitenumero = input('Digite um número: ')

numero = int(digitenumero)

resto = numero % 3

if resto == 0:
    print(numero, 'é múltiplo de 3')

else:
    print(numero,'não é multiplo de 3')




#Exercicio9

nome1 = input('digite o primeiro nome: ')
nome2 = input('digite o segundo nome: ')
nome3 = input('digite o terceiro nome: ')


listadenomes = [nome1, nome2, nome3]

listadenomes.sort(reserve=False)

print(f'Os nomes em ordem alfabetica são: {listadenomes}')


