# DSA Problem Solutions
# 42 Classic Data Structure and Algorithm Problems

# ============================================================================
# NUMBER THEORY PROBLEMS
# ============================================================================

# Problem 1: Check if a Number is Prime
def is_prime(n):
    """
    Check if a number is prime.
    Input: Number
    Output: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
print("Problem 1 - Prime Check:")
print(f"is_prime(29) = {is_prime(29)}")  # True


# Problem 2: Pythagorean Triplets
def pythagorean_triplets(limit):
    """
    Generate all Pythagorean triplets with values smaller than limit.
    A Pythagorean triplet satisfies: a² + b² = c²
    """
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c_squared = a*a + b*b
            c = int(c_squared ** 0.5)
            if c < limit and c*c == c_squared:
                triplets.append((a, b, c))
    return triplets

# Test
print("\nProblem 2 - Pythagorean Triplets:")
triplets = pythagorean_triplets(20)
for triplet in triplets:
    print(f"{triplet[0]} {triplet[1]} {triplet[2]}")


# Problem 3: Maximum Marks in Each Semester
def max_marks_per_semester():
    """
    Find maximum marks scored by Raj in each semester.
    Marks must be between 0-100.
    """
    num_semesters = int(input("Enter no of semester: "))
    
    for sem in range(1, num_semesters + 1):
        num_subjects = int(input(f"Enter no of subjects in {sem} semester: "))
        marks_input = list(map(int, input(f"Marks obtained in semester {sem}: ").split()))
        
        valid_marks = []
        for mark in marks_input:
            if 0 <= mark <= 100:
                valid_marks.append(mark)
            else:
                print("You have entered invalid mark.")
        
        if valid_marks:
            max_mark = max(valid_marks)
            print(f"Maximum mark in {sem} semester: {max_mark}")


# Problem 4: Solve Equation a³ + a²b + 2a²b + 2ab² + ab² + b³
def solve_equation(a, b, c=None):
    """
    Solve the equation: a³ + a²b + 2a²b + 2ab² + ab² + b³
    Simplified to: a³ + 3a²b + 3ab² + b³ = (a+b)³
    """
    result = a**3 + 3*(a**2)*b + 3*a*(b**2) + b**3
    return result

# Test
print("\n\nProblem 4 - Equation Solution:")
a, b = 2, 3
result = solve_equation(a, b)
print(f"For a={a}, b={b}: Result = {result}")


# Problem 5: Calculate Tyres in Dealerships
def calculate_tyres():
    """
    Calculate total tyres in each dealership.
    Cars have 4 tyres, Bikes have 2 tyres.
    """
    num_dealerships = int(input("Enter number of dealerships: "))
    
    for i in range(1, num_dealerships + 1):
        cars, bikes = map(int, input(f"Dealership {i} (cars bikes): ").split())
        total_tyres = (cars * 4) + (bikes * 2)
        print(total_tyres)


# Problem 6: Minimum Discount Offer
def minimum_discount_offer():
    """
    Find items with minimum discount offer.
    Input: number of items, then item name, price, discount percentage
    """
    n = int(input("Enter number of items: "))
    items = {}
    min_discount = float('inf')
    
    for _ in range(n):
        item_data = input().split(',')
        name = item_data[0].strip()
        price = int(item_data[1].strip())
        discount_percent = int(item_data[2].strip())
        discount_amount = (price * discount_percent) / 100
        items[name] = discount_amount
        min_discount = min(min_discount, discount_amount)
    
    # Print all items with minimum discount
    for name, discount in items.items():
        if discount == min_discount:
            print(name)


# Problem 7: Find Factors
def find_factors(n):
    """
    Find all factors of a number.
    If negative, ignore the sign.
    If zero, return "No Factors".
    """
    n = abs(n)  # Ignore sign
    
    if n == 0:
        return "No Factors"
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

# Test
print("\n\nProblem 7 - Find Factors:")
factors = find_factors(54)
print(f"Factors of 54: {','.join(map(str, factors))}")


# ============================================================================
# ARRAY-BASED PROBLEMS
# ============================================================================

# Problem 8: Matrix Rotation by 90 Degrees Clockwise
def rotate_matrix_90(matrix):
    """
    Rotate a 2D matrix by 90 degrees clockwise.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

