import unittest
import mystring

class TestString(unittest.TestCase):
    def testConstructor(self):
        st = mystring.MyString('blah blah')
        newst = st.reverse()
        self.assertEquals(newst, 'halb halb')

    def testArray(self):
        values = [ 'Bubba', 'Gump', 'Shrimp co' ]
        expecting = []
        for i in range(0, len(values)):
            self.assertEquals(value[i], expecting[i])
if __name__ == '__main__':
  unittest.main()
