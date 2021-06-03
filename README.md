# NewtonRaphsonAnimation
Python program to animate the Newton Raphson method for root finding in numerical analysis.

Newton Raphson method uses tangent line of derivates to approximate the next root. 
The script allows you to input your own funcion with a seed, and analize how it converges to the solution.


https://user-images.githubusercontent.com/30214999/120572543-840eda80-c3f2-11eb-92c7-346d7ab5616a.mov

## How to use

Paste the code of ```newtonRaphson.py``` inside a code block of junyper notebook or [Google colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) (preferred)

Right below the pasted code, just call the function ```animacionNewtonRaphson``` receiving the following params:

* ```funcion```: The function to use (ie. lambda x: x**2)
* ```funcionDerivada```: The derivate of the funcion (ie. lambda x: 2*x)
* ```aproximacionInicial```: The initial seed (ie. 0.5)

 *optional parameters:*
 * ```xMenor=-10```: Left x axis bound
 *  ```xMayor=10```: Right x axis bound
 *  ```yMenor=-10```: Bottom y axis bound
 *  ```yMayor=10```: Top y axis bound
 *   ```puntos=1000```: Amount of points (more points for softer functions)
 *   ```tolerancia```: Tolerance for stopping the algorithm
 *   ```maximasIteracionesPermitidas=100```: Maximum allowed iterations before stopping the algorithm
 *   ```zoom=1```: Zoom for having a closer look at the function (2 = 2 times closer)
 *   ```tamanioEnPulgadas=10```: size of animation in inches
 *   ```bitsDeMaquina=64```: 64 or 32 bits for perfoming the calculations
 *   ```label="Newton Raphson"```: Label for the animation

## Examples

## Live example
https://colab.research.google.com/drive/1Bt2g7rIiXUaqKOfZY_1cT0oD94sA2UQN#scrollTo=T_3L5-qLz1im

### Using lambda functions
```python
animacionNewtonRaphson(
    funcion = lambda x: x**2,
    funcionDerivada = lambda x: 2*x,
    aproximacionInicial = 2.0,
    tolerancia = 0.1,
    maximasIteracionesPermitidas = 10,
    xMenor=-20,
    xMayor=20,
    puntos=1000,
    bitsDeMaquina = 64,
    zoom = 4
```

### Using regular functions
```python

sin(x):
  math.sin(x)
  
cos(x):
  math.cos(x)
  
animacionNewtonRaphson(
    funcion = sin,
    funcionDerivada = cos,
    aproximacionInicial = 2.0,
    tolerancia = 0.1,
    maximasIteracionesPermitidas = 10,
    xMenor=-5,
    xMayor=5,
    puntos=1000,
    bitsDeMaquina = 32,
    zoom = 2,
    label = 'Figura 3.1.3: Aproximacion a la raiz pi mediante NR')
```
