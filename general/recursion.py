# December 27th, 2024

def walk(stepCount):
    if stepCount != 0:
        walk(stepCount-1)
        print(f'Youve taken {stepCount} number of steps')

    else:
        return
    
walk(100)

