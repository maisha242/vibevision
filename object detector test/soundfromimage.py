import test
import openaiwrap

def main():

    current_item = test.get_currentitem()

    while current_item == "":
        current_item = test.get_currentitem()

    print(openaiwrap.openai_sound(current_item))


if __name__ == "__main__":
    main()
    