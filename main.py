import re # sfsfs
# [A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]:[A-F0-9][A-F0-9]

# text = '55:9F:E4:69:87:C5 55:95:E4:69:87:C5 batata'
# texts = text.split

results = re.compile(r'((([\w+]{2}[:]){5})[\w+]{2})')
total = results.findall('fsfsf55:9F:E4:69:87:C5batata')
print(total) 
# groups_match = results.groups()
# if groups_match is None:
#     exit()
# print(groups_match)