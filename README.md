# Python practice — one file per question

Each file contains the question as a comment block at the top, the original
solution(s) unchanged, and a `if __name__ == "__main__":` block with the test
data so the file runs on its own.

Helper functions stay in the file of the question they belong to (e.g.
`ispalindrome` and `onetwo` live with the Good Numbers question).

| File | Question | Functions |
|---|---|---|
| `01_max_unique_letters.py` | Word with most letters appearing exactly once (ties → alphabetical) | `numuniqueletters`, `maxunique` |
| `02_good_numbers_product.py` | Product of Good Numbers × odd numbers | `ispalindrome`, `onetwo`, `good1`, `good2`, `ohmygod` |
| `03_vowels_once_word.py` | Word with most vowels appearing exactly once (ties → shortest) | `countvowels`, `highest` |
| `04_first_prime_digit_sum.py` | First number whose digit-sum is prime | `checkprime`, `idek` |
| `05_dict_sum_ab_keys.py` | Sum values whose keys start with A or B | `istilldk` |
| `06_char_frequency.py` | Character → count dictionary, case-insensitive | `abcd` |
| `07_keys_by_value.py` | All keys matching a given value | `abcde` |
| `08_swap_keys_values.py` | Swap keys and values, grouping duplicates | `swapvk` |
| `09_merge_dicts_add.py` | Merge two dicts, adding matching values | `mergedict` |
| `10_most_frequent_word.py` | Most frequent word (ties → alphabetical) | `slaydiva` |
| `11_group_anagrams.py` | Group words into anagram lists | `anagrams` |
| `12_shop_stock_order.py` | Stock vs order → purchased / insufficient | `potionshop` |
| `13_bubble_sort.py` | Bubble sort ascending | `bubblesort` |
| `14_binary_search.py` | Binary search for a target | `binarysearch` |
| `15_linear_search_count.py` | Count occurrences by linear search | `linearocc` |
| `16_bubble_sort_descending.py` | Bubble sort largest → smallest | `bubblesortupsidedown` |
| `17_insert_position_sorted.py` | Insert index to keep list sorted | `insertarg` |
| `18_bubble_sort_swap_count.py` | Count swaps + early-exit optimisation | `bubblesortcount`, `bubblesortopt` |
| `19_merge_sort.py` | Recursive merge sort | `merge`, `mergesort` |
| `20_merge_sort_inversions.py` | Count inversions with merge sort | `merge2`, `mergesort2` |
| `21_last_occurrence.py` | Index of last occurrence in a sorted list | `lastocc` |
| `22_merge_two_sorted_lists.py` | Merge two sorted lists without re-sorting | `merger` |
| `23_rotated_binary_search.py` | Binary search in a rotated sorted array | `rotbin` |
| `24_mountain_peak.py` | Peak index of a mountain array | `mountain` |
| `25_digit_sum_index_multiple_of_k.py` | Repeated digit sum at indices divisible by K | `loop`, `loop2`, `looprecursive`, `loop2recursive` |
| `26_todo_sort_dicts_by_score_name.py` | Merge sort dicts by score desc, name asc | *(stub)* |
| `27_todo_bubble_sort_strings.py` | Case-insensitive bubble sort of strings | *(stub)* |
| `99_scratch_snippets.py` | Loose built-in method tests | — |

Files marked `todo_` are questions that had no implementation yet — the question
comment and a stub are there.

Files with a known bug carry a `# NOTE (review):` comment at the bottom. The
code above the note is untouched.
