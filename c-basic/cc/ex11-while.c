#include <stdio.h>

int main(int argv,char *argc[])
{
    int i=10;
    while(i>0){
        //int i=0;//局部变量
        printf("%d\n",i);
        i--;//优先对局部变量进行计算，导致无限循环
    }
    i=0;
    while(i<argv){
        printf("arg %d:%s %d\n",i,argc[i],argv);
        i++;
    }

    char *states[]={
        "aaa","bbb","ccc" //二维数组
    };

    int num=3;
    i=0;
    // while(i<num){
    //     states[i]=argc[i];
    //     printf("states %d:%s\n",i,states[i]);
    //     i++;
    // }
    
    return 0;
}