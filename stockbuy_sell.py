a = [int(x) for x in input().split()]
n = len(a)
sol = {}
count = 0
if (n == 1):
	return
int i = 0
while (i < n - 1):
	while((i < n -1 ) and a[i + 1] <= a[i]):
		i+=1
	if( i == n - 1):
		break;
	b = []
	b.append(i+=1)		
    while ((i < n) and (a[i] >= a[i - 1]))
        i+=1;
 
    b.append = i-1;
    sol.add(b);
             
	count +=1        
 