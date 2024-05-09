import random

candidates =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

interviewed = []
hired = []

for _ in range(len(candidates)):
    candidate = random.choice(candidates)
    print(f"Interviewing candidate {candidate}")
    candidates.remove(candidate)
    interviewed.append(candidate)

max = -1
for i in interviewed:
    if i > max:
        max = i
        hired.append(i)

print(f"RANDOMISED INTERVIEW ORDER OF CANDIDATES: {interviewed}")
print(f"CANDIDATES HIRED: {hired}")
print(f"HIRING COST: {len(hired)}")
print(f"FIRING COST: {len(hired)-1}")