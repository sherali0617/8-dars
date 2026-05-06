import os 
os.system("cls")

# def func1(list1):
#     list2=[]
#     list3=[]
#     for i in list1:
#         if i==0:
#             list2.append(i)
#         else:
#             list3.append(i)
#     print(list3+list2)


# func1(list1=[3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1])


# 2.m
# def func1(list1):
#     list2=[]
#     for i in list1:
#         a=list1.count(i)
#         if a<=2 and i not in list2:
#             list2.append(i)
#     print(list2)

# func1(list1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])



# 3.m
# def func1(list1,list2):
#     list3=[]
#     min_len=min(len(list1),len(list2))
#     for i in range(min_len):
#         list3.append(list1[i])
#         list3.append(list2[i])
#     if len(list1)>len(list2):
#         for i in range(min_len,len(list1)):
#             list3.append(list1[i])
#     else:
#         for i in range(min_len,len(list2)):
#             list3.append(list2[i])
#     print(list3)
        
# func1(list1=[1, 2, 3, 4, 5],list2=[11, 22, 33,12,1,13,16])


# 4.m
# def func1(a,b):
#     dublikat=[]
#     for i in a:
#         if i in b and i not in dublikat:
#             dublikat.append(i)
#     print(dublikat)
            
# func1(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


# 5.m
# def func1(a):
#     list1=[]
#     list2=[]
#     for i in range(a):
#         b=int(input(f"{i+1}-son:"))
#         list1.append(b)
#     for i in list1:
#         if list1.count(i)>=2 and i not in list2:
#             list2.append(i)
#     print(list2)

# a=int(input("Son kiriting:"))
# func1(a)


# 6.m
# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=list(map(lambda n:n*n,list1))
# print(list2)


# 7.m
def func1(a):
    dict1={}
    for i in a:
        dict1[i]=dict1.get(i,0)+1
    return dict1



a=input("Soz kiriting:")
b=func1(a)
print(b)