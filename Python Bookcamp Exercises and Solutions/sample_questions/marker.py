def marker(test):
    # Initiate 'score' as 0.
    score = 0
    if test == 'You are correct.':
        print('You are correct.')
        # Increase 'score' variable by 1.
        score += 1
        return score
    else:
        print('You are wrong.')
        # 'score' variable remains 0.
        return score