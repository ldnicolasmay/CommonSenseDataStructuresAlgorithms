from my_array import MyArray
from my_set import MySet


def run():

    # Create array
    print("Initialize produce_array:")
    produce_array = MyArray("apples", "bananas", "cucumbers")

    print("produce_array:", end=" ")
    print(produce_array)
    
    # Read array at index
    print("Read produce_array at index 0:", end=" ")
    print(produce_array.read(0))
    print("Read produce_array at index 1:", end=" ")
    print(produce_array.read(1))
    # print("Read produce_array at index -2:", end=" ")
    # print(produce_array.read(-2))
    # print("Read produce_array at index 5:", end=" ")
    # print(produce_array.read(5))

    # Search array for item
    print("Search produce_array for item 'apples':", end=" ")
    print(produce_array.search("apples"))
    print("Search produce_array for item 'kiwis':", end=" ")
    print(produce_array.search("kiwis"))
    
    # Insert into array
    print("Insert into produce_array 'kiwis' at index 2...")
    produce_array.insert(item="kiwis", index=2)
    print("produce_array:", end=" ")
    print(produce_array)
    # produce_array.insert(item="strawberries", index=-2)
    # produce_array.insert(item="blueberries", index=5)

    # Delete from array
    print("Delete from produce_array item at index 2...")
    produce_array.delete(index=2)
    print("produce_array:", end=" ")
    print(produce_array)
    # produce_array.delete(index=-2)
    # produce_array.delete(index=5)
    print()

    # Create set
    print("Initialize produce_set:")
    produce_set = MySet("apples", "bananas", "cucumbers")

    print("produce_set:", end=" ")
    print(produce_set)

    # Read set at index
    print("Read produce_set at index 0:", end=" ")
    print(produce_set.read(0))
    print("Read produce_set at index 1:", end=" ")
    print(produce_set.read(1))
    # print("Read at index -2:", end=" ")
    # print(produce_set.read(-2))
    # print("Read at index 5:", end=" ")
    # print(produce_set.read(5))

    # Search set for item
    print(f"Search produce_set for item 'apples':", end=" ")
    print(produce_set.search(item="apples"))
    print(f"Search produce_set for item 'kiwis':", end=" ")
    print(produce_set.search(item="kiwis"))
    
    # Insert into set
    print("Insert into produce_set 'kiwis'...")
    produce_set.insert(item="kiwis")
    print("produce_set:", end=" ")
    print(produce_set)
    print("Insert into produce_set 'apples'...")
    produce_set.insert(item="apples")
    print("produce_set:", end=" ")
    print(produce_set)

    # Delete from set 
    print("Delete item 'kiwis' from produce_set...")
    produce_set.delete(item="kiwis")
    print("produce_set:", end=" ")
    print(produce_set)
    print("Delete item 'tangerines' from produce_set...")
    produce_set.delete(item="tangerines")
    print(produce_set)
    print()


if __name__ == "__main__":
    run()

