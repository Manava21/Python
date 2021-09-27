total_bill = float(input("What was the total bill? $ "))
tip = (input("What percentzge tip would you like to give? 10, 12, 15?"))
bill_split = int(input("how many people to split the bill? "))


if(tip== "N"):
# each_pay = round(float((total_bill / bill_split) * tip_percent),2) 
# print(f"each person should pay : ${each_pay} ")
  each_pay = round(float(total_bill / bill_split),2)
  print(f" each person should pay : ${each_pay} ")
else:
  tip_percent = ((int(tip)/100) +  1) 
  each_pay = round(float((total_bill / bill_split) * tip_percent),2)
  print(f" each person should pay : ${each_pay} ")
