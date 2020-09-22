# Neotools

A couple of python scripts that enhance day-to-day workflow by automating some very common repetitive tasks.
These tools are saved within your Houdini 'default.shelf', which itself is a file and can be moved
between houdini installations.


## Installation
1. Create a new shelf in houdini (Optional)
2. Right click on the shelf and add 'New Tool'
3. Paste the code in the 'Script' tab
4. Add a hotkey in the 'Hotkeys' tab
5. Accept

### Neonull

Creates a null node that automatically places itself a small distance below your currently selected node.

Immediately asks for a name from the user and renames itself to 'OUT_'+name. If the name that the user
provided already exists, it renames itself by adding an integer at the end of the its name
just like any other houdini node.

_Comment out (#) the 'null.setRenderFlag(True)' line of the code if you plan to use it in LOPs since nodes there do not have render flags and the code errors out.


### Neomerge

Creates a merge node that automatically places itself half way between the user's selected nodes and 
adds a small distance below that. Its inputs are automatically connected to the users selected nodes.


_Comment out (#) the 'mergenode.setRenderFlag(True)' line of the code if you plan to use it in LOPs since nodes there do not have render flags and the code errors out.
