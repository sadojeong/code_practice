def solution(lottos, win_nums):
    max = 7 - len(set(lottos) & set(win_nums))
    min = max-lottos.count(0)
    return [min if min <7 else 6, max if max <7 else 6]