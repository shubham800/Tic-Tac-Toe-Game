total = 0
while True:
    userInput = input("Enter your item prize and press q key to get your total bill: \n")
    if (userInput!='q'):
        total = total + int(userInput)
        print(f"Order total far is {total}")
    else:
        print(f"Your bill total is {total}. Thanks for shoping with us!")
        break

print("*******************************************")

class Library():
    def __init__(self, list_of_books, Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No author have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}){books}")

    def lend_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)


def main():
    # By deafault variables
    list_books = ['Cookbook', 'Sherlock Holmes', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    Harry = Library(list_books, Library_name)

    print(
        f"Welecome To {Harry.library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")

    Exit = False
    while (Exit is not True):
        _input = input("option:")
        print("\n")

        if _input == "q":
            Exit = True

        elif _input == "d":
            Harry.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            Harry.lend_book(_input3, _input2)

        elif _input == "a":
            _input2 = input("Book name:")
            Harry.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                Harry.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Harry.return_book(_input3, _input2)


if __name__ == "__main__":
    main()

print("*******************************************")

print("Select Your Operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")

while True:
    choice = input("Enter choice(+/-/*//): ")

    if choice in ('+', '-', '*', '/'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", num1+num2)

        elif choice == '-':
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '*':
            print(num1, "*", num2, "=", num1*num2)

        elif choice == '/':
            print(num1, "/", num2, "=", num1/num2)
        break
    else:
        print("Invalid Input")

print("*******************************************")

n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")

print("*******************************************")

while True:
    balance = 10000
    print("   ATM   ")
    print("1) Balance\n2) Withdraw\n3) Deposit\n4) Quit")
    try:
        Option = int(input("Enter Option:\n"))
    except Exception as e:
        print("Error:",e)
        print("Enter 1, 2, 3 or 4 only:\n")
        continue
    if Option==1:
        print("Balance:", balance)
    if Option==2:
        print("Balance:\n",balance)
        withdraw = float(input("Enter withdraw amount:\n"))
        if withdraw>0:
            wibalance = (balance-withdraw)
            print("Forwerd balance:",wibalance)
        elif withdraw>balance:
            print("No funds in account!")
        else:
            print("None withdraw made!")
    if Option==3:
        print("Balance:",balance)
        Deposite = float(input("Enter deposit amount:\n"))
        if Deposite>0:
            print("Forwerd Balance:", wibalance)
        else:
            print("None deposit made!")
    if Option==4:
        exit()

print("*******************************************")

lst = list()
total = 0
count = 0
while True:
    user = input("Enter your item prize and press q key to get your total bill:\n")
    if user!='q':
        lst.append(user)
        total = total + int(user)
        print("Your bill total so far:",total)
    else:
        break

print("Kirana Store")
for x in lst:
    count = count + 1
    print(f"{count}. {x}")
print("Your total bill is:", total)

print("*******************************************")

print("***Shubham Kumar Health Managments System***")
def getdate():
    import datetime
    return datetime.datetime.now()
while True:
    print("What do you want!\nPress w for Write or Press R for Read\nType 'exit' to close the program")
    RL = input("Enter> ")
    if RL=='W' or RL=='w':
        print("For whose do you want to Write.\nPress S for Shubham or Press V for Vinay or Press H for Harry")
        user = input("Enter> ")
        if user=='S' or user=='s':
            print("What do you want to write for Shubham!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                S = open("SF.txt","a")
                writeSF = input("Enter Food> ")
                S.write(f"[{str(getdate())}]")
                S.write(f"{writeSF}")
            elif user1=='E' or user1=='e':
                S = open("SE.txt","a")
                writeSE = input("Enter Exercise> ")
                S.write(f"[{str(getdate())}]")
                S.write(f"{writeSE}")
        if user=='V' or user=='v':
            print("What do you want to write for Vinay!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                V = open("VF.txt","a")
                writeVF = input("Enter Food> ")
                V.write(f"[{str(getdate())}]")
                V.write(f"{writeVF}")
            elif user1=='E' or user1=='e':
                V = open("SE.txt","a")
                writeVE = input("Enter Exercise> ")
                V.write(f"[{str(getdate())}]")
                V.write(f"{writeVE}")
        if user=='H' or user=='h':
            print("What do you want to write for Harry!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                H = open("HF.txt","a")
                writeHF = input("Enter Food> ")
                H.write(f"[{str(getdate())}]")
                H.write(f"{writeHF}")
            elif user1=='E' or user1=='e':
                H = open("SE.txt","a")
                writeHE = input("Enter Exercise> ")
                H.write(f"[{str(getdate())}]")
                H.write(f"{writeHE}")
    elif RL=="exit":
        break

    if RL=='R' or RL=='r':
        print("For whose file do you want to Read.\nPress S for Shubham or Press V for Vinay or Press H for Harry")
        user = input("Enter> ")
        if user=='S' or user=='s':
            print("Which file do you want to read for Shubham!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                S = open("SF.txt")
                F = S.read()
                print(F)
            elif user1=='E' or user1=='e':
                S = open("SE.txt")
                F = S.read()
                print(F)

        if user=='V' or user=='v':
            print("Which fiel do you want to read for Vinay!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                V = open("VF.txt")
                F = V.read()
                print(F)
            elif user1=='E' or user1=='e':
                V = open("SE.txt")
                F = V.read()
                print(F)

        if user=='H' or user=='h':
            print("Which do you want to read for Harry!\nPress F for Food or Press E for Exercise.")
            user1 = input("Enter> ")
            if user1=='F' or user1=='f':
                H = open("HF.txt")
                F = H.read()
                print(F)
            elif user1=='E' or user1=='e':
                H = open("SE.txt")
                F = H.read()
                print(F)
    elif RL=="exit":
        break
print("Thank you for using Shubham Kumar Health Managments Services.")

print("*******************************************")

a = 1
n = int(input("Enter 1 or greater for True or 0 for False> "))
u = int(input("How many rows do you want to print> "))
for i in range(1,u+1):
    if n>=1:
        print(a*"*")
        a += 1
    else:
        print(u*"*")
        u -= 1

print("*******************************************")

import random, time

print("***Welcome to the Snake Water Gun game***".center(100))
print("You have to choose a word from Snake/Water/Gun to win the game".center(100))
print("You have 10 chances".center(100))
cwins = 0
uwins = 0
draw = 0
for i in range(10):
    print(f"Chance No. {i+1}")
    while True:
        computer = random.choice(['snake','water','gun'])
        user = input("Enter your choice> ")
        if user == 'snake' or user == 'water' or user == 'gun':
            break
        else:
            print("Wrong Input!\nPlease enter only one from snake/water/gun.")

    if user == computer:
        draw += 1
        print(f"Computer Input: {computer}, Your Input: {user}")


    elif (user=='snake' and computer=='water') or (user=='water' and computer=='snake') or (user=='gun' and computer=='snake') or (user=='water' and computer=='gun'):
        uwins += 1
        print(f"Computer Input: {computer}, Your Input: {user}")


    else:
        cwins += 1
        print(f"Computer Input: {computer}, Your Input: {user}")
    i+=1

print()
print(f"Result is loading........")
time.sleep(5)

if uwins>cwins:
    print(f"Congratulation You won!\nYour Total Score {uwins}\n")
elif cwins>uwins:
    print(f"Sorry You Lose!\nComputer win\nComputer Score {cwins}")
else:
    print("This is Draw!")

print("**********************")

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4],}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('p')