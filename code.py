# population = 10000
# pop =10000
# for i in range (2011,2021):
#   pop = 0.1*pop12
#   population = population+0.1*population
#   print(i,"me itne loga bade-->",pop,"!""Total->",population)
  

lower = int(input('enter lower range'))
upper = int(input('enter upper range'))

for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j == 0:
      break
  else:
    print(i,"prime number") 
