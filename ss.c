#include<stdio.h>
int main(){
	char s[20]="ans is";
	s[8]='B';
	for (int i=0;i<20;i++)
	{
		printf("%c\n", s[i]);
	}
	printf("%s\n", s);
}