#US = user input  Grade calculate
while True:

    US = int(input())
    if US >100:
        print("Error")

    elif US >= 90:
        print('your score: A')

    elif US >= 80:
        print('your score: B')

    elif US >= 70:
        print('your score: C')
    
    elif US >= 60:
        print('your score: D')
    
    elif US >= 50:
        print('your score: E')
    
    else:
        print('your score: F')
    