Integrantes:
- Sebastian Tenorio
- Yoselyn Miranda
# ExamenFinal

## Pregunta 3 (5 puntos)

### Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a transferir por día.
Qué cambiaría en el código (Clases / Métodos) - No realizar la implementación, sólo descripción.

Se agregaría una variable llamada Máximo_transferencia que estaria sumando los montos de las transferencias que se hicieran durante el dia , en la función transferencia se agregaria una condicional que vaya evaluando si esa variable se ha pasado los 200 soles, si se paso le saldra un mensaje diciendole al usuario que se paso del máximo de transferencias por dia y le saldra el monto de transferencias que lleva actualmente.
 
### Qué casos de prueba nuevos serían necesarios?

  Prueba: Múltiples transferencias a varios contactos del usuario hasta llegar al limite por dia.
  Retorna que ha llegado al límite de las transferencias por dia y le devuelve el monto de transferencias que lleva.

  | Test Case                           | Precondition                         | Test Steps                                                        | Test Data                      | Expected Result                                         |
|-------------------------------------|--------------------------------------|-------------------------------------------------------------------|-------------------------------|---------------------------------------------------------|
| Verificar que no se pase la transferencia por dia| Se debe ingresar la data para el test. | Una vez ingresado la data se llamará a la función transferencia |data =[["Juana",500],["Rosa",600]]| ,  Limite de transferencia pasado por dia, devuelve monto de transferencia acumulado|

### Los casos de prueba existentes garantizan que no se introduzcan errores en la funcionalidad existente?

No en todos los casos por ejemplo no hicimos una prueba que tomara en consideración si el usuario a quien se transfirio pertenecia a la lista de contactos, pero si tenemos que se verifique que el saldo tenga que ser suficiente antes de hacer transferencias.



