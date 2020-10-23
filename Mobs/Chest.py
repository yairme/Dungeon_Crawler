from pynput import key, Controller

keyboard = Controller()

def Opening_Chest():
    #Open_Chest = False
    #Open = 1
    print("Press E to open. \nPress Esc to leave.")
    print(Chest(1))
    
    #while not Open_Chest and Open > 0:
    if keyboard.press(Key.space)
            Chest(0)
            keyboard.release(Key.space)
    elif keyboard.press_and_release('esc'):
        print("Place holder.")
    else:
        return Opening_Chest()
    #print("Press E to open. \nPress Esc to leave.")
    #print(Chest(Open))
        
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

Opening_Chest()
