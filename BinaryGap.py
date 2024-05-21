def solution(A, K):
    K = K % len(A)
    return A[-K:] + A[:-K]
    # Implement your solution here
    pass
