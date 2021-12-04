import re

s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"
encontrados1=re.findall(r"User_mentions:\d",s)
print(encontrados1)
encontrados2=re.findall(r"likes: \d",s)
print(encontrados2)
encontrados3=re.findall(r"number of retweets: \d",s)
print(encontrados3)