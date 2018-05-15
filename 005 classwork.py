class Bucket():
    def __init__(self, size):
        self.size = size

    def change_size(self,size):
        self.size = size

    def check_size(self):
        print(f'This bucket size is {self.size}')

    def puth_in(self,some):
        if some.size < self.size:
            print(f'{some} inside the bucket')
        else:
            print(f'{some} to big to fit inside the bucket with size : {some.size}')


class Handbag(Bucket):
    def check_size(self):
        print(f'This bag size is {self.size}')

    def puth_in(self, some):
        if some.size < self.size:
            print(f'{some} inside the bag')
        else:
            print(f'{some} to big to fit inside the bag with size : {some.size}')


class Thing:
    def __init__(self, size):
        self.size = size


def main():
    korzina1 = Bucket(20)
    korzina2 = Bucket(10)
    korzina1.check_size()

    apple = Thing(10)
    korzina2.puth_in(apple)


if __name__ == '__main__':
    main()