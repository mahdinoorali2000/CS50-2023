from random import randrange

level = 0

while True:
    try:
        if level < 1:
            level = int(input("Level: "))

        else:
            x = randrange(1, level + 1)
            g = int(input("Guess: "))

            if g > 0 and g > x:
                print("Too large!")
            elif g > 0 and g < x:
                print("Too small!")
            elif g > 0 and g == x:
                print("Just right! ")
                break
            else:
                continue
    except KeyboardInterrupt:
        quit()
    except:
        pass


