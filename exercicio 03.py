#exercício 03: utilizando a biblioteca datetime informar quanto tempo falta para se aposentar
from datetime import date
dataatual = date.today()
print(dataatual)
ano=dataatual.year

aposentar=int(input("informe o ano em que deseja se a posentar: "))
subtracao=aposentar-ano
subtracao=abs(subtracao)

if aposentar <= ano:
    print(f"voce ja deveria estar aposentado")
else:
    print(f"voce irá se aposentar em {subtração} ano(s) ")