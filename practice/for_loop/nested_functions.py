x="easy"
def word():
    string = 'Python'
    x = 5
    def number():
        print(string)
        print(x)

    number()

print(x) # acting as global variable here when we are calling number then the x inside the function is assigned

word()
