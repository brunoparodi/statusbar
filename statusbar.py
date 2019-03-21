from time import sleep

def loadbar(step, until):
    ''''
    step: is a number incremented step by step
    until: is 100% percent
    '''
    print('\r', end='')
    print(f'\r{"||"} LOADING {"":{until - (until - step - 1)}} '
          f'{(step / until) * 100:{".2f" if (step / until) * 10 < 1 else ".1f"}}% '
          f'{"":{until - step}}||', end='')


def foo():
    '''calculate y ^ 2 (is to difficult and I need wait)'''
    y = 2
    fullpercent = 78  # 100$
    for x in range(fullpercent):
        loadbar(step=x, until=fullpercent)
        sleep(0.2) #only to show step by step the status bar
    print(f'\rthis is my result after exhaustive calculus{y ^ 2}') #\r erasy the loadbar


print('this is one fixed row')
foo()
