

def NotationCheck( filename ):
    #fp = open(filename)
    #testcode = fp.read()
    #fp.close()
    #fp = 0

    import CppHeaderParser

    try:
        cppHeader = CppHeaderParser.CppHeader( filename )

    except CppHeaderParser.CppParseError as e:
        print(e)
        sys.exit(1)

    totalErrors = 0
    #print("CppHeaderParser view of %s"%cppHeader)

    print("\nFree functions are:")
    for func in cppHeader.functions:
        print(" %s"%func["name"])
        if '_' in func['name']:
            print 'error (%d,%s)' % ( func['line_number'], 'use camal case for function names' )
            totalErrors += 1

    print("\nFree variables are:")
    for vars in cppHeader.variables:
        # {'line_number': 42, 'constant': 0, 'name': 'prop1', 'reference': 0, 'type': 'string', 'static': 0, 'pointer': 0}
        print "name:%s, type:%s, static:%s, const:%s"%( vars["name"], vars['type'], vars['static'], vars['constant'] )
        if vars['static']:
            if 's_' not in vars["name"]:
                print 'error (%d,%s)' % ( vars['line_number'], 's_ for static variables' )
                totalErrors += 1
        else:
            if 'g_' not in vars["name"]:
                print 'error (%d,%s)' % ( vars['line_number'], 'g_ for global variables' )
                totalErrors += 1

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
        if '_' in clss:
            sampleClass = cppHeader.classes[ clss ]
            print 'error (%d,%s)' % ( sampleClass['line_number'], 'use camal case for class names' )
            totalErrors += 1
        elif clss[0].isupper() == False:
            sampleClass = cppHeader.classes[ clss ]
            print 'error (%d,%s)' % ( sampleClass['line_number'], 'Capital letter for the first letter of class names' )
            totalErrors += 1



    for clss in cppHeader.classes:
        sampleClass = cppHeader.classes[ clss ]
        print("\nclasses:" + str(clss) )
        #print("Number of public methods %d"%(len(sampleClass["methods"]["public"])))
        print("Number of private properties %d"%(len(sampleClass["properties"]["private"])))
        print("Number of public  properties %d"%(len(sampleClass["properties"]["public"])))

        for cvars in sampleClass["properties"]["public"]:
            print "name: %s,  type:%s, static:%s" % ( cvars["name"], cvars["type"], cvars['static'] )
            if cvars['static'] and 's_' not in vars["name"]:
                print 'error (%d,%s)' % ( cvars['line_number'], 's_ for static variables' )
                totalErrors += 1
            elif 'm_' not in cvars["name"]:
                print 'error (%d,%s)' % ( cvars['line_number'], 'member variable m_' )
                totalErrors += 1

        for cvars in sampleClass["properties"]["private"]:
            print "name: %s,  type:%s, static:%s" % ( cvars["name"], cvars["type"], cvars['static'] )
            if cvars['static'] and 's_' not in vars["name"]:
                print 'error (%d,%s)' % ( cvars['line_number'], 's_ for static variables' )
                totalErrors += 1
            elif 'm_' not in cvars["name"]:
                print 'error (%d,%s)' % ( cvars['line_number'], 'member variable m_' )
                totalErrors += 1



    print '\n\n\n\n'
    print 'Analysis:'
    print 'Errors %d' % (totalErrors)
    print '\n\n\n\n'


import sys, getopt

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

if len(sys.argv) != 2:
    print '******'
    print 'notationcheck.py <inputfile>'
    print '******'
    exit(2)

filenameIn = ''
try:
  filenameIn = sys.argv[1]
except getopt.GetoptError:
  print 'notationcheck.py <inputfile>'
  sys.exit(2)

print 'filename: ' + filenameIn

NotationCheck( filenameIn )





