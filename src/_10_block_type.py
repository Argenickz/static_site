from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

def block_to_block_type(block):
    """The 'block_to_block_type function' takes a text and returns what kind of block type that text is (e.g. if the block type is a quote(>), a heading(#), code (```) and so on)"""
# this checks that the HEADING starts with 1-6 '#' characters, followed by a space and the HEADING text, if it doesn't start with the pattern or there are more than 6 '#' characters then it is not a HEADING.
    for number in range(1, 7):
        pattern = ("#" * number) + f" "
        if block.startswith(pattern):
            return BlockType.HEADING
        
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        blocks = block.split("\n")
        for block in blocks:
            if not block.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
   
    # First check if the very first line starts with the pattern
    if block.startswith("- "):
        # If so split the list into a list of lines to check each for the pattern
        blocks = block.split("\n")
        # Run a loop for each item in the list
        for block in blocks:
            # If there is at least one of the items that doesn't start with the specified pattern for an unordered list, then the item is a PARAGRAPH
            if not block.startswith("- "):
                return BlockType.PARAGRAPH
        # Otherwise, the item is an unordered list, what else could it be?
        return BlockType.UNORDERED_LIST
    
    # Every line in an ordered list block must start with a number followed by a . character and a space. 
    # The number must start with 1 and increment by one for each line.
    
    # Check that the first item start with the pattern
    if block.startswith("1. "):
        # If so split the items by the new line
        blocks = block.split("\n")
        # Assign an index to check for a pattern
        index = 1
        # Run a loop for the items in the list
        for block in blocks:
            # If there is an item in the list that doesn't start with the pattern of an ordered list then is a PARAGRAPH
            if not block.startswith(f"{index}. "):
                return BlockType.PARAGRAPH
            # Increase the index, this increases the number in the ordered list and checks again
            index += 1
        # Finally, if they all check out this block is an ordered list.
        return BlockType.ORDERED_LIST
    # If none of the above conditions are met, the block is a normal PARAGRAPH
    return BlockType.PARAGRAPH




