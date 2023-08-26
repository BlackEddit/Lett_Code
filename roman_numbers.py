# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].



class Solution(object):
    def romanToInt(self, s):

            #Create a mapa for Numerical values 
            #Dict
        roman_to_int = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
        }
        
        #inicializamos
        total = 0
        prev_value = 0

        for c in reversed(s):
            current_value = roman_to_int[c]

            #Si el valor actual es menor uqe el previo entonces lo restamos
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value
            
        return total
    
    
    
#EXPLANATION

# A continuación se resumen las ventajas y sugerencias para mejorar la eficacia:

# Ventajas:
# 1. El enfoque utiliza un diccionario para mapear símbolos romanos a sus valores correspondientes,
#    lo que facilita la conversión de números romanos a enteros.
# 2. El uso del enfoque de iteración en orden inverso permite manejar casos de resta correctamente,
#    siguiendo las reglas de los números romanos.

# Sugerencias para Mejorar la Eficacia:
# 1. Este enfoque tiene un tiempo de ejecución lineal O(n), donde n es la longitud de la cadena romana.
#    Esto es eficiente y adecuado para las restricciones del problema.
# 2. Asegúrate de que el diccionario 'roman_to_int' esté definido correctamente para incluir todos los símbolos necesarios.
# 3. Considera optimizar los símbolos romanos a valores mapeados para mejorar la eficacia si es necesario.
# 4. Realiza pruebas exhaustivas para garantizar que el código maneje correctamente todos los casos posibles.

# ¡Felicitaciones por abordar con éxito el desafío de la conversión de números romanos a enteros!