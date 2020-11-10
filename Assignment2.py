#!/usr/bin/env python
# coding: utf-8

# # Questions 1:
# 

# 
# Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.

# In[1]:


Simple_list=[]


# In[2]:


for i in range(10):
    num=int(input())
    if num % 2 == 0:
        Simple_list.append(num)
print(Simple_list)


# # Questions 3:

# You have seen in the videos how powerful dictionary data structure is. In this assignment, given a number n, you have to write a program that generates a dictionary d which contains (i, i*i), where i is from 1 to n (both included). Then you have to just print this dictionary d. Example: Input: 4 will give output as {1: 1, 2: 4, 3: 9, 4: 16} Input Format: Take the number n in a single line. Output Format: Print the dictionary d in a single line. Example: Input: 8 Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# In[3]:


dict1 ={}
n = int(input(" "))
for i in range(1,n+1):
    dict1[i]=i*i

print(dict1)


# # Questions 4:

# There is a robot which wants to go the charging point to charge itself. The robot moves in a 2-D plane from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2 The numbers after the direction are steps. Write a program to compute the distance between the current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer (use round() function for that and then convert it into an integer). Input Format: The first line of the input contains a number n which implies the number of directions to be given. The next n lines contain the direction and the step separated by a space. Output Format: Print the distance from the original position to the current position. Example: Input: 4 UP 5 DOWN 3 LEFT 3 RIGHT 2 Output: 2

# In[5]:


pos = {
    "x": 0, 
    "y": 0
}
z=int(input())
c=0
while (c!=z):

    n = input()
    c=c+1
    if not n:
        break

    direction,steps=n.split()
    if direction == "UP":
        pos["y"] += int(steps)
    elif direction == "DOWN":
        pos["y"] -= int(steps)
    elif direction == "LEFT":
        pos["x"] -= int(steps)
    elif direction == "RIGHT":
        pos["x"] += int(steps)
print (int(round((pos["x"]**2 + pos["y"]**2)**0.5)))


# 
