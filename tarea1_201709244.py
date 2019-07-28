def search(key,lista):
	index = 0
	for valor in lista:
		if valor == key:
			return index
		index += 1
	return -1
data = {"default":[]} 
rList = data["default"]
mensaje = "Ingrese el numero de la accion que desea realizar"
print("Tarea 1 EDD.")
print(mensaje)
print("0.Crear nueva lista")
print("1.Seleccionar lista")
print("2.Insertar")
print("3.Modificar")
print("4.Listar")
print("5.Eliminar")
print("6.Salir")
seleccion = 0
while seleccion!=6:
	input = raw_input()
	try:
  		seleccion = int(input)
  		if(seleccion == 0):
  			print("Ingrese el nombre que sea darle a la lista:")
  			input = raw_input()
  			data[input]=[]
  			print("Lista "+input+" Guardada con exito.")
  			print(mensaje)
  		elif (seleccion == 1):
  			print("ingrese el nombre de la lista que desee:")
  			for x, y in data.items():
  				print(x)
  			l = raw_input()
  			rList = data[l]
  			print(mensaje)
  		elif (seleccion == 2):
  			print("Ingrese el valor a insertar: ")
  			v = raw_input()
  			rList.append(v)
  			print(mensaje)
  		elif (seleccion == 3):
  			print("Ingrese el valor de la lista que desee modificar: ")
  			print(rList)
  			target = raw_input()
  			print("Ingrese el nuevo valor:")
  			nv = raw_input()
  			i = search(target,rList)
  			if(i == -1):
  				print("Elemento no encontrado")
  			else:
  				rList.pop(i)
  				rList.insert(i,nv)
  			print(mensaje)
  		elif (seleccion==4):
  			print(rList)
  			print(mensaje)
  		elif (seleccion==5):
  			print("Ingrese el valor a eliminar: ")
  			target = raw_input()
  			rList.remove(target)
  			print(mensaje)
	except:
  		print("Ocurrio un error. Vuelva a intentar.")
print("Ejecucion terminada con exito.")
