#include <cstdio>

using namespace std;

int num1, num2;
int appleTotal = 0;
int maxIndex = 0;
int maxNum = 0;

int main()
{
    scanf("%d %d", &num1, &num2);

    for (int i = 0; i < num1; i++)
    {
        int appleNum;
        scanf("%d", &appleNum);

        int delCount = 0;
        for (int m = 0; m < num2; m++)
        {
            int delNum;
            scanf("%d", &delNum);
            delCount += delNum;
        }
        appleTotal += appleNum + delCount;
        if (delCount < maxNum)
        {
            maxIndex = i;
            maxNum = delCount;
        }
    }

    printf("%d %d %d\n", appleTotal, maxIndex + 1, -maxNum);

    return 0;
}