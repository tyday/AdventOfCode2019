
stored_Data = None

def opcInput(data,i, params):
    inp  = input("Input the data: ")
    data[data[i+1]] = int(inp) # stored_Data
    return i + 2

def opcOutput(data,i,params):
    
    # stored_Data = data[data[i+1]]
    print("Output", data[data[i+1]])
    return i + 2

def opcAdd(data,i,params):
    # Adds
    x = data[i+1]
    if params[0] == 0: x = data[x]
    y = data[i+2]
    if params[1] == 0: y = data[y]
    z = data[i+3]
    if params[2] == 1:
        raise Exception("Add op codes shouldn't have a third parameter")
    data[z] = x + y
    return i + 4 # number of positions to move forward along op code

def opcMultiply(data, i, params):
    # Multiplies
    x = data[i+1]
    if params[0] == 0: 
        x = data[x]
    y = data[i+2]
    if params[1] == 0: 
        y = data[y]
    z = data[i+3]
    if params[2] == 1:
        raise Exception("Add op codes shouldn't have a third parameter")
    data[z] = x * y
    return i + 4

def opcStop(data, i, params):
    return 0

OPCODES = {
    1: opcAdd,
    2: opcMultiply,
    3: opcInput,
    4: opcOutput,
    99: opcStop
}
def split_op_code(code):
    instruction = code %100
    param3 = code // 10000
    code = code % 10000
    param2 = code // 1000
    code = code % 1000
    param1 = code // 100
    return (instruction, (param1, param2, param3))

def evaluate_op_code(data):
    i = 0
    while i < len(data):
        instruction, params = split_op_code(data[i])
        result = OPCODES[instruction](data, i, params)
        if result == 0:
            break
        else:
            i = result

if __name__ == '__main__':
    test_data = [1,1,1,4,99,5,6,0,99]
    evaluate_op_code(test_data)
    print(test_data)

    test_data = []
    with open("/home/pi/Programming/AdventOfCode/2019/Day02/input.txt", "r") as f:
        test_data = f.read().split(',')
        test_data = [int(item) for item in test_data]
    test_data[1] = 12
    test_data[2] = 2
    evaluate_op_code(test_data)
    print(test_data)
    # for noun in range(100):
    #     for verb in range(100):
    #         data = test_data[:]
    #         data[1] = noun
    #         data[2] = verb
    #         evaluate_op_code(data)
    #         if data[0] == 19690720:
    #             print(f"{noun} {verb} {100 * noun + verb}")
    #             break
    data = [1002,4,3,4,33]
    evaluate_op_code(data)
    print(data)