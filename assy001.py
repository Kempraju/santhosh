#1
null_vector = [0] * 10
null_vector[4] = 1
#2
vector = [i for i in range(10, 50)]
#3
import numpy as np

matrix = np.arange(9).reshape(3, 3)
#4
lst = [1, 2, 0, 0, 4, 0]
non_zero_indices = [index for index, value in enumerate(lst) if value != 0]
#5
import numpy as np

# Create a 10x10 array with random values
array = np.random.random((10, 10))

# Find the minimum and maximum values
minimum_value = np.min(array)
maximum_value = np.max(array)
#6
import numpy as np

# Generate a random vector of size 30
random_vector = np.random.rand(30)

# Calculate the mean value
mean_value = np.mean(random_vector)

print("Random Vector:")
print(random_vector)
print("\nMean Value:", mean_value)