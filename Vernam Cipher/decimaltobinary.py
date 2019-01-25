finbinary = ""
denary = input("denary\n")
denary = int(denary)
while denary != 0:
    remainder = denary % 2
    denary = denary // 2
    finbinary = str(remainder) + finbinary

while len(finbinary) < 7:
    finbinary = "0" + finbinary
    
#endwhile
print(finbinary)

