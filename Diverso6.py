import re

s = """AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company
ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"""
encontrados=re.findall(r"[aeiouAEIOU]{2,3}.+txt",s)
print(encontrados)
