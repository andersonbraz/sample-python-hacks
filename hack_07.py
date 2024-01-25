import re


def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)


email = "contato@andersonbraz.com"
check_email = is_valid_email(email)
if check_email:
    print("email ok")
else:
    print("email fail")
