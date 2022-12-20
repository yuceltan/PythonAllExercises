"""from 0 KW to 100 price per KW is 0.5
from 100 kw to 200 price per KW is 0.75
from 200 KW to 1000 price per KW is 0.93"""



userUsage=input("Please enter your usage of electric KW")
convertedUsage=float(userUsage)
if convertedUsage >=0 and convertedUsage <= 100:
    totalUsage = convertedUsage * 0.5
    print("Bill is :{} ".format(totalUsage))
elif convertedUsage <= 200 and convertedUsage > 100:
    totalUsage = convertedUsage * 0.75
    print("Bill is :{} ".format(totalUsage))

elif convertedUsage > 200 and convertedUsage <= 1000:
    totalUsage = convertedUsage * 0.93
    print("Bill is :{} ".format(totalUsage))

else:
    print("Please enter valid value")





