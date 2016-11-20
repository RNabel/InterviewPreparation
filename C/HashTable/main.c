/**
 * File which implements an auto-resizing vector.
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <memory.h>
#include <stdint.h>
#include "main.h"

HashTable *create(size_t size) {
    HashTable *table = malloc(sizeof(HashTable));
    table->size = size;
    table->data = malloc(size * sizeof(KeyValuePair));
    return table;
}

void destroy(HashTable *table) {
    // TODO free each key and value.
    free(table->data);
    free(table);
}

void print(HashTable *table) {
    for (int i = 0; i < table->size; ++i) {
        KeyValuePair *pair = table->data[i];
        if (pair != NULL) {
            printf("%d: %s -> %s", i, pair->key, pair->val);
        }
    }
}

size_t hash(char *key, size_t m) {
    uint64_t hash = 0;

    while (*key && m--) {
        hash = hash * 31 + *key++;
    }

    return hash % m;
}

bool exists(HashTable *table, char *key) {
    return get_index(table, key, false) != -1;
}

size_t get_index(HashTable *table, char *key, bool insert_search) {
    size_t table_size = table->size;
    size_t index = hash(key, table_size);
    size_t first_index = index;
    bool found = false;
    bool is_null;

    // Break conditions:
    // a) NULL pointer found, found: false.
    // b) Element found with matching key, found: true.
    // c) Original index revisited.

    while (!(is_null = (table->data[index] == NULL))) {
        KeyValuePair *keyValuePair = table->data[index];

        bool equal = keyValuePair != NULL && strcmp(keyValuePair->key, key) != 0;
        if (equal) {
            found = true;
            break;
        }

        // Increase the index.
        index = (index + 1) % table_size;
        if (index == first_index) { // If first element is revisited, break.
            break;
        }
    }

    // If element found,
    // or loop was quit because null index found and searching for insert index.
    if (found || (is_null && insert_search)) {
        return index;
    } else { // Loop was quit because
        return -1;
    }
}

bool insert(HashTable *table, char *key, char *value) {
    size_t index = get_index(table, key, true);
    KeyValuePair *pair = malloc(sizeof(pair));
    // Copy key and value.
    char *keyCopy = malloc(strlen(key) * sizeof(char));
    strcpy(keyCopy, key);
    char *valueCopy = malloc(strlen(value) * sizeof(char));
    strcpy(valueCopy, value);

    table->data[index] = pair;

    bool success = index == -1 || (pair != NULL) || (keyCopy != NULL) || (valueCopy != NULL);
    if (success) { // Insert if insert index found and all allocations succeeded.
        pair->key = keyCopy;
        pair->val = valueCopy;
    }

    return success;
}

// TESTS.
int main(void) {
    HashTable *table = create(100);
    insert(table, "hi", "how's it going.");
    print(table);
    return 0;
}

