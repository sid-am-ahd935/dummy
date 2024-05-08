import random
import string

user_list = []

def generate_id():
    tokens = list(string.ascii_letters+string.digits)
    uid = ''
    for i in range(6):
        uid += random.choice(tokens)

    return uid

class Amazon:
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.order_cart = None
        self.is_prime = 0       # 0 (high priority) is prime, 1 (low priority) is non_prime

    def buy_items(self):
        self.order_cart = [i for i in input("Enter you items:").split(",")]

    def get_details(self):
        self.id = generate_id()
        self.name = input("Enter name:")
        self.email = input("Enter email:")

    def buy_prime(self):
        self.is_prime = 1

ch = 'y'

while ch in ['y', 'Y']:
    new_user = Amazon()
    new_user.get_details()
    op = input("Want to order?[y/N]:") or "N"

    if op in ['y', 'Y']:
        new_user.buy_items()

    op = input("Do you want to buy prime? [y/N]:") or 'N'

    if(op in ['y', "Y"]):
        new_user.buy_prime()

    user_list.append(new_user)

    ch = input("Want to add more users? [y/N]:") or 'N'

user_list = sorted(user_list, key= lambda user: user.is_prime)

for user in user_list:
    if user.is_prime == 0:
        print(f"Hi {user.name}, your order has been shipped under Prime delivery.")
    else:
        print(f"Hi {user.name}, your order has been shipped via normal delivery.")
    user.order_cart.clear()
