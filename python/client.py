import random

def greet(name):
    return f"Hello, {name}!"

class DummyClass:
    def __init__(self, value):
        self.value = value

    def increment_value(self):
        self.value += 1

    def get_value(self):
        return self.value

# Generate random numbers
def generate_random_numbers(count=5):
    return [random.randint(1, 100) for _ in range(count)]

if __name__ == "__main__":
    print(greet("Alice"))

    obj = DummyClass(10)
    obj.increment_value()
    print(f"Current value: {obj.get_value()}")

    numbers = generate_random_numbers()
    print(f"Random numbers: {numbers}")
        
        
def fun():
    print('hello')
    

def add(a,b):
    return a+b