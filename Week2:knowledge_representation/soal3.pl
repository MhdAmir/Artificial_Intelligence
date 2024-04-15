meninggal(korban).
sex(korban, perempuan).
korban(susi).
mengenal(jono, X) :- korban(X).
mengenal(suryo, X) :- korban(X).
mengenal(X, toni) :- korban(X).
mengenal(X, jono) :- korban(X).
mengenal(pembunuh, X) :- korban(X).
membenci(jono, susi).
membenci(suryo, toni).
membenci(toni, jono).
pembunuh(X) :- korban(Z), mengenal(Z, Y), membenci(Y, X), mengenal(X, Z).