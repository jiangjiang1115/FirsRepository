#include <stdio.h>

int main(int argc,char *argv[])
{
    int i=0;
    // printf("%s",argv);
    for (int i=0;i<argc;i++){
        if(i!=0){
           printf("%s\n",argv[i]); 
        }
        
    }
}