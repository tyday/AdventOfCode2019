import os


def get_fuel_requirement(module_mass):
    module_mass = int(module_mass)
    fuel_required = module_mass//3 -2
    return fuel_required

def calculate_fuel_fuel(module_mass):
    if get_fuel_requirement(module_mass) <= 0:
        return 0
    else:
        fuel_needed = get_fuel_requirement(module_mass)
        return fuel_needed + calculate_fuel_fuel(fuel_needed)

if __name__=='__main__':
    data = []
    fileName = os.path.join(os.getcwd(), 'Day1/input.txt')
    with open(fileName, "r") as f:
        data = f.read().strip().split('\n')

    total_fuel_required = [get_fuel_requirement(module) for module in data]
    print(sum(total_fuel_required))

    total_fuel_required_with_fuel = [calculate_fuel_fuel(module) for module in data]
    print(sum(total_fuel_required_with_fuel))