from regex import search
from classifier import classify
text = 'Fui no E0-06-E6-CE-D9-10mercadinho\nPra fazer00-D7-6D-70-E4-E6isso'\
       'mesmoE8-11-32-B8-CF-CBe chegando la.A pipa foi cortada94-E2-3C-71-A8-B3'
result = search(text)
for item in classify(result):
   print(item)

# E0-06-E6-CE-D9-10
# 00-D7-6D-70-E4-E6
# E8-11-32-B8-CF-CB
# 94-E2-3C-71-A8-B3
