import re


def convert(s):
    '''
    this function converts lakhs and crores to more user-friendly numbers.
    INPUT:
     s: string from API ex: "1.07 lakhs"
    OUTPUT:
     number: the float number in the string
     final_value: value converted in english numbering system
    '''
    number = re.findall(r"[0-9.]+",s)[0]
    word = re.findall(r"[a-zA-Z]+",s)[0]
    final_value = 0
    if word == "lakhs":
         final_value = 10 **5
         # f'*10\N{SUPERSCRIPT FIVE}'#"hundred thousand"
    elif word == "crores":
         final_value = 10**7#"ten million"
         
    return float(number)* final_value
    
    
