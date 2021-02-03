


def opcAdd(data,i):
    # Adds
    x = data[i+1]
    y = data[i+2]
    z = data[i+3]
    data[z] = data[x] + data[y]
    return 4 # number of positions to move forward along op code

def opcMultiply(data, i):
    # Multiplies
    x = data[i+1]
    y = data[i+2]
    z = data[i+3]
    data[z] = data[x] * data[y]
    return 4

def opcStop(data, i):
    return 0

OPCODES = {
    1: opcAdd,
    2: opcMultiply,
    99: opcStop
}

def evaluate_op_code(data):
    i = 0
    while i < len(data):
        result = OPCODES[data[i]](data, i)
        if result == 0:
            break
        else:
            i += result

if __name__ == '__main__':
    # test_data = [1,1,1,4,99,5,6,0,99]
    # evaluate_op_code(test_data)
    # print(test_data)
    test_data = []
    with open("/home/pi/Programming/AdventOfCode/2019/Day02/input.txt", "r") as f:
        test_data = f.read().split(',')
        test_data = [int(item) for item in test_data]
    # test_data[1] = 12
    # test_data[2] = 2
    # evaluate_op_code(test_data)
    # print(test_data)
    for noun in range(100):
        for verb in range(100):
            data = test_data[:]
            data[1] = noun
            data[2] = verb
            evaluate_op_code(data)
            if data[0] == 19690720:
                print(f"{noun} {verb} {100 * noun + verb}")
                break