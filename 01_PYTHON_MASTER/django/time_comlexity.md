Certainly! Here’s a detailed breakdown of each time complexity with point-wise explanations and examples:

### 1. **Logarithmic: \(O(\log n)\)**
- **Definition:** The time complexity grows logarithmically as the input size increases.
- **Characteristics:**
  - Efficient for large datasets.
  - Reduces the problem size significantly with each step.
- **Example:**
  - **Binary Search:**
    - **Description:** Searches for a target value in a sorted array by repeatedly dividing the search interval in half.
    - **How it works:** 
      1. Compare the target with the middle element.
      2. If equal, return the index.
      3. If less, search the left half; if more, search the right half.
    - **Complexity:** \(O(\log n)\)

### 2. **Linear: \(O(n)\)**
- **Definition:** The time complexity grows linearly with the input size.
- **Characteristics:**
  - Directly proportional to the input size.
  - Each element is processed once.
- **Example:**
  - **Finding an Element in an Unsorted Array:**
    - **Description:** Iterate through each element to check if it matches the target value.
    - **How it works:**
      1. Loop through the array.
      2. Compare each element with the target.
    - **Complexity:** \(O(n)\)

### 3. **Linearithmic: \(O(n \log n)\)**
- **Definition:** The time complexity is a combination of linear and logarithmic growth.
- **Characteristics:**
  - Common in algorithms that divide and conquer.
  - Efficient for sorting large datasets.
- **Example:**
  - **Mergesort:**
    - **Description:** A divide-and-conquer sorting algorithm that divides the array into halves, sorts them, and merges them back.
    - **How it works:**
      1. Divide the array into two halves.
      2. Sort each half recursively.
      3. Merge the sorted halves.
    - **Complexity:** \(O(n \log n)\)

### 4. **Quadratic: \(O(n^2)\)**
- **Definition:** The time complexity grows quadratically as the input size increases.
- **Characteristics:**
  - Inefficient for large datasets.
  - Often arises from nested loops.
- **Example:**
  - **Bubble Sort:**
    - **Description:** A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    - **How it works:**
      1. Loop through the array.
      2. For each element, compare it with every other element.
    - **Complexity:** \(O(n^2)\)

### 5. **Exponential: \(O(c^n)\) for some fixed \(c > 1\)**
- **Definition:** The time complexity grows exponentially with the input size.
- **Characteristics:**
  - Highly inefficient for large inputs.
  - Often impractical for large datasets.
- **Example:**
  - **Naive Fibonacci Calculation:**
    - **Description:** A recursive approach to calculate the \(n\)th Fibonacci number.
    - **How it works:**
      1. \(F(n) = F(n-1) + F(n-2)\)
      2. Each call generates two more calls, leading to an exponential growth in calls.
    - **Complexity:** \(O(2^n)\)

### Summary Table

| Time Complexity   | Notation     | Characteristics                                 | Example                  |
|-------------------|--------------|------------------------------------------------|--------------------------|
| Logarithmic       | \(O(\log n)\)| Efficient for large datasets                    | Binary Search            |
| Linear            | \(O(n)\)     | Directly proportional to input size             | Finding an element       |
| Linearithmic      | \(O(n \log n)\)| Common in divide-and-conquer algorithms       | Mergesort                |
| Quadratic         | \(O(n^2)\)   | Inefficient for large datasets                   | Bubble Sort              |
| Exponential       | \(O(c^n)\)   | Highly inefficient for large inputs             | Naive Fibonacci          |

Understanding these complexities helps in selecting the right algorithm based on the problem requirements and input size.