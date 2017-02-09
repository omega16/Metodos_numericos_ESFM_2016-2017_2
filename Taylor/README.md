Calculo del polinomio P_n de Taylor par una función dada como argumento f(x) al rededor de un punto x0 y aproximación de un valor x así como el calculo de los errores absoluto, relativo y porcentual respecto al calculado por python .


Ejemplo de ejecución (ejercicio solicitado en clase)


./driver.py "h(x) = sin(x) " 2.2 2.37 6


x0=2.2


x=2.37


n=6



El programa esta escrito en python3 usando la libreria sympy, para instalarla se puede usar por ejemplo el comando:


pip3 install sympy


En sistemas ubuntu se puede usar alternativamente :


sudo apt install python3-sympy

Nota: la libreria sympy tiene un error de implementación en la función que escribe  la serie Taylor combinando los primeros dos coeficientes, esto causa que la serie calculada por el programa y la serie calculada por sympy difieran en los primeros coeficientes, el problema es resuelto después del coeficiente n=3 .
