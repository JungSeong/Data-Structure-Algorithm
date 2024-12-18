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

## 2751.cpp
배열의 사이즈가 1,000,000이 되자 Segmentation fault 에러가 떴음. 배열의 크기를 너무 크게 하면 안되는 것으로 보이며, <vector> 자료구조를 사용해야 하는 것으로 보인다.<br>
std::sort 자료구조의 경우 시간 복잡도가 **nlogn**이 된다.<br>
std::endl의 경우 줄 바꿈 뿐만 아니라 스트림의 버퍼를 비운는 Flush 작업도 수행하게 되는데, 이 때문에 시간이 더 소요되는 문제가 생긴다. 이는 **스트림을 통한 입출력**이 많은 경우 특히 문제가 도드라지게 된다.<br>
이 문제의 경우 시간 복잡도가 nlogn인 알고리즘으로 해결이 가능하다. 이 알고리즘의 구현도 한 번쯤 해봐야 할 지는? 잘 모그렜다.

## 10989.cpp
수의 범위가 작을 때에는 카운팅 정렬을 사용하는 것이 속도가 더 빠르다. (본 문제에서는 10,000보다 작거나 같은 자연수)<br>

