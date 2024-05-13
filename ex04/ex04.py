def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        
        indice_min = i
        for j in range(i+1, n):
            if tab[j] < tab[indice_min]:
                indice_min = j
        
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab

import random


tab = [random.randint(1, 100) for _ in range(15)]


tab_trie = tri_selection(tab)


print(tab_trie)
