# continue and break
# while loop
i = 0
while i <= 3:
    if i == 1:
        break
    i += 1
print(i)

# for loop
# forEach loop on a string
for item in 'hello':
    print(item)
# forEach loop on an array
for item in [1, 2, 3, 4]:
    print(item)

for item in range(5, 10, 1):  # starts from 5 and ends at 9 but 10 is not included, step is 1
    print(item)
