/**
 * File which implements an auto-resizing vector.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <memory.h>

#include "main.h"

// CORE FUNCTIONS.
Vector *initialize() {
    Vector *prop_ptr = (Vector *) malloc(sizeof(Vector));
    prop_ptr->capacity = 8;
    prop_ptr->current_max_index = -1;
    prop_ptr->arr = (int *) malloc(prop_ptr->capacity * sizeof(int)); // Allocate array.
    return prop_ptr;
}

void print(Vector *vec) {
    printf("====================================\n");
    for (int i = 0; i < vec->current_max_index + 1; ++i) {
        printf("Val %d: %d\n", i, vec->arr[i]);
    }
}

int capacity(Vector *vec) {
    return vec->capacity;
}

int size(Vector *vec) {
    return vec->current_max_index + 1;
}

bool is_empty(Vector *vec) {
    return vec->current_max_index < 0;
}

int at(Vector *vec, int index) {
    if (is_in_bounds(vec, index)) {
        return vec->arr[index];
    } else {
        // TODO Blow up.
        return -1;
    }
}

void push(Vector *vec, int value) {
    if (!can_insert(vec)) {
        increase_capacity(vec);
    }
    // Add element to array.
    vec->arr[++vec->current_max_index] = value;
}

void insert(Vector *vec, int index, int value) {
    bool need_expanding = !can_insert(vec);
    if (need_expanding) {
        increase_capacity(vec);
    }

    // Move all elements at >= index over to the right.
    for (int i = vec->current_max_index + 1; i >= index; i--) {
        vec->arr[i] = vec->arr[i - 1];
    }
    vec->arr[index] = value;
    vec->current_max_index++;
}

void prepend(Vector *vec, int item) {
    insert(vec, 0, item);
}

int pop(Vector *vec) {
    int value = vec->arr[vec->current_max_index];
    vec->current_max_index--; // Decrease max index.

    // Automatically shrink as required.
    shrink(vec);

    return value;
}

int delete(Vector *vec, int index) {
    int to_return = at(vec, index); // Validates index.

    // Shift trailing elements in array.
    for (int i = index; i < size(vec); ++i) {
        vec->arr[i] = vec->arr[i + 1];
    }
    vec->current_max_index--;
    shrink(vec);

    return to_return;
}

void rem(Vector *vec, int value) {
    int current_index;
    while((current_index = find(vec, value)) != -1) {
        delete(vec, current_index);
    }
}

int find(Vector *vec, int value) {
    for (int i = 0; i < size(vec); ++i) {
        if (at(vec, i) == value) {
            return i;
        }
    }
    return -1;
}

// HELPERS.
bool is_in_bounds(Vector *vec, int index) {
    return index < vec->capacity;
}

bool can_insert(Vector *vec) {
    int insert_index = vec->current_max_index + 1;
    return is_in_bounds(vec, insert_index);
}

void increase_capacity(Vector *vec) {
    // Calculate new capacity.
    int old_capacity = vec->capacity;
    int new_capacity = 2 * old_capacity;

    // Allocate new array.
    int *arr = (int *) malloc(new_capacity * sizeof(int));

    // Copy data into new array.
    for (int i = 0; i < old_capacity; ++i) {
        arr[i] = vec->arr[i];
    }

    // Dispose of old array and update reference in Vector object.
    free(vec->arr);
    vec->arr = arr;
    vec->capacity = new_capacity;
}

bool shrink(Vector *vec) {
    bool resized = false;

    // Check if current utilisation is 1/4 of total capacity.
    if (vec->current_max_index + 1 < (vec->capacity / 4)) {
        // Create new array which is half the size of the current capacity.
        int new_capacity = vec->capacity / 2;
        int *arr = (int *) malloc(new_capacity * sizeof(int));
        // Copy over array.
        int copy_size = (vec->current_max_index + 1) * sizeof(int);
        memcpy(arr, vec->arr, (size_t) copy_size);
        resized = true;
    }

    return resized;
}

// TESTS.
int main(void) {
    Vector *vec = initialize();
    assert(is_empty(vec) == true); // Test is_empty.
    for (int i = 0; i < vec->capacity; ++i) {
        push(vec, i);
        assert(is_empty(vec) == false);
        assert(at(vec, i) == i);
    }

    // Test push and capacity.
    assert(capacity(vec) == 8);
    push(vec, 100);
    assert(capacity(vec) == 16);
    assert(at(vec, 8) == 100);
    assert(size(vec) == 9);

    // Test insert.
    insert(vec, 3, 87);
    assert(at(vec, 3) == 87);
    assert(at(vec, 9) == 100);
    assert(size(vec) == 10);

    // Test pop.
    int returnVal = pop(vec);
    assert(returnVal == 100);
    assert(size(vec) == 9);

    // Test prepend.
    prepend(vec, 31);
    assert(at(vec, 0) == 31);
    assert(size(vec) == 10);

    // Test delete.
    assert(at(vec, 2) == 1);
    delete(vec, 2);
    assert(size(vec) == 9);
    assert(at(vec, 2) == 2);

    // Test find.
    int found = find(vec, 0);
    assert(found == 1);

    // Test remove (single).
    assert(at(vec, 1) == 0);
    assert(size(vec) == 9);
    rem(vec, 0);
    assert(at(vec, 1) == 2);
    assert(size(vec) == 8);

    // Test remove (multiple).
    insert(vec, 3, 10);
    insert(vec, 5, 10);
    insert(vec, 7, 10);
    rem(vec, 10);
    assert(size(vec) == 8);
    assert(at(vec, 3) == 3);
    assert(at(vec, 5) == 5);
    assert(at(vec, 7) == 7);

    print(vec);

    return 0;
}

