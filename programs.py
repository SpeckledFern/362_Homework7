def output_at(x):
   if(x%5 == 0):
      if(x%3 == 0):
         return "FizzBuzz"
      return "Buzz"
   elif(x%3 == 0):
      return "Fizz"
