#include <assert.h>
#include <stdbool.h>

int binary_search_it(int *arr, int len, int searched) {
    int min = 0,
            max = len - 1,
            middleIndex = 0;

    // Element found, or min <= max or similar.
    while (min <= max) {
        // Get middle element.
        middleIndex = (min + max) / 2;
        int middleElement = arr[middleIndex];

        // Compare middle element.
        if (middleElement == searched) {
            break;
        } else if (middleElement < searched) {
            // Search right half of sliced space.
            min = middleIndex + 1;
        } else {
            // Search left half of sliced space.
            max = middleIndex;
        }
    }

    // Handle not found.
    if (min > max) {
        return -1;
    } else {
        return middleIndex;
    }

}

int binary_search_rec_helper(int* arr, int min, int max, int searched) {
    int middleIndex = (min + max) / 2;
    int middleElement = arr[middleIndex];

    if (middleElement == searched) {
        return middleIndex;
    } else if (middleElement < searched) {
        min = middleIndex + 1;
    } else {
        max = middleIndex;
    }

    return binary_search_rec_helper(arr, min, max, searched);
}

int binary_search_rec(int *arr, int len, int searched) {
    int min = 0;
    int max = len - 1;
    return binary_search_rec_helper(arr, min, max, searched);
}

void test_search(bool iterative) {
    // searchFunction is a pointer to the function to be called to search the array.
    int (*searchFunction)(int*, int, int) = (iterative) ? binary_search_it : binary_search_rec;

    int array1[] = {1, 4, 7, 8, 12, 16, 19};
    int index = (*searchFunction)(array1, 7, 1); // Left-most element.
    assert(index == 0);
    index = (*searchFunction)(array1, 7, 19); // Right-most element.
    assert(index == 6);
    index = (*searchFunction)(array1, 7, 8); // Middle element.
    assert(index == 3);
    index = (*searchFunction)(array1, 7, 12); // Element in right half.
    assert(index == 4);
    index = (*searchFunction)(array1, 7, 4); // Element in left half.
    assert(index == 1);
}

// TESTS.
int main(void) {
    test_search(true);
    test_search(false);


    return 0;
}

