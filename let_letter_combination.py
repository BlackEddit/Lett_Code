""""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 
 Go to the web to check the problem https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

# Primero, estamos definiendo una clase llamada 'Solution'. Piensa en una clase como un plano para crear algo. En este caso, 'Solution' es el plano que vamos a usar para crear 'soluciones'.
class Solution(object):
 
    def letterCombinations(self, digits):

        # Si no nos dan ningún número (es decir, si la cadena 'digits' está vacía), no podemos hacer ninguna combinación de letras. Por lo tanto, simplemente devolvemos una lista vacía.
        if not digits:
            return []

        # En este caso, nuestras claves son los dígitos del 2 al 9, y los valores son las letras que esos dígitos representan en un teclado de teléfono.
        phone_digits = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

 
        # Uso de una funcion recursiva, que se llame a si misma
        def backtrack(combination, next_digits):

            # Dentro de 'backtrack', primero verificamos si ya no quedan dígitos para procesar (es decir, si hemos llegado al final de la cadena 'digits').
            # Si ese es el caso, significa que hemos construido una combinación completa de letras, así que la añadimos a nuestra lista de resultados.
            if len(next_digits) == 0:
                res.append(combination)
            
            # Si todavía quedan dígitos para procesar, entonces para cada letra que corresponde al primer dígito no procesado...
            else:
                for letter in phone_digits[next_digits[0]]:  
                    # ... agregamos esa letra a nuestra combinación actual de letras y llamamos a 'backtrack' nuevamente, pero ahora sin el primer dígito y con la nueva combinación de letras.
                    # Al hacer esto, estamos explorando todas las posibles combinaciones de letras que podemos hacer con los dígitos restantes.
                    backtrack(combination + letter, next_digits[1:]) 

        # Aquí estamos creando una lista vacía llamada 'res'. Esta es la lista en la que vamos a guardar todas nuestras combinaciones finales de letras.
        res = []

        # Ahora estamos comenzando el proceso de 'backtracking'. Empezamos con una combinación de letras vacía (porque aún no hemos procesado ningún dígito) y con todos los dígitos que necesitamos procesar (es decir, todos los dígitos en la cadena 'digits').
        backtrack("", digits)

        # Una vez que el proceso de 'backtracking' ha terminado y hemos explorado todas las posibles combinaciones de letras, simplemente devolvemos la lista 'res' que ahora contiene todas nuestras combinaciones.
        return res