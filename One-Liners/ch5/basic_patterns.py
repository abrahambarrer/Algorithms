import re

def main():
    ## Data
    text = 'peter piper picked a peck of pickled peppers'

    result = re.findall('p.*?e.*?r', text)

    print(result)

if __name__ == '__main__':
    main()