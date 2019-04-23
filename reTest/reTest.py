import re

pat_K = r"(.*)K-(.*)K"
data="7K-12K/月"
low, high = re.findall(pattern=pat_K, string=data)[0]
print(high)
print(low)
regular_v3 = re.findall(r"html$","https://docs.python.org/3/whatsnew/3.6.html")
print (regular_v3)
regular_v4 = re.findall(r"[t,w]h","https://docs.python.org/3/whatsnew/3.6.html")
print (regular_v4)