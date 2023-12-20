from itertools import product
def is_entailed(query, knowledge_base):
    # Evaluate the query and knowledge base using a simple truth table
    for assignment in product([True, False], repeat=len(query + knowledge_base)):
        assignment_dict = dict(zip(query + knowledge_base, assignment))
        
        # Check if the query is true while the knowledge base is false
        if all(assignment_dict[prop] for prop in query) and not any(assignment_dict[prop] for prop in knowledge_base):
            return False
    
    # If no counterexample is found, the query entails the knowledge base
    return True

# Example usage
input_string = input("Enter a rule: ")
input_string2 = input("Enter the querry: ")
# Convert the string into a list of characters

knowledge_base= list(input_string)
query = list(input_string2)
#knowledge_base = ['(','~','Q','V','~','P','V','R',')','^','(','~','Q','^','P',')','^','Q']
#query = ['R']

result = is_entailed(query, knowledge_base)
if result==True:
   print("The knowledge Base entails query")
else:
    print("The knowledge Base doesnot entail query")
    