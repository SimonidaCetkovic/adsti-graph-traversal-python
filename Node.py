class Node:
    def __init__(self, completeWordFlag):
        self.completeWordFlag = completeWordFlag
        self.children = [None] * 26
    
    def setChild(self, character: chr, completeWordFlag: bool):
        child = Node(completeWordFlag)
        self.children[ord(character)-97] = child
        return child
