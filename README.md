# Neotools

A couple of python scripts that enhance day to day workflow by making it slightly faster.
Create a new tool at any houdini shelf, paste the code and add a hotkey.



## Neonull

Creates a null node that automatically places itself a small distance below your currently selected node.

Immediately asks for a name from the user and renames itself to 'OUT_'+name. If the name that the user
provided already exists, it renames itself by adding an integer at the end of the its name
just like any other houdini node.



## Neomerge

Creates a merge node that automatically places itself half way between the user's selected nodes and 
adds a small distance below that. Its inputs are automatically connected to the users selected nodes.
