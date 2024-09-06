def smallest_lexicographical_string(s):
    s = list(s)
    changed = False
    
    for i in range(len(s)):
        if s[i] != 'a':
            # Start changing characters from the first non-'a'
            while i < len(s) and s[i] != 'a':
                s[i] = chr(ord(s[i]) - 1)  # Replace by the previous character
                i += 1
            changed = True
            break
    
    # If no change was made, it means the string is full of 'a's
    if not changed:
        return ''.join(s)
    
    return ''.join(s)

# Example usage
# s = "hackerrank"
s = "aacde"
print(smallest_lexicographical_string(s))  # Output: gackerrank
