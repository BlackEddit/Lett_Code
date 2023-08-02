# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

#URL
#https://leetcode.com/problems/two-sum/description/

class Solution_2(object):
#Primera opcion de solucion:
    def twoSum(self, nums, target):
            # Crear un diccionario vacío, dado que acceder a ellos es mas sencillo que a una lista o tupla, y su complejidad logaritmica es de 0(1), Es decir tiempo constante
            num_map = {}
            
            # Supongamos que nums = [2, 7, 11, 15] y target = 9
            # Recorremos el arreglo nums, obteniendo tanto el índice (i) como el número (num) en cada iteración
            for i, num in enumerate(nums):
                # En la primera iteración, i = 0, num = 2
                
                # Calculamos el complemento del número actual, es decir, la cantidad que necesitaríamos sumar a este número para llegar al objetivo
                complement = target - num
                # En la primera iteración, complement = 9 - 2 = 7
                
                if complement in num_map:
                    # Si es así, hemos encontrado una solución. Devolvemos los índices de los dos números que suman al objetivo
                    # En la primera iteración, esto no se cumple, porque num_map aún está vacío
                    return [num_map[complement], i]
                
                # Si no encontramos el complemento, agregamos el número actual a nuestro diccionario, con su índice como valor
                # Esto nos permitirá encontrarlo más tarde cuando lleguemos al complemento
                num_map[num] = i
                # En la primera iteración, num_map se convierte en {2: 0}
                
                # En la segunda iteración, i = 1, num = 7, complement = 9 - 7 = 2
                # Esta vez, vemos que el complemento (2) sí está en num_map, porque lo agregamos en la iteración anterior
                # Por lo tanto, devolvemos [num_map[2], 1], que es [0, 1]. Estos son los índices de los dos números que suman al objetivo

s = Solution_2() # Instanciacion de la clase
print(s.twoSum([2,7,11,15], 9))


# el uso de un diccionario proporciona una mejora significativa en la eficiencia en comparación con una lista
# aprovechar la búsqueda rápida de los diccionarios en Python (que es O(1)
#Los diccionarios en Python, también conocidos como mapas hash o tablas de hash en ciencia de la computación



#Con el uso de punteros:
class Solution(object):
    def twoSum2(self, nums, target):
    # Asociamos cada número con su índice original en la lista
    # Para [2,7,11,15] esto se convierte en [(2, 0), (7, 1), (11, 2), (15, 3)]
        nums = [(num, i) for i, num in enumerate(nums)] # función incorporada que permite recorrer elementos en una colección (como una lista o una cadena), obteniendo al mismo tiempo el índice del elemento actual dentro de la colección.

    # Ordenamos la lista de números. Esto nos da: [(2, 0), (7, 1), (11, 2), (15, 3)]
    # Python ordena las tuplas basándose en el primer elemento, y usa el segundo solo para desempatar
        nums.sort()

    # Definimos dos punteros, izquierdo y derecho
    # 'left' empieza en el índice 0 y 'right' en el último índice
        left, right = 0, len(nums) - 1  

        while left < right:  # Mientras que el puntero izquierdo sea menor al derecho
        # Calculamos la suma actual de los números en las posiciones 'left' y 'right'
        # Para la primera iteración, es nums[0][0] + nums[3][0] = 2 + 15 = 17
            current_sum = nums[left][0] + nums[right][0] # el segundo cero se refiere al primer elemento de la tupla

            if current_sum == target:  # Si la suma actual es igual al objetivo, hemos encontrado la respuesta
            # Devolvemos los índices originales de los números, no sus posiciones en la lista ordenada
            # Esto sería nums[left][1] y nums[right][1]
                return [nums[left][1], nums[right][1]]

            elif current_sum < target:  # Si la suma actual es menor que el objetivo, necesitamos una suma mayor
            # Para obtener una suma mayor, movemos el puntero izquierdo hacia la derecha
                left += 1

            else:  # Si la suma actual es mayor que el objetivo, necesitamos una suma menor
            # Para obtener una suma menor, movemos el puntero derecho hacia la izquierda
                right -= 1

    # Si hemos salido del bucle sin encontrar una respuesta, entonces no existe tal pareja de números
        return None