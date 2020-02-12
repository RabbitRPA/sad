"""
def cat_dog(str= ''):
    cat = 0
    dog = 0

    for i in range(len(str)):
        if str[i:i+3] == "cat":
            cat += 1
        if str[i:i+3] == "dog":
            dog += 1
  
        
    return cat == dog
            
  """
"""
  def count_code(str):
    ile = 0

    for i in range(len(str)):
        if str[i:i+4] == "code":
            ile += 1
        if str[i:i+4] == "cope":
            ile += 1
        if str[i:i+4] == "coze":
            ile += 1  
        if str[i:i+4] == "cooe":
            ile += 1
        if str[i:i+4] == "core":
            ile += 1
        if str[i:i+4] == "cole":
            ile += 1
    return ile
"""
"""
Id = {
    0: 1,
    1: 3,
    2: 7,
    3: 9,
    4: 1,
    5: 3,
    6: 7,
    7: 9,
    8: 1,
    9: 3,
    10: 1
}

#last number is zero it True

how_may = int(input())
soultion = []


while how_may > 0:
    how_may -= 1
    soultion.clear()
    pesel = list(map(int, input()))
    for i in range(0, 11):
        soultion.append(Id[i]* pesel[i])
    if sum(soultion) % 10 == 0 :
        print("D")
    else:
        print("N") 

"""
"""

import sys

string = str(input())
result = string.title().replace(" ", "")
print(result)

"""
"""
def sum67(nums):
    total = 0
    found6 = False
      
    for i in range(len(nums)):
        if nums[i] == 6:
            found6 = True
        if not found6:
            total += nums[i]
        if nums[i] == 7 and found6:
            found6 = False
            
    return total
    """
"""
    def print_formatted(number):
    N = number
    wynik = []
    
    koncowe = list()
    for i in range(1, number+1):
        wynik.clear()
        wynik.append(i)
        wynik.append(oct(i)[2:])
        wynik.append(hex(i)[2:].upper())
        wynik.append(bin(i)[2:])
        koncowe.append(list(wynik))

    for i in koncowe:
        dlug = ""
        if int(i[3]) %10 == 0 :
            new = " "
        else: new = "  "
        print(i[0],"",i[1],"",str(i[2])+new+str(i[3]))

print(print_formatted(20))
"""


def DNA_strand(dna):
    cos = []
    for i in dna:
        if i =="G":
            cos.append("C")
        elif i == "C":
            cos.append("G")
        if i == "T":
            cos.append("A")
        elif i == "A":
            cos.append("T")
    return "".join(cos)

