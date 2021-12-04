import re

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
encontrados=re.findall(r"@robot\d\W",s)
print(encontrados)
