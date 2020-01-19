def first_recurring_char(string): 
  
    temp = {}  
    for ch in string: 
   
        if ch in temp: 
            return ch;  
        else: 
            temp[ch] = 0
  
    return None
  
  
# Driver code 
print(first_recurring_char("abcbc")) 
print(first_recurring_char("abcdef"))