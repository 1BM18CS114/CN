#include<stdio.h>
#include<stdlib.h>
#include<string.h>



char g[]="10001000000100001",p[50],c[50];
int n1,n2;

void xor()
{
	int i;
	for(i=0;i<n1;i++)
	{
		if(c[i]==g[i])
		{
			c[i]='0';
		}
		else
		{
			c[i]='1';
		}
	}
}

void crc()
{
	int i,count;
	for(count=0;count<n1;count++)
	{
		c[count]=p[count];
	}
	do
	{
		 if(c[0]=='1')
		 {
			xor();
		 }
		 for(i=0;i<n1-1;i++)
		 {
			c[i]=c[i+1];
		 }
		 c[i]=p[count++];
	 }while(count<n2+n1);
 }

int main()
{
	int i;
	printf("Enter code to be transmitted\n");
	scanf("%s",p);
	n1=strlen(g);
	n2=strlen(p);
	for(i=n2;i<n2+n1;i++)
	{
		p[i]='0';
	}
	crc();
	printf("Checksum(Remainder) : %s\n",p);
	printf("Current code(Generating polynomial) : %s\n",g);
	for(i=n2;i<n2+n1;i++)
	{
		p[i]=c[i-n2];
	}
	printf("Transmitted code(Codeword) : %s\n",p);
	



	printf("Enter the Code you recieved to check for errors\n");
	scanf("%s",p);
	crc();
	for(i=0;i<strlen(c);i++)
	{
		if(c[i]=='1')
		{
			printf("Error found, there has been a change in code sent and code transmitted\n");
			exit(0);
		}
	}
	printf("No error, Well done\n");
    return 1;
}
