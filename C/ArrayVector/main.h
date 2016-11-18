//
// Created by rn30 on 18/11/16.
//

#ifndef C_MAIN_H
#define C_MAIN_H

// The data struct
typedef struct {
    int capacity;
    int current_max_index;
    int *arr;
} Vector;

// Core functions.
Vector *initialize();
int at(Vector* vec, int index);
int capacity(Vector* vec);
bool is_empty(Vector* vec);
void insert(Vector* vec, int index, int value);
int pop(Vector *vec);
void prepend(Vector* vec, int item);
void print(Vector* vec);
void push(Vector* vec, int value);
int size(Vector* vec);
int find(Vector *vec, int value);

// Helpers.
bool can_insert(Vector* vec);
bool is_in_bounds(Vector* vec, int index);
void increase_capacity(Vector *vec);
bool shrink(Vector *vec);



#endif //C_MAIN_H
