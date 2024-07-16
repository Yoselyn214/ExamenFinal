#Casos de prueba

# Pruebas

# Inicializar cuentas
init_cuentas()

# Caso de éxito 1
realizar_transaccion(12345678, 98764321, 50)
historial_transacciones(12345678)
temp = findCuenta_by_numero(12345678)
print(temp.toStr())

# Caso de éxito 2
realizar_transaccion(98764321, 98764322, 30)
historial_transacciones(98764321)
temp = findCuenta_by_numero(98764321)
print(temp.toStr())

# Caso de error 1: Transacción con cuenta de origen inexistente
realizar_transaccion(11111111, 98764321, 50)
historial_transacciones(11111111)
temp = findCuenta_by_numero(11111111)
print(temp.toStr())

# Caso de error 2: Transacción con cuenta de destino inexistente
realizar_transaccion(12345678, 11111111, 50)
historial_transacciones(12345678)
temp = findCuenta_by_numero(12345678)
print(temp.toStr())

# Caso de error 3: Transacción con saldo insuficiente
realizar_transaccion(98764321, 98764322, 150)
historial_transacciones(98764321)
temp = findCuenta_by_numero(98764321)
print(temp.toStr())