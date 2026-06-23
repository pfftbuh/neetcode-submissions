class Solution:
    def isPalindrome(self, s: str) -> bool:
        keep_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        clean_text = "".join([char for char in s if char in keep_chars])
        print(list(clean_text.lower()))
        split_chars = list(clean_text.lower())
        is_palindrome = False
        if (len(split_chars) <= 1):
            is_palindrome = True
        else:
            for i in range(len(split_chars)//2):
                print(f"{split_chars[i]} and {split_chars[-1 - i]}")
                if split_chars[i] != split_chars[-1 - i]:
                    is_palindrome = False
                else:
                    is_palindrome = True
        return is_palindrome

        