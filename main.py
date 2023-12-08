from gui import *


def main() -> None:
    """
    Main function of the program, runs the GUI window.
    """
    window = Tk()
    window.title('Personality Quiz!')
    window.geometry('500x300')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
