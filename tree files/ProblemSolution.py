"""
Expand the Tree class to find songs 
that are between a certain time. Let's 
say you wanted all songs between 90 
and 300 seconds. You could call the 
function with those 2 inputs and it 
would return all of the songs in that 
time.
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
                return self._contains(length, node.left)
        else: # Right
            # The length belongs on the right side.
            if node.right is None:
                # did not find it
                return False
            else:
                # It is deeper call the funciton again
                return self._contains(length, node.right)

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
    
    def find_songs_between(self, min, max):
        """
        Finds the songs in the tree between 
        the min and max values
        """
        yield from self._find_songs_between(min, max, self.root)

    def _find_songs_between(self, min, max, node):
        """
        This is used to find the songs of a given
        length. It is called recursively 
        """
        if (max >= node.length and min <= node.length): #Yield if the song is the right length
            yield node.name
        
        if node.length <= max and node.right != None: #If we are small get bigger
            yield from self._find_songs_between(min, max, node.right)
        if node.length >= min and node.left != None: #If we are to big get smaller
            yield from self._find_songs_between(min, max, node.left)


Songs = BST() #Create the Tree

keep_going = True
#Keep going until quit
while(keep_going): #Keep going until quit
    print(" 1: Add Song \n 2: Find between\n 3: Quit")
    again = input ("Chose an option: ")
    if again == "1": #Add a song
        name = input("What is the Name: ")
        length = int(input("How long is the song in Seconds: "))
        Songs.insert(length, name) #Add the song to the tree
        print("\n\n")

    if again == "2": #If Find between
        min = int(input("What is the min time in Seconds: "))
        max = int(input("What is the max time in Seconds: "))
        for x in Songs.find_songs_between(min, max): #Find songs between
            print(x) #Print each song
        print("\n\n")


    if again == "3": #Quit if no
        keep_going = False