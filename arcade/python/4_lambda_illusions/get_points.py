def getPoints(answers, p):
    questionPoints = lambda x, correct_answer: x+1 if correct_answer else p * -1

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
