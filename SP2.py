def conversation():
    greetings = "Hello"  
    print(greetings)
    
    while True:
        answer = input("... ")

        if answer in ('Hi', 'Hello'):
            a = input ("How is your day? ")
            if a in ('good', 'bad'):
                print ("Same as me")
            else:
                print ("mine was GREAT!")
            break 
        else:
            print("I didn't understand that. Please say 'Hi' or 'Hello'.")

if __name__ == "__main__":
    conversation()
