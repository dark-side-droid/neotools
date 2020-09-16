#============================================
#                  NeoMerge                  
#
#    https://github.com/dark-side-droid
#============================================




selectednodes = hou.selectedNodes()


#Find and set merge node position
avgpos = [0,0]
nodecounter = 0
for node in selectednodes:
    node_pos = node.position()
    avgpos[0] += node_pos[0]
    avgpos[1] += node_pos[1]
    nodecounter = nodecounter + 1

avgpos[0] = avgpos[0] / nodecounter
avgpos[1] = (avgpos[1] / nodecounter) - 3


#Create merge node

basecontext = selectednodes[0].parent().path()    
basecontext = hou.node(basecontext)
mergenode = basecontext.createNode('merge')
mergenode.setPosition(avgpos)

#Connect inputs to merge

for node in selectednodes:
    mergenode.setNextInput(node)
    node.setSelected(False)
    

#Set node shape, color and display/render flags  
mergenode.setUserData('nodeshape','circle')
mergenode.setColor(hou.Color(0,.25,.75))
mergenode.setSelected(True)
mergenode.setRenderFlag(True)
mergenode.setDisplayFlag(True)
    

