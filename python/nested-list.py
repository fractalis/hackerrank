# https://www.hackerrank.com/challenges/nested-list/problem

from collections import defaultdict

if __name__ == '__main__':

    scores = []
    scores_dict = defaultdict(lambda: [])

    for _ in range(int(input())):
        name = input()
        score = float(input())

        ns = [name, score]
        scores.append(ns)

    scores = sorted(scores, key=lambda x: x[1])

    for score in scores:
        scores_dict[score[1]].append(score[0])

    snd = list(sorted(scores_dict.keys()))[1]
    res = sorted(scores_dict[snd])
    for x in res:
        print(x)

