#include <stdio.h>
int main()
{
    // switch
    int type;
    scanf("%d",&type);
    switch (type){  //type必须为整型
        case 1:
            printf("1");
            break;
        case 2:
            printf("2");
            break;
        default:
            printf("大于1，2");
            break;
    }
}