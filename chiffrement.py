import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Génère une clé de chiffrement et demande à l'utilisateur où la sauvegarder.
    """
    key = Fernet.generate_key()
    file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key files", "*.key")])
    if file_path:  # Vérifie si l'utilisateur a choisi un emplacement
        with open(file_path, "wb") as key_file:
            key_file.write(key)
        messagebox.showinfo("Succès", "La clé de chiffrement a été sauvegardée avec succès.")
    else:
        messagebox.showwarning("Annulé", "L'opération de sauvegarde de la clé a été annulée.")

def encrypt_file(file_path, key_path):
    """
    Chiffre le fichier avec la clé fournie.
    """
    key = open(key_path, "rb").read()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    messagebox.showinfo("Succès", "Le fichier a été chiffré avec succès!")

def import_document():
    """
    Importe un document et demande la clé pour le chiffrement.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        key_path = filedialog.askopenfilename(title="Sélectionnez la clé de chiffrement", filetypes=[("Key files", "*.key")])
        if key_path:
            encrypt_file(file_path, key_path)
        else:
            messagebox.showwarning("Annulé", "Le chiffrement a été annulé. Aucune clé sélectionnée.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chiffreur de fichier")

# Bouton pour importer un document et chiffrer
import_button = tk.Button(root, text="Importer et chiffrer un document", command=import_document)
import_button.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

root.mainloop()
