import Bob
import Alice
import Letter
import Letterbox

class Person:

    def __init__(self, name):
        self.name = name

    def write_Letter(self):
        if self.name == Alice.name:
            print('Alice is writing a letter to Bob')

        elif self.name == Bob.name:
            print('Bob is wrting a letter to Alice')

        else:
            print('ERROR')

    def deliver_Letter(self):
        if self.name == Alice.name:
            print('Alice has delivered a letter to Bob')
            Letterbox.empty = False
            if Letterbox.empty == False:
                Letterbox.flagUp = True
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Bob has a new letter!')
            else:
                print(f'Flag Status (Has Letter?): {Letterbox.flagUp}, Bob has no new message')

        elif self.name == Bob.name:
            print('Bob has dilivered a letter to Alice')
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
person1.deliver_Letter()
person1.read_letter()


