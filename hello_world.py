# print("hello world")
# a="hello world"
# print(a)
# l=[1,2,2,5]
# print(l)
# l[1]=7
# print(l)
#
# t=(12,34,56)
# print(t)
#
#
# s={1,2,5,3,3,1,8}
# print(s)

# a=12
# b=2.3
# print(a+b)
#
# a="12"
# b=2.3
# print(int(a)+b)
# print(a+str(b))
#
#
# a=12
# b="2.3"
# print(a+float(b))
# print(str(a)+b)
#
# a=True
# b=False
# print(a+b)

#
# a = {"name":"echo","age":18}
# print(a)
# print(a["name"])
# a["name"]="ella"
# print(a)

# l = [1,2,2,3,4,5,1,8]
# print(tuple(l))
# print(set(l))
# print(str(l))
#
# t = (1,2,3,4,5,1,2,3)
# print(list(t))
# print(set(t))
# print(str(t))
#
# s = {1,2,3,8,7,6}
# print(list(s))
# print(tuple(s))
# print(str(s))
#
# a = "1238799"
# print(list(a))
# print(set(a))
# print(tuple(a))

# l = [1,2,3,"all"]
# t = (1,2,3,4)
# s ={1,2,3,4}
# d = {"name":"echo","age":18}
# print(1 in l)
# print(2 in t)
# print(3 in s)
# print("name" in d)
#
# a = 123
# b = 234
# print(a<b)
# print(a*2)
# print(str(a)*2)

# a = 10
# if a > 1:
#     print(a)
# else:
#     print(1)
#

# a = 11
# if a <= 1:
#     print(a+1)
# elif a <= 10:
#     print(a-1)
# elif a <= 20:
#     print(a-10)
# else:
#     print(a)

# for a in [1,2,3,4,5,6]:
#     # print(a)
#     print(a+1)

# print(list(range(1,9,2)))
# print(list(range(100,5,-5)))
# print(list(range(10,1,-1)))
# i = 1
# while i<10:
#     print(i)
#     i += 1

# i = 1
# while i<10:
#     i += 1
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
#     if i > 7:
#         break

# for i in range(1,10):
#     if i == 6:
#         pass
#     else:
#         print(i)

#
#
#
# def div(a,b):
#     if a <= b and a != 0:
#         print(b/a)
#     else:
#         print(a/b)
#
# div(10,20)
# div(20,10)
# div(25,23)


# def para():
#     for i in range(10):
#         print(i*2)
#
# para()
#
#
# def var(res):
#     l = [1,2,3,12,23,78]
#     return l
#
# result = var("")
# print(result)


# def var(a,b):
#     if a >= b:
#         c = a*b
#     else:
#         c = a+b
#     return c
#
# print(var(2,6))


# def v(a=2,b=4):
#     return a*b
# print(v(1,2))
#
# def l(a,b):
#     print(a)
#     print(b)
#     return a*b
#
# def log(func,*args,**kwargs):
#     print("first",args,kwargs)
#     print("second",func(*args,**kwargs))
# log(l,1,2)

#
# a=open("1.txt","w")
# a.write("hello world")
# a.close()
#
# f = isinstance("",int)
# print(f)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end="\t")
#     print()

# a = 10
# def abs():
#     global a
#     a = 20
# abs()
# print(a)

# s = "1234567890"
# print(s[:])
# print(s[1:])
# print(s[-1:])
# print(s[1:-1])
# print(s[2:-2])
# print(s[:-3])

# l = [1,2,3,4,5,6,7,8,9,0]
# print(l[0])
# print(l[1:2])
# print(l[1:-1])
# print(l[2:])

# line = " as,acho,echo,all  "
# print(line.strip())
# print(line.split(","))
# line = line.replace("acho","echo")
# print(line)
# line = line.split(',')
# print(line[1])

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(j,i,i*j),end="\t")
#     print()


# l = [1,2,3,4,5,6,7,9]
# l[:2]=0,9,8
# l.append(6)
# l.insert(2,9)
# l.pop(1)
# l.extend([10,20])
# l.remove(3)
# l.sort(reverse=True)
# print(l.index(7))
# print(l)
#
# d = {"name":"echo","age":18,"sex":"male"}
# d["name"]="ella"
# print(d)
# d.pop("sex")
# print(d)
# d2 = {"tel":"13178905643"}
# d.update(d2)
# print(d)
# print(dict(d,addr="shanghai"))
# d.clear()
# print(d)
# l = [12,2,3,32,78,19]

# for i in range(len(l)):
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
# import random
# l = [random.randint(1,2000) for b in range(1,3000)]
#
# for i in range(len(l)-1,0,-1):
#     for j in range(0,i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)









