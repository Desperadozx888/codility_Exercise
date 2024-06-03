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

#Count a minimal number of jumps from position X to Y.
def solution(X, Y, D):
    # Implement your solution here
    Z = Y - X
    if (Z % D) == 0:
        R = Z//D
        return R
    else:
        R = (Z//D) + 1
        return R
    pass

#PermMissingElem
def solution(A):
    N = len(A)
    # The sum of the first N+1 natural numbers
    total_sum = (N + 1) * (N + 2) // 2
    # Subtract the sum of the array elements from the total sum
    array_sum = sum(A)
    missing_element = total_sum - array_sum
    return missing_element
    pass

#TapeEquilibrium
def solution(A):
    # Implement your solution here
    total_sum = sum(A)
    left_sum = 0
    min_diff = float('inf')
    
    # Iterate through the array and calculate the difference
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
    pass

#FrogRiverOne
#Find the earliest time when a frog can jump to the other side of a river.
def solution(X, A):
    covered_positions = set()
    total_positions = 0

    for time in range(len(A)):
        position = A[time]
        if position not in covered_positions:
            covered_positions.add(position)
            total_positions += 1
        
        if total_positions == X:
            return time
    
    return -1


#PermCheck
#Check whether array A is a permutation.
def solution(A):
    # Implement your solution here
    n = len(A)
    seen = set()
    
    for number in A:
        if number < 1 or number > n:
            return 0
        if number in seen:
            return 0
        seen.add(number)
    
    return 1 if len(seen) == n else 0

    pass

#MaxCounters
#Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
def solution(N, A):
    # Implement your solution here
    counters = [0] * N
    current_max = 0
    last_max = 0
    
    for value in A:
        if 1 <= value <= N:
            if counters[value - 1] < last_max:
                counters[value - 1] = last_max
            counters[value - 1] += 1
            if counters[value - 1] > current_max:
                current_max = counters[value - 1]
        elif value == N + 1:
            last_max = current_max
    
    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max
    
    return counters
    
    pass


#MissingInteger
#Find the smallest positive integer that does not occur in a given sequence.
def solution(A):
    # Filter out non-positive numbers and create a set of positive numbers
    positive_numbers = set(x for x in A if x > 0)
    
    # Start checking from 1 upwards for the first missing positive integer
    smallest_missing = 1
    
    while smallest_missing in positive_numbers:
        smallest_missing += 1
    
    return smallest_missing
    pass


#PassingCars
#Count the number of passing cars on the road.
def solution(A):
    eastbound_cars = 0
    passing_pairs = 0
    
    for car in A:
        if car == 0:
            eastbound_cars += 1
        elif car == 1:
            passing_pairs += eastbound_cars
            if passing_pairs > 1_000_000_000:
                return -1
    
    return passing_pairs
#CountDiv
def solution(A, B, K):
    # Count the multiples of K up to B
    count_up_to_B = B // K
    
    # Count the multiples of K up to A-1
    count_up_to_A_minus_1 = (A - 1) // K
    
    # The count of multiples of K in the range [A, B]
    return count_up_to_B - count_up_to_A_minus_1
    pass

#GenomicRangeQuery
#Find the minimal nucleotide from a range of sequence DNA.
def solution(S, P, Q):
    N = len(S)
    M = len(P)

    # Create prefix sums for each nucleotide
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)
    prefix_T = [0] * (N + 1)

    for i in range(1, N + 1):
        prefix_A[i] = prefix_A[i - 1] + (1 if S[i - 1] == 'A' else 0)
        prefix_C[i] = prefix_C[i - 1] + (1 if S[i - 1] == 'C' else 0)
        prefix_G[i] = prefix_G[i - 1] + (1 if S[i - 1] == 'G' else 0)
        prefix_T[i] = prefix_T[i - 1] + (1 if S[i - 1] == 'T' else 0)

    result = []

    for k in range(M):
        start = P[k]
        end = Q[k] + 1

        if prefix_A[end] - prefix_A[start] > 0:
            result.append(1)
        elif prefix_C[end] - prefix_C[start] > 0:
            result.append(2)
        elif prefix_G[end] - prefix_G[start] > 0:
            result.append(3)
        else:
            result.append(4)

    return result

#MinAvgTwoSlice
#Find the minimal average of any slice containing at least two elements.
def solution(A):
    # Implement your solution here
    N = len(A)
    min_avg = float('inf')
    min_index = 0

    for i in range(N - 1):
        # Check slice of size 2
        avg2 = (A[i] + A[i + 1]) / 2.0
        if avg2 < min_avg:
            min_avg = avg2
            min_index = i

        # Check slice of size 3
        if i < N - 2:
            avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            if avg3 < min_avg:
                min_avg = avg3
                min_index = i

    return min_index
    pass

#We are given two strings P and Q, each consisting of N lowercase English letters. 
#For each position in the strings, we have to choose one letter from either P or Q, to construct a new string S, such that the number of distinct letters in S is minimal. 
#Our task is to find the number of distinct letters in the resulting string S.
def solution(P, Q):
    # Implement your solution here
    all_strings = generate_all_strings(P, Q)
    min_distinct_count = float('inf')
    
    for s in all_strings:
        distinct_count = len(set(s))
        if distinct_count < min_distinct_count:
            min_distinct_count = distinct_count
    
    return min_distinct_count
    pass
    

def generate_all_strings(P, Q):
    from itertools import product
    
    N = len(P)
    all_strings = set()
    
    for choices in product((0, 1), repeat=N):
        S = ''.join(P[i] if choice == 0 else Q[i] for i, choice in enumerate(choices))
        all_strings.add(S)
    
    return all_strings
