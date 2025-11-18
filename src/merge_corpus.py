import os

# 🔹 Mets ici le chemin EXACT de ton dossier TRANS_TXT
source_folder = r"C:\Users\Lenovo\Downloads\DISTRIBUTION_ACCUEIL_UBS\TRANS_TXT"

output_file = "data/corpus.txt"

print("📁 Dossier source :", source_folder)

# Lister tous les fichiers
all_files = os.listdir(source_folder)
print("📄 Fichiers trouvés dans le dossier :")
for f in all_files:
    print("   -", f)

# Garder seulement les fichiers .txt
txt_files = [f for f in all_files if f.lower().endswith(".txt")]
print("\n📄 Fichiers .txt détectés :")
for f in txt_files:
    print("   -", f)

if not txt_files:
    print("\n⚠ Aucun fichier .txt trouvé ! Vérifie bien le chemin source_folder.")
else:
    # Créer dossier data si n'existe pas
    os.makedirs("data", exist_ok=True)

    # Ouvrir corpus.txt en écriture
    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in txt_files:
            file_path = os.path.join(source_folder, filename)  # 🔹 ici file_path est défini correctement
            print("➡ Fusion de :", file_path)

            # Lire fichier source
            with open(file_path, "r", encoding="latin-1", errors="ignore") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")   # séparation entre fichiers

    print("\n✅ Fusion terminée →", output_file)
