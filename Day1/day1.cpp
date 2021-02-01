#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int get_fuel_requirement(int module_mass);
int calculate_fuel_fuel(int module_mass);

int main() {
    std::fstream input_file;
    std::vector <int> modules;

    // Populate modules with values from input.txt
    input_file.open("input.txt", std::ios::in);
    if (!input_file){
        std::cout << "No file found.\n";
    } else {
        std::string line;
        while (getline(input_file, line)){
            modules.push_back(std::stoi(line));
        }
    }
    // int fr = get_fuel_requirement(1969);
    // std::cout << fr << std::endl;
    int part_one_weight {0};
    for (int i: modules){
        part_one_weight += get_fuel_requirement(i);
    }
    std::cout << "Part one:\n";
    std::cout << part_one_weight << std::endl;

    int part_two_weight {0};
    for (int i: modules){
        part_two_weight += calculate_fuel_fuel(i);
    }
    std::cout << "Part two:\n";
    std::cout << part_two_weight << std::endl;
}


int get_fuel_requirement(int module_mass) {
    int fuel_required {0};
    fuel_required = module_mass/3 -2;
    return fuel_required;
}

// def calculate_fuel_fuel(module_mass):
//     if get_fuel_requirement(module_mass) <= 0:
//         return 0
//     else:
//         fuel_needed = get_fuel_requirement(module_mass)
//         return fuel_needed + calculate_fuel_fuel(fuel_needed)
int calculate_fuel_fuel(int module_mass){
    if (get_fuel_requirement(module_mass) <= 0){
        return 0;
    }
    else {
        int fuel_needed = get_fuel_requirement(module_mass);
        return fuel_needed + calculate_fuel_fuel(fuel_needed);
    }
}