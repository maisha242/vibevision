import test
import openaiwrap
import detector

def norm():
    #current_item = test.get_currentitem()
    current_item = detector.main()
    for item in current_item:
        if (item != None):
           # sound_to_use = item
            sound_to_use = openaiwrap.openai_sound(item)
            print(sound_to_use)
            yield sound_to_use

def exp():
    #current_item = test.get_currentitem()
    current_item = detector.main()
    for item in current_item:
        if (item != None):
            sound_to_use = item
           # sound_to_use = openaiwrap.openai_experimental(item)
            print(sound_to_use)
            yield sound_to_use

def main():
    return


if __name__ == "__main__":
    main()
    