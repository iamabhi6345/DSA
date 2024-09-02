def find_extra_letter(s1: str, s2: str) -> str:
    # Ensure s2 is the longer string
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    extra_char = 0
    for char in s1:
        extra_char ^= ord(char)
    
    for char in s2:
        extra_char ^= ord(char)
    
    return chr(extra_char)

# Example usage
s1 = "abcdeg"
s2 = "abcdegh"
print(find_extra_letter(s1, s2))  # Output: 'e'
