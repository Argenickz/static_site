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




# These are some more tests that I ran while making this function.
def main():
    ORDERED_LIST = "1. This is item one\n2. This is item two\n3. This is item three"
    block_to_block_type(ORDERED_LIST)
    PARAGRAPH = "1. This is not an ordered list because\n2 the second item is missing the (.) in its pattern"
    block_to_block_type(PARAGRAPH)    

    PARAGRAPH = "- This is actually a PARAGRAPH because\nThe second line doesn't start with the unordered lis pattern"
    block_to_block_type(PARAGRAPH)

    UNORDERED_LIST = "- This is an actual unordered list, look how\n- This item starts with the pattern\n- This one too"
    block_to_block_type(UNORDERED_LIST)


    heading1 = "## is this a HEADING?"
    block_to_block_type(heading1)

    CODE = "```this is\nsome CODE```"
    not_code = "```this is not CODE and it doesn't match anything so is a normal PARAGRAPH"
    block_to_block_type(CODE)
    block_to_block_type(not_code)

    QUOTE = "> this is a QUOTE"
    block_to_block_type(QUOTE)

    listo = "- this is an unordered list"
    block_to_block_type(listo)

    PARAGRAPH = "this is a normal PARAGRAPH"
    block_to_block_type(PARAGRAPH)

    quotes = "> this is a QUOTE\n> this is another QUOTE"
    block_to_block_type(quotes)

    not_quotes = "> this is a QUOTE\nnot really, just a PARAGRAPH"
    block_to_block_type(not_quotes)

if __name__ == "__main__":
    main()



