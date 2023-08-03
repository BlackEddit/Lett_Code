# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]



class ListNode(object):
    # El inicializador para cada nodo en la lista.
    # Cada nodo tiene un valor (por defecto 0 si no se especifica) y un apuntador al siguiente nodo (por defecto None si no se especifica).
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Crear un nodo inicial 'dummy'. Este nodo no tiene un significado real y sólo se usa para mantener el inicio de la lista de resultados.
        dummy = ListNode(0)
        
        # La variable 'current' apunta al último nodo en la lista de resultados. Si es un apuntador pero no
        current = dummy
        
        # Iniciar 'carry' en 0. 'carry' almacena el valor que se lleva a la siguiente iteración cuando la suma de dos dígitos es mayor o igual a 10.
        #carry sirve para mantener la parte de la suma que debe "llevarse"
        #a la siguiente posición del dígito cuando sumas los dígitos de las dos listas de entrada.
        carry = 0
        
        # Mientras haya nodos para procesar en l1 o l2, o haya un 'carry' distinto de 0.
        while l1 or l2 or carry:
            # Extraer los valores en los nodos actuales de l1 y l2. Si la lista se ha agotado, usar 0.
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            
            # Sumar los valores extraídos y el 'carry'.
            carry, out = divmod(val1 + val2 + carry, 10)
            #divmod(17, 5) retorna (3, 2). Esto se debe a que 17 dividido por 5 es 3 con un residuo de 2.
            
            # Añadir el resultado a la lista de resultados.
            current.next = ListNode(out)
            current = current.next
            
            # Avanzar a los siguientes nodos en l1 y l2.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Devolver el inicio de la lista de resultados. Dado que 'dummy' es un nodo inicial sin significado, devolvemos 'dummy.next'.
        return dummy.next
    
    
        """
        We should ask to develpment tools to use node list of another algoritms 
        
        """