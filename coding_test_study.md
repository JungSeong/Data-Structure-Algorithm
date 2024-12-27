# 코딩 테스트 준비

내가 설계한 알고리즘이 모든 경우에 요구 조건을 정확히 수용하는지 증명, 시간과 메모리가 문제의 제한 내에 들어가는지 확인할 것<br>
문제를 풀 때마다 코드와 함께 나의 경험을 기록으로 남길 것. + 한 번에 맞추지 못 한 경우 오답 원인도 꼭 적을 것

## 정렬 알고리즘의 복잡도

시간 복잡도 : 수행 시간<br>
공간 복잡도 : 메모리 사용량

|정렬 알고리즘|공간 복잡도||시간 복잡도|| 
|----------|:---:|:---:|:---:|:---:|
||최악|최선|평균|최악|
|Bubble Sort|O(1)|O(n)|O(n^2)|O(n^2)|
|Heap Sort|O(1)|O(nlogn)|O(nlogn)|O(nlogn)|
|Insertion Sort|O(1)|O(n)|O(n^2)|O(n^2)|
|Merge Sort|O(n)|O(nlogn)|O(nlogn)|O(nlogn)|
|Quick Sort|O(logn)|O(nlogn)|O(nlogn)|O(n^2)|
|Selection Sort|O(1)|O(n^2)|O(n^2)|O(n^2)|
|Shell Sort|O(1)|O(n)|O(nlogn^2)|O(nlogn^2)|

## 자료 구조의 복잡도

| Data Structures     | Average Case         |                     |                     | Worst Case          |                      |                     |
|---------------------|----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|                     | Search              | Insert              | Delete              | Search              | Insert              | Delete              |
| Array               | O(n)                | N/A                 | N/A                 | O(n)                | N/A                 | N/A                 |
| Sorted Array        | O(log n)            | O(n)                | O(n)                | O(log n)            | O(n)                | O(n)                |
| Linked List         | O(n)                | O(1)                | O(1)                | O(n)                | O(1)                | O(1)                |
| Doubly Linked List  | O(n)                | O(1)                | O(1)                | O(n)                | O(1)                | O(1)                |
| Stack               | O(n)                | O(1)                | O(1)                | O(n)                | O(1)                | O(1)                |
| Hash Table          | O(1)                | O(1)                | O(1)                | O(n)                | O(n)                | O(n)                |
| Binary Search Tree  | O(log n)            | O(log n)            | O(log n)            | O(n)                | O(n)                | O(n)                |
| B-Tree              | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            |
| Red-Black Tree      | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            |
| AVL Tree            | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            | O(log n)            |

# 정렬

## 2751.cpp
배열의 사이즈가 1,000,000이 되자 Segmentation fault 에러가 떴음. 배열의 크기를 너무 크게 하면 안되는 것으로 보이며, <vector> 자료구조를 사용해야 하는 것으로 보인다.<br>
std::sort 자료구조의 경우 시간 복잡도가 **nlogn**이 된다.<br>
std::endl의 경우 줄 바꿈 뿐만 아니라 스트림의 버퍼를 비운는 Flush 작업도 수행하게 되는데, 이 때문에 시간이 더 소요되는 문제가 생긴다. 이는 **스트림을 통한 입출력**이 많은 경우 특히 문제가 도드라지게 된다.<br>
이 문제의 경우 시간 복잡도가 nlogn인 알고리즘으로 해결이 가능하다. 이 알고리즘의 구현도 한 번쯤 해봐야 할 지는? 잘 모그렜다.

## 10989.cpp
수의 범위가 작을 때에는 카운팅 정렬을 사용하는 것이 속도가 더 빠르다. (본 문제에서는 10,000보다 작거나 같은 자연수)<br>

## 1427.cpp
문자 -> 정수로 변환 이후 sort 하는 간단한 문제<br>
문자열의 길이 : num.length(), 벡터의 크기 : v.size() 로 구한다<br>
문자를 숫자로 바꾸기 : '문자' - '0'을 하면 된다.<br>
내림차순으로 정렬 : compare() 함수 구현 후 sort(v.begin(), v.end(), compare)로 인자로 넣기

## 11650.cpp & 11651.cpp
2차원 배열을 정렬하기 위해서는 vector을 사용해야 한다.<br>
pair 클래스 : 2차원 좌표 저장에 유용하게 사용됨, #include <utility>를 통해 불러올 수 있음<br>

생성 : pair <type1, type2> pv<br>
초기화 : make_pair(pv_x, pv_2)<br>

인자의 첫 번째 값 : pv_x.first<br>
인자의 두 번째 값 : pv_x.second<br>

오름차순 정렬은 기본, sort(pv.begin(), pv.end()) 하면 된다<br>
내림차순 정렬을 원하면 sort(pv.begin(), pv.end(), greater<pair<int, int>>()) 로 선언

bool cmp(pair<int, int> a, pair<int, int> b)
{
    if (a.second != b.second) // y 좌표가 다르면
    {
        return a.second < b.second; // y 좌표를 기준으로 오름차순 정렬
    }
    else
    {
        return a.first < b.first; // x 좌표를 기준으로 오름차순 정렬
    }
}

## 1181.cpp

문자열을 길이가 짧은 것부터, 길이가 같다면 사전 순으로 정렬하는 방법

bool cmp (string str1, string str2)
{
    if (str1.length() != str2.length())
    {
        return str1.length() < str2.length(); // 문자열의 길이가 다르면, 문자열의 길이를 기준으로 오름차순 정렬 한다.
    }
    else
    {
        return str1 < str2; // 문자열의 길이가 같으면, 벡터를 사전 순서대로 정렬 한다.
    }
}

std::unique -> algorithm 헤더에 존재, 배열에서 중복되지 않는 원소들을 앞에서부터 채워나가되,중복되는 요소는 그 이후로 존재하게끔 한다. 이후 새로운 끝 위치 (=중복된 원소들이 있는 첫 위치)를 반환하게 된다.
vector::erase -> vector에서 특정 원소들을 삭제하는 함수

vec.erase(std::unique(vec.begin(), vec.end()), vec.end());