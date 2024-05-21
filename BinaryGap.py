#Swap the Last int for the First int in the List
def solution(A, K):
    K = K % len(A)
    return A[-K:] + A[:-K]
    # Implement your solution here
    pass

#Binary Gap
def solution(self, N):
    # Convert the integer to a binary string and strip the '0b' prefix
    binary_rep = bin(N)[2:]
        
    # Initialize variables to track the current gap length and the maximum gap length
    max_gap = 0
    current_gap = 0
    inside_gap = False
        
    # Iterate over each character in the binary representation
    for char in binary_rep:
         if char == '1':
            if inside_gap:
                # If we are inside a gap and find a '1', update max_gap
                max_gap = max(max_gap, current_gap)
                current_gap = 0
                inside_gap = True  # We are inside a gap
            elif inside_gap:
                # If we are inside a gap and find a '0', increase current_gap
                current_gap += 1
        
    return max_gap

#OddOccurrencesInArray
def solution(A):
    # Implement your solution here
    result = 0
    for number in A:
        result ^= number
    return result
    pass
