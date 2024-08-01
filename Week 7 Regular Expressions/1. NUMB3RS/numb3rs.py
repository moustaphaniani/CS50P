import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^(\d{1,3}\.){3}(\d{1,3}){1}$", ip):
        ubication = ip.split('.')
        for x in ubication:
            if 0 <= int(x) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
