#============================================
#                  NeoNull                   
#
#    https://github.com/dark-side-droid
#============================================



selnode = hou.selectedNodes()

if selnode:
    #Get the selected node, its parent context and its position
    inputnode = selnode[0]
    inputnode.setSelected(False)
    inputnodepos = inputnode.position()
    geocontext = selnode[0].parent().path()
    
    #create a null in the context, set its input to be the selected node
    #set its position 3 graph units below it
    base = hou.node(geocontext)
    null = base.createNode('null')
    null.setInput(0,inputnode)
    null.setPosition(inputnodepos)
    null.move((0,-3))
    
    #Set its shape, colour and display/render flags
    null.setUserData('nodeshape','circle')
    null.setColor(hou.Color(0,.75,0))
    null.setSelected(True)
    null.setDisplayFlag(True)
    null.setRenderFlag(True)
    
    #Create name
    nullname = hou.ui.readInput('Enter a name')
    nullname = nullname[1] #string
    fullname = 'OUT_'+nullname
    try:
         null.setName(fullname)
         
    except:
        #search for all nodes in context that contain the fullname
        #count how many they are
        #add that many to the fullname and set it
        contextnode = hou.node(geocontext)
        contextnodechildren = contextnode.children()
        count = 0
        for child in contextnodechildren:
            if fullname in child.name():
                count += 1
        fullname+=str(count)
        null.setName(fullname)

    
else :
    hou.ui.displayMessage('Please select a node first')
