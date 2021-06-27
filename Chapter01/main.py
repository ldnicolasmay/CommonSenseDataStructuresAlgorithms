from my_array import MyArray


def run():

    # Create array

    print("Initialize produce_array:")
    produce_array = MyArray("apples", "bananas", "cucumbers")

    print("produce_array:", end=" ")
    print(produce_array)

    
    # Read

    print("Read at index 0:", end=" ")
    print(produce_array.read(0))
    print("Read at index 1:", end=" ")
    print(produce_array.read(1))
    # print("Read at index 5:", end=" ")
    # print(produce_array.read(5))
    

    # Search

    print("Search for item 'apples':", end=" ")
    print(produce_array.search("apples"))
    print("Search for item 'kiwis':", end=" ")
    print(produce_array.search("kiwis"))

    
    # Insert

    print("Insert 'kiwis' at index 2...")
    produce_array.insert(item="kiwis", index=2)
    print("produce_array:", end=" ")
    print(produce_array)
    # produce_array.insert(item="strawberries", index=-2)
    # produce_array.insert(item="starfruits", index=5)


    # Delete

    print("Delete item at index 2...")
    produce_array.delete(index=2)
    print("produce_array:", end=" ")
    print(produce_array)
    # produce_array.delete(index=-2)
    # produce_array.delete(index=5)


if __name__ == "__main__":
    run()

