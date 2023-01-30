import re

def main():
    ip_add = input("IPv4 Address: ").strip()
    print(validate(ip_add))


def validate(ip):
    check = re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)
    # check = re.search(r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])", ip)
    # check = re.search(r"^(([0-9]|[0-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)

    if check:
        return True
    else:
        return False

if __name__ == "__main__":
    main()