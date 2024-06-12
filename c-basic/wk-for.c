#include <stdio.h>
int main()
{
    // 正整数正序输出 ,判断程序是否正确，用边界值 7000输出0007
    // int n=7001;
    // int mask=1;
    // int x=n;
    // 判断是个几位数
    // do{
    //     n=n/10;
    //     mask*=10;
    // }while(n>9);
    // while(mask){
    //     // 从头取数字  1234/1000=1
    //     printf("%d ",x/mask);
    //     x%=mask;
    //     mask/=10;
    // }

    // 正整数构成逆序数字
    // 1、四位数/10，除3次后，余数为0， 10的3次方，可以取得四位数的第一位数，也可以取最后一位数
    // 2、不断乘10，不断+最后一位
    // int n=7000,t=0;
    // do{
    //     t=t*10+n%10;
    //     n/=10;
    // }while(n>0);
    // printf("%d",t);

    // 正整数正序输出
    // 1、用/10取出第一位数，用计数器得到/10的次方数
    // int n=1234;
    // int tmp=n;
    // int cnt=1;
    // do{
    //     tmp/=10;
    //     cnt*=10;
    // }while(tmp>9);
    // while(n>0){
    //     printf("%d",n/cnt);
    //     n%=cnt;
    //     cnt/=10;
    // }

    // 求最大公约数，辗转相除法：余数和除数的最大公约数
    // 1、不断将除数和余数作为被除数和除数
    // 2、除数为0时循环结束，被除数为最大公约数
    // int a=12,b=18;
    // int t;
    // while(b!=0){
    //     t=a%b;
    //     a=b;
    //     b=t;
    // }
    // printf("gcd=%d",a);

    // 给定最大为6的正整数，往后连续三个数字，用它们构成各个位数不相等的三位数，由小到大排列
    // 1、一个正整数，三层循环，最后判断是否互不相等
    // int n=2;
    // int cnt=0;
    // for(int i=n;i<=n+3;i++){
    //     for(int j=n;j<=n+3;j++){
    //         for(int k=n;k<=n+3;k++){
    //             if(i!=j&&i!=k&&j!=k){
    //                 printf("%d%d%d",i,j,k);
    //                 cnt++;
    //                 if(cnt==6){
    //                     printf("\n");
    //                     cnt=0;
    //                 }else{
    //                     printf(" ");
    //                 }
    //             }
    //         }
    //     }
    // }

    // 水仙花数，n位数 = 每位的n次幂相加 例如153=1^3+5^3+3^3  固定次数用for
    // 1、一个正整数n，得到n位数的区间，
    // 2、得到每一位上的数，循环累乘n-1次，每一位数的n次方相加
    // 3、判断是否是n区间内的数
    // int n = 2;
    // int cnt = n;
    // int first = 1;
    // while (--cnt)   //循环n-1次，得到最小n位数， 循环的次数，代入具体的数确定 ,
    // {
    //     first *= 10; // 算区间最小值
    // };
    // int i = first;
    // while (i < first * 10)  //遍历n位数的区间
    // {
    //     int k=i;//用来解析i
    //     int t;//用来存放每一位数
    //     int sum = 0;//每一位数的n次方，相加的总和
    //     do
    //     {
    //         t =k % 10;
    //         k/=10;
    //         int j = 0;
    //         int p = 1;
    //         while (j < n)   //循环n次
    //         {
    //             p *= t;
    //             j++;
    //         }
    //         sum += p;
    //     } while (k>0); //循环n次，取数字
    //     if(i==sum){
    //         printf("%d\n",i);
    //     }
    //    i++;
    // }

    // 九九乘法表  行列关系，i行j列
    // for(int i=1;i<10;i++){
    //     for(int j=1;j<=i;j++){
    //         printf("%dx%d=%d  ",j,i,i*j);
    //         if(i*j/10==0){
    //             printf(" ");
    //         }
    //     }
    //     printf("\n");
    // }

    // 求[M,N]区间，素数的个数和总和
    // int m=1,n=100;
    // int sum=0;
    // int cnt=0;
    // if(m==1)m++;    //1不是素数
    // for(int i=m;i<=n;i++){
    //     int isPrism=1;
    //     for(int j=2;j<i;j++){   //除小于自身的数
    //         if(i%j==0){
    //             isPrism=0;
    //             break;
    //         }
    //     }
    //     if(isPrism){
    //         sum+=i;
    //         cnt++;
    //         printf("%d ",i);
    //     }
    // }
    // printf("%d个素数，总和为%d",cnt,sum);



    // 水仙花数，for循环，n位数=每位n次方的总和
    // int n = 10;
    // int i = n;
    // int cnt = 1;
    // do
    // {
    //     i --;
    //     cnt *= 10;
    // } while (i > 1); // 循环次数的正确性
    // for (i = cnt; i < cnt * 10; i++)
    // { // 区间
    //     int k = i;
    //     int sum = 0;
    //     do
    //     {
    //         int p = 1;
    //         int j = 0;
    //         while (j < n)
    //         {
    //             p *= k % 10;
    //             j++;
    //         }
    //         k /= 10;
    //         sum+=p;
    //     }while(k>0); 
    //     if(i==sum){
    //         printf("%d\n",i);
    //     }
    // }


    // 前n项和，分子是前一项的分子+分母，分母是前一项的分子
    // int n=20;
    // double dividend=2,divisor=1;
    // double sum=0;
    // for(int i=1;i<=n;i++){
    //     int ch=0;
    //     sum+=dividend/divisor;
    //     ch=dividend;
    //     dividend+=divisor;  //分子=前一项分子+分母
    //     divisor=ch;  //分母=前一项分子
    // }
    // printf("sum=%.2f",sum);

    
    //求a+aa+aaa……n个a的和
    // int a=2,n=3;
    // int t=0;
    // int sum=0;
    // for(int i=0;i<n;i++){
    //     t=t*10+a;
    //     sum+=t;
    // }
    // printf("%d",sum);
    

    // 约分最简公式
    // int dividend=12,divisor=18;
    // int a=dividend,b=divisor;
    // int t;
    // while(b>0){
    //     t=a%b;
    //     a=b;
    //     b=t;
    // }
    // printf("%d/%d %d",dividend/a,divisor/a);

    // 强类型语言，sizeof()计算占多少字节，sizeof()括号内不做运算，只输出变量类型所占的内存大小
    // printf("%d\n",sizeof(1+1.0)); //8  整型和浮点数相加，转化为浮点型
    // printf("%d\n",sizeof(1.0)); //8 double  float占4字节
    // printf("%d\n",sizeof(int)); //4
    // printf("%d",sizeof(long));


    
} 