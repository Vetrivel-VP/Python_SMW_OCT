import re


def searchPattern():
    txt = "The rain in spain"
    x = re.search("^The.*ssds$", txt)

    if x:
        print("Yes ! we have that pattern")
    else:
        print("No Match")


def findAll():
    txt = "The rain in spain"
    x = re.findall("ai", txt)
    print(x)


def splitfunc():
    txt = "The rain in spain"
    x = re.split("\s", txt)
    print(x)


def subfunc():
    txt = "The rain in spain"
    x = re.sub("\s", "9", txt)
    print(x)


# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[\._]+[@]\w+[.]\w+$'
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# sam09.sample@gmail.edu


def check(email):
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Not a valid email")


if __name__ == "__main__":
    email = input("Enter the email id:")
    check(email)
