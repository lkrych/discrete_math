#Develop a Python method change(amount) that for any integer amount in the range from 24 to 1000 returns a 
#list consisting of numbers 5 and 7 only, such that their sum is equal to amount. For example, change(28) 
#may return [7, 7, 7, 7], while change(49) may return [7, 7, 7, 7, 7, 7, 7] or [5, 5, 5, 5, 5, 5, 5, 7, 7] or 
#[7, 5, 5, 5, 5, 5, 5, 5, 7].

def change(amount):
  if amount == 24:
    return [5, 5, 7, 7]
  elif amount == 25:
    return [5, 5, 5, 5, 5]
  elif amount == 26:
    return [5, 7, 7, 7]
  elif amount == 27:
    return [5, 5, 5, 5, 7]
  elif amount == 28:
    return [7, 7, 7, 7]
  coins = change(amount - 5)
  coins.insert(0, 5)

  return coins


print(change(28))
print(change(49))
