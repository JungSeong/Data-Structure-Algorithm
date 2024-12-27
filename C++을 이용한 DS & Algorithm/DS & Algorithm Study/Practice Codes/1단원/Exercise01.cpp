/* 
C++에서는 파일이나 콘솔의 입출력을 스트림을 통해 다룬다. (스트림 : 운영체제가 입력과 출력을 다루기 위해 가상으로 만들어 준 것)
스트림은 내부에 버퍼라는 임시 메모리 공간을 가진다. 버는 문자를 묶어서 한 번에 전달하여 전송 시간이 적게 걸린다.
 */

#include <iostream>
#include <sstream> 
#include <algorithm>

template <typename T>
class dynamic_array
{
    T* data;
    size_t n; // size_t : 어떤 타입의 사이즈든지 최대 사이즈를 보장한다.

    public:
        dynamic_array(int n)
        {
            this->n = n;
            data = new T[n];
        }

        dynamic_array(const dynamic_array<T>& other) // 복사 생성자의 선언
        {
            n = other.n;
            data = new T[n];

            for (int i=0; i<n; i++)
            {
                data[i] = other[i];
            }
        }

        // 멤버 데이터로의 접근을 위한 [] 연산자와 at()함수의 선언

        T& operator[](int index)
        {
            return data[index];
        }

        const T& operator[](int index) const
        {
            return data[index];
        }

        T& at(int index)
        {
            if (index < n)
            {
                return data[index];
            }
            throw "Index out of range";
        }

        size_t size() const
        {
            return n;
        }

        ~dynamic_array()
        {
            delete[] data;
        }
}