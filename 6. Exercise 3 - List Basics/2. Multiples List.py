factor = int(input())
count = int(input())

my_list = []

for number in range(1, count + 1):
    my_list.append(factor * number)

print(my_list)
