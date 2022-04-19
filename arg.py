import argparse

def main() -> None:
    a =argparse.ArgumentParser(description="this is a test app",)
    a.add_argument("-a","--add",help= 'this takes a string and print it')
    c= a.parse_arg()
    print(c.add)

if __name__ == '__main__':
    main()
