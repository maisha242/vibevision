import test
import openaiwrap
import detector
def main():

    #current_item = test.get_currentitem()
    current_item = detector.main()
    for item in current_item:
        if (item != None):
            sound_to_use = openaiwrap.openai_sound(item)
            print(sound_to_use)
            yield sound_to_use


if __name__ == "__main__":
    main()
    