import numpy as np

array_1 = np.array([2,3,10,19])
array_2 = np.array([4,1,3,11])
print(array_1)
print(array_2)

adding = array_1+array_2
print(f"After adding Two arrays :{adding}")

substraction = array_1 - array_2
print(f"After subracting Two arrays :{substraction}")

mul = array_1 * array_2
print(f"After Multiplying Two arrays :{mul}")

div = array_1 / array_2
print(f"After dividing Two arrays :{div}")

power_2 = np.power(array_1,2)
print(power_2)