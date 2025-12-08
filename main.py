# menu
import os
print(" Hi,I'm  Kristin (⁠ •⁠ ‿⁠ •⁠ )\n")
name = input("what's you name?:  ").upper()

while True:
    os.system("clear")
    print(f"Hi,~+{name}+~, What do you want to learn? ")
    print('                 •⁠ ‿⁠ •')
    print("                *================ ~*MENU *~ =================*")
    print("                | A - What is Programming?                   |")
    print("                | B - What is the Python language            |")
    print("                | C - What are Data types?                   |")
    print("                | D - Variables                              |")
    print("                | E - Learn Types of Operators               |")
    print("                | F - Learn Assignments                      |")
    print('                *============================================*')
    print("                             X - EXIT SYSTEM                            ")
    print("             *===================================================*")
    print("(⁠◠⁠‿⁠・⁠)⁠—⁠☆")
    unak = input("\nPlease select option above what you want to learn~~ :  ").lower()
    if unak == 'a':
        os.system("clear")
        print("    (⁠人⁠ ⁠•͈⁠ᴗ⁠•͈⁠) ")
        print("     What is Programming? ")
        # dagdagan mo pa Yung meaning neto
        print("    ====================================================")
        print("    |Programming is telling a computer what to do.     |")
        print("    ====================================================")
        e = input("\nPress 'enter' to CONTINUE  : ")
        if e == ' ':
            continue
        else :
            continue    
        continue
    elif unak == 'b':
        os.system("clear")
        print("    (⁠✯⁠ᴗ⁠✯⁠) ")
        print("    what is the Python language? ")
        print("    =========================================================================================================")
        print("    |Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.     |")
        print("    |Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it     |")
        print("    |very attractive for Rapid Application Development, as well as for use as a scpriting or glue langauge  |")
        print("    |to connect existing components together. Python's simple easy to learn syntax emphasizes readability   |")
        print("    |and therefore reduces the cost of program maintenance.                                                 |")
        print("    =========================================================================================================")
        e = input("\nPress 'enter' to CONTINUE : ")
        if e == ' ' :
            continue
        else:
            continue
            
    elif unak == "c":
        while True:
            os.system("clear")
        # mag lagay Ka g data type dito para SA options
        # ang haba nito  huhu 
            print('                (⁠*⁠˘⁠︶⁠˘⁠*⁠)⁠.⁠｡⁠*⁠♡')
            print("                what are the Data types?   ")
            print("                *===================================*")
            print("                | 1 - str                           |")
            print("                | 2 - int, float                    |")
            print("                | 3 - range function                |")
            print("                | 4 - list                          |")
            print("                | 5 - bool                          |")
            print('                *===================================*')
            print("                      x - exit data types menu          ")
            print("             *===========================================*")
        # Yung v ay option nang mga data types
            v = input("         (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡\n        Please select potions above : ")
            if v == '1':
                os.system("clear")
                print('        (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡')
                print("\n        *========================= ~* str *~ ===========================*")
                print("        |str, refers to the build-in string data type and str() function  |")
                print("        |used for converting objects to their string represention.        |")
                print("        *===============================================================*\n")
                def unak(): {
                    print("Hello world")
                }
                print("\n############################################################################################")
                print("RESULT:\n")
                unak()
                print("\n############################################################################################")
                e = input("\n(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE  : ")
                if e == ' ':
                    continue
                else:
                    continue
            elif v == '2':
                os.system('clear')
                print('        (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡')
                print("        Numerical Data Types :")
                print("        *===================== * int and float *~ ===================*")
                print("        | int - or Intergers, is whole number, positive or negative   |")
                print("        |       without decimals of unlimited length.                 |")
                print("        |                                                             |")
                print("        | float - or 'floating point numbers is a numbers positive or |")
                print("        |         or negative , containing one more decimals.         |")
                print("        *=============================================================*")
                # dagdagan mo pa Ng examples Yan
                # int and float
                def unak(): {
                    # int
                    print(13 + 5),
                    # float
                    print(13 + 3.5)
                }
                print("\n############################################################################################")
                print("RESULT:\n")
                unak()
                print("\n############################################################################################")
                e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE :  ")
                if e == ' ':
                    continue
                else:
                    continue
            elif v == '3':
                os.system('clear')
                print('        (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡')
                print("        *======================== ~* range *~ ========================*")
                print("        |The range() function returns a sequence of numbers,starting  |")
                print("        |from 0 by default, and increments by 1 (by defult), and stops|")
                print("        |before a specified numbers.                                  |")
                print("        *=============================================================*")
                # range
                print("\n############################################################################################")
                print("RESULT:\n")
                # range(start,stop,step)
                ts = range(1, 6, 1)
                for howl in (ts):
                    print(howl)
                for nak in range(1,7,1):
                    for woo in range(7,nak,-1):
                        print("*",end=(" "))
                    print()
                print("\n############################################################################################")
                e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                if e == ' ':
                    continue
                else:
                    continue

            elif v == '4':
                os.system('clear')
                print('        (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡')
                print("        *======================= ~* list *~ ==========================*")
                print("        |Lists are used to share nutiple items in a single variable.  |")
                print("        *=============================================================*")
                # list
                print("RESULT:")
                #         0       1         2       3        4
                bnd = ['sungho','riwoo','jaehyun','taesan','leehan']
                print(bnd,'\n')
                # how to add in the list?
                print('add on the list')
                bnd.append('zico')
                bnd.append('woonhak')
                bnd.append('doja cat')
                print(bnd,'\n')
                # how to remove?
                bnd.remove('zico')
                print('remove on list')
                # pop - remove the last value on the list
                bnd.pop()
                print(bnd,'\n')
                # sort - arrange the list in alphabetical order
                bnd.sort()
                print(bnd,'\n')
                # reverse
                bnd.reverse()
                print(bnd)
                bnd.insert(0,'bnd')
                print(bnd)
                print("\n############################################################################################")
                e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                if e == ' ':
                    continue
                else:
                    continue

            elif v == '5':
                os.system('clear')
                print('        (⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡')
                print("        *======================== ~* bool *~ =========================*")
                print("        | Booleans represent one of two values : True or False.       |")
                print("        *=============================================================*")
                ##############################################################
                # bool
                def unak(): {
                    print(20 < 10),
                    print(15 == 15),
                }
                print("\n############################################################################################")
                print("RESULT:\n")
                unak()
                pw = 'tintin'
                print("\nnote : password = tintin ")
                ask = input('what is the password? : ')
                print("result :")
                print(ask == pw)
                print("\n############################################################################################")
                e = input("\nPress 'enter' to CONTINUE : ")
                if e == ' ':
                    continue
                else:
                    continue
            elif v == 'x':
                os.system("clear")
                break
    elif unak == 'd':
        os.system('clear')
        # huhu ang haba nanaman neto whaaaa~~
        print("(⁠ ⁠╹⁠▽⁠╹⁠ ⁠)\n        Variables")
        print("        *===============================================================*")
        print("        |Variables are ne of the most basic essential concepts in       |")
        print("        |programming, used to store values.                             |")
        print("        *===============================================================*")
        print("\n############################################################################################")
        print("RESULT:\n")
        food = 'pizza'
        drink = 'coke'
        print(food,'and', drink)
        print("\n############################################################################################")
        e = input("\nPress 'enter' to CONTINUE  : ")
        if e == ' ' :
            continue
        else:
            continue
    elif unak == 'e':
        while True:
            os.system("clear")
            print("                (⁠ ⁠╹⁠▽⁠╹⁠ ⁠)\n        Learn Types of Operators ")
            print('                \n        Arithmetic operators are used with numeric values to\n                perform common mathematical operations:')
            print('             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("                 *===========================================*")
            print("                 | 1 - Arithmetic Operators                  |")
            print("                 | 2 - Comparison Operators                  |")
            print("                 | 3 - Logical Operators                     |")
            print('                *============================================*')
            print("                          x - EXIT TYPES OF OPERATORS               ")
            print("                 *===========================================*")
            f = input("\n(⁠◠⁠‿⁠◕⁠) \n select options above :   ").lower()
            if f == '1':
                while True:
                    os.system('clear')
                    print('                ༼⁠ ⁠つ⁠ ⁠◕⁠‿⁠◕⁠ ⁠༽⁠つ')
                    print("                *======= ~* Arithmetic Oprerators *~ ======*")
                    print("                | 1 - Addition                             |")
                    print("                | 2 - Subtraction                          |")
                    print("                | 3 - Miltiplcation                        |")
                    print('                | 4 - Division                             |')
                    print('                | 5 - Exponent                             |')
                    print('                | 6 - Floor Division                       |')
                    print('                | 7 - Modulor                              |')
                    print('                *==========================================*')
                    print("                      x - EXIT ARITHMETIC OPERATORS            ")
                    print("            *===================================================*")
                    yah = input('(⁠ ⁠╹⁠▽⁠╹⁠ ⁠)\nSeclect option above : ')
                    if yah == '1':
                        os.system('clear')
                        print('Adition')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *============ ~* Adidtion *~ =============*')
                        print('        | addition numbers, strings or variables. |')
                        print('        *=========================================*')
                        ###########################################################
                        # Additon
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : +')
                        a = 18
                        b = 20
                        c = a + b
                        print(c)
                        name = 'Kristin'
                        greet = ' Hello '
                        print(greet + name )
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '2':
                        os.system('clear')
                        print('Subtraction')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *========== ~* Subtraction *~ ============*')
                        print('        | Subtract numbers.                       |')
                        print('        *=========================================*')
                        ###########################################################
                        # Subtraction
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : +')
                        a = 18 
                        b = 20
                        c = a - b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue

                    elif yah == '3':
                        os.system('clear')
                        print('Multiplication')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *========== ~* Subtraction *~ ============*')
                        print('        | Multiply numbers.                       |')
                        print('        *=========================================*')
                        ###########################################################
                        # mmultiplication
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : -')
                        a = 18
                        b = 20
                        c = a * b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '4':
                        os.system('clear')
                        print('Division')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *============ ~* Division *~ =============*')
                        print('        | Divide numbers.                       |')
                        print('        *=========================================*')
                        ###########################################################
                        # divition
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : /')
                        a = 18 
                        b = 20
                        c = a / b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '5':
                        os.system('clear')
                        print('Exponent')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *============ ~* Exponent *~ =============*')
                        print('        | Multiply a base numbers by itself.      |')
                        print('        *=========================================*')
                        ###########################################################
                        # exponent
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : *')
                        a = 18 
                        b = 20
                        c = a ** b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '6':
                        os.system('clear')
                        print('Floor Division')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *========================= ~* Floor Dvision *~ ======================*')
                        print('        | Perform division and then result down to the nearest whole number. |')
                        print('        *====================================================================*')
                        ###########################################################
                        # floor divition
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : //')
                        a = 18
                        b = 20
                        c = a // b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '7':
                        os.system('clear')
                        print('Modulor')
                        print('        o⁠(⁠(⁠*⁠^⁠▽⁠^⁠*⁠)⁠)⁠o')
                        print('        *=========================== ~* Modulor *~ ==============================*')
                        print('        | Calculates the remainder of the division operation between two numbers.|')
                        print('        *========================================================================*')
                        ###########################################################
                        # modulor
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        print('SYMBOL : **')
                        a = 18 
                        b = 20
                        c = a % b
                        print(c)
                        print("\n############################################################################################")
                        e = input("\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == 'x':
                        break
                    else:
                        break
            elif f == '2':
                while True:
                    os.system('clear')
                    print('        ✧⁠◝⁠(⁠⁰⁠▿⁠⁰⁠)⁠◜⁠✧')
                    print("        *======================= ~* Comparison Operators *~ =======================*")
                    print("         Comparison Operators used to compare two value and return a boolean result ")
                    print("         True or False . These operators are fundamental for conditional logic and  ")
                    print("         controlling program flow.                                                  ")
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print('                            *==================================*')
                    print('                            | 1 - Equal                        |')
                    print('                            | 2 - Not equal                    |')
                    print('                            | 3 - Greater than                 |')
                    print('                            | 4 - Less than                    |')
                    print('                            | 5 - Greater than or equal        |')
                    print('                            | 6 - Less than or equal           |')
                    print('                            *==================================*')
                    print('                               x - EXIT COMAPARISON OPERATOR     ')
                    print("                         *==========================================*")
                    print('(⁠ﾉ⁠◕⁠ヮ⁠◕⁠)⁠ﾉ⁠*⁠.⁠✧')
                    yah = input('select options above : ')
                    if yah == '1':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('     ~* Equal *~ ==================================================*')
                        print('            check for equality between two values or objects.  ')
                        print('     *==============================================================*')
                        ###########################################################
                        # equal
                        print("RESULT:\n")
                        print('symbol : == ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris == woo)
                        print(kris == tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '2':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('         ~* Not equal *~ ==============================================*')
                        print('              check for UNEQUALITY between two values or objects.  ')
                        print('         *=============================================================*')
                        ###########################################################
                        # not equal
                        print("RESULT:\n")
                        print('symbol : != ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris != woo)
                        print(kris != tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '3':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('         ~* Greater than *~ ========================================================*')
                        print('                Checks if the left operand is greater than the right operand.')
                        print('         *==========================================================================*')
                        ###########################################################
                        # gt
                        print("RESULT:\n")
                        print('symbol : > ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris > woo)
                        print(kris > tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '4':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('         ~*Less than *~ ===========================================================*')
                        print('                  Checks if the left operand is less than the right operand.')
                        print('         *=========================================================================*')
                        ###########################################################
                        # lt
                        print("RESULT:\n")
                        print('symbol : < ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris < woo)
                        print(kris < tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '5':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('         ~* Greater than or Equal *~ =====================================================*')
                        print('              Checks if the left operand is greater than or equal to the right operand')
                        print('         *================================================================================*')
                        ###########################################################
                        # GT or e
                        print("RESULT:\n")
                        print('symbol : >= ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris >= woo)
                        print(kris >= tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '6':
                        os.system('clear')
                        print('(     •⁠ ‿⁠ •⁠  ')
                        print('         ~* Less than or Equal *~ ========================================================*')
                        print('              Checks if the left operand is less than or equal to the right operand. ')
                        print('         *================================================================================*')
                        ###########################################################
                        # lt or e
                        print("RESULT:\n")
                        print('symbol : <= ')
                        kris = 18
                        woo = 19
                        tin = 18
                        print(kris <= woo)
                        print(kris <= tin)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == 'x':
                        break
                    else:
                        break
            elif f == '3':
                while True:
                    os.system('clear')
                    print('        (⁠人⁠*⁠´⁠∀⁠｀⁠)⁠｡⁠*ﾟ⁠+')
                    print("        *============== ~* Logical Oprerators *~ ==============*")
                    print("                Logical True if both statements are true.   ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("                    *==============================*")
                    print('                    | 1 - and                      |')
                    print('                    | 2 - or                       |')
                    print('                    | 3 - not                      |')
                    print('                    *==============================*')
                    print('                       x - EXIT LOGICAL OPERATORS   ')
                    print("                 *=====================================*")
                    yah = input('•⁠ ‿⁠ • \nSelect options above :  ')
                    if yah == '1':
                        os.system('clear')
                        print('            (⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)⁠✧⁠*⁠。')
                        print('        ~** and **~ ')
                        print('             Returns True if both statements are true')
                        print('        ++++++++++++++++++++++++++++++++++++++++++++++++++++')
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        kris = 'pizza'
                        tin = 'buger'
                        woo = 'pizza'
                        print(kris == tin and tin == woo)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '2':
                        os.system('clear')
                        print('        ~** or **~ ')
                        print('            Returns True if one of the statements is true')
                        print('        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        kris = 'pizza'
                        tin = 'buger'
                        woo = 'pizza'
                        print(kris != tin or kris != woo)
                        print("\n############################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == '3':
                        os.system('clear')
                        print('            (⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)⁠✧⁠*⁠。')
                        print('        ~** not **~ ')
                        print('         	Reverse the result, returns False if the result is true')
                        print('        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                        print("\n############################################################################################")
                        print("RESULT:\n")
                        kris = 'pizza'
                        tin = 'buger'
                        woo = 'pizza'
                        print(not(kris and woo))
                        print(not(kris and tin))
                        print("\n)###########################################################################################")
                        e = input("(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\nPress 'enter' to CONTINUE : ")
                        if e == ' ':
                            continue
                        else:
                            continue
                    elif yah == 'x':
                        break
                    else:
                        break
            elif f == 'x':
                break
            else:
                break    
    elif unak == 'f':
        while True:
            os.system("clear")
            print("             (⁠ ⁠╹⁠▽⁠╹⁠ ⁠) \n            ~+Assigments +~")
            print('             used to assign values to values  ')
            print('        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("             *===================================*")
            print("             | 1 - Addition                      |")
            print("             | 2 - Subtraction                   |")
            print("             | 3 - Multiplication                |")
            print("             | 4 - Division                      |")
            print("             | 5 - Modulo                        |")
            print("             | 6 - Exponent                      |")
            print("             | 7 - Floor division                |")
            print('             *===================================*')
            print("                   x - EXIT LEARN ASSIGNMENTS         ")
            print("          *==========================================*")
            f = input("\n(⁠◠⁠‿⁠◕⁠) \n select options above :   ").lower()
            if f == '1':
                os.system('clear')
                print(" ~* Addition assign. *~ ================*")
                print('SYMBOL : +=')
                order = 5
                order += 2
                print(order)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input("Press ,'enter' to CONTINUE : ")
            elif f == '1':
                os.system('clear')
                print(" ~* Subtraction assign. *~ ================*")
                print('SYMBOL : -=')
                order = 5
                order += 2
                print(order)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input("Press ,'enter' to CONTINUE : ")    
            elif f == '1':
                os.system('clear')
                print(" ~* Multiplication assign *~ ================*")
                print('SYMBOL : *=')
                a = 18
                b = 20
                a *= 3
                b *= 5
                print(a)
                print(b)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input(" Press ,'enter' to CONTINUE : ")
            elif f == '1':
                os.system('clear')
                print(" ~*Division assign. *~ ================*")
                print('SYMBOL : /=')
                a = 18
                b = 20
                a /= 3
                b /= 5
                print(a)
                print(b)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input("Press ,'enter' to CONTINUE : ")
            elif f == '1':
                os.system('clear')
                print(" ~* Modulor *~ ================*")
                print('SYMBOL : %=')
                a = 18
                b = 20
                a %= 3
                b %= 5
                print(a)
                print(b)

                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input("Press ,'enter' to CONTINUE : ")
            elif f == '1':
                os.system('clear')
                print("~* Exponent assign. *~ ================*")
                print('SYMBOL : **=')
                a = 18
                b = 20
                a **= 3
                b **= 5
                print(a)
                print(b)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input(" Press ,'enter' to CONTINUE : ")
            elif f == '1':
                os.system('clear')
                print("~* floor Division assign. *~ ================*")
                print('SYMBOL : //=')
                a = 18
                b = 20
                a //= 3
                b //= 5
                print(a)
                print(b)
                print("*==================================================*")
                print(' •⁠ ‿⁠ • ')
                e = input("Press'enter' to CONTINUE : ")
            elif f == 'x':
                break
            else:
                break
    elif unak == 'x':
        break
    else:
        break    