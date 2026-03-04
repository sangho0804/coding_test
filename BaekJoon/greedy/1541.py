import sys
input = sys.stdin.readline

expr = input().strip()

tokens = []
num = ""
for ch in expr:
    if ch in "+-":
        tokens.append(num)
        tokens.append(ch)
        num = ""
    else:
        num += ch
tokens.append(num)

nums = [int(tokens[i]) for i in range(0, len(tokens), 2)]
ops  = [tokens[i] for i in range(1, len(tokens), 2)]

result = nums[0]
minus_started = False

for i, op in enumerate(ops):
    if op == '-':
        minus_started = True
    
    if minus_started:
        result -= nums[i+1]
    else:
        result += nums[i+1]

print(result)