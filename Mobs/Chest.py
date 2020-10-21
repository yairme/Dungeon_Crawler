import keyboard

def Opening_Chest():
    Open_Chest = False
    Open = 2
    print("Press E to open. \nPress Esc to leave.")
    print(Chest(Open))
    while not Open_Chest and Open > 0:
        if keyboard.press_and_release('e', do_press=True, do_release=True):
            Open -= 1
        elif keyboard.press_and_release('esc'):
            print("Place holder.")
        else:
            return Opening_Chest()
        print("Press E to open. \nPress Esc to leave.")
        print(Chest(Open))
        
def Chest(Open):
    stages = [
        """
                    __________________________                       
                   |\\                        |\\
                   | \\                       | \\
                   |  |                       |  |
                   |  |                       |  | 
                   |  |                       |  |
                   | /                        | /
                   |/_________________________|/
                  /                          /|
                 /                          / |
                /_________________________ /  |
                |            _            |   |
                |          |( )|          |   |
                |          |/_\|          |  /
                |                         | /
                |=========================|/
        """,
        """
                   _________________________
                 /                         / \\  
                /_________________________/___|
                |            _            |   |
                |          |( )|          |   |
                |          |/_\|          |  /
                |                         | /
                |=========================|/
        """
    ]
    return stages[Open]

