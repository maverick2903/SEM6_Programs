import random

num_interviewees = 10
interview_cost = 20
hiring_cost = 100
firing_cost = 50
total_cost = 0
currScore = -1  # Initialize to -1 to ensure it gets updated the first time
currBestCand = None

order = random.sample(range(0, num_interviewees), num_interviewees)
print(f"Order of candidates in the interview {order}")

candidate_info = {
    'role': [1, 2, 1, 2, 2, 3, 1, 2, 3, 3],
    'cgpa': [7.3, 8.1, 8.5, 9.0, 9.2, 6.7, 7.5, 9.4, 8.8, 8.2],
    'experience': [0, 2, 5, 2, 3, 2, 2, 1, 0, 4]
}

criteria = {
    'role': 2,
    'cgpa': 8,
    'experience': 2
}

for i in range(num_interviewees):
    total_cost += interview_cost
    if candidate_info['role'][order[i]] >= criteria['role'] and candidate_info['cgpa'][order[i]] >= criteria['cgpa'] and candidate_info['experience'][order[i]] >= criteria['experience']:  # activate the threshold
        if candidate_info['experience'][order[i]] != 0:  # Check for division by zero
            candScore = random.randint(1,10)*(candidate_info['role'][order[i]] * candidate_info['cgpa'][order[i]]) / candidate_info['experience'][order[i]]
            if currScore < candScore:
                currScore = candScore
                currBestCand = order[i]
                total_cost += hiring_cost  # Add hiring cost
            elif currScore == candScore:
                total_cost += firing_cost  # Add firing cost
                currBestCand = order[i]
    print(f'Candidate {order[i]+1} Score: {candScore}')

print(f'Best Score: {currScore}')
print(f'Best candidate: Candidate {currBestCand+1}')
print(f'Total cost: {total_cost}')