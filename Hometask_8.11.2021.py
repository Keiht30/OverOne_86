class House:
    def __init__(self, floor, windows, doors):
        self.floor = floor
        self.windows = windows
        self.doors = doors

    def watchman_multistory(self, watchman):
        print(f'{watchman} works as a watchman in a house with {self.floor} floors')


class SalonBeauty:
    def __init__(self, name, open_time, close_time):
        self.name = name
        self.open_time = open_time
        self.close_time = close_time

    def manicure(self, manicure_price):
        print(f'In the {self.name} salon there is a manicure cost {manicure_price} rubles')

    def haircut(self, haircut_price):
        print(f'In the {self.name} salon there is a haircut cost {haircut_price} rubles')


def time(open_time, close_time):
    print(f'Opening hours of the salon: {open_time} - {close_time}')


class HouseSalonBeauty(House, SalonBeauty):
    def __init__(self, floor, windows, doors, name, open_time, close_time):
        super(HouseSalonBeauty, self).__init__(floor, windows, doors)
        self.name = name
        self.open_time = open_time
        self.close_time = close_time

    def salon_opening_hours(self, opening_hours):
        if opening_hours < self.open_time or opening_hours > self.close_time:
            print(f'The salon is closed')
        else:
            print(f'The salon is open')


if __name__ == '__main__':
    multistory = House(45, 270, 135)
    multistory.watchman_multistory('Vasia')
    SalonBeauty_smile = SalonBeauty('Smile', 9, 22)
    SalonBeauty_smile.manicure(15)
    SalonBeauty_smile.haircut(25)
    Salon_dream = HouseSalonBeauty(25, 150, 70, 'Dream', 10, 22)
    Salon_dream.salon_opening_hours(22)

    print(multistory.__dict__)
    print(SalonBeauty_smile.__dict__)
    print(Salon_dream.__dict__)
