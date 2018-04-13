"""
 Practice 1.
"""
from itertools import repeat

def gen():
  int_rate = [0.01, 0.02, 0.03, 0.035, 0.05]
  for r in int_rate:
    yield r
  for r in repeat(0.05):
    yield r 

def num_year_pay() :
  house_price = 500000
  year_pay = 30000
  year_n = 1
  rem = house_price

  print(year_pay)

  for r in gen():
    if rem <=0:
      break
    print(r)
    rem = rem * (1 + r) - year_pay
    year_n = year_n + 1
    print(rem)

  return year_n

if __name__ == "__main__":
  print("Number of years to pay loan: ", num_year_pay())

