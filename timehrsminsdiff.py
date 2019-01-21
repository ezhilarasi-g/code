#ezhil
h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if h1>h2:
	if m1>m2:
		hrs=h1-h2
		mins=m1-m2
		print(hrs,mins)
	else:
		h1=h1-1
		m1=m1+60
		hrs=h1-h2
		mins=m1-m2
		print(hrs,mins)
elif h1<h2:
	if m1<m2:
		hrs=h2-h1
		mins=m2-m1
		print(hrs,mins)
	else:
		hrs=h2-h1
		mins=m1-m2
elif h1==h2:
	if m1==m2:
		hrs=h1-h2
		mins=m1-m2
		print(hrs,mins)
