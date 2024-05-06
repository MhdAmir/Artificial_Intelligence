#Rumor Barcelona mau rekrut Erling Haaland belum mereda. Rencananya, Blaugrana mau boyong sang striker tersebut di tahun 2026 mendatang!
#
#Diawali pada akhir Februari kemarin, Direktur Olahraga Barcelona, Deco menemui agennya Erling Haaland, Rafaela Pimenta. Pertemuan itu disinyalir salah satunya membahas soal rencana Barcelona mau rekrut Erling Haaland.
#
#Setelahnya, rumor tersebut tidak mereda juga. Diyakini, Barcelona memang butuh penyerang tengah baru mengingat Robert Lewandowski sudah uzur.
#
#Apalagi, rivalnya, Real Madrid dinilai akan mendapatkan Kylian Mbappe di musim panas nanti. Maka dinilai, Erling Haaland akan jadi pilihan yang tepat buat Barca.
#
#Dilansir dari Diario Sport, Barcelona diyakini akan merekrut Erling Haaland di tahun 2026. Itu ketika, masa jabatan Presiden Joan Laporta akan habis.
#
#Diyakini pula, Laporta akan coba mencuri hati para voters untuk memberikan suara di pemilihan presiden klub Barcelona selanjutnya. Kalau bisa datangkan Haaland, laporta bakal punya 'modal' oke buat jadi presiden klub untuk kali ketiga.
#
#Di tahun 2026 juga, neraca keuangan Barca diprediksi mulai sehat. Ketika itu pun Stadion Camp Nou selesai direnovasi, jadi kedatangan Haaland akan menjadi sebagai simbol kebangkitan baru.
#
#Kontrak Haaland di Manchester City akan habis di musim panas 2027. Maka setahun sebelum kontraknya habis, Barca dan tim-tim lain punya peluang untuk mendekati Haaland.

#2
# import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
# from nltk.tokenize import sent_tokenize, word_tokenize

# text="Rumor Barcelona mau rekrut Erling Haaland belum mereda. Rencananya, Blaugrana mau boyong sang striker tersebut di tahun 2026 mendatang! Diawali pada akhir Februari kemarin, Direktur Olahraga Barcelona, Deco menemui agennya Erling Haaland, Rafaela Pimenta. Pertemuan itu disinyalir salah satunya membahas soal rencana Barcelona mau rekrut Erling Haaland. Setelahnya, rumor tersebut tidak mereda juga. Diyakini, Barcelona memang butuh penyerang tengah baru mengingat Robert Lewandowski sudah uzur. Apalagi, rivalnya, Real Madrid dinilai akan mendapatkan Kylian Mbappe di musim panas nanti. Maka dinilai, Erling Haaland akan jadi pilihan yang tepat buat Barca. Dilansir dari Diario Sport, Barcelona diyakini akan merekrut Erling Haaland di tahun 2026. Itu ketika, masa jabatan Presiden Joan Laporta akan habis. Diyakini pula, Laporta akan coba mencuri hati para voters untuk memberikan suara di pemilihan presiden klub Barcelona selanjutnya. Kalau bisa datangkan Haaland, laporta bakal punya 'modal' oke buat jadi presiden klub untuk kali ketiga. Di tahun 2026 juga, neraca keuangan Barca diprediksi mulai sehat. Ketika itu pun Stadion Camp Nou selesai direnovasi, jadi kedatangan Haaland akan menjadi sebagai simbol kebangkitan baru.Kontrak Haaland di Manchester City akan habis di musim panas 2027. Maka setahun sebelum kontraknya habis, Barca dan tim-tim lain punya peluang untuk mendekati Haaland."

# tokenized_word=word_tokenize(text)
# print(tokenized_word)


# #3
# import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords

# teks = "Rumor Barcelona mau rekrut Erling Haaland belum mereda. Rencananya, Blaugrana mau boyong sang striker tersebut di tahun 2026 mendatang! Diawali pada akhir Februari kemarin, Direktur Olahraga Barcelona, Deco menemui agennya Erling Haaland, Rafaela Pimenta. Pertemuan itu disinyalir salah satunya membahas soal rencana Barcelona mau rekrut Erling Haaland. Setelahnya, rumor tersebut tidak mereda juga. Diyakini, Barcelona memang butuh penyerang tengah baru mengingat Robert Lewandowski sudah uzur. Apalagi, rivalnya, Real Madrid dinilai akan mendapatkan Kylian Mbappe di musim panas nanti. Maka dinilai, Erling Haaland akan jadi pilihan yang tepat buat Barca. Dilansir dari Diario Sport, Barcelona diyakini akan merekrut Erling Haaland di tahun 2026. Itu ketika, masa jabatan Presiden Joan Laporta akan habis. Diyakini pula, Laporta akan coba mencuri hati para voters untuk memberikan suara di pemilihan presiden klub Barcelona selanjutnya. Kalau bisa datangkan Haaland, laporta bakal punya 'modal' oke buat jadi presiden klub untuk kali ketiga. Di tahun 2026 juga, neraca keuangan Barca diprediksi mulai sehat. Ketika itu pun Stadion Camp Nou selesai direnovasi, jadi kedatangan Haaland akan menjadi sebagai simbol kebangkitan baru.Kontrak Haaland di Manchester City akan habis di musim panas 2027. Maka setahun sebelum kontraknya habis, Barca dan tim-tim lain punya peluang untuk mendekati Haaland."


