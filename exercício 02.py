#exercício 2: recebe cpf e retorna sua formatação usando "-" e "."
cpf=input("CPF: ")
print(f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")