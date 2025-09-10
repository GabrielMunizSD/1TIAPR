ano = int(input("Digite um ano: "))

if ano % 4 != 0:
    print(f"{ano} não é bissexto")
elif (ano % 4 == 0) and (ano % 100 !=0 ):
    print(f"{ano} é bissexto")
elif ano % 100 == 0 and ano % 400 != 0:
    print(f"{ano} não é bissexto")
elif ano % 400 ==0:
    print (f"{ano} é bissexto")