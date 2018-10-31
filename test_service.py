import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from unittest import TestCase
from service import Service

'''
The selenium test should run on your development (local) 
machine. It does not (and should not)  be running on your 
cybera instance

The method bad_random in service.py DOES NOT work.  The 
assignment cannot be completed without mocking bad_random 
completely

For the test of bad_random, testing a mock of bad random 
always returning a value is sufficient (eg. make it always return 
10, and check that it does so)
'''

class Assign4TestService(TestCase):
    
    def test_bad_random(self):
        mockService = Service()
    
        #test case good data
        mockData = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
        with patch('service.open', mock_open(read_data = mockData)):
            mockService.bad_random = mock.Mock(return_value = 5)
            badNumber = Service.bad_random()
            fileLines = mockData.count('\n') + 1
        
        self.assertTrue(0 <= badNumber <= fileLines)
        
        #test case file not found 
        self.assertRaises(FileNotFoundError, Service.bad_random)
        
        #test case empty file
        mockData = ""
        with patch('service.open', mock_open(read_data = mockData)):
            fileLines = mockData.count('\n') + 1
        
        self.assertTrue(fileLines == 1)
        self.assertRaises(FileNotFoundError, Service.bad_random)
        
        #test case not a number 
        mockData = "A\nB\nC\nD\nE"
        with patch('service.open', mock_open(read_data = mockData)):
            fileLines = mockData.count('\n') + 1
        
        self.assertTrue(fileLines == 5)
        self.assertRaises(FileNotFoundError, Service.bad_random)
        
    
    def test_divide(self):
       
        mockService = Service()
        
        #test case divisor is zero
        mockService.bad_random = mock.Mock(return_value = 4)
        self.assertRaises(ZeroDivisionError, mockService.divide, 0)
        
        #test case dividend is zero
        mockService.bad_random = mock.Mock(return_value = 0)
        quotient = mockService.divide(4)
        self.assertTrue(quotient == 0)
        
        #test case dividend and divisor both same non zero value
        mockService.bad_random = mock.Mock(return_value = 7)
        quotient = mockService.divide(7)
        self.assertTrue(quotient == 1)        
        
        #test case non zero dividend and divisor different non zero value
        mockService.bad_random = mock.Mock(return_value = 6)
        quotient = mockService.divide(3)
        self.assertTrue(quotient == 2)              
        
        #test case non zero dividend and divisor not a number
        mockService.bad_random = mock.Mock(return_value = 9)
        self.assertRaises(TypeError, mockService.divide, 'string')
        
    
    def test_abs_plus(self):
        mockService = Service()
        
        #test case very large negative integer
        self.assertTrue(mockService.abs_plus(-2147483648) == 2147483649)
        
        #test case integer just less than zero
        self.assertTrue(mockService.abs_plus(-1) == 2)
        
        #test case zero
        self.assertTrue(mockService.abs_plus(0) == 1)
        
        #test case integer just larger than zero
        self.assertTrue(mockService.abs_plus(1) == 2)
        
        #test case very large positive integer
        self.assertTrue(mockService.abs_plus(2147483647) == 2147483648)
        
        #test case not a number
        self.assertRaises(TypeError, mockService.abs_plus, 'string')
        
    
    '''
    divide and bad_random are already tested
    therefore comlicated_function needs to test the modulus divsion only
    '''
    def test_complicated_function(self):
        mockService = Service()
        
        #Test case negative odd integer dividend
        mockService.divide = mock.Mock(return_value = 5)
        mockService.bad_random = mock.Mock(return_value = -5)
        modulus = mockService.complicated_function(1)
        self.assertTrue(modulus == (5, 1))
        
        #Test case negative even integer dividend
        mockService.divide = mock.Mock(return_value = 6)
        mockService.bad_random = mock.Mock(return_value = -6)
        modulus = mockService.complicated_function(1)
        self.assertTrue(modulus == (6, 0))
        
        #Test case zero dividend
        mockService.divide = mock.Mock(return_value = 4)
        mockService.bad_random = mock.Mock(return_value = 0)
        modulus = mockService.complicated_function(1)
        self.assertTrue(modulus == (4, 0))
        
        #Test case positive odd integer dividend
        mockService.divide = mock.Mock(return_value = 5)
        mockService.bad_random = mock.Mock(return_value = 5)
        modulus = mockService.complicated_function(1)
        self.assertTrue(modulus == (5, 1))
        
        #Test case positive even integer dividend
        mockService.divide = mock.Mock(return_value = 6)
        mockService.bad_random = mock.Mock(return_value = 6)
        modulus = mockService.complicated_function(1)
        self.assertTrue(modulus == (6, 0))
        
        #test case dividend not a number
        mockService.divide = mock.Mock(return_value = 7)
        mockService.bad_random = mock.Mock(return_value = "A")
        self.assertRaises(TypeError, mockService.complicated_function, 'string')
    

if __name__ == '__main__':
    unittest.main(verbosity=2)