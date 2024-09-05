def longest_substring_k_unique(s, k):
    # Edge case: if k is greater than the number of unique characters in the string
    if len(set(s)) < k:
        return ""

    # Dictionary to store the frequency of characters in the current window
    char_count = {}

    start = 0  # Start pointer of the window
    max_len = 0  # Length of the longest valid substring
    max_substr = ""  # The actual longest substring with exactly k unique characters

    # Iterate over the characters of the string using the end pointer
    end = 0  # Initialize end pointer
    for char in s:
        # Add the current character to the dictionary or update its frequency
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # If we have more than k unique characters, shrink the window from the start
        while len(char_count) > k:
            start_char = s[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                del char_count[start_char]
            start += 1

        # Check if we have exactly k unique characters and update the result
        if len(char_count) == k:
            current_len = end - start + 1
            print(current_len)
            if current_len > max_len:
                max_len = current_len
                max_substr = s[start:end + 1]

        end += 1  # Increment end pointer
        print(char_count, start, end, max_len, max_substr)

    return max_substr


# Example usage:
s = "aabacbebebe"
k = 3
result = longest_substring_k_unique(s, k)
print("Longest substring with exactly", k, "unique characters is:", result)
