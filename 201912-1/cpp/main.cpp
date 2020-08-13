#include <cstdio>

using namespace std;

bool isJump(int n)
{
    if (n % 7 == 0)
    {
        return false;
    }

    for (int i = 1; n / i >= 1; i *= 10)
    {
        if ((n / i) % 10 == 7)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int total;
    scanf("%d", &total);

    int counts[4] = {0, 0, 0, 0};

    for (int i = 0; total > 0; i++)
    {
        if (isJump(i + 1))
        {
            total--;
        }
        else
        {
            counts[i % 4]++;
        }
    }

    for (int i = 0; i < 4; i++)
    {
        printf("%d\n", counts[i]);
    }

    return 0;
}