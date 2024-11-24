#include <iostream>
#include <cstring>

typedef struct {
    char subject_name[51];
    float gpa;
    char grade[2];
} SUBJECT;

int main()
{
    SUBJECT subject[20];
    float total_GPA = 0.0f;
    int total_time = 0;

    for (int i=0; i<20; i++)
    {
        std::cin >> subject[i].subject_name >> subject[i].gpa >> subject[i].grade;
    }

    for (int i=0; i<20; i++)
    {
        if (strcmp(subject[i].grade, "A+") == 0)
        {
            total_GPA += subject[i].gpa * 4.5;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "A0") == 0)
        {
            total_GPA += subject[i].gpa * 4.0;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "B+") == 0)
        {
            total_GPA += subject[i].gpa * 3.5;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "B0") == 0)
        {
            total_GPA += subject[i].gpa * 3.0;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "C+") == 0)
        {
            total_GPA += subject[i].gpa * 2.5;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "C0") == 0)
        {
            total_GPA += subject[i].gpa * 2.0;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "D+") == 0)
        {
            total_GPA += subject[i].gpa * 1.5;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "D0") == 0)
        {
            total_GPA += subject[i].gpa * 1.0;
            total_time += subject[i].gpa;
        }
        else if (strcmp(subject[i].grade, "F") == 0)
        {
            total_GPA += subject[i].gpa * 0.0;
            total_time += subject[i].gpa;
        }
    }

    std::cout << total_GPA / total_time;
}