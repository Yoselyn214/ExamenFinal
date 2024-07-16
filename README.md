# ExamenFinal

## Pregunta 3 (5 puntos)

### Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir por día.
Qué cambiaría en el código (Clases / Métodos) - No realizar la implementación, sólo descripción.

Se agregaría una variable llamada Máximo_transferencia que estaria sumando los montos de las transferencias que se hicieran durante el dia , en la función transferencia se agregaria una condicional que vaya evaluando si esa variable se ha pasado los 200 soles, si se paso le saldra un mensaje diciendole al usuario que se paso del máximo de transferencias por dia y le saldra el monto de transferencias que lleva actualmente.
 
### Qué casos de prueba nuevos serían necesarios?

  Prueba: Múltiples transferencias a varios contactos del usuario hasta llegar al limite por dia.
  Retorna que ha llegado al límite de las transferencias por dia y le devuelve el monto de transferencias que lleva.

### Los casos de prueba existentes garantizan que no se introduzcan errores en la funcionalidad existente?

Si, ya que en las transferencias se toma en consideración el saldo del usuario, que el contacto a quien se transfiera debe ser contacto del usuario y en agregar nuevo contacto se toma en consideración de que el usuario exista y que no este en la lista de contactos antes de agregarlo.
