from cProfile import label
import numpy as np 
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
labels = ['Constante', 'Linear', 'Quadratica', 'Cubica']
big_o = [np.ones(n.shape), np.log(n), n]

plt.figure(figsize=(5, 4))
plt.ylim(0, 10)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])
plt.legend()
plt.ylabel('Tempo de execução')
plt.xlabel('N')
plt.show()