# i_tokenized_word=word_tokenize(teks)

# i_stopwords = stopwords.words('indonesian')

# i_filtered_list = []
# for word in i_tokenized_word:
#   if word.casefold() not in i_stopwords:
#     i_filtered_list.append(word)

# print(i_filtered_list)

# #4

# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# import nltk
# nltk.download('punkt')
# nltk.download("stopwords")
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords

# teks = "Rumor Barcelona mau rekrut Erling Haaland belum mereda. Rencananya, Blaugrana mau boyong sang striker tersebut di tahun 2026 mendatang! Diawali pada akhir Februari kemarin, Direktur Olahraga Barcelona, Deco menemui agennya Erling Haaland, Rafaela Pimenta. Pertemuan itu disinyalir salah satunya membahas soal rencana Barcelona mau rekrut Erling Haaland. Setelahnya, rumor tersebut tidak mereda juga. Diyakini, Barcelona memang butuh penyerang tengah baru mengingat Robert Lewandowski sudah uzur. Apalagi, rivalnya, Real Madrid dinilai akan mendapatkan Kylian Mbappe di musim panas nanti. Maka dinilai, Erling Haaland akan jadi pilihan yang tepat buat Barca. Dilansir dari Diario Sport, Barcelona diyakini akan merekrut Erling Haaland di tahun 2026. Itu ketika, masa jabatan Presiden Joan Laporta akan habis. Diyakini pula, Laporta akan coba mencuri hati para voters untuk memberikan suara di pemilihan presiden klub Barcelona selanjutnya. Kalau bisa datangkan Haaland, laporta bakal punya 'modal' oke buat jadi presiden klub untuk kali ketiga. Di tahun 2026 juga, neraca keuangan Barca diprediksi mulai sehat. Ketika itu pun Stadion Camp Nou selesai direnovasi, jadi kedatangan Haaland akan menjadi sebagai simbol kebangkitan baru.Kontrak Haaland di Manchester City akan habis di musim panas 2027. Maka setahun sebelum kontraknya habis, Barca dan tim-tim lain punya peluang untuk mendekati Haaland."


# i_tokenized_word=word_tokenize(teks)

# i_stopwords = stopwords.words('indonesian')

# i_filtered_list = []
# for word in i_tokenized_word:
#   if word.casefold() not in i_stopwords:
#     i_filtered_list.append(word)

# factory = StemmerFactory()
# i_stemmer = factory.create_stemmer()
# i_stemmed_words = [i_stemmer.stem(word) for word in i_filtered_list]

# print(i_stemmed_words)

# #5

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

import nltk
nltk.download('punkt')
nltk.download("stopwords")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

teks = "Rumor Barcelona mau rekrut Erling Haaland belum mereda. Rencananya, Blaugrana mau boyong sang striker tersebut di tahun 2026 mendatang! Diawali pada akhir Februari kemarin, Direktur Olahraga Barcelona, Deco menemui agennya Erling Haaland, Rafaela Pimenta. Pertemuan itu disinyalir salah satunya membahas soal rencana Barcelona mau rekrut Erling Haaland. Setelahnya, rumor tersebut tidak mereda juga. Diyakini, Barcelona memang butuh penyerang tengah baru mengingat Robert Lewandowski sudah uzur. Apalagi, rivalnya, Real Madrid dinilai akan mendapatkan Kylian Mbappe di musim panas nanti. Maka dinilai, Erling Haaland akan jadi pilihan yang tepat buat Barca. Dilansir dari Diario Sport, Barcelona diyakini akan merekrut Erling Haaland di tahun 2026. Itu ketika, masa jabatan Presiden Joan Laporta akan habis. Diyakini pula, Laporta akan coba mencuri hati para voters untuk memberikan suara di pemilihan presiden klub Barcelona selanjutnya. Kalau bisa datangkan Haaland, laporta bakal punya 'modal' oke buat jadi presiden klub untuk kali ketiga. Di tahun 2026 juga, neraca keuangan Barca diprediksi mulai sehat. Ketika itu pun Stadion Camp Nou selesai direnovasi, jadi kedatangan Haaland akan menjadi sebagai simbol kebangkitan baru.Kontrak Haaland di Manchester City akan habis di musim panas 2027. Maka setahun sebelum kontraknya habis, Barca dan tim-tim lain punya peluang untuk mendekati Haaland."


i_tokenized_word=word_tokenize(teks)

i_stopwords = stopwords.words('indonesian')

i_filtered_list = []
for word in i_tokenized_word:
  if word.casefold() not in i_stopwords:
    i_filtered_list.append(word)

factory = StemmerFactory()
i_stemmer = factory.create_stemmer()
i_stemmed_words = [i_stemmer.stem(word) for word in i_filtered_list]

fdist = FreqDist(i_stemmed_words)
print(fdist)