def printNos(self,N):
        #Your code here
        if N==0:
            return
        else:
            self.printNos(N-1)
            print(N,end=" ")

def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        if n<=9:
            return n
        else:
            return n%10+self.sumOfDigits(n//10)

  def countDigits(self, n):
        '''
        :param n: given number
        :return: count of digits of n.
        '''
        # code here
        if n<=0 or n<=9:
            return 1
        else:
            return 1+self.countDigits(n//10)
