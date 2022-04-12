import subprocess


def main(c=4):
    subprocess.run(['python', '-V'])
    a = 10
    print(f'{a*c=}')

    return 'Nothing'


if __name__ == '__main__':
    main()
