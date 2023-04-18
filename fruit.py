class FruitList:
    def __init__(self, fruits):
        self.fruits = fruits

    def reverse_fruit_list(self):
        self.fruits.reverse()

    def append_to_fruit_list(self, fruit):
        self.fruits.append(fruit)

    def insert_cherry_before_apple(self, fruit):
        try:
            apple_index = self.fruits.index("apple")
            self.fruits.insert(apple_index, fruit)
        except ValueError as val_err:
            print(type(val_err).__name__, val_err, sep=": ")
        except IndexError as index_err:
            print(type(index_err).__name__, index_err, sep=": ")

    def remove_banana_from_list(self):
        try:
            self.fruits.remove("banana")
        except ValueError as val_err:
            print(type(val_err).__name__, val_err, sep=": ")

    def pop_last_fruit(self):
        try:
            return self.fruits.pop()
        except IndexError as index_err:
            print(type(index_err).__name__, index_err, sep=": ")
            return None

    def sort_fruit_list(self):
        self.fruits.sort()

    def clear_fruit_list(self):
        self.fruits.clear()

def main():
    # Create and print a list named fruit.
    fruit_list = FruitList(["pear", "banana", "apple", "mango"])
    print(f"original: {fruit_list.fruits}")

    fruit_list.reverse_fruit_list()
    print(f"reversed: {fruit_list.fruits}")

    fruit_list.append_to_fruit_list("orange")
    print(f"appended: {fruit_list.fruits}")

    fruit_list.insert_cherry_before_apple("cherry")
    print(f"inserted cherry: {fruit_list.fruits}")

    fruit_list.remove_banana_from_list()
    print(f"removed banana: {fruit_list.fruits}")

    popped_fruit = fruit_list.pop_last_fruit()
    print(f"popped: {popped_fruit}, remaining: {fruit_list.fruits}")

    fruit_list.sort_fruit_list()
    print(f"sorted: {fruit_list.fruits}")

    fruit_list.clear_fruit_list()
    print(f"cleared: {fruit_list.fruits}")

if __name__ == "__main__":
    main()