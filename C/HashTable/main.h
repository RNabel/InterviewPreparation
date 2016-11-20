//
// Created by rn30 on 18/11/16.
//

#ifndef C_MAIN_H

typedef struct {
    char* key;
    char* val;
} KeyValuePair;

typedef struct {
    size_t size;
    KeyValuePair** data;
} HashTable;

// CORE FUNCTIONS.
HashTable* create(size_t size); // Create a hash map.
void destroy(HashTable* table);
void print(HashTable* table);
size_t hash(char *key, size_t m);
size_t get_index(HashTable *table, char *key, bool insert_search);
bool exists(HashTable *table, char *key);

#define C_MAIN_H

#endif //C_MAIN_H
