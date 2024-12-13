class employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"


  def bonus(self,rate):
    empbonus=self.pay*rate
    return empbonus

empl1=employee("correy", "J", 50000)
empl2=employee("Test","user",60000)

print(empl1.first,empl1.last,empl1.pay,empl1.email)

print("Employee 1's bonus is",empl1.bonus(.10))


print(empl2.first,empl2.last,empl2.pay,empl2.email)
print("Employee 2's bonus is",empl2.bonus(.10))
