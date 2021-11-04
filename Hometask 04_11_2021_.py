# #Hometask_14_1

class Dog:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def jump(self, jump_on):
        print(f'{self.name} jump on {self.height * jump_on} centimeters')

    def run(self, run_km):
        print(f'{self.name} runs at a speed of {run_km} km/h')

    def bark(self, bark_elisa):
        print(f'{self.name} when angry publishes {bark_elisa} ')

    # Hometask_14_1
    def change_name(self, new_name):
        setattr(dachshund, 'name', new_name)


if __name__ == '__main__':
    dachshund = Dog('Elisa', 2, 25, 15)
    dachshund.jump(3)
    dachshund.run(15)
    dachshund.bark('Woof! Woof! Woof!')
    dachshund.change_name(new_name=input('Введите новое имя для Вашего питомца: ').title())
    print(dachshund.__dict__)
