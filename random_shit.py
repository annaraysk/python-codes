n=int(input())
l=list(map(int,input().split()))
s=set(l)
m=max(s)
ans=sum(s)
for i in range(m+1,m+n-len(s)+1):
	ans+=i
print(ans)