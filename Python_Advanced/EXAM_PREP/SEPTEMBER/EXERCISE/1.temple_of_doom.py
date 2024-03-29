from collections import deque

tools = deque(map(int, input().split()))
substances = [int(x) for x in input().split()]
challenges = [int(y) for y in input().split()]

while challenges:
    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

    result = 0
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)

        current_substance -= 1
        if current_substance <= 0:
            continue
        else:
            substances.append(current_substance)
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools:", ', '.join([str(x) for x in tools]))
if substances:
    print(f"Substances:", ', '.join([str(x) for x in substances]))
if challenges:
    print(f"Challenges:", ', '.join([str(x) for x in challenges]))

