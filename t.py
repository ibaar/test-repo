import subprocess


def main(c=4):
    ad = input('hello input any thing: ')
    subprocess.run(['python', '-V'])
    a = 10
    print(f'{a*c=}')
    print(ad)
    return 'Nothing'


if __name__ == '__main__':
    main()
