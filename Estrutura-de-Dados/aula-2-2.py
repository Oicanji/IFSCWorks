
import numpy as np 
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
labels = ['Constante', 'Logaritmo', 'linear', 'loglinear', 'Quadratica', 'Cubica', 'Exponencial']
big_o = [np.ones(n.shape), np.log(n), n, np.multiply(n, np.log(n)), np.multiply(n, n), np.multiply(np.multiply(n, n), n), np.exp2(n)]

plt.figure(figsize=(5, 4))
plt.ylim(0, 100)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])
plt.legend()
plt.ylabel('Tempo de execução')
plt.xlabel('N')
plt.show()