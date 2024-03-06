bawahanlgsg(adi, burhan).
bawahanlgsg(burhan, bahrun).
bawahanlgsg(burhan, bisrin).

bawahanlgsg(bahrun, fahri).
bawahanlgsg(bahrun, farah).

bawahanlgsg(bisrin, ferdi).

atasanlgsg(AT, BW) :- bawahanlgsg(BW, AT).
anakbuah(AT, BW) :- bawahanlgsg(AT, BW).
anakbuah(AT, BW) :- bawahanlgsg(X, BW), anakbuah(AT, X).