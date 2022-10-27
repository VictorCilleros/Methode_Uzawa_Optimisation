# Methode_Uzawa_Optimisation
Implémentation de la méthode d'uzawa dans le cadre du cours d'optimisation


TD - Algorithmes d’Uzawa et des points int´erieurs
Soit N ≥ 1, γ > 0 et J ∈ C
1
(R
N , R) une fonction γ-convexe. De mani`ere ´equivalente, on a :
J(y) ≥ J(x) + ∇J(x) · (y − x) + γ
2
|x − y|
2
, ∀x, y ∈ R
N . (1)
Soit n ≥ 0 un entier et soit f1, . . . , fm des fonctions de classe C
1
et convexes sur R
N . On note
C := {x ∈ R
N , fi(x) ≤ 0 pour i = 1, . . . , m},
f(x) := (f1(x), f2(x), . . . , fm(x))T
et D+ := (R+)
m.
On suppose que C est non vide et on s’int´eresse au probl`eme suivant :
Trouver x ∈ C tel que J(x) ≤ J(y), ∀y ∈ C. (P)
