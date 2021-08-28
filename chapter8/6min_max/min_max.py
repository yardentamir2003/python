def list_creator():
    num_list = []
    while True:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        else:
            try:
                value = float(inp)
                num_list.append(value)
            except:
                print("Please enter a number")
                continue

    print("Maximum: ", max(num_list))
    print("Minimum: ", min(num_list))


list_creator()
