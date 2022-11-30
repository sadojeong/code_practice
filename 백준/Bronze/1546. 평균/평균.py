n = int(input())
score_list = input().split()
score_list = list(map(int, score_list))

new_score_list = []

max_ = max(score_list)

for score in score_list:
    new_score_list.append(score/max_*100)

print(sum(new_score_list)/n)