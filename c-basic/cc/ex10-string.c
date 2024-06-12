#include <stdio.h>

int main(int argc,char *argv[])
{
    int i=0;
 
    for(i=0;i<argc;i++){  //赋值，判断，累加
        printf("arg %d:%s\n",i,argv[i]); //命令行输入的值，0下标为可执行文件名字
    }

    printf("string size(list?):%ld",sizeof(argv[1]));
    char *states[]={   //二维数组
        "aaa","bbb","ccc","ddd"
    };

    states[0]=NULL;
    int num_states=4;
    for(i=0;i<num_states;i++){
        printf("state %d:%s\n",i,states[i]); 
    }

    int num1=0;
    int num2=0;
    // printf("输入两个操作数>");
    // scanf("%d %d",&num1,&num2);
    // printf("%d ",num1+num2);
     
    //直接打印数组元素
}