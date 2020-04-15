# _*_ coding: UTF-8 _*_
print"100-200间的素数为:"
count = 0  ##统计素数的个数
for i in range(101,201):
    a=2
    while a<i:
        if i%a==0:break
        else:a=a+1
    if a==i:
        print i
        count=count+1
print "素数的总数为:",count
