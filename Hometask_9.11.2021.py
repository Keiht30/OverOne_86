class House:
    def __init__(self, floor, apartments, windows, doors, roof_exit):
        self.floor = floor
        self.apartments = apartments
        self.apartments_num = [None] * apartments
        self.windows = windows
        self.doors = doors
        self.__roof_exit = roof_exit

    def build(self):
        print(f'The house was built {self.floor} of {self.apartments} apartments ')

    def __setitem__(self, apartments_num, family):
        self.apartments_num[apartments_num] = family

    def __getitem__(self, apartments_num):
        return self.apartments_num[apartments]

    def populate(self):
        print(f'The house was populated {self.apartments}')

    def watchman_multistory(self, watchman):
        print(f'{watchman} works as a watchman in a house with {self.floor} floors')

    def getRoof_exit(self):
        print(self.__roof_exit)

    def setRoof_exit(self, roof_exit):
        self.__roof_exit = roof_exit


class SalonBeauty:
    def __init__(self, name, open_time, close_time, price):
        self.name = name
        self.open_time = open_time
        self.close_time = close_time
        self.price = price

    def manicure(self, manicure_price):
        print(
            f"In the {self.name} salon there is a manicure cost {(self.price + (self.price * manicure_price // 100))}rubles")

    def haircut(self, hair_length):
        if hair_length < 30:
            print(f'In the {self.name} salon there is a haircut cost {(self.price + (self.price * 20 // 100))} rubles')
        elif 30 <= hair_length < 50:
            print(f'In the {self.name} salon there is a haircut cost {(self.price + (self.price * 50 // 100))} rubles')
        else:
            print(f'In the {self.name} salon there is a haircut cost {(self.price + (self.price * 80 // 100))} rubles')

    def time_work(self, open_time, close_time):
        print(f'Opening hours of the salon: {open_time} - {close_time}')


if __name__ == '__main__':
    multistory = House(45, 180, 270, 135, 45)
    multistory.build()
    multistory.populate()
    multistory.apartments_num[1] = 'Sidorov'
    multistory.apartments_num[2] = 'Petrov'
    multistory.apartments_num[3] = 'Smirnov'
    multistory.watchman_multistory('Vasia')
    SalonBeauty_smile = SalonBeauty('Smile', 9, 22, 50)
    SalonBeauty_smile.manicure(20)
    SalonBeauty_smile.haircut(50)
    # print(multistory.__dict__)
    # print(SalonBeauty_smile.__dict__)
