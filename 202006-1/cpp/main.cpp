#include <cstdio>
#include <cstring>

using namespace std;

struct Info
{
    int x;
    int y;
    char type[2];
};

struct Line
{
    int a;
    int b;
    int c;
};

Info infoList[1000];
Line lineList[1000];

int num1, num2;

char infoType[2];

int main()
{
    scanf("%d %d", &num1, &num2);

    for (int i = 0; i < num1; i++)
    {
        scanf("%d %d %s", &infoList[i].x, &infoList[i].y, &infoList[i].type[0]);
    }

    for (int i = 0; i < num2; i++)
    {
        scanf("%d %d %d", &lineList[i].a, &lineList[i].b, &lineList[i].c);
    }

    for (int i = 0; i < num2; i++)
    {
        char ok[] = "Yes";

        Line *line = &lineList[i];
        Info *firstInfo = &infoList[0];

        int firstRes = line->a + line->b * firstInfo->x + line->c * firstInfo->y;
        if (firstRes == 0)
        {
            strcpy(ok, "No");
        }
        else
        {
            if ((firstRes > 0 && firstInfo->type[0] == 'A') || (firstRes < 0 && firstInfo->type[0] != 'A'))
            {
                strcpy(infoType, "A");
            }
            else
            {
                strcpy(infoType, "B");
            }

            for (int m = 1; m < num1; m++)
            {
                Info *info = &infoList[m];
                int result = line->a + line->b * info->x + line->c * info->y;
                if (result == 0 || (result > 0 && info->type[0] != infoType[0]) || (result < 0 && info->type[0] == infoType[0]))
                {
                    strcpy(ok, "No");
                    break;
                }
            }
        }
        printf("%s\n", ok);
    }

    return 0;
}