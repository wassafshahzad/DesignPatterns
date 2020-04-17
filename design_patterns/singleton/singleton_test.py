from singleton import singleton
import unittest
@singleton
class TestSingletonResourceOne:
    def __init__(self):
        self.h=1
        pass
    def p(self):
        return "resource one"

    @staticmethod
    def st_method():
        return "called"   

@singleton
class TestSingletonResourceTwo:
    def __init__(self):
        pass
    
    def p(self):
        return "resource two"

class SingletonTest(unittest.TestCase):
    
    def setUp(self):
        self.r1 = TestSingletonResourceOne()
        self.r2 = TestSingletonResourceTwo()
    
    def test_issingleton(self):
        self.assertTrue(self.r1 == TestSingletonResourceOne())
        self.assertTrue(self.r2 == TestSingletonResourceTwo())
    
    def test_multiclass_singleton(self):
        self.assertTrue(self.r1 != self.r2)

    def  test_is_object_mutable(self):
        self.r1.h = "Test"
        self.assertTrue(self.r1.h == "Test")
    
    def test_instance_method_callable(self):
        self.assertTrue(self.r1.p() == "resource one")
        self.assertTrue(self.r2.p() == "resource two")
    

if __name__ == "__main__":
    print(TestSingletonResourceOne.st_method)

