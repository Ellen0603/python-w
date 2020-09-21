#
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])



# list = [12,48,34,23,89,19]
# list.sort(reverse=False)
# print(list)


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()







import random

#指定长度和内容的随机字符串
def string():
    str = random.choices("0123456789abcdefgsxcdeljhg",k=6)
    # print(str)
    print("".join(str))
string()
#随机手机号
def phone():
    list = ["131","137","186","189","136"]
    first = random.choice(list)
    # print(first)
    str = random.choices("0123456789", k=8)
    second = "".join(str)
    # print(second)
    print(first + second)
phone()

#随机姓名
def name():
    L1 = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤"
    first = random.choice(L1)
    # print(first)
    L2 = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽"
    length = random.randint(1,2)
    random_str = random.choices(L2,k=length)
    second = "".join(random_str)
    # print(second)

    return first+second

print(name())




