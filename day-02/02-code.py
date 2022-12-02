def data_prep(raw: str) -> list:
    raw_input = [x.split() for x in raw.split('\n')]
    return raw_input


def score_hand(match):
    if match == []:
        return 0
    # "A" and "X" are rock
    if match[0] == 'A' and match[1] == 'X':
        score = 1 + 3
    elif match[0] == 'A' and match[1] == 'Y':
        score = 2 + 6
    elif match[0] == 'A' and match[1] == 'Z':
        score = 3 + 0
    # "B" and "Y" are paper
    elif match[0] == 'B' and match[1] == 'X':
        score = 1 + 0
    elif match[0] == 'B' and match[1] == 'Y':
        score = 2 + 3
    elif match[0] == 'B' and match[1] == 'Z':
        score = 3 + 6
    # "C" and "Z" are scissors
    elif match[0] == 'C' and match[1] == 'X':
        score = 1 + 6
    elif match[0] == 'C' and match[1] == 'Y':
        score = 2 + 0
    elif match[0] == 'C' and match[1] == 'Z':
        score = 3 + 3
    return score


def score_two(match):
    if match == []:
        return 0
    # "A" is rock, "X" means lose, "Y" means draw, "Z" means win
    if match[0] == 'A' and match[1] == 'X':
        score = 3 + 0
    elif match[0] == 'A' and match[1] == 'Y':
        score = 1 + 3
    elif match[0] == 'A' and match[1] == 'Z':
        score = 2 + 6
    # "B" is paper
    elif match[0] == 'B' and match[1] == 'X':
        score = 1 + 0
    elif match[0] == 'B' and match[1] == 'Y':
        score = 2 + 3
    elif match[0] == 'B' and match[1] == 'Z':
        score = 3 + 6
    # "C" is scissors
    elif match[0] == 'C' and match[1] == 'X':
        score = 2 + 0
    elif match[0] == 'C' and match[1] == 'Y':
        score = 3 + 3
    elif match[0] == 'C' and match[1] == 'Z':
        score = 1 + 6
    return score


if __name__ == '__main__':
    with open('./02-input.txt', 'r') as f:
    # with open('./02-example-1.txt', 'r') as f:
        raw_input = f.read()

    games = data_prep(raw_input)
    total_score = 0
    for match in games:
        total_score += score_hand(match)

    print(f'Part One: {total_score}')

    total_score = 0
    for match in games:
        total_score += score_two(match)

    print(f'Part Two: {total_score}')

