
def validate_email(emaill):
    valuu = emaill.split("@")
    host = valuu[1]
    host2 = host.split(".")
    return host2[0]


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
    com = num[0:3]
    if check_len(num):
        if com == "010":
            return "vodafone"
        elif com == "011":
            return "Etisalate"
        elif com == "012":
            return "Orange"
        elif com == "015":
            return "We"
        else:
            return "Error"
    else:
        return "the number should be 11 digte nume"


def select_validation_type():
    print("select validation type\n")
    ine = input("1- phone \n2- email \n0-exit\n ")
    inee = int(ine)
    if inee == 1:
        phone = input("enter your phone\n")
        print(validate_phone(phone))
        select_validation_type()
    elif inee == 2:
        emails = input("enter your email\n")
        mail = validate_email(emails)
        print(get_host(mail))
        select_validation_type()
    else:
        return


select_validation_type()
