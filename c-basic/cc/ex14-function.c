#include <stdio.h>
#include <ctype.h> //头文件，用来访问函数（isalpa和isblank）
#include <string.h>

// 前向声明，不在main函数定义但有使用，预先声明要在程序中用的函数，实际还未定义
int can_print_it(char ch);
void print_letters(char arg[]);

void print_arguments(int argc, char *argv[])
{
    int i = 0;
    for (i = 0; i < argc; i++)
    {
        print_letters(argv[i]); // 命令行参数
    }
}

void print_letters(char arg[])
{
    int i = 0;
    for (i = 0; arg[i] != '\0'; i++)
    {
        char ch = arg[i]; // 命令行参数的单字符

        if (can_print_it(ch))
        {
            printf("'%c'==%d-->%d", ch, ch, (int)ch); // 输出空格或字母，以及类型转成整型后的数字
        }
    }

    printf("\n");
}

int can_print_it(char ch)
{
    return isalpha(ch) || isblank(ch); // 返回0或1

    // isalpha()用于判断字符是否未字母，是返回非0，否返回0；
    //  isblank()用来判断一个字符是否为TAB或者空格，是返回非0，否返回0；
}

int main(int argc, char *argv[])
{
    // print_arguments(argc, argv);
    print_alphabet(argc, argv);
    return 0;
}

// 在一个函数内，将列表的字母单个输出
