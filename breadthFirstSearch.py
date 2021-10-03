class Node(object):
    def __init__(self,value=0) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert (self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            pointer = self.root
            print(f"Root: {pointer.value}")
            print(f"search value: {value}")
            while(True):
                if (value < pointer.value):
                    # Move Left
                    if(not pointer.left):
                        pointer.left = newNode
                        return
                    pointer=pointer.left
                else:
                    if(not pointer.right):
                        pointer.right = newNode
                        return
                    pointer = pointer.right
                    
            

    def lookup(self, value):
        if self.root == None :
            print("Tree is Empty")
            return
        else:
            pointer = self.root
            print (pointer.left, pointer.right)
            while(pointer != None):
                if (pointer.value == value):
                    print("Found the value in tree")
                    return True
                elif (pointer.value > value):
                    pointer = pointer.left
                else:
                    pointer =pointer.right

            if pointer == None:
                print("Value is not present in tree")
                return False
    

    def breadthFirstSearch(self):
        # Good  -- For finding Shortest path
        #       -- Searches for closer nodes to parent/root node
        # Bad   -- Uses extra space.
        currentNode = self.root
        list_of_values = []
        queue_of_node = []
        queue_of_node.append(currentNode)
        while(len(queue_of_node)>0):
            # ideally pop will remove last element from list hence use index ie 0
            currentNode = queue_of_node.pop(0)
            list_of_values.append(currentNode.value)
            if(currentNode.left != None):
                queue_of_node.append(currentNode.left)
            if(currentNode.right != None):
                queue_of_node.append(currentNode.right)
        print(f"BFS = {list_of_values}")
        return list_of_values


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
tree.breadthFirstSearch()
            # 9
        # 4           20
    # 1       6   15      170



                

