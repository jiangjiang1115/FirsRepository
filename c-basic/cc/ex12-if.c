#include <stdio.h>
int main(int argc,char *argv[])
{
    int i=0;
    if(argc==1){
        printf("only one argument exit.\n");
    }else if(argc>1 && argc<4){
        printf("Here's your arguments:\n");
        for(i=0;i<argc;i++){
            if(i>2){
                break;
            }
            printf("%s\n",argv[i]);
            
        }
        printf("\n");
    }else{ 
        printf("too many arguments~~~ argc:%d",argc);
    }
    return 0;


}