# Test
print("\nProblem 8 - Matrix Rotation:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate_matrix_90(matrix)
for row in rotated:
    print(row)


# Problem 9: Binary Search
def binary_search(arr, target):
    """
    Implement binary search to find target in sorted array.
    Returns index of target, -1 if not found.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test
print("\nProblem 9 - Binary Search:")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = binary_search(arr, target)
print(f"Index of {target}: {index}")


# Problem 10: Count Occurrences of Each Integer
def count_occurrences(arr):
    """
    Print the number of times each integer has occurred in the array.
    """
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    for num in sorted(count_dict.keys()):
        print(f"{num} occurs {count_dict[num]} times")

# Test
print("\nProblem 10 - Count Occurrences:")
arr = [1, 2, 3, 3, 4, 1, 4, 5, 1, 2]
count_occurrences(arr)


# Problem 11: Spiral Matrix Traversal
def spiral_traversal(matrix):
    """
    Traverse a matrix in spiral format (clockwise from outside).
    """
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Test
print("\nProblem 11 - Spiral Matrix Traversal:")
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
spiral = spiral_traversal(matrix)
print(" ".join(map(str, spiral)))


# Problem 12: Second Largest and Second Smallest
def second_largest_smallest(arr):
    """
    Find the second largest and second smallest element in array.
    Return -1 if they don't exist.
    """
    unique_sorted = sorted(set(arr))
    
    if len(unique_sorted) < 2:
        return -1, -1
    
    second_smallest = unique_sorted[1]
    second_largest = unique_sorted[-2]
    
    return second_smallest, second_largest

# Test
print("\nProblem 12 - Second Largest and Smallest:")
arr = [1, 2, 4, 7, 7, 5]
second_small, second_large = second_largest_smallest(arr)
print(f"Second Smallest: {second_small}")
print(f"Second Largest: {second_large}")


# Problem 13: Merge Intervals
def merge_intervals(intervals):
    """
    Merge all overlapping intervals.
    """
    if not intervals:
        return []
    
    # Sort intervals by start point
    intervals.sort()
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping intervals, merge them
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # Non-overlapping interval, add to result
            merged.append(current)
    
    return merged

# Test
print("\nProblem 13 - Merge Intervals:")
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged = merge_intervals(intervals)
print(merged)


# Problem 14: Matrix Identity Check
def are_matrices_identical(matA, matB):
    """
    Check if two given matrices are identical.
    """
    if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
        return False
    
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            if matA[i][j] != matB[i][j]:
                return False
    
    return True

# Test
print("\nProblem 14 - Matrix Identity Check:")
matA = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
matB = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
if are_matrices_identical(matA, matB):
    print("Matrices are identical")
else:
    print("Matrices are not identical")


# Problem 15: Reverse an Array
def reverse_array(arr):
    """
    Reverse the array in place.
    """
    return arr[::-1]

# Test
print("\nProblem 15 - Reverse Array:")
arr = [5, 4, 3, 2, 1]
reversed_arr = reverse_array(arr)
print(reversed_arr)


# Problem 16: Kth Largest Element
def find_kth_largest(nums, k):
    """
    Find the kth largest element in the array without sorting.
    Uses min-heap approach for efficiency.
    """
    import heapq
    return heapq.nlargest(k, nums)[-1]

# Test
print("\nProblem 16 - Kth Largest Element:")
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"Kth largest ({k}): {find_kth_largest(nums, k)}")


# Problem 17: Missing Number
def find_missing_number(nums):
    """
    Find the missing number in range [0, n].
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test
print("\nProblem 17 - Missing Number:")
nums = [3, 0, 1]
print(f"Missing number: {find_missing_number(nums)}")


# Problem 18: Find Duplicate Number
def find_duplicate(arr):
    """
    Find the duplicate number in array of size N+1 with elements 1 to N.
    """
    # Using Floyd's cycle detection
    slow = fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

# Test
print("\nProblem 18 - Find Duplicate:")
arr = [1, 3, 4, 2, 2]
print(f"Duplicate: {find_duplicate(arr)}")


# Problem 19: Merge Two Sorted Arrays
def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 in place.
    nums1 has size m+n, first m elements valid, last n are 0s.
    """
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    
    return nums1

# Test
print("\nProblem 19 - Merge Two Sorted Arrays:")
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
result = merge_sorted_arrays(nums1, 3, nums2, 3)
print(result)


# Problem 20: Rotate Array
def rotate_array(nums, k):
    """
    Rotate array to the right by k steps.
    """
    k = k % len(nums)  # Handle k > len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

# Test
print("\nProblem 20 - Rotate Array:")
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = rotate_array(nums, k)
print(result)


# Problem 21: Maximum Product Subarray
def max_product_subarray(nums):
    """
    Find subarray with maximum product.
    """
    if not nums:
        return 0
    
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        # If current number is negative, min_prod and max_prod swap
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result

# Test
print("\nProblem 21 - Maximum Product Subarray:")
nums = [2, 3, -2, 4]
print(f"Maximum product: {max_product_subarray(nums)}")


# Problem 22: Count Pairs with Given Sum
def count_pairs_with_sum(arr, target):
    """
    Count pairs of integers with given sum.
    """
    count = 0
    seen = {}
    
    for num in arr:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        seen[num] = seen.get(num, 0) + 1
    
    return count

# Test
print("\nProblem 22 - Count Pairs with Given Sum:")
arr = [1, 5, 7, -1, 5]
target = 6
print(f"Pairs with sum {target}: {count_pairs_with_sum(arr, target)}")


# Problem 23: Move Zeros to End
def move_zeros_to_end(nums):
    """
    Move all zeros to the end while maintaining relative order.
    """
    insert_pos = 0
    
    # First pass: move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1
    
    # Second pass: fill remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    
    return nums

# Test
print("\nProblem 23 - Move Zeros to End:")
nums = [0, 1, 0, 3, 12]
result = move_zeros_to_end(nums)
print(result)


# Problem 24: Majority Element
def find_majority_element(nums):
    """
    Find element that appears more than ⌊n/2⌋ times.
    Uses Boyer-Moore voting algorithm.
    """
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

# Test
print("\nProblem 24 - Majority Element:")
nums = [3, 2, 3]
print(f"Majority element: {find_majority_element(nums)}")


# Problem 25: Intersection of Two Arrays
def intersection_of_arrays(nums1, nums2):
    """
    Find intersection of two arrays (unique elements).
    """
    set1 = set(nums1)
    result = []
    
    for num in set(nums2):
        if num in set1:
            result.append(num)
    
    return result

# Test
print("\nProblem 25 - Intersection of Two Arrays:")
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection_of_arrays(nums1, nums2)
print(result)


# ============================================================================
# STRING-BASED PROBLEMS
# ============================================================================

# Problem 26: Move Hashes to Front
def move_hash_to_front(s):
    """
    Move all '#' characters to the front of the string.
    """
    hashes = s.count('#')
    non_hashes = s.replace('#', '')
    return '#' * hashes + non_hashes

# Test
print("\n" + "="*70)
print("STRING-BASED PROBLEMS")
print("="*70)
print("\nProblem 26 - Move Hash to Front:")
result = move_hash_to_front("Move#Hash#to#Front")
print(f"Result: {result}")


# Problem 27: Find Season by Month
def find_season(month):
    """
    Find season based on month number (1-12).
    """
    if month < 1 or month > 12:
        return "Invalid Month Entered"
    
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:  # 12, 1, 2
        return "Winter"

# Test
print("\nProblem 27 - Find Season:")
print(f"Month 6 -> {find_season(6)}")


# Problem 28: Counting Valleys
def counting_valleys(path):
    """
    Count number of valleys traversed in a path (U=up, D=down).
    Valley is sequence of steps below sea level.
    """
    level = 0
    valleys = 0
    
    for step in path:
        prev_level = level
        if step == 'U':
            level += 1
        else:  # step == 'D'
            level -= 1
        
        # If we just came back to sea level from below
        if prev_level == -1 and level == 0:
            valleys += 1
    
    return valleys

# Test
print("\nProblem 28 - Counting Valleys:")
path = "UDDDUDUU"
print(f"Valleys: {counting_valleys(path)}")


# Problem 29: String Compression
def compress_string(s):
    """
    Reduce string by replacing consecutive repeated characters with count.
    """
    if not s:
        return s
    
    result = []
    count = 1
    
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result.append(s[i] + str(count))
            count = 1
    
    return ''.join(result)

# Test
print("\nProblem 29 - String Compression:")
compressed = compress_string("aabbbbeeeeffggg")
print(f"Compressed: {compressed}")


# Problem 30: Reverse a String
def reverse_string(s):
    """
    Reverse the string.
    """
    return s[::-1]

# Test
print("\nProblem 30 - Reverse String:")
print(f"'Capgemini' reversed: {reverse_string('Capgemini')}")


# Problem 31: Valid Anagram
def is_valid_anagram(s, t):
    """
    Check if t is an anagram of s.
    """
    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)

# Test
print("\nProblem 31 - Valid Anagram:")
print(f"'anagram' and 'nagaram': {is_valid_anagram('anagram', 'nagaram')}")


# Problem 32: First Unique Character in String
def first_unique_character(s):
    """
    Find index of first non-repeating character, return -1 if none.
    """
    char_count = {}
    
    # Count occurrences
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

# Test
print("\nProblem 32 - First Unique Character:")
print(f"First unique in 'leetcode': {first_unique_character('leetcode')}")


# Problem 33: Find First Non-Repeated Character
def find_first_non_repeated(s):
    """
    Find the first character that does not repeat.
    """
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Test
print("\nProblem 33 - First Non-Repeated Character:")
print(f"First non-repeated in 'swiss': {find_first_non_repeated('swiss')}")


# Problem 34: Palindrome String Check
def is_palindrome(s):
    """
    Check if string is a palindrome.
    """
    clean = ''.join(char.lower() for char in s if char.isalnum())
    return clean == clean[::-1]

# Test
print("\nProblem 34 - Palindrome Check:")
print(f"'madam' is palindrome: {is_palindrome('madam')}")


# Problem 35: Longest Palindromic Substring
def longest_palindromic_substring(s):
    """
    Find the longest palindromic substring.
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(s)):
        # Check for odd-length palindromes
        pal1 = expand_around_center(i, i)
        if len(pal1) > len(longest):
            longest = pal1
        
        # Check for even-length palindromes
        pal2 = expand_around_center(i, i + 1)
        if len(pal2) > len(longest):
            longest = pal2
    
    return longest

