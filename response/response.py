from validator_collection import validators


def main():
    email = input("What's your email address: ").strip()
    print(validate(email))

def validate(s):
    try:
        if validators.email(s):
            return "Valid"
        else:
            return "Invalid"
    except:
        return "Invalid"

if __name__ == "__main__":
    main()