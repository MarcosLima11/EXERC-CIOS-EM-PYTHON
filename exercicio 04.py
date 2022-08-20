#exercicio 04: repetição de login de usuário
login="tapioca"
senha="12345"
login_user=input("Informe o login ou nome de usuário: \n")

while login_user != login:
    login_user=input("!LOGIN OU NOME DE USUÁRIO DESCONHECIDO! \n informe o login ou nome de usuário: \n")
        

if login_user == login:
  senha_user=input("informe a senha: \n")
  while senha_user != senha:
    senha_user=input("senha incorreta! informe a senha: ")
  if senha_user==senha:
    print("bem vindo!")