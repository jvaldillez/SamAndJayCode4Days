class MyClass():
    #def __init__(self):
    classAttribute = 12345

    def classMethod(self):
        print ("hello world")


class Dog():
    kindOfAnimal = 'canine'


    # Constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print(self.name + " barked")
        #print("barked")

# class Tetronimo():
#     color
#     shape
#     numberOfBlocks
#     position


#     def updatePosition(newPosition):
#         position = newPosition




def main():
    Jay = Dog("Jay", "Blue")
    print("What color is Jay?", Jay.color)

    Sam = Dog("Sam", "Green")
    print("What color is Sam?", Sam.color)

    Jay.bark()
    Sam.bark() 
    


if __name__ == "__main__":
    main()
