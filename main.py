import numpy as np
import pandas as pd
import json
import datetime

class Cuenta:
  def __init__(self,nombre, numero, numeros_contacto,saldo):
    self.nombre = nombre
    self.numero = numero
    self.numeros_contacto = numeros_contacto
    self.saldo = saldo

  def miNro(self):
    return self.numero
    
  def toStr(self):
    result = ""
    result += str(self.nombre)
    result += "|" + str(self.numero)
    result += "|" + str(self.numeros_contacto)
    result += "|" + str(self.saldo)
    return result

class Operacion:
  def __init__(self, origen, destino, valor, fecha):
    self.origen = origen
    self.destino = destino
    self.valor = valor
    self.fecha = fecha

  def transaccion(self):
    return str(self.origen) + " a " + str(self.destino) + " " + str(self.valor) + " " + str(self.fecha)

  def toStr(self):
    result = ""
    result += str(self.origen)
    result += "|" + str(self.destino)
    result += "|" + str(self.valor)
    result += "|" + str(self.fecha)
    return result

def findCuenta_by_numero(numero):
  result = Cuenta("None",-1,[0],0)
  with open('cuentas.txt', 'r') as f:
    for line in f:
      cuenta = line.split("|")
      if str(cuenta[1]) == str(numero):
        result = Cuenta(cuenta[0], cuenta[1], cuenta[2], cuenta[3])

  return result
  

def init_cuentas():
  BD = []
  usuario1 = Cuenta("Juan", 12345678, [98764321, 98764322],0)
  usuario2 = Cuenta("Maria", 98764321, [12345678, 98764322],100)
  usuario3 = Cuenta("Pedro", 98764322, [12345678, 98764321],50)

  BD.append(usuario1)
  BD.append(usuario2)
  BD.append(usuario3)

  BD = np.array(BD)

  with open('cuentas.txt', 'w') as f:
    for i in range(len(BD)):
      f.write(BD[i].toStr()+"\n")

def realizar_transaccion(origen, destino, valor):
  x = datetime.datetime.now()
  fecha = x.strftime("%d/%m/%Y %H:%M:%S")
  operacion = Operacion(origen, destino, valor, fecha)
  
  with open('transacciones.txt', 'w+') as f:
    f.write(operacion.toStr()+"\n")
      
  print(operacion.transaccion())

def historial_transacciones(origen):
  with open('transacciones.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
      arr = str(line).split("|")
      if str(arr[0]) == str(origen):
        print("Origen: " + str(arr[0]) + " Destino: " + str(arr[1]) + " Valor: " + str(arr[2]) + " Fecha: " + str(arr[3]))

init_cuentas()
realizar_transaccion(12345678, 98764321, 500)

historial_transacciones(12345678)

temp = findCuenta_by_numero(12345678)

print(temp.toStr())