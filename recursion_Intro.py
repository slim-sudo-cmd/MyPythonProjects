

""" iteration Method """
def find_sum_one(n):
   sum = 0
   for x in range (1,n+1):
      sum += x
   return sum

""" Recursion method """
def find_sum_two(m):
   if m == 1:return 1
   return m + find_sum_two(m-1)

"""fibonacci method """
def fib(n):
   if n == 0 or n ==1:return n
   return fib(n-1) + fib(n-2)


if __name__ == '__main__':
   print ("\n______ Hello & You Suck @ Programming ______\n")
   print (find_sum_one(5))
   print (find_sum_two(5))

