"""
 You have a large collection of sheet music
 and you want to have it all organized. You 
 decided that a tree is good for this. The 
 example will use the length of the song as 
 the value in the tree. This way we know how 
 to find it based on the length of the song.
"""

class BST:
    """
    A class for a Binary Search Tree in Python
    """

    class Node:
        """
        Each node will have 4 entries, the name,
        length, right value, and the left value
        """

        def __init__(self, length, name):
            self.name = name
            self.length = length
            self.right = None
            self.left = None

    def __init__ (self):
        self.root = None

    def insert(self, length, name):
        """
        Inserts the length into the Tree
        """

        if self.root is None: # If there is no root add a root
            self.root = BST.Node(length, name)
        else: # If not add it to the tree
            self._insert(length, name, self.root) 

    def _insert(self, length, name, node):
        """
        This function will keep calling itself 
        digging deeper and deeper into the tree
        until it finds the right spot
        """
        if (length == node.length): #if the length is already in the tree, 
                                # do not insert it
            return
        if length < node.length: #Left
            # The length belongs on the left side.
            if node.left is None:
                # An empty spot
                node.left = BST.Node(length, name)
            else:
                # It is deeper call the funciton again
                self._insert(length,name, node.left)
        else: # Right
            # The length belongs on the right side.
            if node.right is None:
                # An empty spot
                node.right = BST.Node(length,name)
            else:
                # It is deeper call the funciton again
                self._insert(length,name, node.right)

    def __contains__(self, length):
        """ 
        Looks for the song based on length
        """
        return self._contains(length, self.root) 

    def _contains(self, length, node):
        """
        This will call it self again and again 
        until it either reaches the end of the tree
        or finds the data
        """
        if (length == node.length): #if the length is in the tree
            return True
        if length < node.length: #Left
            # The length belongs on the left side.
            if node.left is None:
                # Did not find it
                return False
            else:
                # It is deeper call the funciton again
                self._contains(length, node.left)
        else: # Right
            # The length belongs on the right side.
            if node.right is None:
                # did not find it
                return False
            else:
                # It is deeper call the funciton again
                self._contains(length, node.right)

    def __iter__(self):
        """
        Returns all the songs for shortest to longest
        """            
        yield from self._traverse_forward(self.root)  


    def _traverse_forward(self, node):
        """
        This will call it self again and again
        until al values are returned. 
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.name
            yield from self._traverse_forward(node.right)

    def __reversed__(self):
        """
        Returns all the songs for longest to shortest
        """        
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        """
        This will call it self again and again
        until al values are returned.    
        """
        if node is not None:    # if we have not reached the end of the tree keep finding
            yield from self._traverse_backward(node.right)
            yield node.name # yeild the length only after reaching the right most branch
            yield from self._traverse_backward(node.left)

    def get_height(self):
        """
        Returns the Height of the Tree
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root) 

    def _get_height(self, node):
        """
        Returns the height of the tree
        """
        if node.left is None:
            # Found the end of the tree
            left_side = 1
        else:
            # Keep going
            left_side = self._get_height(node.left) + 1
        if node.right is None:
            # End of the Right side
            right_side = 1
        else:
            # Need to keep looking.
            right_side = self._get_height(node.right) + 1

        if right_side >= left_side: #only keep the biger side, we want the height.
            return right_side
        else:
            return left_side


Songs = BST() #Create the Tree

keep_going = True
#Keep going until quit
while(keep_going): #Keep going until quit
    again = input ("Add a song (Y/N): ")
    if again == "Y": #If yes
        name = input("What is the Name: ")
        length = int(input("How long is the song in Seconds: "))
        Songs.insert(length, name) #Add the song to the tree
        print("\n\n")
    if again == "N": #Quit if no
        keep_going = False
for x in Songs: #Return the songs in order
    print(x)