import unittest
import func

class Testmain( unittest.TestCase ):
    
    def test_siz(self):
        for i in range(0,10000):
            if i%10 == 0 and i != 0 :
                self.assertEqual(func.siz(i),1)
            else:
                self.assertEqual(func.siz(i),0)   
            
    
    def test_printt(self):
        for i in range(1,10000):
            tot = i/2 + i/3 - i/6 
            self.assertEqual(func.printt(i,v),tot)
            
        
if __name__ == '__main__':
    unittest.main()
        
        
        
    