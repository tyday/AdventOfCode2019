data = [134564, 585159]


def passes_test(number, max):
    numb = str(number)
    longest_streak = 0
    streak = 0
    for i in range(len(numb) -1):
        if numb[i] == numb[i+1]:
            streak += 1
            if streak >= max:
                return False
            elif streak > longest_streak:
                longest_streak = streak
        elif numb[i] > numb[i+1]:
            return False
        else:
            streak = 0
    if longest_streak > 1:
        return True
    else:
        return False
        

def has_repeating_number(number, mini, maxi):
    numb = str(number)
    check = {}
    for i in range(len(numb)):
        if (i < len(numb)-1 and numb[i] > numb[i+1]):
            return False
        elif numb[i] in check:
            check[numb[i] ] += 1
        else:
            check[numb[i] ] = 1
    # longest = 0
    # for k, v in check.items():
    #     if v > longest:
    #         longest = v
    # if mini <= longest <= maxi:
    for k, v in check.items():
        if mini <= v <= maxi:
            return True
    return False


def part_one_check(number, reqs):
    passable_numbers = []
    for i in range(number[0], number[1]+1):
        if has_repeating_number(i, reqs[0], reqs[1]):
            passable_numbers.append(i)
    
    # for i in range(number[0], number[1]+1):
    #     if passes_test(i, 10):
    #         passable_numbers.append(i)
    print(len(passable_numbers))


part_one_check(data, (2, 2))
# print(has_repeating_number(111111,2,20))
# print(has_repeating_number(223450,2,10))
# print(has_repeating_number(123789,2,10))
# print(passes_test(111111,10))
# print(passes_test(223450,10))
# print(passes_test(123789,10))
