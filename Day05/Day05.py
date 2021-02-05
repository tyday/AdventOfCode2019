import sys
sys.path.append("/home/pi/Programming/AdventOfCode/2019/")
import intcode

test_data = []
with open("/home/pi/Programming/AdventOfCode/2019/Day05/input.txt", "r") as f:
        test_data = f.read().split(',')
        test_data = [int(item) for item in test_data]
# print(test_data)
intcode.stored_Data = 1
intcode.evaluate_op_code(test_data)