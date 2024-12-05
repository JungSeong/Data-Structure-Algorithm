#include <iostream>

int main()
{
    int N;
    std::cin >> N;

   int* arr_x = new int[N];
   int* arr_y = new int[N];

   for (int i=0; i<N; i++)
   {
        std::cin >> arr_x[i] >> arr_y[i];
   }

   int min_x = arr_x[0], max_x = arr_x[0], min_y = arr_y[0], max_y = arr_y[0];

   for (int i=0; i<N; i++)
   {
        if (min_x > arr_x[i])
        {
            min_x = arr_x[i];
        }

        if (max_x < arr_x[i])
        {
            max_x = arr_x[i];
        }

        if (min_y > arr_y[i])
        {
            min_y = arr_y[i];
        }

        if (max_y < arr_y[i])
        {
            max_y = arr_y[i];
        }
   }

   std::cout << (max_x - min_x) * (max_y - min_y);
}