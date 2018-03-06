
"""
- Function/class names don't have underscores
- m_, s_, g_ 
- p - pointer 
- c - constant 


Issue formatting (print):
error (line-number,issues) - other details...

"""


import CppHeaderParser

try:
    cppHeader = CppHeaderParser.CppHeader("test.cpp")

except CppHeaderParser.CppParseError as e:
    print(e)
    sys.exit(1)

#print("CppHeaderParser view of %s"%cppHeader)

print("\nFree functions are:")
for func in cppHeader.functions:
    print(" %s"%func["name"])

print("\nFree variables are:")
for vars in cppHeader.variables:
    # {'line_number': 42, 'constant': 0, 'name': 'prop1', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
    print "name:%s, type:%s, static:%s, const:%s"%( vars["name"], vars['type'], vars['static'], vars['constant'] )
    if 'array_size' in vars:
       print 'array: ' + vars['array_size']
	
print("\n#includes are:")
for incl in cppHeader.includes:
    print(" %s"%incl)

print("\n#defines are:")
for define in cppHeader.defines:
    print(" %s"%define)

print("\nclasses are:")
for clss in cppHeader.classes:
    print(" %s"%clss)

	
	

for clss in cppHeader.classes:
	sampleClass = cppHeader.classes[ clss ]
	print("\nclasses:" + str(clss) )
	#print("Number of public methods %d"%(len(sampleClass["methods"]["public"])))
	print("Number of private properties %d"%(len(sampleClass["properties"]["private"])))
	print("Number of public  properties %d"%(len(sampleClass["properties"]["public"])))
	
	for cvars in sampleClass["properties"]["public"]:
		print "name: %s,  type:%s, static:%s" % ( cvars["name"], cvars["type"], cvars['static'] )

		
