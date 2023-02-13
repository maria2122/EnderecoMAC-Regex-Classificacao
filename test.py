from regex import search
from classifier import classify
text = 'E0-06-E6-CE-D9-10\n\
        fsfsf00-D7-6D-70-E4-E6batata\n\
        E8-11-32-B8-CF-CBbatata\n\
        fsfsf55-94-E2-3C-71-A8-B3\n'
result = search(text)
print(classify(result))

# E0-06-E6-CE-D9-10
# 00-D7-6D-70-E4-E6
# E8-11-32-B8-CF-CB
# 55-94-E2-3C-71-A8