import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import pandas as pd
from io import BytesIO
import os
import random
import xlsxwriter

def generate_key():
    key = Fernet.generate_key()
    file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key")])
    if file_path:
        with open(file_path, "wb") as key_file:
            key_file.write(key)
        messagebox.showinfo("Succès", "La clé de chiffrement a été sauvegardée avec succès.")
    else:
        messagebox.showwarning("Annulé", "L'opération de sauvegarde de la clé a été annulée.")

def encrypt_file(file_data, key_path):
    key = open(key_path, "rb").read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    return encrypted_data

def anonymiser_fichier(df, chemin_prenoms):

    # Supprimer les lignes correspondant à "Prélèvement Web" et "Prélèvement Web Pro" avant de supprimer les colonnes
    df = df[~df['Type de paiement'].isin(["Prélèvement Web", "Prélèvement Web Pro"])]

    # Liste des colonnes à supprimer
    colonnes_a_supprimer = ['Numéro de transaction', 'De', 'Du compte', 'Vers le groupe', 'Vers le compte', 'Reçu par', 'Type de paiement', 'Description', 'Source paiement euro']
    df = df.drop(columns=colonnes_a_supprimer)

    # Charger la liste des prénoms nettoyés
    with open(chemin_prenoms, 'r') as file:
        prenoms = [line.strip() for line in file.readlines()]
    print(f"{len(prenoms)} prénoms chargés pour l'anonymisation.")

    # Créer un dictionnaire pour mapper chaque identifiant unique à un prénom unique
    mapping_adherents = {}
    random.shuffle(prenoms)  # Mélanger les prénoms pour l'attribution

    # Fonction pour attribuer un prénom unique à chaque adhérent de manière cohérente
    def attribuer_prenom_unique(valeur):
        if pd.notna(valeur):
            # Remplacer les lignes spécifiques par "La Gonette - Association"
            if "(Gestion réseau)" in valeur or "VIOT - Solène" in valeur:
                return "La Gonette - Association"
            # Renommer "Anonyme" en "Conversion"
            if "Anonyme" in valeur:
                return "Conversion"
            
            prefix = valeur.split('-')[0].strip().upper()
            if prefix.startswith('U'):
                if valeur not in mapping_adherents:
                    if prenoms:
                        mapping_adherents[valeur] = 'U_' + prenoms.pop(0)
                    else:
                        raise ValueError("Plus de prénoms disponibles pour l'attribution.")
                return mapping_adherents[valeur]
            elif prefix.startswith('P'):
                parts = valeur.split('-')
                if len(parts) > 1:
                    return '-'.join(parts[:2]).strip()
                else:
                    return valeur
        return valeur

    # Appliquer la fonction de cryptage de manière cohérente à chaque adhérent
    df.loc[:, 'Réalisé par'] = df['Réalisé par'].apply(attribuer_prenom_unique)
    df.loc[:, 'Vers'] = df['Vers'].apply(attribuer_prenom_unique)
    
    return df  # Retourner le DataFrame modifié

def anonymiser_et_chiffrer_document():
    file_path = filedialog.askopenfilename(title="Importer vos données", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return
        print("Aucun fichier sélectionné.")

    chemin_prenoms = filedialog.askopenfilename(title="Importer le dictionnaire des prénoms", filetypes=[("CSV files", "*.csv")])
    if not chemin_prenoms:
        return

    df = pd.read_excel(file_path)
    print("Fichier chargé dans un DataFrame.")
    
    df_anonymise = anonymiser_fichier(df, chemin_prenoms)
    print("DataFrame après anonymisation :")

    messagebox.showinfo("Succès", "Vos données ont été nettoyées et anonymisées.")

    if messagebox.askyesno("Chiffrement", "Procéder au chiffrement ?"):
        key_path = filedialog.askopenfilename(title="Importer votre clé de chiffrement", filetypes=[("Key files", "*.key")])
        if key_path:
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_anonymise.to_excel(writer, index=False)
            encrypted_data = encrypt_file(output.getvalue(), key_path)
            if messagebox.askyesno("Enregistrer", "Enregistrer le fichier chiffré ?"):
                save_path = filedialog.asksaveasfilename(defaultextension=".encrypted", filetypes=[("Encrypted files", "*.encrypted")])
                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(encrypted_data)
                    messagebox.showinfo("Succès", "Le fichier chiffré a été enregistré avec succès.")
                else:
                    messagebox.showwarning("Annulé", "L'enregistrement du fichier chiffré a été annulé.")
        else:
            messagebox.showwarning("Annulé", "Le chiffrement a été annulé.")
    else:
        # Demander à l'utilisateur s'il souhaite enregistrer le fichier anonymisé
        if messagebox.askyesno("Enregistrer", "Enregistrer le fichier anonymisé ?"):
            save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if save_path:
                df_anonymise.to_excel(save_path, index=False)
                messagebox.showinfo("Succès", "Le fichier anonymisé a été enregistré avec succès.")
            else:
                messagebox.showwarning("Annulé", "L'enregistrement du fichier anonymisé a été annulé.")

# Interface utilisateur Tkinter
root = tk.Tk()
root.title("Outil d'anonymisation et de chiffrement")

generate_key_button = tk.Button(root, text="Générer une clé de chiffrement", command=generate_key)
generate_key_button.pack(padx=10, pady=10)

import_anonymize_encrypt_button = tk.Button(root, text="Importer, anonymiser et chiffrer un document", command=anonymiser_et_chiffrer_document)
import_anonymize_encrypt_button.pack(padx=10, pady=10)

root.mainloop()
