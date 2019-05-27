# string functions

def is_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()


def is_pincode(pincode):
    return len(pincode) == 6 and pincode.isdigit()

if __name__ == "__main__":
    print("Running str_funs module")
else:
    print("Importing str_funs module")
