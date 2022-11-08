import re
pattern = re.compile(r"[; :]-*[\(\)\]\]\[]+")
result = pattern.findall(":)df\;-----------][;;lkjn]]]](:----------))----adf:)----]")
print(result)

