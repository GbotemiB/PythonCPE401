import matplotlib.pyplot as plt
import numpy as np
import LogicalFunc
import subtractionFunction


def subtract_and_convert_to_decimal(a, b):
    [output, carry, sign] = subtractionFunction.subtraction(a, b)
    print(a, b, f"{sign}{output}")
    if sign == '-':
        return - (int(output, 2))
    return int(output, 2)


random = np.random
# Prepare the data
x = np.linspace(0, 15, 16)
y = [random.randint(1, 15) for i in range(len(x))]
first = [LogicalFunc.decimal_to_binary(i) for i in x]
second = [LogicalFunc.decimal_to_binary(y[i]) for i in range(len(y))]
result = [subtract_and_convert_to_decimal(first[i], second[i]) for i in range(len(x))]

print(result)
# Plot the data
plt.plot(x, x, label='linear')
plt.scatter(x, x, edgecolors='blue', color='blue')
plt.plot(x, y)
plt.scatter(x, y, edgecolors='red', color='red')
plt.plot(x, result)
plt.scatter(x, result, edgecolors='red', color='yellow')
plt.annotate('input a', xy=(x[2], x[2]))
plt.annotate('input b', xy=(x[2], y[2]))
plt.annotate('output', xy=(x[2], result[2]))
plt.ylim([-16, 16])
plt.yticks(np.arange(-16, 16, 1))
plt.xticks(np.arange(0, 16, 1))

plt.text(13, 13, 'input a', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})
plt.text(0, 13, 'subtact b', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.text(0, -13, 'output', bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})
# Show the plot
plt.show()
