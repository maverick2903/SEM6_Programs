import re

with open('AA\samplec.c', 'r') as file:
    lst = [line.strip() for line in file if line.strip()]

code = []
for line in lst:
    if ";" in line:
        code.append(line.rstrip(";"))
    else:
        code.append(line)

top = size = 0
for line in code:
    if "int top" in line:
        top = int(line.split()[-1])
    elif "int stack" in line:
        size = int(re.search(r'\d+', line).group())

print("Top variable of stack is =", top)
print("Total length of stack is =", size)

void_main = code[code.index("void main()") + 2: -1]
print("\nVoid function is :", void_main, "\n")

account_push = 0
func_count = {"pop": [], "push": []}
for line in void_main:
    if "pop" in line:
        if top != -1:
            func_count['pop'].append(1)
            top -= 1
    elif "push" in line:
        if top != size - 1:
            func_count['push'].append(1)
            top += 1
            account_push += 2

var = next((line[line.index("<") + 1: line.index(";", line.index("<"))].strip() for line in void_main if "for" in line), None)

print(func_count)
pop_sum = sum(func_count['pop'])
push_sum = sum(func_count['push'])
pop_count = len(func_count['pop'])
push_count = len(func_count['push'])

print(
    f"\nAggregate analysis = ({pop_sum + push_sum} + {var}) / ({pop_count + push_count} + {var})"
)
print("\nAccounting analysis =", account_push / (pop_count + push_count))

# for stack implementation, we get same heuristic values for operations as in accounting method
print("\nFor potential analysis of push operation:", account_push / push_count)
print("\nFor potential analysis of pop operation: 0")
print("\nFor potential analysis of multipop operation: 0")
