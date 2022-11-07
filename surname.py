import re
str_Names = '''Michael, how are you? - Cool, how is John Williamns and Michael Jordan? 
I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James
, Michael Green AKA Star and Michael Wood?'''
print(re.findall(r'Michael ([A-Z]\w+)',str_Names))

