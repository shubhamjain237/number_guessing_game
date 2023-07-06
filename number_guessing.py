from random import randint

def define_range():
    try:
        x = input('Enter the range of numbers between which you want to guess separated by space ').split(' ')
        return (int(x[0]), int(x[1]))
    except Exception as e:
        print(e)
        return None

def guess(k:int, n:int):
    if n>k:
        print('Try Again! You guessed too high')
        return 0
    elif n<k:
        print('Try Again! You guessed too small')
        return 0
    else:
        print('Bingo!!')
        return 1

def set_number(x:int, y:int):
    return randint(x,y)

def main():
    count = 0
    x = define_range()
    if x is not None:
        k = set_number(x[0], x[1])
        while 1:
            count = count+1
            try:
                n = int(input('Enter a number to guess'))
                if guess(k,n):
                    print(f'You have made {count} attempts to guess the number')
                    break
            except Exception as e:
                print(e)

if __name__ == '__main__':
    main()