given_names_count = int(input())

unique_usernames = set()

for name in range(given_names_count):
    unique_usernames.add(input())

for name in unique_usernames:
    print(name)

### or ##

#print(*unique_usernames, sep="\")



#### Second solution ####

print(*{input() for _ in range(int(input()))}, sep ="\n")