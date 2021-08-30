import timeit
def timer(function):
  def new_function():
    start_time=timeit.default_timer()
    function()
    elapsed=timeit.default_timer()-start_time
    print(' took:::{time} seconds to complete'.format(name=function._name_, time=elapsed))
  return new_function()

@timer
def addition():
  total=0
  for i in range(0,1000000):
       total+=i
  return total
