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

