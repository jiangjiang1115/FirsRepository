#include <stdio.h>
int main()
{
    // 计算时间差
    // 输入小时，分钟数
    // int h1,m1;
    // int h2,m2;
    // scanf("%d %d",&h1,&m1);
    // scanf("%d %d",&h2,&m2);
    // int num=(h2*60+m2)-(h1*60+m1);
    // int ih=num/60;
    // int im=num%60;
    // printf("%d %d",ih,im);

    // 用if语句，进行借位运算
    int h1,m1;
    int h2,m2;
    scanf("%d %d",&h1,&m1);
    scanf("%d %d",&h2,&m2);
    int ih;
    int im;
    // my方式
    // if(m2<m1)
    // {
    //     h2-=1;
    //     m2+=60;
    //     ih=h2-h1;
    //     im=m2-m1;
    //        printf("时间差为%d时%d分",ih,im);
    // }else{
    //     ih=h2-h1;
    //     im=m2-m1;
    //     printf("%d时%d分",ih,im);
    // }
    
    // 翁方式
    ih=h2-h1;
    im=m2-m1;
    if(m2<0)
    {
        im+=60;
        ih--;
    }

}