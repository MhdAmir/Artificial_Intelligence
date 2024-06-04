from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

# Hierarki atau tree dari penyakit gastro usus
bagansakit=[
    [0,1,2,3,9],  # 20,21,22,23,29
    [0,1,2,4,10], # 20,21,22,24,30
    [0,1,2,5,6,9], # 20,21,22,25,26,29
    [1,7,11],     # 21,27,31
    [8,2,5,12]    # 28,22,25,32
] 

bagangejala=[
    [1,2,4,5],
    [4,5,6],
    [4,7],
    [4,8,9],
    [8,10],
    [4,5,9,11],
    [4,8,11,12],
    [4,13],
    [1,2,3,4],
    [14,15],
    [14,16],
    [14,17],
    [18,19]
]

penyakit=[
    "Staphylococcus aureus",
    "Jamur beracun",
    "Salmonellae",
    "Clostridium botulinum",
    "Campylobacter"
]

txtgejala = [
    "1. Sering mengalami buang air besar (> 2 kali)?",
    "2. Mengalami berak encer?",
    "3. Mengalami berak berdarah?",
    "4. Merasa lesu dan tidak bergairah?",
    "5. Tidak selera makan?",
    "6. Merasa mual dan sering muntah (lebih dari 1 kali) ?",
    "7. Merasa sakit di bagian perut ?",
    "8. Tekanan darah anda rendah ?",
    "9. Anda merasa pusing ?",
    "10. Anda mengalami pingsan ?",
    "11. Suhu badan anda tinggi ?",
    "12. Mengalami luka di bagian tertentu ?",
    "13. Tidak dapat menggerakkan anggota badan tertentu ?",
    "14. Pernah memakan sesuatu ?",
    "15. Memakan daging ?",
    "16. Memakan jamur ?",
    "17. Memakan makanan kaleng ?",
    "18. Membeli susu ?",
    "19. Meminum susu ?"
]

var = {}
for i, gejala in enumerate(txtgejala):
    var[i] = widgets.Checkbox(
        value=False,
        description=gejala,
        disabled=False,
        indent=False
    )
    display(var[i])

threshold = widgets.FloatText(
    value=20,
    description='Th(%): ',
    disabled=False
)
threshold.layout = widgets.Layout(width='150px')
display(threshold)

def proses(button):
    jawaban = {}
    for i, gejala in enumerate(var):
        jawaban[i] = var[i].value
    
    total_penyakit = len(penyakit)
    percentages = [0] * total_penyakit

    for i, disease_symptoms in enumerate(bagansakit):
        match_count = sum(jawaban[j] for j in disease_symptoms)
        percentages[i] = (match_count / len(disease_symptoms)) * 100

    print("Percentage match for each disease:")
    for i, disease in enumerate(penyakit):
        print(f"{disease}: {percentages[i]}%")

button = widgets.Button(
    description='Proses',
    disabled=False,
    button_style='success',
    tooltip='Proses Gejala Gastro-Usus',
)
display(button)
button.on_click(proses)