# Test
print("\nProblem 35 - Longest Palindromic Substring:")
print(f"Longest palindrome in 'babad': {longest_palindromic_substring('babad')}")


# Problem 36: Longest Common Prefix
def longest_common_prefix(strs):
    """
    Find the longest common prefix string amongst array of strings.
    """
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    
    return strs[0]

# Test
print("\nProblem 36 - Longest Common Prefix:")
strs = ["flower", "flow", "flight"]
print(f"Common prefix: '{longest_common_prefix(strs)}'")


# Problem 37: String Rotation Check
def is_string_rotation(s, goal):
    """
    Check if s can become goal after some shifts.
    Shift = move leftmost character to rightmost.
    """
    if len(s) != len(goal):
        return False
    
    return goal in (s + s)

# Test
print("\nProblem 37 - String Rotation Check:")
print(f"'abcde' rotates to 'cdeab': {is_string_rotation('abcde', 'cdeab')}")


# Problem 38: Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    """
    Find length of longest substring without duplicate characters.
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Test
print("\nProblem 38 - Longest Substring Without Repeating:")
print(f"Length in 'abcabcbb': {length_of_longest_substring('abcabcbb')}")


# ============================================================================
# LINKED LIST PROBLEMS
# ============================================================================

class ListNode:
    """Node class for Linked List"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

print("\n" + "="*70)
print("LINKED LIST PROBLEMS")
print("="*70)

# Problem 39: Reverse a Linked List
def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    return prev

def create_linked_list(values):
    """Helper function to create linked list from list"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to list for printing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test
