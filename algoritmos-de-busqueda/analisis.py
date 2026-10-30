## Análisis · Algoritmos de búsqueda
Nombre: Luis Manuel Castillo Zeledón
## Proyecto 1 · Tipo de cambio del BCN

| Fecha buscada | Comparaciones lineal | Comparaciones binaria |
|---------------|----------------------|-----------------------|
| 2023-10-02    | 1                    | 4                     |
| 2023-10-20    | 15                   | 4                     |
| 2023-10-31    | 22                   | 5                     |
| 2023-10-07    | 22                   | 4                     |

La lineal solo le gana a la binaria con 2023-10-02. Esa fecha está en la posición 0, entonces la lineal la encuentra en la primera comparación. La binaria siempre empieza por el medio y tiene que ir descartando mitades hasta llegar al principio, por eso hace 4.

### Pregunta 2
Con 22 fechas el peor caso de la lineal es 22 comparaciones (revisar todas). El de la binaria es 5, porque 22 se puede dividir entre 2 cinco veces hasta llegar a 0 (22, 11, 5, 2, 1). Lo comprobé buscando una fecha que no existe, 2023-11-01, y me dio 22 comparaciones en la lineal y 5 en la binaria.

### Pregunta 3
`"2023-10-09" < "2023-10-16"` da `True` y `"31/10/2023" < "02/11/2023"` da `False`. Python compara los textos letra por letra de izquierda a derecha. Con AAAA-MM-DD lo primero que se compara es el año, luego el mes y luego el día, así que el orden de texto es el mismo que el orden de las fechas y la lista queda ordenada para la binaria. Con DD/MM/AAAA se compara primero el día: "31" contra "02" dice que el 31 de octubre es mayor que el 2 de noviembre, y eso está mal. La lista no quedaría ordenada como texto y la binaria fallaría.

### Pregunta 4
Las tasas están de menor a mayor porque en 2023 el córdoba se deslizaba un poquito cada día, o sea que la tasa siempre subía y nunca bajaba, y las fechas también van en orden. Si el tipo de cambio estuviera fijo, como dice la práctica que pasa desde 2024, todas las fechas tendrían la misma tasa. No tendría sentido buscar una fecha a partir de una tasa porque habría muchas fechas con el mismo valor y la búsqueda no sabría cuál devolver.

### Pregunta 5
Con unas 2,600 fechas la lineal haría 2,600 comparaciones en el peor caso y la binaria 12 (2,600 se divide entre 2 doce veces hasta llegar a 0, lo comprobé con la calculadora de la página).

## Proyecto 2 · Consulta de estudiantes por carné UNI

| Carné buscado | Comparaciones lineal | Comparaciones binaria |
|---------------|----------------------|-----------------------|
| 2023-0118U    | 1                    | 4                     |
| 2024-0344U    | 15                   | 1                     |
| 2025-0560U    | 30                   | 5                     |
| 2024-0999U    | 30                   | 5                     |

El carné 2024-0344U se encuentra con una sola comparación en la binaria porque está en la posición 14, que es justo el medio de la primera vuelta: (0 + 29) // 2 = 14. Es el primer elemento que revisa.

### Pregunta 2
Porque la lista de nombres no está en orden alfabético y la binaria solo sirve con listas ordenadas. Para usarla tendría que ordenar los nombres, pero las tres listas son paralelas, así que no puedo ordenar solo una. Tendría que reordenar las tres con el mismo orden, moviendo cada estudiante completo (nombre, carné y carrera) a la misma posición nueva. Si ordeno solo los nombres, quedarían mezclados con carnés y carreras de otros estudiantes.

### Pregunta 3
Porque puede haber varios estudiantes de la misma carrera, y no solo uno. Si se detuviera en la primera coincidencia, se perderían los demás. Por eso tiene que recorrer los 30 elementos siempre.

### Pregunta 4
Con 12,000 estudiantes la lineal haría 12,000 comparaciones en el peor caso y la binaria 14. Con 24,000 la lineal haría 24,000 y la binaria 15. Al duplicar los estudiantes, la lineal también se duplica, pero la binaria solo sube 1 comparación.

### Pregunta 5
El carné 2026-0001U tiene que ir al final, en la posición 30, porque el año 2026 es mayor que todos los de la lista y la lista está ordenada por año y luego por número. Si se insertara al inicio la lista ya no estaría ordenada, y la binaria podría no encontrar carnés que sí existen (como pasó en el proyecto 3).

## Proyecto 3 · ¿Por qué falla la binaria?

### Pregunta 1 (tabla del paso 3)

| Buscado | Real | Binaria | Comparaciones | Veredicto |
|---------|------|---------|---------------|-----------|
| 8875    | 7    | 7       | 1             | CORRECTO  |
| 4821    | 0    | -1      | 4             | FALLA     |
| 2290    | 3    | 3       | 2             | CORRECTO  |
| 7041    | 11   | -1      | 4             | FALLA     |
| 9210    | 13   | 13      | 3             | CORRECTO  |
| 1180    | 8    | -1      | 4             | FALLA     |

La binaria falló en 3 de los 6 valores (4821, 7041 y 1180), aunque todos existen en la lista.

### Pregunta 2 (traza de 7041)
En la vuelta 1 con izq = 0 y der = 14, el medio es 7 y `lista[7]` es 8875. Como 8875 es mayor que 7041, la binaria pensó que 7041 solo podía estar a la izquierda y puso der = 6, descartando las posiciones 7 a 14. Pero 7041 está en la posición 11, o sea que justo descartó la parte donde estaba. La decisión sería correcta si la lista estuviera ordenada, porque entonces todo lo que está a la derecha sería mayor que 8875. Como no está ordenada, esa suposición es falsa. Después siguió buscando en una parte donde no estaba y terminó con -1.

### Pregunta 3
Fue casualidad. El 8875 estaba justo en la posición 7, que es el medio de la lista, y la binaria siempre revisa el medio primero. El algoritmo no hizo nada especial, simplemente el valor cayó ahí. Lo mismo pasa con 2290 y 9210, que también se encontraron, pero porque el camino que tomó la binaria coincidió con la posición donde estaban, no porque la lista estuviera ordenada.

### Pregunta 4
No lo demuestra. Que encuentre algunos valores es suerte, como se vio arriba (3 de 6). La binaria necesita que la lista esté ordenada. Cada vez que descarta una mitad supone que, si el medio es mayor que lo buscado, todo lo que está a la derecha también es mayor (y al revés), y eso solo es cierto con la lista ordenada.

### Pregunta 5
Después de `sorted()` la posición que devuelve la binaria es la posición en la copia ordenada, no en `facturas` original. Por ejemplo 8875 está en la posición 12 de la copia pero en la 7 de `facturas`. Sería un problema si hubiera una lista paralela de montos en córdobas: `montos[12]` sería el monto de otra factura, no el de la 8875, y se mostrarían datos equivocados.

### Pregunta 6
Si voy a buscar una sola vez conviene la lineal, porque para ordenar hay que revisar todos los elementos al menos una vez, así que ya gasté lo mismo o más que una búsqueda lineal completa. Si voy a hacer 1,000 búsquedas sobre la misma lista sí conviene ordenar una vez y usar la binaria, porque el costo de ordenar se paga una sola vez y después cada búsqueda cuesta pocas comparaciones (unas 4 con 15 facturas) en vez de hasta 15.
