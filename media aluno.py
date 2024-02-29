nome = input ("Qual seu nome: ");
nota1 = float(input ("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))

media =(nota1 + nota2)/2

if media >= 6:
    print(nome,"foi Aprovado com media de:",media)
else:
    print (nome, "foi Reprovado com media de:",media)
