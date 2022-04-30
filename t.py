import subprocess


def main(c=4):
    ad = input('hello input only strings and lists: ')
    subprocess.run(['python', '-V'])
    a = 10
    print(f'{a*c=}')
    print(ad)
    return [x for x in 'hello']
    

if __name__ == '__main__':
    print(main())
