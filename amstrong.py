ab=int(input(""))
sum=0
temp=ab
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if ab==sum:
   print("yes")
else:
   print("no")
