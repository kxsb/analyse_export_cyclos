import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def decrypt_file(file_path, key_path):
    """
    Déchiffre le fichier avec la clé fournie.
    """
    key = open(key_path, "rb").read()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    original_file_path = file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)
    messagebox.showinfo("Succès", "Le fichier a été déchiffré avec succès!")

def decrypt_document():
    """
    Importe un document chiffré et demande la clé pour le déchiffrer.
    """
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.encrypted")])
    if file_path:
        key_path = filedialog.askopenfilename(title="Sélectionnez la clé de déchiffrement", filetypes=[("Key files", "*.key")])
        if key_path:
            decrypt_file(file_path, key_path)
        else:
            messagebox.showwarning("Annulé", "Le déchiffrement a été annulé. Aucune clé sélectionnée.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Déchiffreur de fichier")

# Bouton pour importer et déchiffrer un document
decrypt_button = tk.Button(root, text="Importer et déchiffrer un document", command=decrypt_document)
decrypt_button.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

root.mainloop()
