import Day2

def test_opcAdd():
    test_data = [1,9,10,3,2,3,11,0,99,30,40,50]
    Day2.opcAdd(test_data, 0)
    assert test_data == [1,9,10,70,2,3,11,0,99,30,40,50]

def test_opcMultiply():
    test_data = [2,3,0,3,99]
    Day2.opcMultiply(test_data, 0)
    assert test_data == [2,3,0,6,99]

def test_evaluate_op_code():
    data = [
        [[1,0,0,0,99], [2,0,0,0,99]],
        [[2,3,0,3,99], [2,3,0,6,99]],
        [[2,4,4,5,99,0], [2,4,4,5,99,9801]],
        [[1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]]
        ]
    for item in data:
        Day2.evaluate_op_code(item[0])
        assert item[0] == item[1]