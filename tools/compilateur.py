import os
import pandas as pd

# Chemin du dossier contenant les fichiers
dossier = r"C:\Users\micka\Documents\code\module_pro\rapprot cyclos 2024"

# Liste des fichiers à fusionner
mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
fichiers = [os.path.join(dossier, f"{mois[i]}-24.xlsx") for i in range(12)]

# Liste pour stocker les DataFrames
dfs = []

# Charger et concaténer les fichiers
for fichier in fichiers:
    if os.path.exists(fichier):  # Vérifie que le fichier existe
        df = pd.read_excel(fichier)
        df["mois"] = fichier.split("\\")[-1].split("-")[0]  # Ajouter une colonne 'mois' pour l’identification
        dfs.append(df)

# Fusionner les DataFrames
if dfs:
    df_final = pd.concat(dfs, ignore_index=True)
    
    # Sauvegarde du fichier fusionné
    fichier_sortie = os.path.join(dossier, "rapport_cyclos_2024.xlsx")
    df_final.to_excel(fichier_sortie, index=False)
    print(f"Fusion terminée : {fichier_sortie}")
else:
    print("Aucun fichier trouvé pour la fusion.")
