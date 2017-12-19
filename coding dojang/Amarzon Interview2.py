log = [
'09:12:23 11:14:35',
'10:34:01 13:23:40',
'10:34:31 11:20:10'
]
user = "10:50:30"
come=[]
out=[]
n=0
for time in log:
	com,day= time.split(' ')
	come.append(com)
	out.append(day)
sec_sum=[]
for sec in come:
	h,m,s=map(int,sec.split(":"))
	sec_sum.append(str(h*60*60+m*60+s))
se_sum=[]
for se in out:
	h,m,s=map(int,se.split(":"))
	se_sum.append(str(h*60*60+m*60+s))
	
h,m,s=map(int,user.split(":"))
u_sum=str(h*60*60+m*60+s)

for i in range(len(sec_sum)):
	if int(sec_sum[i]) < int(u_sum) < int(se_sum[i]):
		n+=1
		

#print(sec_sum)
#print(se_sum)
#print(u_sum)
print(n)