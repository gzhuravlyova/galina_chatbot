def test():
    while True:
        user_input = input("test: ")
        if user_input.lower() == "exit":
            print("Bye")
            break
        elif user_input.lower() ==  "hi":
            print("hello<3")
        elif user_input.lower() == "how are you":
            print("Fuck off")
        else:
            continue
test()
