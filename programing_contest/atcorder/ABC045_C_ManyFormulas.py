S = list(input())
N = len(S) -1 
all_formula = []
result = 0


for i in range(2**N):
    temp = S
    for j in range(N):
        all_formula.append(S[j])
        if i & 2**j:
            all_formula.append("+")
    all_formula.append(S[-1])
    all_formula.append("+")

all_formula.pop(-1)
all_formula = ''.join(all_formula)
result = eval(all_formula)

print(result)

