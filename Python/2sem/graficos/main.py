from matplotlib import pyplot as plt
import numpy as np
# fig = plt.figure() # Figura vazia sem axes
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.ylabel('some numbers')
# plt.show()

x = np.linspace(0, 2)
plt.plot(x, x, color='gray', linestyle='--', label='linear')
plt.plot(x, x**2, label='quadratico')
plt.plot(x, x**3, label='cubico')
plt.xlabel('x label')
plt.xlabel('y label')
plt.title('Grafico Simples')
plt.legend()
plt.show()