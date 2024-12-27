#include <iostream>
#include <array>

void print(std::array<int, 5> arr);

int main()
{
    std::array<int, 10> arr1;

    arr1[0] = 1;
    std::cout << arr1[0] << std::endl;

    std::array<int, 4> arr2 = {1, 2, 3, 4};
    
    for (int i=0; i<arr2.size(); i++)
    {
        std::cout << arr2[i] << " ";
    }
    std::cout << std::endl;

    std::array<int, 4> arr3 = {1, 2, 3, 4};

    try
    {
        std::cout << arr3.at(3) << std::endl;
        std::cout << arr3.at(4) << std::endl;
    }
    catch (const std::out_of_range& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    std::array<int, 5> arr4 = {1, 2, 3, 4, 5};
    print(arr4);

    std::array<int, 5> arr5 = {1, 2, 3, 4, 5};
    std::cout << arr5.front() << ' ' << arr5.back() << ' ' << *(arr5.data() + 1) << std::endl;
}

// void print(std::array<int, 5> arr)
// {
//     for (auto ele : arr) // 배열의 원소에 차례대로 접근할 수 있다.
//         std::cout << ele << ", ";
// }

void print(std::array<int, 5> arr)
{
    for (auto it = arr.begin(); it != arr.end(); it++)
    {
        std::cout << (*it) << ' ';
    }
    std::cout << std::endl;
}