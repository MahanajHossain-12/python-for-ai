import os

from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()


class APIConfig:
    def __init__(self, api_key=None, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig(max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(model="gpt-4", max_tokens=1000)

print("Default Key Loaded:", dev_config.api_key)
print("Custom Model:", prod_config.model)

# Access the configuration
print(dev_config.model)  # gpt-3.5-turbo
print(prod_config.model)  # gpt-4
print(prod_config.max_tokens)  # 1000


# _____________________________________________________#
class Dog:
    def __init__(
        self, name, breed
    ):  # init method is a constructor that initializes the attributes of the class
        self.name = name
        self.breed = breed


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


Tomy = Dog("Tomy", "BullDog")
Whiskers = Cat("Whiskers", "Orange")


# ______________________________________________________#
# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def meow(self):
        return f"{self.name} says meow!"


# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Create a cat - using positional argument
my_cat = Cat("Whiskers")
# Or with named argument
my_cat2 = Cat(name="Fluffy")

# Dog can do animal things (inherited)
print(my_dog.eat())  # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())  # Buddy says woof!

# Cat can do animal things (inherited)
print(my_cat.eat())  # Whiskers is eating
print(my_cat.sleep())  # Whiskers is sleeping

# Cat can also do cat things
print(my_cat.meow())  # Whiskers says meow!
