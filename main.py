# Alright, I start this awesome program by making a simple and nice looking main menu
# I really enjoy making menus in Python, idk why

def main_menu():
        while True:
            print("""
              ####################################################################################
              #                                                                                  #
              #                   Universal NFS SaveGame Editor                                  #
              #                      Made by: linuxbastian                                       #
              #                   https://github.com/linuxbastian                                #
              #                                                                                  #
              ####################################################################################
              # Please of which game you want to edit your SaveGame.                             #
              #                                                                                  #                                                                                        
              # 1. Need for Speed: Underground                                                   #
              # 2. Need for Speed: Underground 2                                                 #
              # 3. Need for Speed: Most Wanted (2005)                                            #
              # 4. Need for Speed: Carbon                                                        #
              # 5. Need for Speed: ProStreet                                                     #
              #                                                                                  #
              ####################################################################################               
              """)
        

            choice = input("\nSelect the number corresponding your choice: ")

def print_disclaimer():
    print("""n
    ####################################################################################
    #                                                                                  #
    #                   Universal NFS SaveGame Editor                                  #
    #                      Made by: linuxbastian                                       #
    #                   https://github.com/linuxbastian                                #
    #                                                                                  #
    ####################################################################################
    # Please be aware that you are using this program at your own risk.                #
    #                                                                                  #                                                                                        
    # The author or contributors are not responsible for any potential                 #
    # damage or loss that may occur as a result of using this program.                 #
    #                                                                                  #
    # Please ensure you have backups of any files you modify with this tool.           #
    # This tool creates an automatic backup of your given File at: XXX                 #
    #                                                                                  #
    ####################################################################################               
    """)

    choice = input("\nI agree and continue (y)\nExit (n)\nYour choice: ")

    if(choice=="y"):
         main_menu()
    else:
         exit()

# Call the function to print the disclaimer
print_disclaimer()
