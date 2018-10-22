
# coding: utf-8

# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[2]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[4]:


s = "Hi there Sam!"


# In[5]:


s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[6]:


planet = "Earth"
diameter = 12742


# In[11]:


print('The diameter of {x} is {y} kilometers'.format(x=planet, y=diameter))


# In[6]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[12]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[14]:


lst[3][1][2][0]


# In[14]:





# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[16]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[22]:





# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[17]:


def domain(mystr):
    return mystr.split('@')[1]


# In[18]:


domain('user@domain.com')


# In[26]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[24]:


def checker(str):
    if 'dog' in str:
        return 'True'


# In[25]:


checker('Is there is a dog here?')


# In[28]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[26]:


def counter(str):
    i = 0
    for 


# In[31]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[27]:


seq = ['soup','dog','salad','cat','great']


# In[29]:


list(filter(lambda str:str[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[36]:


def caught_speeding(speed, is_birthday):
    pass


# In[42]:


caught_speeding(81,True)


# In[43]:


caught_speeding(81,False)


# In[35]:


def caught(speed, is_birthday):
    if is_birthday==1:
        if speed<=65:
            print("No ticket")
        elif (speed>66)and(speed<85):
            print("Small ticket")
        else:
            print("Big ticket")
    elif is_birthday==0:
        if speed<=60:
            print("No ticket")
        elif (speed>61)and(speed<80):
            print("Small Ticket")
        else:
            print("Big Ticket")


# In[36]:


caught(81,False)


# In[37]:


caught(81,True)


# # Great job!
