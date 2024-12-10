
def count_characters(input_string): 
# Initialize an empty dictionary to store character counts 
    char_count = {} 
# Loop through each character in the input string 
    for char in input_string: 
# If the character is already in the dictionary, increment its count 
        if char in char_count: 
            char_count[char] += 1 
        else: 
# Otherwise, add the character to the dictionary with a count of 1 
            char_count[char] = 1 
    return char_count 
# Example usage: 
input_string = input("Enter a string: ") 
result = count_characters(input_string) 
print("Character counts:", result) 
