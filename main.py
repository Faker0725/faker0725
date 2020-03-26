# mathScores =[60,70,10,20,81,63,4]
# # print(mathScores[2])
# # print(mathScores[1:6])
# # print(mathScores[-1])
# # print(mathScores[5:])
# # print(sum(mathScores))
# # print(max(mathScores))
# # print(min(mathScores))
# # print((sum(mathScores))/(len(mathScores)))
# # mathScores2 = []
# # print(mathScores2)
# # mathScores2.append(60)
# # print(mathScores2)
# # mathScores2.append(70)
# # print(mathScores2)
# # mathScores2.append(70)
# # mathScores2.append(50)
# # mathScores2.append(40)
# # mathScores2.insert(2,30)
# # print(mathScores2)
# # mathScores2.remove(70)
# # print(mathScores2)
# #
# # mathScores2[1] = 55
# # print(mathScores2)
# # 33  in mathScores2
# # print(mathScores)
# # print(mathScores2)
# # print(sorted(mathScores2, reverse=True))
# # ls = [[1,2,3],[4,5,6]]
# # print(ls[0] [2])
# # grades=[[5,14,7],[23,36,28],[88,80,92]]
# # print(grades[2])
# # print(sum(grades[2])/len(grades[2]))
# # grades.append([94,90,96])
# # print(grades)
# # grades[0][1]=20
# # print(grades)
# # turple1 = (88,12,20)
# # x, y , z= turple1
# # print(x)
# # print(y)
# # print(z)
# # grasesTuple=[[5,14,7],[23,36,38],[88,80,92]]
# # print(grasesTuple[2])
# # print(sum(grasesTuple[0])/len(grasesTuple[0]),sum(grasesTuple[1])/len(grasesTuple[1]),sum(grasesTuple[2])/len(grasesTuple[2]))
# # family = {}
# # print(family)
# # family["cousin"] = "Max"
# # print(family)
# # family["cousin"] = "Eric"
# # print(family)
# # family.update({
# #     "uncle": "Martin",
# #     "aunt": "May"
# # })
# # del family["uncle"]
# # print(family)
# # print(family.pop("cousin"))
# # gradesDict = {
# #     "chinese1": [5,14,7],
# #     "english": [23,36,38],
# #     "math": [88,80,92]
# # }
# # print(gradesDict["math"])
# # print(gradesDict.get("math"))
# #
# #
# # fruits = {
# #     "apple",
# #     "banana",
# #     "guava",
# #     "guava"
# # }
# # print(fruits)
# # fruits.add("watermelon")
# # print(fruits)
# # print(sorted(fruits))
# # allStudents = {
# #     "John",
# #     "Eva",
# #     "Jill",
# #     "Eric",
# #     "Andy",
# #     "Albert",
# #     "Polina",
# #     "Kristin",
# #     "Angela",
# # }
# # danceClub = {
# #     "Andy",
# #     "Eric",
# #     "Albert",
# #     "Polina",
# #     "Kristin",
# # }
# # guitarClub = {
# #      "John",
# #     "Eva",
# #     "Jill",
# #     "Eric",
# #     "Andy"
# # }
# # Set = {
# #     "Andy",
# #     "Eric",
# #     "Albert",
# #     "Polina",
# #     "Kristin",
# #      "John",
# #     "Eva",
# #     "Jill",
# #     "Eric",
# #     "Andy"
# # }
# # print(danceClub & guitarClub)
# # print(guitarClub - danceClub)
# # print(allStudents - Set)
# #
# #
# # import math
# # x = 6
# # print(6/2*3.14*x)
# # x = (10+30+40+90+100+61)/6
# # print(round(x))
# # score = 70
# # if score >= 60:
# #     print("及格了")
# #     if score >= 90:
# #         print("不錯喔")
# #     else:
# #         print("還行啦")
# # elif 55 <= score < 60:
# #     print("駱阿堯拜託調分")
# # elif 50 <= score <= 55:
# #     print("哭阿差一點點")
# # else:
# #     print("食屎啦你")
# # print("Hello","Word","!")
# # print("Hello\nworld\n!")
# # print("123", end=" ")
# # print("456")
# # x = 42
# # print(f"Value of x is {x}")
# # mathScores = [60,70,10,20,81,63,4]
# # print(mathScores[0])
# # firstItem = f"first item in mathScore is {len(mathScores)}"
# # print(firstItem)
# # for i in range(0,20,3):
# #     print(i)
# # mathScores = [60,70,10,20,81,63,4]
# # for i in mathScores:
# #     print(i)
# #
# # family = {
# #     "dad": "Homer",
# #     "mom": "Marge",
# #     "son": "Bart",
# #     "daughter": "Lisa"
# # }
# # for member in family.items():
# #     print(member)
# #
# # for key,value in family.items():
# #     print(f"my {key} is {value}")
# #
# # import  math
# # mathScores = [60,70,10,20,81,63,4]
# # for score in mathScores:
# #     print(math.sqrt(score)*10)
# #
# # for i in range(10):
# #     print(i)
# # [print(i) for i in range(10)]
# # mathScores = [60,70,10,20,81,63,4]
# # [print(math.sqrt(x)*10) for x in mathScores]
# #
# # mathScores = [60,70,10,20,81,63,4]
# # for score in mathScores:
# #     if score > 80:
# #         continue
# #     print(score)
# #
# # import random
# # i = random.randint(1,50)
# # print(i)
# #
# # rows = eval(input("How many rows:"))
# # print(type(x))
import vending_machint.vending_service as machine

flag = True

while flag:
    print("\n=============================")
    select = eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:'))
    if select == 1:
        machine.desposit()
    elif select == 2:
        machine.buy()
    elif select == 3:
        print(f'目前餘額為{machine.balance}元')
        pass
    elif select == 4:
        print("bye")
        flag = False
        break
    else:
        print("====請輸入1-4之間")
        continue
weight = 100
weight1= 80

def add_weight(w1, w2):
    result = w1+ w2
    result1 = w1 * w2
    return result, result1
x = add_weight(weight,weight1)
print(x)



































