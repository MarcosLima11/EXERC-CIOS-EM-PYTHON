#exercício 5
nome=input("")
nome= nome.lower()
print("seu nome em letra minuscula:", nome)
nome= nome.upper()
print("seu nome em letra maiuscula:", nome)

nome=nome.split()
nomejunto = "".join(nome)
tamanho=len(nomejunto)
print("seu nome tem %d letras" %(tamanho))

tamanho=len(nome[0])
print("seu primeiro nome tem %d letras" %(tamanho))

tamanho=len(nome[-1])
print("seu ultimo nome tem %d letras" %(tamanho))