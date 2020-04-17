from design_patterns import singleton
@singleton
class HelloWorld:
    def __init__(self):
        self.name = "one instance"


h = HelloWorld()
r = HelloWorld()

if __name__ == "__main__":
    print(r == h)