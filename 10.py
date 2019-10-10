array = []
arra_y = []
arr_ay = []

for i in range (10):
  count = random.randint(0,10)
  array.append(count)

for x in range (10):
  count = random.randint(0,10)
  arra_y.append(count)

for x in range(10):
  arr_ay.append(array[x])
  arr_ay.append(arra_y[x])


print(array)
print(arra_y)
print(arr_ay)
