import Bob
import Alice
import Charli
import Letter
import Letterbox
import PostOffice
import Postman


class Person:

    def __init__(self, name):
        self.name = name

    def write_Letter(self):
        if self.name == Alice.name:
            print('Alice is writing a letter to Bob')

        elif self.name == Bob.name:
            print('Bob is writing a letter to Alice')

        else:
            print('ERROR')

    def encrypted(self):
        if self.name == Alice.name:
            print('Alice has encrypted the letter')
        elif self.name == Bob.name:
            print('Bob has encrypted the letter')
        else:
            print('ERROR')

    def decrypted(self):
        if self.name == Alice.name:
            print('Bob has decrypted the letter')
        elif self.name == Bob.name:
            print('Alice has decrypted the letter')
        else:
            print('ERROR')

    def deliver_Letter_To_PostOffice(self):
        if self.name == Alice.name:
            PostOffice.delivered = True
            if PostOffice.delivered == True:
                print('Alice has delivered a letter to the Post Office')
            else:
                print("Alice has not delivered her letter to the Post Office")

        elif self.name == Bob.name:
            PostOffice.delivered = True
            if PostOffice.delivered == True:
                print('Bob has dilivered a letter to the Post Office')
            else:
                print("Alice has not delivered her letter to the Post Office")

    def postman_Gets_Letter(self):
        if self.name == Alice.name:
            Postman.picksUpLetter = True
            if Postman.picksUpLetter == True:
                print(f'{Charli.name}, the Postman, has picked up the letter from the Post Office')
            else:
                print(f'{Charli.name}, the Postman, has NOT picked up the letter from the Post Office')

        elif self.name == Bob.name:
            Postman.picksUpLetter = True
            if Postman.picksUpLetter == True:
                print(f'{Charli.name}, the Postman, has picked up the letter from the Post Office')
            else:
                print(f'{Charli.name}, the Postman, has NOT picked up the letter from the Post Office')

    def postman_delivers_letter(self):
        if self.name == Alice.name:
            print(f'{Charli.name} has delivered the letter')
            Letterbox.empty = False
            if Letterbox.empty == False:
                Letterbox.flagUp = True
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Bob has a new letter!')
            else:
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Bob has no new message')

        elif self.name == Bob.name:
            print(f'{Charli.name} has delivered the letter')
            Letterbox.empty = False
            if Letterbox.empty == False:
                Letterbox.flagUp = True
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Alice has a new letter!')
            else:
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Alice has no new message')

        else:
            print('ERROR')

    def read_letter(self):
        if letterReader == Alice.name:
            Letter.read = True
            print(f'Letter Status (Read?): {Letter.read}, Alice read the letter')
        elif letterReader == Bob.name:
            Letter.read = True
            print(f'Letter Status (Read?): {Letter.read}, Bob has read the letter')

letterWritter = input('Who is writing the letter: ')
if letterWritter == 'Alice':
    letterReader = 'Bob'
elif letterWritter == 'Bob':
    letterReader = 'Alice'
else:
    print('ERROR')

person1 = Person(letterWritter)
person1.write_Letter()
person1.encrypted()
person1.deliver_Letter_To_PostOffice()
person1.postman_Gets_Letter()
person1.postman_delivers_letter()
person1.decrypted()
person1.read_letter()


