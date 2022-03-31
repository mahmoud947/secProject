
def validate_email(emaill):
    valu = emaill.split("@")
    email_after_at_split = valu[1]
    email_after_dot_split = email_after_at_split.split(".")
    return email_after_dot_split[0]


def get_host(host):
    if host == "gmail":
        return "it is gmail"
    elif host == "yahoo":
        return "it is yahoo"
    elif host == "hotmail":
        return "it is hotmail"
    else:
        return "Error"


def check_len(num):
    if len(num) == 11:
        return True
    else:
        return False


def validate_phone(num):
    first_three_num = num[0:3]
    if check_len(num):
        if first_three_num == "010":
            return "vodafone"
        elif first_three_num == "011":
            return "Etisalat"
        elif first_three_num == "012":
            return "Orange"
        elif first_three_num == "015":
            return "We"
        else:
            return "Error"
    else:
        return "the number should be 11 digte nume"


def select_validation_type():
    print("select validation type\n")
    opts = input("1- phone \n2- email \n0-exit\n ")
    selected_num = int(opts)
    if selected_num == 1:
        phone = input("enter your phone\n")
        print(validate_phone(phone))
        select_validation_type()
    elif selected_num == 2:
        emails = input("enter your email\n")
        mail = validate_email(emails)
        print(get_host(mail))
        select_validation_type()
    else:
        return


select_validation_type()
