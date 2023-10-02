# Numerical Root Finding Methods

Este programa proporciona una implementación de varios métodos numéricos para encontrar raíces de funciones matemáticas. Los métodos implementados incluyen:

1. **Método de Bisección**: Divide iterativamente un intervalo en dos partes hasta que se encuentra una raíz dentro de una tolerancia especificada.

2. **Método de Newton**: Utiliza el método de Newton-Raphson para encontrar una raíz aproximada de una función dada.

3. **Método de Newton Modificado**: Extiende el método de Newton para manejar casos donde la segunda derivada es necesaria para la convergencia.

4. **Método de la Secante**: Utiliza una aproximación de la derivada para encontrar raíces de una función.

## Requisitos

- Python 3.x
- Bibliotecas: NumPy, SymPy, matplotlib (instaladas mediante `pip install numpy sympy matplotlib`)

## Uso

1. Ejecute el programa principal `main.py`.
2. Elija uno de los métodos disponibles y proporcione los detalles requeridos, como la función, valores iniciales y tolerancias.
3. El programa calculará una raíz aproximada y mostrará los resultados en forma gráfica, si es posible.

## Ejemplo de entrada para la función

Cuando se le solicite ingresar una función, puede usar notación de Python estándar para expresiones matemáticas. Por ejemplo:

- `x**2 - 2` para representar la función \(x^2 - 2\).
- `2*x*cos(2*x) - (x + 1)**2` para representar \(2x\cos(2x) - (x + 1)^2\).

También puede utilizar funciones trigonométricas como `cos`, `sin`, `tan`, etc., junto con operadores matemáticos.

## Resultados

Los resultados se mostrarán en la consola y se guardará una gráfica en un archivo llamado "Solution.png" en el directorio de trabajo.

## Contribuciones

¡Esperamos que encuentres este programa útil para tus necesidades de cálculo de raíces numéricas! Si tiene alguna pregunta o necesita ayuda adicional, no dude en ponerse en contacto.

## Autor

- Andrea Lima Blanca
- Contacto: andrealimablanca@outlook.com
