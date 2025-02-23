import test
import openaiwrap
import detector


def main():
    #current_item = test.get_currentitem()
    current_item = detector.main()
    while current_item == "":
        current_item = detector.main()

    sound_to_use = openaiwrap.openai_sound(current_item)
    print(sound_to_use)
    return sound_to_use


if __name__ == "__main__":
    main()
    