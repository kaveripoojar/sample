start=0
end=100
increment=1
print("the following tables shows conversion of celsius to farenheit")
print("between 0 to 99 degree celsius. ")
print("")
print("celsius\t farenheit")
for celsius in range(start,end,increment):
    farenheit=(9/5)*(celsius+32)
print(celsius,'\t',format(farenheit,'.1f'))
