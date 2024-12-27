# 자료 구조

자료 구조를 제대로 이해하고 있으면 응용 프로그램의 성능 향상, 유지 보수, 가독성..등등의 관점에서 유리하게 데이터 관리를 할 수 있다.<br>
선형 자료구조는 크게 연속된 구조, 연결된 구조로 분류할 수 있다.

## 연속된 자료 구조, 연결된 자료 구조

**연속된 자료 구조** : 모든 원소를 단일 메모리 청크에 저장 (메모리 청크 = 연속된 메모리 덩어리)<br>

C++에서 동적 메모리 배열 할당

~~~
int arr* = new int[size];
~~~

배열 같은 연속된 자료 구조에서는 각 원소가 서로 인접해 있기 때문에 하나의 원소에 접근할 때 옆에 있는 원소 몇 개도 함께 **캐시**로 가져온다. (캐시 지역성)

**연결된 자료 구조** : **노드**라고 하는 여러 개의 메모리 청크에 데이터를 저장, 이 경우 서로 다른 메모리 위치에 데이터가 저장된다.<br>

![연결된 자료 구조](Datas/Linked_Structure.jpg)

새로운 원소를 삽입하려면 일단 새로운 노드를 생성하고, 각 노드의 link(next) 포인터를 수정하면 된다.

연결 리스트에서는 캐시 지역성은 기대할 수 없다. 즉, 현재 노드가 가르키는 다음 노드에 직접 방문하지 않고 다음 원소를 캐시로 가져올 수는 없다. 모든 원소를 차례대로 방문하는 작업은 이론적으로 같은 시간 복잡도를 가지지만, 실제로는 **연결 리스트의 성능이 조금 떨어진다.**

C 스타일 배열의 경우 메모리 할당과 해제를 수동으로 처리해야 하고, 해제하지 못하면 메모리 릭이 발생할 수도 있다.<br>
-> **C++의 경우 std::array, std::vector, std::list 같은 다양한 자료 구조 클래스를 제공한다.**

## std::array

~~~
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
}

void print(std::array<int, 5> arr)
{
    for (auto ele : arr) // 배열의 원소에 차례대로 접근할 수 있다.
        std::cout << ele << ", ";
}
~~~

배열의 크기를 탬플릿으로 전달하기 :

~~~
template <size_t N>
void print(const std::array<int, N>& arr);
~~~

std::array는 begin()과 end()라는 이름의 멤버 함수를 제공한다. (각각 가장 첫 번째 원소, 가장 마지막 원소의 위치를 반환)

~~~
void print(std::array<int, 5> arr)
{
    for (auto it = arr.begin(); it != arr.end(); it++)
    {
        std::cout << (*it) << ' ';
    }
}
~~~

std::array.front() : 배열의 첫 번째 원소에 대한 참조를 반환<br>
std::array.back() : 배열의 마지막 원소에 대한 참조를 반환<br>
std::array.data() : 배열의 객체 내부에서 실제 데이터 메모리 버퍼를 가리키는 포인터를 반환