lulusSD(anas).
kebangsaan(anas, wni).
lahir(anas, 1962).
age(X, AGE) :- lahir(X, BIRTH), tahun_now(Y), AGE is (Y-BIRTH).
age_daftar(X, AGE) :- lahir(X, BIRTH), tahun_daftar(Y), AGE is (Y-BIRTH).
pensiun(X) :- lulusSD(X), age(X, AGE), AGE > 60.
lulus_pns(X) :- lulusSD(X), age_daftar(X, AGE), AGE < 36.
tahun_daftar(1990).
tahun_now(2023).