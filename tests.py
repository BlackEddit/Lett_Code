#  Probability to get a value
import scipy.stats as st 


# Por favor, ten en cuenta que he utilizado un 
# valor de 1 para la desviación estándar (sigma) porque no se proporciona en el enunciado 
# del problema. Para un cálculo real, necesitarías 
# conocer la desviación estándar de las temperaturas de la playa.
mu = 35  # mean
sigma = 1  # This is a placeholder, you would need to know the standard deviation

print(st.norm.pdf(35, mu, sigma))