class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, point):
        self.x = self.x + point.x
        self.y = self.y + point.y
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def value(self):
        return (self.x,self.y)

MOVES = {
    'U': Point(0,1),
    'D': Point(0,-1),
    'L': Point(-1,0),
    'R': Point(1,0)
}
def create_point_list(data):
    points_dictionary = {}
    points = set()
    position = Point(0,0)
    steps = 0
    for move in data:
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            steps += 1
            position.__add__(MOVES[direction])
            points.add(position.value())
            if position.value() not in points_dictionary:
                points_dictionary[position.value()] = steps
    return points, points_dictionary

def get_manhattan_distance(intersections):
    shortest_distance = None
    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if shortest_distance is None:
            shortest_distance = distance
        elif distance < shortest_distance:
            shortest_distance = distance
    return shortest_distance

def get_shortest_signal_distance(intersections, dict1, dict2):
    shortest_distance = None
    for intersection in intersections:
        distance = dict1[intersection] + dict2[intersection]
        if shortest_distance is None:
             shortest_distance = distance
        elif shortest_distance > distance:
            shortest_distance = distance
    return shortest_distance       

if __name__ == '__main__':
    # line1 = ['R8','U5','L5','D3']
    # line2 = ['U7','R6','D4','L4']
    line1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    line2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

    # line1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
    # line2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')

    # set1 = create_point_list(line1)
    # set2 = create_point_list(line2)
    # intersections = set1.intersection(set2)
    # print(intersections)
    # print(get_manhattan_distance(intersections))

    line1 = []
    line2 = []
    with open('/home/pi/Programming/AdventOfCode/2019/Day04/input.txt', "r") as f:
        data = f.read()
        data = data.split('\n')
        line1 = data[0].split(',')
        line2 = data[1].split(',')
    set1, dict1 = create_point_list(line1)
    set2, dict2 = create_point_list(line2)
    intersections = set1.intersection(set2)
    print(intersections)
    print(get_manhattan_distance(intersections))

    print(get_shortest_signal_distance(intersections, dict1, dict2))
    