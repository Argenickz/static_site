from enum import Enum

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_blocktype(block):
# Todo this checks that the heading starts with 1-6 '#' characters, followed by a space and the heading text, if it doesn't start with the pattern or there are more than 6 '#' characters then it is not a heading.
    for number in range(1, 7):
        pattern = ("#" * number) + f" "
        if block.startswith(pattern):
            print(BlockType.heading)
            return BlockType.heading
        
    if block.startswith("```") and block.endswith("```"):
        print(BlockType.code)
        return BlockType.code
    
    if block.startswith(">"):
        print(BlockType.quote)
        return BlockType.quote
    
    # Todo this needs revision, every line in an unordered list block must start with '-' followed by a space, The problem with this condition as it is, is that I can start a paragraph with a '- ' and start a new line with out that pattern and it would be returned as a list instead of a paragraph. Maybe split the block by the new line '\n' and check that each one start with this pattern: '- '
    if block.startswith("- "):
        print(BlockType.unordered_list)
        return BlockType.unordered_list
    
    # Every line in an ordered list block must start with a number followed by a . character and a space. 
    # The number must start with 1 and increment by one for each line.
    # Todo, for the ordered list take a look at the unordered list thoughts and adjust this one accordingly, I recommend also splitting by the new line '\n' run a range for every item in the list and check that they all start with a set pattern.

    # If none of the conditions are met the block is a normal paragraph
    print(BlockType.paragraph)
    return BlockType.paragraph

        
        
    
        

heading1 = "## is this a heading?"
block_to_blocktype(heading1)

code = "```this is some code```"
not_code = "```this is not code and it doesn't match anything so is a normal paragraph"
block_to_blocktype(code)
block_to_blocktype(not_code)

quote = "> this is a quote"
block_to_blocktype(quote)

listo = "- this is an unordered list"
block_to_blocktype(listo)


paragraph = "this is a normal paragraph"
block_to_blocktype(paragraph)

