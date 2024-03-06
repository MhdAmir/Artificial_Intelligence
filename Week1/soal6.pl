canary(tweety).

cat(garfield).
cat(sylveator).

penguin(opus).

bird(X) :- canary(X).
bird(X) :- penguin(X).

eats(garfield, lasagna).
eats(B, seeds) :- bird(B).
eats(C, catfood) :- cat(C).

pet(C) :- cat(C).
pet(D) :- dog(D).
pet(CA) :- canary(CA).

mammal(C) :- cat(C).
%mammal(D) :- dog(D).

animal(M) :- mammal(M).
animal(B) :- bird(B).

attribute(M, tail, true) :- mammal(M).
attribute(B, tail, true) :- bird(B).
attribute(B, wing, true) :- bird(B).
attribute(B, feather, true) :- bird(B).

fly(X):-bird(X), X\=opus.
