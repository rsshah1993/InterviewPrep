# Time Complexity Notes
- Big-O notation -> describes the limiting nature of a function
    - Complexity as input size approaches infinity
    - Described as a function of `n` which is the input size.

- Constant time - O(1)
    - complexity is independent of input size
    - Example:
        ```python
        def get_first(x: List[int]) -> int:
            return x[0]
        ```

- Logarithmic Time - O(log n)
    - Reduces size of input data at each step, don't have to look at all of the data
    - base 2 for big O - log(x) = y iff 2^y = x
        - when x doubles y increases by 1
    - Example:
        ```python
        def binary_search(data: List[int], value: int) -> int:
            n = len(data)
            left = 0
            right = n - 1
            while left <= right:
                middle = (left + right) // 2
                if value < data[middle]:
                    right = middle - 1
                elif value > data[middle]:
                    left = middle + 1
                else:
                    return middle
            raise ValueError('Value is not in the list')
            
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(binary_search(data, 8))
        ```
    - An algorithm cannot be in logarithmic time if it must access all elements of the input data.

- Linear time - O(n)
    - Time complexity increases linearly with size of input data -- worst case scenario requires as many operations as size of input
    - Example:
        ```python
        def linear_search(data: List[int], value: int) -> int:
            for index in range(len(data)):
                if value == data[index]:
                    return index
            raise ValueError('Value not found in the list')

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(binary_search(data, 8))
        ```
- Quasilinear Time - O(n log n)
    - Where each element of the input data takes log time to process
    - Example: mergesort, timesort, heapsort
- Quadratic Time - O(n^2)
    - Each element requires a linear time operation
    - Example - nested for-loops