# Slicing is the process of carving out a substring
# string[start:stop:step]

'''
The start argument is the index at which we want to start the string and is included in the slice, and stop is the index at which we want the string to stop and is excluded from the slice. Forgetting that the stop index is excluded is a

common source of bugs, so bear it in mind. The step argument tells Python which elements to include, so a step of 2 would include every other element and a step of 3 would include every third element. Here is an example with a step size of 2:
'''
s = '----p-y-t-h-o-n----'
print(s[4:15:2])


'''
All three arguments are optional, so you can skip them to use the default values of start=0, stop=len(string), and step=1. Leaving out the start argument before the slicing colon indicates that the slice starts from the first position, and leaving out the stop argument ends the slice at the final element. Leaving out the step argument assumes a step of 1. Here we skip the step
'''
x = 'universe'
print(x[2:4])


'''
Here we specify the start but not the stop, and give a step of 2, so we get every other character, starting at the third character and going to the end of the string:
'''
print(x[2::2])


'''
You can also provide negative integers for all three arguments. A negative index for start or stop tells Python to count from the end. For example, string[–3:] would start slicing with the third-to-last element and string[–10:–5] would start slicing with the tenth-to-last element (included) and stop with the fifth-to-last element (excluded). A negative step size means that Python slices from the right to the left. For example, string[::–1] would reverse the string and string[::–2] would take every other character, starting from the last and moving forward toward the left.
'''
