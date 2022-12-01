def data_prep(raw: str) -> list:
    raw_input = [x.split() for x in raw.split('\n')]
    return raw_input


def create_list_of_elves(list) -> list:
    list_of_elves = []
    list_of_snacks = []
    for item in list:
        if item != []:
            list_of_snacks.append(item)
        else:
            list_of_elves.append(list_of_snacks)
            list_of_snacks = []
    return list_of_elves


def count_calories(list, num) -> int:
    calories = 0
    for item in list[num]:
        calories += int(item[0])
    return calories


def create_calorie_list(elves) -> list:
    calorie_list = []
    for number, elf in enumerate(elves):
        calorie_list.append(count_calories(elves,number))
    return calorie_list


if __name__ == '__main__':
    with open('./01-input.txt', 'r') as f:
    # with open('./01-example-1.txt', 'r') as f:
        raw_input = f.read()
    data = data_prep(raw_input)
    elves = create_list_of_elves(data)
    calories = create_calorie_list(elves)
    print(sorted(calories))

    # print(f'Part 1: = {part_one(data)}')
    # print(f'Part 2: = {part_two(data)}')
