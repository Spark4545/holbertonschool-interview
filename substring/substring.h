#ifndef _SUBSTRING_H
#define _SUBSTRING_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int *find_substring(char const *s, char const **words, int nb_words, int *n);
int *init_indices(int len);
int *init_count(int nb_words);
int check_words(const char *s, const char **words, int i, int nb_words, int word_len, int *count);
int add_index_if_match(int *indices, int *n, int i, int match);

#endif /* _SUBSTRING_H */
