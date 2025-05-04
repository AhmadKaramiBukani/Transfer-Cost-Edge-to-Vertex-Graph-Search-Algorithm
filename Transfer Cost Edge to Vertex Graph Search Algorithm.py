
#/////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////
#/////      CopyRight: Ahmad Karmi Bukani     احمد کرمی بوکانی    //////
#/////          Rojhalat Kurdistan  2025          روژهلات کوردستان     ///////
#//////////////////////////////////////////////////////////////////////////////////


import random
from itertools import permutations 
List=[]
List2=[]
List3=[]
List4=[]
List5=[]
ListFinal=[]
MyPathList=[]
MyPathList2=[]
PathSum=""
Sum=0
AllListCost=[]
PathListCost=[]

print()
print()
print()
print()
print("------------------------------------------------------------------------------------------")
print("-------------------------  Ahmad Karami Bukani   -----------------------------------")
print("Welcome To \"Transfer Cost Edge to Vertex Graph\" Search Algorithm")
print("------------------------------------------------------------------------------------------")
print()
print()


print("-----------------------------------")


s=ord(input("Please Enter a chracter A-Z for Start, example = B : "))
e=ord(input("Please Enter a chracter A-Z for End , example = H : "))+1
print('----------------------------------')
for i in range(s,e):
    List.append(chr(i))
    List2.append(random.randint(1,20))

print()
print("List = ",List)
print()
print("List2 = ",List2)
print()


Select=input("Please Select For Make Graph via Permutations or Random, Enter Press Key 1 or Key 2 : ")

print()
print('--------------   Processing   ---------------')
print()

if Select=="1" :
   Tuple=()
   Tuple = permutations(List)
   List3=list(Tuple)


if Select=="2":
     d=e-s
     for v in range(0,2**d*d**2):
       exec("ss=''")
       for r in range(0,d):
            exec("a = chr(random.randint(s,e-1))")
            exec("ss=ss+a")
       List3.append(list(ss))


print("List3 = \n",List3)
print('--------------   Done   ---------------')       
print()
print()
print()
print()
print()
print()
split=int(input("Please Enter a number for Splite List (1-length(List)) , example = 3 : "))

print()
print('--------------   Processing   ---------------')
print()

for i in range(0,int(len(List3)//split)):
     List4.append(List3[i])

print("List4 = \n",List4)
print('--------------   Done   ---------------')
print()
print()
print()
print()
print()
print()
print('--------------   Processing   ---------------')
print()

for j in range(0,len(List4)):
     List5_2=list(List4[j])
     for i in range(0,len(List4)):
         List5=list(List4[i])
         List5.reverse()
         List6=List5.copy()
         if List5_2==List6 :
             ListFinal.append(List4[i])
             ListFinal.append(List6)


ListFinal_help=list()          
EmptyTuple=tuple()

for i in ListFinal:
    if type(i) != type(EmptyTuple):
      ListFinal_help.append(i)

ListFinal.clear()
ListFinal=ListFinal_help.copy()

print("List Final =\n", ListFinal)

print('--------------   Done   ---------------')   
print()
print()
print()
print()
print()
print()
str1="Please enter start point (example : B) : "
Start=input(str1)
str2="Please enter end point (example : H) : "
End=input(str2)

print()
print('--------------   Processing   ---------------')
print()

for j in range(0,e-s):
    for i in range(0,len(ListFinal)):
         if Start==ListFinal[i][j] or End==ListFinal[i][j]:
             MyPathList.append(ListFinal[i])
             



print("My Path List = ",MyPathList)
print('--------------   Done   ---------------')   
print()
print()
print()
print()
print()
print()
print('--------------   Processing   ---------------')



for i in MyPathList:
    for j in range(0,e-s):
         if Start==i[j]:
            for k in range(j,e-s):
                 if i[k]==End:
                     MyPathList2.append(i)
                     break
            break 


print("My Path List 2 = ",MyPathList2)



Run=False
for i in MyPathList2:
     Sum=0
     PathSum=""
     Run=False
     for j in range(0,e-s):
        if i[j]==Start and Run==False :
             Run=True
             for k in range(0,e-s):
                 if i[j]==List[k]:
                        """Sum=Sum+List2[k]"""
                        PathSum=PathSum+i[j]+" -> "
                        break
                    
        elif i[j]!=End and Run :
              for k in range(0,e-s):
                 if i[j]==List[k]:
                        Sum=Sum+List2[k]
                        PathSum=PathSum+i[j]+" -> "
                        break
        elif i[j]==End and Run:
               for k in range(0,e-s):
                  if i[j]==List[k]:
                        Sum=Sum+List2[k]
                        PathSum=PathSum+i[j]+" . "
                        break
               break
     AllListCost.append(Sum)
     PathListCost.append(PathSum)
     
print('--------------   Done   ---------------')   
print()
print()
print()
print()
print()
print()

print('--------------   Processing   ---------------')
print()
print()
Min=AllListCost[0]
Pos=0
for i in range(1,len(AllListCost)):
    if Min>AllListCost[i]:
        Min=AllListCost[i]
        Pos=i


Max=AllListCost[0]
Pos2=0
for i in range(1,len(AllListCost)):
    if Max<AllListCost[i]:
        Max=AllListCost[i]
        Pos2=i


print("Min List Cost = ",Min)
print("Pos List Cost = ",PathListCost[Pos])
print()
print("Max List Cost = ",Max)
print("Pos List Cost = ",PathListCost[Pos2])
print()
print()
print('--------------   Done   ---------------')   
print()
print()
print()
print('--------------   Please press Enter key on the keyboard   ---------------')   
input()
