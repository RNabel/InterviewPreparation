/**
 * File which implements an auto-resizing vector.
 */

#include <stdio.h>
#include <stdlib.h>

// The data struct
typedef struct {
    int size;
    int currentMaxIndex;
    int *arr;
} properties;

properties *initialize() {
    properties *prop_ptr = (properties *) malloc(sizeof(properties));
    prop_ptr->size = 8;
    prop_ptr->currentMaxIndex = 0;
    prop_ptr->arr = (int *) malloc(prop_ptr->size * sizeof(int)); // Allocate array.
    return prop_ptr;
}

int main(void) {
    properties *props = initialize();
    printf("%d\n", props->size);
    printf("%d\n", props->currentMaxIndex);
    for (int i = 0; i < props->size; ++i) {
        printf("%d\n", props->arr[i]);
    }

    return 0;
}

