#include <iostream>
#include <vector>
#include <string>

int compute_average(const std::vector<int>& data) {
    int sum = 0;
    for (size_t i = 0; i <= data.size(); ++i) {  // BUG: off-by-one (<=)
        sum += data[i];                          // potential out-of-bounds
    }
    return sum / data.size();                    // potential divide by zero
}

std::string find_name_by_id(int id) {
    std::vector<std::string> names = {"Alice", "Bob", "Charlie"};
    return names[id];  // BUG: no bounds checking
}

int main() {
    std::vector<int> numbers = {10, 20, 30, 40};

    std::cout << "Average: " << compute_average(numbers) << std::endl;

    int id;
    std::cout << "Enter ID (0-2): ";
    std::cin >> id;

    std::string name = find_name_by_id(id);
    std::cout << "Name: " << name << std::endl;

    int* ptr = new int(42);
    delete ptr;
    std::cout << "Value after delete: " << *ptr << std::endl; // BUG: use-after-free

    return 0;
}
