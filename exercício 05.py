#exercício 05: conversor de temperatura celsis/fahrenheit
temp=float(input("INFORME A TEMPERATURA: \n"))
converter=input("informe C para Celcius ou F para Fahrenheit: \n")

if converter == "C":
  converter = "CELSIUS"
  tempc = (temp - 32) * (5 / 9)
  print(f"temperatura em Fahrenheit é de {temp}, convertida para Celsius é de {tempc}")
elif converter == "F":
  converter = "FAHRENHEIT"
  tempf = (temp * (9 / 5)) + 32
  print(f"temperatura em Celsius é de {temp}, convertida para Fahrenheit é de {tempf}")