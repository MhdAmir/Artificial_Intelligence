is_a(man, person).
is_a(woman, person).
is_a(oscar, man).
is_a(antje, woman).

is_married_to(oscar, antje).
is_married_to(X, Y) :- is_married_to(Y, X).

is_father_of(oscar, bernd).

is_cousin_of(bernd, susi).
is_cousin_of(X, Y) :- is_cousin_of(Y, X).

is_aunt_of(antje, susi).
is_uncle_of(oscar, susi).
