def lines(lines):
        try:
            for line in lines:
                print(line)
        except KeyboardInterrupt:
             print("That's all folks")
        print("That's all wrong lines!")