#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
arbol= []
numeros= input().split()
for numero in numeros:
  if arbol==[]:
    arbol = [numero, [], [], []]
  elif arbol[0]== numero:
    arbol[2].append(numero)
  elif numero < arbol[0]:
    nuevo_nodo = [numero, [], [], []]
    arbol[1].append(nuevo_nodo)
  elif numero > arbol[0]:
    nuevo_nodo = [numero, [], [], []]
    arbol[3].append(nuevo_nodo)

print(arbol)
