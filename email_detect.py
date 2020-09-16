import pyperclip, re

#find phone number
#phone = re.compile(r'(\d{3}-\d{3}-\d{4}')


#find email
email = re.compile(r'[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}', re.VERBOSE)

text = str(pyperclip.paste())
match = []
for groups in email.findall(text):
    match.append(groups)

if len(match)>0:
    pyperclip.copy('\n'.join(match))
    print('\n'.join(match))

else:
    print('Match not found')

