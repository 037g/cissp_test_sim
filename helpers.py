from os import system, name

#Alias colos
class bc:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


#Clear screen
def clear() -> None:
    """Clear the screen"""
    if name == "posix":
        _ = system("clear")
    else:
        _ = system('cls')