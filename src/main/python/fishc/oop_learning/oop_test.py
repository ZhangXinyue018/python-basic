class Turtle:
    """an example for class"""
    name = 'turtle123'
    color = 'green'
    weight = 10
    legs = 4
# self相当于this
    def run(self):
        print(self.name, 'is running')

    def bite(self):
        print(self.name, 'bites')

tt = Turtle()
tt.bite()
tt.run()

class FlyingTurtle(Turtle):
    pass

ftt = FlyingTurtle();
ftt.run()