#Programa que converte um relógio do formato 24 horas para 12 horas

a = "AM"
p = "PM"
horas = 1
def converter_horas(horas):
    if horas > 12:
      return horas - 12
    else:
      return horas

def imprimir_horas(hora_convertida, minutos):
    if horas >=24:
      print(f"Não existe a hora {horas}, pois um dia tem apenas 24 horas")
    elif horas < 0:
      print("Parando...")
    elif minutos < 0 or minutos >= 60:
      print(f" Não exite o minuto {minutos} uma hora é composta de 0 a 59 minutos")
    elif horas < 12:
      print(f"A hora é: {hora_convertida}:{minutos} {a}")
    else:
      print(f"A hora é {hora_convertida}:{minutos} {p}")

while horas >= 0:
  horas = int(input("Digite apenas a hora: "))
  minutos = int(input("Digite apenas os minutos: "))

  hora_convertida = converter_horas(horas)
  imprimir_horas(hora_convertida, minutos)