# -------- List comprehension --------

'''
List comprehension is a compact way of creating lists with the simple one-liner formula [expression + context]. The context tells Python which elements to add to the new list. The expression defines what to do with each of those new elements before adding them. For example, the list comprehension statement
'''
[x for x in range(3)]
'''
creates the new list [0, 1, 2]. The context in this example is for x in range(3), so the loop variable x takes on the three values 0, 1, and 2. The expression x is very basic in this example: it simply adds the current loop variable to the list without modification. However, list comprehensions are capable of handling far more advanced expressions.
'''
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
options = [{'label': day, 'value': day} for day in days]
print(options)
'''
The context is for day in days, so we iterate over each weekday 'Mon',…, 'Sun'. The expression creates a dictionary with two key-value pairs, {'label': day, 'value': day}.
'''

'''
Here the dropdown menu will show the label 'Mon' and, if selected by the user, will associate the label with the value 'Mon' to it. The context consists of an arbitrary number of for and if statements. We could use an if statement within the list comprehension to filter results; for example, we can create dropdown options with only weekdays:
'''
other_options = [{'label': day, 'value': day}
                 for day in days if day not in ['Sat', 'Sun']]
print(other_options)
