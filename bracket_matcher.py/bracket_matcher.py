def isBalanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

# Blok utama yang benar
if __name__ == "__main__":
    tests = [
        ("()", True),
        ("([]{})", True),
        ("[({)]", False),
        ("", True)
    ]
    
    for input_str, expected in tests:
        result = isBalanced(input_str)
        print(f"Input: '{input_str}' => {result} (Expected: {expected})")