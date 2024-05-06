laki(rudi).
laki(roy).
laki(ali).
laki(budi).
laki(jaya).
laki(sukri).

perempuan(asiah).
perempuan(uun).
perempuan(nuni).
perempuan(imas).
perempuan(siti).

menikah(rudi, asiah).
menikah(roy, uun).
menikah(ali, nuni).
menikah(budi, imas).

menikah(X, Y) :- menikah(Y, X).

anak(roy, rudi).
anak(roy, asiah).
anak(ali, roy).
anak(ali, uun).
anak(imas, roy).
anak(imas, uun).
anak(siti, ali).
anak(siti, nuni).
anak(sukri, ali).
anak(sukri, nuni).
anak(jaya, budi).
anak(jaya, imas).

ibu(I, A)  :- orangtua(I, A), perempuan(I).

orangtua(X, Y) :- anak(Y, X).
kakeknenek(X, Y) :- orangtua(X, Z), orangtua(Z, Y).

saudara(X, Y) :- ibu(Z, X), ibu(Z, Y), X\=Y.
ipar(X, Y) :- saudara(X, Z), menikah(Z, Y).
moyang(X, Y) :- orangtua(X, Y).
moyang(MYG, AN) :- orangtua(X, AN), moyang(MYG, X).