print("\nProblem 39 - Reverse Linked List:")
head = create_linked_list([1, 2, 3, 4, 5])
reversed_head = reverse_linked_list(head)
print(f"Reversed: {linked_list_to_list(reversed_head)}")


# Problem 40: Detect Loop in Linked List
def has_cycle(head):
    """
    Detect if linked list has a cycle using Floyd's algorithm.
    """
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# Test
print("\nProblem 40 - Detect Loop:")
head = create_linked_list([3, 2, 0, -4])
# head.next.next.next.next = head.next  # Create cycle (commented for safety)
print(f"Has cycle: {has_cycle(head)}")


# Problem 41: Find Middle Node
def find_middle_node(head):
    """
    Find the middle node of linked list.
    If two middle nodes, return the second one.
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Test
print("\nProblem 41 - Find Middle Node:")
head = create_linked_list([1, 2, 3, 4, 5])
middle = find_middle_node(head)
middle_val = middle.val if middle else None
print(f"Middle node value: {middle_val}")


# Problem 42: Merge Two Sorted Linked Lists
def merge_two_sorted_lists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list.
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next

# Test
print("\nProblem 42 - Merge Two Sorted Lists:")
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged = merge_two_sorted_lists(list1, list2)
print(f"Merged: {linked_list_to_list(merged)}")


print("\n" + "="*70)
print("All 42 DSA Problems Completed!")
print("="*70)
