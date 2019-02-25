import numpy as np
#Creating an array of shape 1,2 and is of the type int
a = np.ndarray(shape=(1,2),dtype = np.int_)
print("the shape is {shape}".format(shape = a.shape))
print("the array is {a}".format(a=a))
print()

#creating an array with values
a= np.array([1,2,3])
print("The array with values is+{a}".format(a=a))
a=np.array([(1,2,3),(4,5,6)])
print("the array with more than one more row is+{a}".format(a=a))
print()

#creating an array with empty values which is not exactly empty(shape,type,dim):
a= np.empty((2,3))
print("The empty array is {a}".format(a=a))

#creating an array full of ones:
a= np.ones((2,3))
print("The empty array is {a}".format(a=a))
print()

#creating an array of random of a typical size and shape(It takes only dim as the argument)
a= np.random.rand(5,4)
print("The random array is {a}".format(a=a))
print()

#creating an array from random that explicitly takes in value of shape as an argument:
a= np.random.random((2,3))
print("The random array that takes in more than one argumen:")
print(a)
print()

#Creating an array from a gaussian distribution
a= np.random.normal(size=(2,3))
print("The array with gaussian distribution a random numbers:")
print(a)
print()
a=np.random.normal(50,10,size=(2,3))
print("The array with mean as 50 and std deviation as 10")
print(a)
print()


#Creating a random array from integers in a range
a = np.random.randint(10)
print("Random number from range 10:")
print(a)
print("three other different ways of using the random integer generator ")
a= np.random.randint(0,10)
b=np.random.randint(0,10,size=5)
c=np.random.randint(0,10,size=(2,3))
print(a)
print()
print(b)
print()
print(c)
print()

#finding out the shape and size and dim of a array
a= np.random.random(size=(1,2,3))
print("The shape, size and dim of an array can be done as follows:")
print(a.shape)
print(a.size)
print(len(a.shape))
print()
print("Individual dim shapes can also be accessed ")
print(a.shape[0])
print(a.shape[1])
print(a.shape[2])

#Different mathematical operations on arrays
np.random.seed(693)#Used to create the same set of random numbers everytime
a = np.random.random(0,10,size= (2,3))



#slicing in an numpy array:




