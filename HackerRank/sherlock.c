#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct letter_map {
    int count;
} letter_map;

void countLetterMap(letter_map * map, char* string);
int checkValid(letter_map * map);
int compareFrequencies(letter_map *map);

int main(int argv, char** argc) {

    int i = 0;
    char * stringInput = argc[1];
    letter_map map[26];
    memset(map, 0, sizeof(map));
    countLetterMap(map, stringInput);

    for(i = 0; i < 26; i++) {
        printf("Map %c is %d\n", i+'a', map[i].count);
    }
    if(checkValid(map)){//} && compareFrequencies(map)) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}

void countLetterMap(letter_map * map, char* string) {
    int i = 0;
    for(i = 0; i < strlen(string); i++) {
        map[string[i] - 'a'].count += 1;
    }
}

int compareFrequencies(letter_map *map) {
    int temp = 0, i = 0;

    for(i = 0; i < 26; i++) {
        if(map[i].count != 0 && temp == 0) {
            temp = map[i].count;
        } else if((map[i].count != temp) && (temp == 0)) {
            if(map[i].count == temp) continue;
        } else {
            return 0;
        }
    }
    return 1;
}

int checkValid(letter_map *map) {
    int i = 0;
    int freq = 0;
    int offByOne = 0;
    for(i = 0; i < 26; i++) {
        if(map[i].count != 0) {
            if(freq != 0) {
                freq = map[i].count;
            } else {
                if(freq - 1 == map[i].count) {
                    if(offByOne++) {
                        return 0;
                    }
                }
            }
        }
    }
    return 1;
}
