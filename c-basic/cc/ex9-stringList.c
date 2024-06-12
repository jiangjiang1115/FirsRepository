#include <stdio.h>
int main()
{
    int number[4]={0};
    char name[]={'a','2'};
    //未定义的部分系统默认为 0
    printf("numbers:%d %d %d %d\n,------%ld\n",
            number[0],number[1],number[2],number[3],sizeof(number)/sizeof(int));
    
    //未定义的部分系统默认为'\0',打印出来是空格,有效长度为1，以'\0'为数组结束标志
    printf("name each: %c %c %c %c----\n,------%ld\n",
            name[0],name[1],name[2],name[3],sizeof(name)/sizeof(char));
    
    printf("name:%S\n",name);

    number[0]=1;
    number[1]='a'; //%d输出 97
    number[2]=3;
    number[3]=4;

    name[0]='x';
    name[1]='b';
    name[2]='b';
    name[3]='a'; //'\0'方便计算有效长度,但此处字符串长度仍与定义长度一致

    printf("numbers:%d %d %d %d,------%ld\n",
            number[0],number[1],number[2],number[3],sizeof(number)/sizeof(int));
    char ss1[]={'a'};
    ss1[0]='b';ss1[1]='b';ss1[2]='c';
    printf("name each: %c %c %c %c----------%d\n",
            name[0],name[1],name[2],name[3],sizeof(ss1));//sizeof计算的长度为初始化字符串的大小
    printf("%ld",sizeof(name));
    printf("print name like a string --%s\n",name); //%s输出完整的字符数组

    //常用创建字符串方法       --Segmentation fault--越界访问
    char *another="something";
    printf("another:%s;size:%ld\n",another,sizeof(another));
    printf("another each: %c %C %C ",another[0],another[2],another[8]);

    printf("----------------\n");
    char str[]={'b'}; //定义一个数组，要先初始化一个元素
    str[0]='a';
    
    char ss[]="helloworld";
    printf("%s,%ld",ss,sizeof(ss));
    char s1[]={"helloworld"};
    printf("\n%ld,%d,%ld",sizeof(s1)/sizeof(s1[0]),strlen(s1),sizeof(name)/sizeof(name[0]));
    char s2[]={};
    s2[0]='a';

    
}