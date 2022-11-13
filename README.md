Muricio Juarez 43137319
Facundo Visa 42453631

# Proyecto Final Investigacion Operativa II

## Informe
### Unidad 1: Juegos
#### Eliminación de dominadas
Consiste en ir eliminando iterativamente todas las estrategias dominadas. Partiendo de la matriz de pagos, en el primer paso, se elimina una estrategia dominada, ya que ningún jugador racional jugaría nunca esa estrategia. Esto se traduce en un nuevo juego más pequeño. Algunas estrategias que en el primer paso no eran dominadas, pueden resultar dominadas en este nuevo juego más pequeño. Este primer paso se repite sucesivamente creando cada vez un juego más pequeño hasta que el proceso se detiene. Esto ocurre cuando ningún jugador es capaz de encontrar una estrategia estrictamente dominante o dominada.
![](https://i.postimg.cc/Hn5skFSJ/Screenshot-1.png)

#### Minimax
Este teorema establece que en los juegos bipersonales de suma cero, donde cada jugador conoce de antemano la estrategia de su oponente y sus consecuencias, existe una estrategia que permite a ambos jugadores minimizar la pérdida máxima esperada. En particular, cuando se examina cada posible estrategia, un jugador debe considerar todas las respuestas posibles del jugador adversario y la pérdida máxima que puede acarrear. El jugador juega, entonces, con la estrategia que resulta en la minimización de su máxima pérdida. Tal estrategia es llamada óptima para ambos jugadores sólo en caso de que sus minimaxes sean iguales (en valor absoluto) y contrarios (en signo). Si el valor común es cero el juego se convierte en un sinsentido.
![](https://i.postimg.cc/zXZGcXBT/Screenshot-2.png)

#### Estrategia mixta
En teoría de juegos una estrategia mixta, a veces también llamada estrategia mezclada (del nombre en inglés mixed strategy), es una generalización de las estrategias puras, usada para describir la selección aleatoria de entre varias posibles estrategias puras, lo que determina siempre una distribución de probabilidad sobre el vector de estrategias de cada jugador. Una estrategia totalmente mixta es aquella en la que el jugador asigna una probabilidad estrictamente positiva a cada estrategia pura. Las estrategias totalmente mixtas son importantes para el refinamiento del equilibrio.
Ejemplo: Piedra, Papel Tijera

Supongamos que el jugador 1 juega siempre en estrategias puras, por ejemplo piedra. Entonces el jugador 2 podría sacar ventaja de ello jugando siempre papel. Una mejor respuesta del jugador 1 sería entonces jugar con estrategias mixtas, es decir, asignarle cierta probabilidad a cada estrategia y en cada jugada elegir aleatoriamente de acuerdo a la distribución elegida.
Puede demostrarse que siempre que haya sesgo en estas probabilidades (es decir, cuando se le asigne más probabilidad a una estrategia que a otra), el otro jugador puede sacar ventaja de ello y mejorar su pago esperado. De este modo, el juego sólo tiene un equilibrio de Nash y es (1/3,1/3,1/3), es decir, jugar con igual probabilidad cada estrategia (siempre y cuando se mantengan los pagos dados por la matriz).
![](https://i.postimg.cc/vmqmqrgm/Screenshot-3.png)

#### Equilibrio de Nash
El equilibrio de Nash es, en la teoría de juegos,​ un “concepto de solución” para juegos con dos o más jugadores, el cual asume que:
Cada jugador conoce y ha adoptado su mejor estrategia, y todos conocen las estrategias de los otros.
Consecuentemente, cada jugador individual no gana nada modificando su estrategia mientras los otros mantengan las suyas. Así, cada jugador está ejecutando el mejor "movimiento" posible teniendo en cuenta los movimientos de los demás jugadores.
En otras palabras, un equilibrio de Nash es una situación en la cual todos los jugadores han puesto en práctica, y saben que lo han hecho, una estrategia que maximiza sus ganancias dadas las estrategias de los otros. Consecuentemente, ningún jugador tiene ningún incentivo para modificar individualmente su estrategia.
Es importante tener presente que un equilibrio de Nash no implica que se logre el mejor resultado conjunto para los participantes, sino solo el mejor resultado para cada uno de ellos considerados individualmente. Es perfectamente posible que el resultado fuera mejor para todos si, de alguna manera, los jugadores coordinarán su acción.
![](https://i.postimg.cc/3RkxPkmF/Screenshot-4.png)

### Unidad de Grafos:
#### Árbol de mínima expansión
El árbol de expansión de peso mínimo es aquel que comienza desde un vértice y encuentra todos sus nodos accesibles y las relaciones en conjunto que permiten que se conecten dichos nodos con el menor peso posible Dado un grafo conexo, no dirigido y con pesos en las aristas, un árbol de expansión mínima es un árbol compuesto por todos los vértices y cuya suma de sus aristas es la de menor peso.
El problema de hallar el Árbol de Expansión Mínima (MST) puede ser resuelto con varios algoritmos, los más conocidos son Prim y Kruskal
![](https://i.postimg.cc/nc4hbbjg/Screenshot-5.png)

#### Algoritmo de la ruta más corta
El algoritmo de rutas más cortas es uno de los módulos de análisis más importantes de los algoritmos de grafos. Este se encarga de detectar dentro de un grafo cuál es la ruta más eficiente o el recorrido de menor distancia entre un par de vértices que conforman un grafo.
Este algoritmo es usado por los dispositivos GPS para encontrar el camino más corto entre la ubicación actual y el destino del usuario. Tiene amplias aplicaciones en la industria, especialmente en aquellas áreas que requieren modelar redes.
Una de sus aplicaciones más importantes reside en el campo de la telemática. Gracias a él, es posible resolver grafos con muchos nodos, lo que sería muy complicado resolver sin dicho algoritmo, encontrando así las rutas más cortas entre un origen y todos los destinos en una red.
![](https://i.postimg.cc/ZqKRx7qg/Screenshot-6.png)

#### Algoritmo de flujo máximo
El procedimiento para obtener el flujo máximo de una red, consiste en seleccionar repetidas veces cualquier trayectoria de la fuente al destino y asignar el flujo máximo posible en esa trayectoria.
Las aristas representan canales por los que puede circular cierta cosa: transmisión de datos, redes de corriente eléctrica, líneas de oleoductos, agua, automóviles, etc.
![](https://i.postimg.cc/XJtY3ngS/Screenshot-7.png)

#### Algoritmo de la ruta crítica
El método de la ruta crítica es una técnica que te permite identificar las tareas necesarias para finalizar un proyecto y determinar cierta flexibilidad en el cronograma. Una ruta crítica en la gestión de proyectos es la secuencia más larga de actividades que deben finalizar a tiempo para completar todo el proyecto.
El método de la ruta crítica tiene como fin identificar las tareas más importantes del cronograma del proyecto, detectar las dependencias de las tareas y calcular la duración de las tareas.
El método de la ruta crítica fue desarrollado a fines de la década de 1950 como un método para dar solución al aumento de los costos producido por la planificación ineficiente. Desde entonces, se usa con frecuencia para planificar proyectos y priorizar tareas. Te ayuda a desglosar tareas complejas en tareas individuales y a tener una idea general de la flexibilidad de un proyecto.
![](https://i.postimg.cc/Cx45DTwk/Screenshot-8.png)




### Unidad de Colas
#### Modelos
#### M/M/1
En la teoría de colas una cola M/M/1 representa la longitud de la cola en un sistema que tiene un solo servidor, donde las llegadas están determinadas por un proceso de Poisson y los tiempos de servicio del trabajo tienen una distribución exponencial. El nombre del modelo está escrito en la notación de Kendall. El modelo es el más elemental de los modelos de colas  y un atractivo objeto de estudio ya que se pueden obtener expresiones de forma cerrada para muchas métricas de interés en este modelo. Una extensión de este modelo con más de un servidor es la cola M/M/c .
#### M/G/1
En la teoría de colas una cola M /G/1 es un modelo de cola donde las llegadas son markovianas (moduladas por un proceso de Poisson ), los tiempos de servicio tienen una distribución general y hay un solo servidor. El nombre del modelo está escrito en la notación de Kendall y es una extensión de la cola M/M/1, donde los tiempos de servicio deben distribuirse exponencialmente. La aplicación clásica de la cola M/G/1 es modelar el rendimiento de un disco duro de cabeza fija.
#### M/D/1
En la teoría de colas , una disciplina dentro de la teoría matemática de la probabilidad , una cola M/D/1 representa la longitud de la cola en un sistema que tiene un solo servidor, donde las llegadas están determinadas por un proceso de Poisson y los tiempos de servicio del trabajo son fijos (deterministas). El nombre del modelo está escrito en la notación de Kendall. Una extensión de este modelo con más de un servidor es la cola M/D/c.
#### M/M/s
Modelo donde tanto los tiempos entre llegada como los tiempo de servicio son exponenciales y se tienen s servidores.
Este modelo supone que existen en el sistema s (entero positivo) servidores
