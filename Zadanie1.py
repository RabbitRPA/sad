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
