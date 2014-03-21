/*c installer relased under GPL v3 by rohit (roit.shetty@gmail.com)*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main()
{
FILE *fp;
char str[100];
system(" chmod a+x main.py");
printf("Done \n ");
system("pwd>list");
fp=fopen("list","r");
system("clear");
if(fp==NULL)
{
printf("\nerror\n");
exit(0);	
}
fscanf(fp,"%s",str);
fclose(fp);
fp=fopen("Vipy.desktop","w");
fprintf(fp,"[Desktop Entry]\nName=Vipy\nComment=A brief description\nExec=%s/./main.py\nStartupNotify=true\nIcon=%s/hacker1.jpg\nTerminal=false\nType=Application\nName[en_IN]=Vipy",str,str);
fclose(fp);

system("cp Vipy.desktop Vipy1.desktop");
system("chmod a+x Vipy.desktop");
system("chmod a+x Vipy1.desktop");
system("mv Vipy.desktop ~/Desktop");
system("clear");
printf("file installed\n");
}

