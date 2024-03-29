from collections import deque

given_input = deque(input().split())
possible_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {"orange": {"red", "yellow"},
                    "purple": {"red", "blue"},
                    "green": {"yellow", "blue"},}
colors = []

while given_input:
    left_part = given_input.popleft()
    right_part = given_input.pop() if given_input else ''


    for color in (left_part + right_part, right_part + left_part):
        if color in possible_colors:
            colors.append(color)
            break
    else:
        for el in (left_part[:-1], right_part[:-1]):
            if el:
                given_input.insert(len(given_input) // 2, el)

for color in set(secondary_colors.keys()).intersection(colors):
    if not secondary_colors[color].issubset(colors):
        colors.remove(color)
print(colors)
