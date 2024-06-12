#include <stdio.h>
int main(){
    int a1[5]={0};//设置列表长度（初始化列表长度）
    int i;
    int j;
    printf("\n--%d--%d--%d--%d--%d",a1[0],a1[1],a1[2],a1[3],a1[4],a1[5]);
    for(i=0;i<5;i++){
        int aa=i;
        printf("\n%d",aa);
        a1[i]=i;       
        // 将i赋值给下标对应的列表值，需确初始化列表长度
         //未初始化的数组元素内容是不确定的，可能包含任意值。
    }
    printf("\n--%d--%d--%d----%d--%d",a1[0],a1[1],a1[2],a1[3],a1[4],a1[5]);
    for(j=0;j<5;j++){
        printf("\n*%d-%d",j,a1[j]);
    }
    printf("\n--%d--%d--%d--%d--%d",a1[0],a1[1],a1[2],a1[3],a1[4],a1[5]);


     int argc=3;
    char *argv[]={"'1111'","'2222'","'3333'","'4444'"}; //列表用花括号,字符串用双引号
    //printf("----%s---\n",*argv); //输出argv[0]的值,不能在二维数组里直接输出所有的字符串
    char words[]={'a','b'};
    //printf("----%c---\n",*words);  //不能将列表里的多个单字符，作为字符串输出
    int num[]={1,2,3,4};
    printf("中文输出，abc");
    for(int i=0;i<argc;i++){
        // printf("\n%c",argv[i]); 
        printf("\n%s",argv[i]);
        printf("\n%c",words[i]);
        printf("\n%d",num[i]);
    }
}
