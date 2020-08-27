#include<stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a[n];
	int ma=0;
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		if(a[i]>ma)
		{
			ma=a[i];
		}
	}
	int hashtable[ma];
	int added=0;
	int ans=0;
	for (int i=0;i<n;i++)
	{
		if(hashtable[a[i]-1]!=1){
			hashtable[a[i]-1]=1;
			ans+=a[i];
			added++;
		}
	}
	//printf("%d %d\n",ans,added );
	for(int i=0;i<n-added;i++)
	{
		ans+=++ma;
	}
	printf("%d\n",ans );
}