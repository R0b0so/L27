class Bird:
    def __init__(self):
        print("Bird is ready")
    def who_am_i(self):
        print("Bird")
    def swim(self):
        print("swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def who_am_i(self):
        print("Penguin")
    def run(self):
        print("run faster")
penguin = Penguin()
penguin.who_am_i()
penguin.swim()
penguin.run()
    