# def rezultats(sk1, sk2):
#     if sk1<6 and sk2<6:
#         rez = sk1*sk2
#     else:
#         rez = sk1+sk2
#     return rez

# for skaitlis in range(1, 11, 2):       #range  - funkcija, kas skaita skaitļus
#     for otrs in range(2, 11, 2):
#         print("pirmais skaitlis:", skaitlis,"otrais skaitlis:", otrs, "rezultāts:", rezultats(skaitlis, otrs))

# skaitlis1 = 7
# skaitlis2 = 4

# print("pirmais skaitlis:", skaitlis1)
# print("otris skaitlis:", skaitlis2) 
# print("rezultats:", rezultats(skaitlis1, skaitlis2))


# saraksts1 = [1, 7, 5, 9, 35, 2]
# saraksts2 = [4, 2, 2, 39, 6, 4]

# for skaititajs in range(len(saraksts1)):
#     print("skaititajs:", skaititajs, "pirmais skaitlis:", saraksts1[skaititajs],"otrais skaitlis:", saraksts2[skaititajs], "rezultāts:", rezultats(saraksts1[skaititajs], saraksts2[skaititajs]))

# skaitlu_pari = [[2,5], [4,7], [3,4], [7,9]]

# print("------------------------------------------------")

# def zvaigznites1(skaits):
#     for rindasNr in range(1, skaits+1):
#         for zvaigzne in range(rindasNr):
#             print("*", end="")
#         print("")

# def zvaigznites2(skaits):
#     for rindasNr in range(1, skaits+1):
#         print("*"*rindasNr)


# zvaigznites1(7)

# print("------------------------------------------------")

# for i in range(len(skaitlu_pari)):
#     print("skaititajs:", i, "pirmais skaitlis:", skaitlu_pari[i][0],"otrais skaitlis:", skaitlu_pari[i][1], "rezultāts:", rezultats(skaitlu_pari[i][0], skaitlu_pari[i][1]))

# print("------------------------------------------------")

# for elements in skaitlu_pari:
#      print("pirmais skaitlis:", elements[0],"otrais skaitlis:", elements[1], "rezultāts:", rezultats(elements[0], elements[1]))



def calculation(n1, n2):
    if n1*n2 <= 1000:
        calc = n1*n2
    else:
        calc = n1+n2
    return calc

number1 = 40
number2 = 30

print("The result is:", calculation(number1, number2))


print("------------------------------------------------")



prev_number = 0
curr_number = 0

for i in range(1, 11):
    curr_number = prev_number + i
    print("Previous number:", prev_number, "Current number:", i, "Sum:", curr_number)
    prev_number = i

print("---------------------------------------------")

def same_list(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False

numbers_1 = [1, 2, 3, 4, 5, 1]

print("Given list:", numbers_1, "result is", same_list(numbers_1))

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Given list:", numbers_2, "result is", same_list(numbers_2))

print("---------------------------------------------")


def print_divisible_by_five(lst):
    for num in lst:
        if num % 5 == 0:
            print(num)

my_list = [10, 15, 20, 25, 30, 89, 93, 34]
print_divisible_by_five(my_list)

print("---------------------------------------------")


def create_new_list(list1, list2):
    new_list = []

    for num in list1:
        if num % 2 != 0:
            new_list.append(num)

    for num in list2:
        if num % 2 == 0:
            new_list.append(num)

    return new_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
result = create_new_list(list1, list2)
print(result)



