#   Rubahlah CFG berikut kedalam NLTK CFG fromstring:
#   Kalimat → Subyek Predikat
#   Kalimat → Subyek Predikat Keterangan
#   Subyek → Determinan KataBenda
#   Predikat → KataKerja KataBenda
#   Determinan → seorang, seekor
#   KataBenda → manusia, anjing, nasi, daging, air
#   KataKerja → makan, minum
#   Keterangan → kemaren, tadi
#   • lakukan percobaan dengan kalimat berikut
#   
#   “seekor anjing makan daging tadi” dan “seorang manusia minum air
#   kemaren”
#   
#   • Tampilkan tree-nya keduanya

from nltk.tokenize import word_tokenize
import nltk
groucho_grammar = nltk.CFG.fromstring("""
Kalimat -> Subyek Predikat | Subyek Predikat Keterangan
Subyek -> Determinan KataBenda
Predikat -> KataKerja KataBenda
Determinan -> 'seorang' | 'seekor'
KataBenda -> 'manusia' | 'anjing' | 'nasi' | 'daging' | 'air'
KataKerja -> 'makan' | 'minum'
Keterangan -> 'kemaren' | 'tadi'
""")

def parse_sentence(sentence):
    tokens = word_tokenize(sentence)
    parser = nltk.ChartParser(groucho_grammar)
    trees = list(parser.parse(tokens))
    return trees[0]

sentence1 = "seekor anjing makan daging tadi"
trees1 = parse_sentence(sentence1)
print(trees1)
trees1


sentence2 = "seorang manusia minum air kemaren"
trees2 = parse_sentence(sentence2)
print(trees2)
trees2
