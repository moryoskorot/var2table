#!/usr/bin/python3
import sys
import os
# Need to pip3 install pyhcl
import hcl

# A script that recieves a variables.tf file and outputs a textfile with the table representation for a README.
# Requires pyhcl

# Input check
if len(sys.argv) != 2 : # Checks to see we got an argument
    print( "The application requires a single variables.tf file argument.")
    exit ()
if not os.path.isfile(sys.argv[1]) :
    print( "Argument files does not exist/is a directory.")
    exit ()

with open(sys.argv[1], 'r') as varfile:
    obj = hcl.load(varfile)
    
variables = obj['variable']
output = " | Name | Description | Type | Default | Required |\n | --- | --- | --- | --- | :-: |\n"
for variable in  variables:
    # Initialize a line
    table_line = ''

    # Gets the content of the current variable definition into 'Fields' for readability
    fields = variables[variable]

    # The name of the variable.
    table_line += " | " + variable 

    # The description of the variable
    if 'description' in  fields.keys():
        table_line +=  " | " + str(fields['description'])
    else : 
        table_line +=  " | TODO " 

    # The type of the variable
    if 'type' in  fields.keys():
        table_line +=  " | `" + str(fields['type'])+"`"
    else : 
        table_line +=  " | TODO " 

    # Default/Required
    if 'default' in  fields.keys(): 
        # The variable has a default value and is not required
        table_line +=  " | " + str(fields['default']) + " | no |\n"

    else :  
        # The variable does not have a default value, and is required
        table_line +=  " | n/a | yes |\n" 
    output += table_line

print (output)


