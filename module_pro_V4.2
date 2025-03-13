import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from io import BytesIO
import functools
import time

import threading

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import re

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, PageBreak, Paragraph, image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import tempfile
import pandas as pd

import plotly.express as px
from cryptography.fernet import Fernet

class DataManager:
    def __init__(self):
        self.df_total = pd.DataFrame()

    def decrypt_file(self, file_path, key_path):
        try:
            with open(key_path, "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Fichier de clé non trouvé.")
            return None
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture du fichier de clé : {e}")
            return None

        try:
            f = Fernet(key)
        except ValueError as e:
            messagebox.showerror("Erreur", f"La clé de déchiffrement est invalide : {e}")
            return None

        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            return decrypted_data
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Fichier à déchiffrer non trouvé.")
            return None
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement : {e}")
            return None

    def load_file(self, file_path, parent):
        """Lit un fichier Excel ou chiffré. Pour les fichiers chiffrés, demande à l'utilisateur la clé."""
        if file_path.endswith('.encrypted'):
            if not messagebox.askyesno("Fichier chiffré détecté",
                                       "Un fichier chiffré a été sélectionné. Voulez-vous le déchiffrer pour l'importer ?"):
                messagebox.showinfo("Annulé", "Importation annulée pour le fichier chiffré.")
                return None
            key_file_path = filedialog.askopenfilename(
                title="Sélectionner le fichier de clé de déchiffrement",
                filetypes=[("Key files", "*.key"), ("All files", "*.*")],
                parent=parent
            )
            if not key_file_path:
                messagebox.showinfo("Annulé", "Déchiffrement annulé. Aucun fichier de clé fourni.")
                return None
            decrypted_data = self.decrypt_file(file_path, key_file_path)
            if decrypted_data is None:
                messagebox.showerror("Erreur", "Le déchiffrement a échoué.")
                return None
            try:
                df = pd.read_excel(BytesIO(decrypted_data))
            except Exception as e:
                messagebox.showerror("Erreur d'importation", f"Erreur lors de l'importation du fichier déchiffré : {e}")
                return None
        else:
            try:
                df = pd.read_excel(file_path)
            except Exception as e:
                messagebox.showerror("Erreur d'importation", f"Erreur lors de l'importation du fichier {file_path} : {e}")
                return None
        return df

    def add_data(self, df):
        if df is not None:
            self.df_total = pd.concat([self.df_total, df], ignore_index=True)

    def get_global_statistics(self):
        if self.df_total.empty:
            return None
        stats = {}
        df = self.df_total
        stats['periode'] = f"{df['Date'].min().strftime('%d/%m/%Y')} - {df['Date'].max().strftime('%d/%m/%Y')}"
        stats['nb_utilisateurs'] = len(pd.unique(df[['Réalisé par', 'Vers']].values.ravel('K')))
        transactions_PP = df[(df['Réalisé par'].str.startswith('P')) & (df['Vers'].str.startswith('P'))]
        stats['moyenne_transactions_PP'] = transactions_PP['Montant'].mean() if not transactions_PP.empty else 0
        paiements_UP = df[(df['Réalisé par'].str.startswith('U')) & (df['Vers'].str.startswith('P'))]
        stats['moyenne_paiement_UP'] = paiements_UP['Montant'].mean() if not paiements_UP.empty else 0
        transactions_UU = df[(df['Réalisé par'].str.startswith('U')) & (df['Vers'].str.startswith('U'))]
        stats['moyenne_transactions_UU'] = transactions_UU['Montant'].mean() if not transactions_UU.empty else 0
        return stats

    def extraire_identifiants_professionnels(self):
        if self.df_total.empty:
            return []
        
        pattern = r"P\d{4}"
        data_concat = pd.concat([self.df_total['Réalisé par'], self.df_total['Vers']])
        identifiants = data_concat[data_concat.str.contains(pattern, regex=True, na=False)].unique()

        professionnels_corriges = []
        for ident in identifiants:
            match_id = re.search(pattern, ident)
            if match_id:
                num_pro = match_id.group(0)
                nom_structure = ident.replace(num_pro, "").strip(" -")
                nom_structure = nom_structure.split(" - ")[0]
                professionnels_corriges.append(f"{num_pro} - {nom_structure}")

        return sorted(professionnels_corriges)
    
    def compute_professional_statistics(self, num_professionnel):
        df = self.df_total
        df_user = df[
            (
                (df['Réalisé par'].fillna("").str.contains(num_professionnel, regex=False)) |
                (df['Vers'].fillna("").str.contains(num_professionnel, regex=False))
            )
            & (df['Vers'] != "P0000")
        ]
        if df_user.empty:
            messagebox.showinfo("Résultat", f"Aucune activité trouvée pour {num_professionnel}.")
            return None
        stats = {}
        df_particuliers = df_user[
            df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Réalisé par'].fillna("").str.startswith('U')
        ]
        stats['nb_particuliers'] = df_particuliers['Réalisé par'].nunique()
        
        # Ici, on peut soit utiliser re.escape et laisser regex activé, soit utiliser regex=False directement.
        # Par souci de cohérence, nous optons pour regex=False sans re.escape.
        df_professionnels = df_user[
            df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Réalisé par'].fillna("").str.startswith('P')
        ]
        stats['nb_professionnels'] = df_professionnels['Réalisé par'].nunique()
        stats['premiere_date'] = df_user['Date'].min().strftime('%d/%m/%Y')
        stats['derniere_date'] = df_user['Date'].max().strftime('%d/%m/%Y')
        
        transactions_recues = df_user[
            df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False) &
            (~df_user['Réalisé par'].fillna("").str.contains('conversion', case=False, regex=False))
        ]
        stats['nb_transactions_recues'] = transactions_recues.shape[0]
        stats['somme_transactions_recues'] = transactions_recues['Montant'].sum()
        
        stats['montant_emis_vers_pro'] = df_user[
            df_user['Réalisé par'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Vers'].fillna("").str.startswith('P')
        ]['Montant'].sum()
        
        stats['montant_emis_vers_particuliers'] = df_user[
            df_user['Réalisé par'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Vers'].fillna("").str.startswith('U')
        ]['Montant'].sum()
        
        stats['montant_reconverti'] = df_user[
            df_user['Réalisé par'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Vers'].fillna("").str.contains('conversion', case=False, regex=False)
        ]['Montant'].sum()
        
        stats['montant_converti'] = df_user[
            df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False) &
            df_user['Réalisé par'].fillna("").str.contains('conversion', case=False, regex=False)
        ]['Montant'].sum()
        
        stats['total_montant_emis_sans_reconversion'] = stats['montant_emis_vers_pro'] + stats['montant_emis_vers_particuliers']
        return stats

    def get_professional_fullname(self, num_professionnel):
        for _, row in self.df_total.iterrows():
            if num_professionnel in str(row['Réalisé par']):
                return str(row['Réalisé par'])
            elif num_professionnel in str(row['Vers']):
                return str(row['Vers'])
        return num_professionnel

    def compute_professionals_ranking(self):
        df = self.df_total
        if df.empty:
            return pd.DataFrame()
        somme_B2B_recu = df[(df['Vers'].str.startswith('P')) & (df['Réalisé par'].str.startswith('P'))] \
            .groupby('Vers')['Montant'].sum().reset_index() \
            .rename(columns={'Montant': 'B2B Reçu', 'Vers': 'Professionnel'})
        somme_B2B_emis = df[(df['Réalisé par'].str.startswith('P')) & (df['Vers'].str.startswith('P'))] \
            .groupby('Réalisé par')['Montant'].sum().reset_index() \
            .rename(columns={'Montant': 'B2B Emis', 'Réalisé par': 'Professionnel'})
        somme_B2C = df[(df['Réalisé par'].str.startswith('U')) & (df['Vers'].str.startswith('P'))] \
            .groupby('Vers')['Montant'].sum().reset_index() \
            .rename(columns={'Montant': 'B2C', 'Vers': 'Professionnel'})
        somme_remuneration = df[(df['Réalisé par'].str.startswith('P')) & (df['Vers'].str.startswith('U'))] \
            .groupby('Réalisé par')['Montant'].sum().reset_index() \
            .rename(columns={'Montant': 'Rémunération', 'Réalisé par': 'Professionnel'})
        ranking = pd.merge(somme_B2B_recu, somme_B2B_emis, on='Professionnel', how='outer')
        ranking = pd.merge(ranking, somme_B2C, on='Professionnel', how='outer').fillna(0)
        ranking = pd.merge(ranking, somme_remuneration, on='Professionnel', how='outer').fillna(0)
        ranking['Total Reçu'] = ranking['B2B Reçu'] + ranking['B2C']
        ranking['Paiements Reçu B+C'] = ranking['Total Reçu']
        ranking.sort_values(by='Total Reçu', ascending=False, inplace=True)
        ranking = ranking[['Professionnel', 'B2B Reçu', 'B2B Emis', 'B2C', 'Paiements Reçu B+C', 'Rémunération', 'Total Reçu']]
        return ranking

class GraphManager:

    def __init__(self, ui_manager):
        """Le GraphManager a besoin d'une référence à UIManager pour exporter en PDF."""
        self.ui_manager = ui_manager  # Stocke UIManager pour y accéder plus tard

    def creer_jauge(self, montant_emis, montant_reconverti, parent):
        fig, ax = plt.subplots(figsize=(4, 0.5))
        total = montant_emis + montant_reconverti
        rapport_emis = montant_emis / total if total > 0 else 0
        rapport_reconverti = 1 - rapport_emis
        ax.barh(0, rapport_emis, color='green')
        ax.barh(0, rapport_reconverti, left=rapport_emis, color='red')
        ax.set_xlim(0, 1)
        ax.axis('off')
        pourcentage_emis = rapport_emis * 100
        texte_emis = f"{montant_emis:.2f}€ ({pourcentage_emis:.1f}%)"
        ax.text(0, 0.5, texte_emis, ha='center', va='center', color='black', fontsize=12, transform=ax.transAxes)
        pourcentage_reconverti = rapport_reconverti * 100
        texte_reconverti = f"{montant_reconverti:.2f}€ ({pourcentage_reconverti:.1f}%)"
        ax.text(1, 0.5, texte_reconverti, ha='center', va='center', color='black', fontsize=12, transform=ax.transAxes)
        canvas = FigureCanvasTkAgg(fig, master=parent)
        plt.close(fig)
        return canvas

    def identifier_operations_de_change(self, df):
        return df[df['Réalisé par'].fillna("").str.contains('conversion', case=False)]
    
    def create_payment_analysis_graph(self, df_user, num_professionnel, stats, fullname, root):
        graph_window = tk.Toplevel(root)
        graph_window.title(f"Analyse de l'Activité {num_professionnel}")

        # Variable pour suivre l'état de la fenêtre des données brutes
        self.raw_data_window = None  


        # Jauge
        montant_emis = stats['montant_emis_vers_pro'] + stats['montant_emis_vers_particuliers']
        canvas_jauge = self.creer_jauge(montant_emis, stats['montant_reconverti'], graph_window)
        canvas_jauge.get_tk_widget().pack(fill=tk.X)
        canvas_jauge.draw()

        # Résumé textuel
        info_text = (
            f"{stats['nb_particuliers']} particuliers (U) et {stats['nb_professionnels']} professionnels (P) ont payé {fullname} "
            f"du {stats['premiere_date']} au {stats['derniere_date']}, soit {stats['nb_transactions_recues']} paiements "
            f"pour un montant total de {stats['somme_transactions_recues']:.2f}€.\n\n"
            f"Montant total émis (hors reconversions): {stats['total_montant_emis_sans_reconversion']:.2f}€ "
            f"(Détail: {stats['montant_emis_vers_pro']:.2f}€ vers pro, {stats['montant_emis_vers_particuliers']:.2f}€ vers particuliers, "
            f"{stats['montant_reconverti']:.2f}€ reconvertis).\n"
            f"Montant total converti en direction de {fullname}: {stats['montant_converti']:.2f}€."
        )
        tk.Label(graph_window, text=info_text, wraplength=500).pack()

        # Ajout du bouton dans la fenêtre d'analyse du professionnel
        view_raw_data_button = ttk.Button(graph_window, text="📄 Afficher les données brutes",
                                        command=lambda: self.ui_manager.show_professional_raw_data(num_professionnel, df_user))
        view_raw_data_button.pack(pady=5)

        # # 👉 Ajout d'un cadre pour le bouton Export en PDF avant les graphiques
        # button_frame = ttk.Frame(graph_window)
        # button_frame.pack(fill=tk.X, pady=5)

        # export_button = ttk.Button(button_frame, text="📄 Exporter en PDF",
        #                         command=lambda: self.ui_manager.export_professional_to_pdf(num_professionnel, fullname, stats, fig, df_user))
        # export_button.pack(pady=5)

        # Figure globale avec plusieurs sous-graphes
        fig = plt.Figure(figsize=(16, 16), dpi=100)
        fig.subplots_adjust(top=0.95, bottom=0.05, left=0.05, right=0.95, hspace=0.3, wspace=0.35)
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Graphique 1 : Paiements reçus et conversions
        df_recu = df_user[
            (df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False)) & 
            (~df_user['Réalisé par'].fillna("").str.contains('conversion', case=False))
        ].sort_values(by='Date')

        ax1 = fig.add_subplot(311)
        df_conversions = self.identifier_operations_de_change(df_user).sort_values(by='Date')
        ax1.plot(df_recu['Date'], df_recu['Montant'], marker='o', linestyle='-', label='Paiements Reçus')
        ax1.scatter(df_conversions['Date'], df_conversions['Montant'], color='black', marker='x', label='Conversions')
        ax1.set_title("Paiements reçus")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Montant")
        ax1.tick_params(axis='x', rotation=45)
        ax1.legend()

        # Graphique 2 : Diagramme circulaire des ventes vers professionnels
        ax2 = fig.add_subplot(323)
        df_recus_pro = df_user[
            (df_user['Vers'].fillna("").str.contains(num_professionnel, regex=False)) &
            (df_user['Réalisé par'].fillna("").str.startswith('P'))
        ]        
        montant_par_emetteur = df_recus_pro.groupby('Réalisé par')['Montant'].sum()
        ax2.pie(montant_par_emetteur, labels=montant_par_emetteur.index, autopct='%1.1f%%', startangle=140)
        ax2.set_title("Ventes vers pro")

        # Graphique 3 : Diagramme circulaire des achats vers professionnels
        ax3 = fig.add_subplot(324)
        df_emis_pro = df_user[
            (df_user['Réalisé par'].fillna("").str.contains(num_professionnel, regex=False)) &
            (df_user['Vers'].fillna("").str.startswith('P'))
        ]
        montant_par_destinataire = df_emis_pro.groupby('Vers')['Montant'].sum()
        ax3.pie(montant_par_destinataire, labels=montant_par_destinataire.index, autopct='%1.1f%%', startangle=140)
        ax3.set_title("Achats vers pro")

        # Graphique 4 : Réseau de transactions professionnelles
        ax4 = fig.add_subplot(313)
        G = nx.DiGraph()
        transactions_pros = df_user[
            (df_user['Réalisé par'].str.contains(r'P\d{4}')) &
            (df_user['Vers'].str.contains(r'P\d{4}'))
        ]
        for _, transaction in transactions_pros.iterrows():
            if transaction['Réalisé par'] == num_professionnel:
                G.add_edge(transaction['Réalisé par'], transaction['Vers'], color='red')
            elif transaction['Vers'] == num_professionnel:
                G.add_edge(transaction['Réalisé par'], transaction['Vers'], color='blue')
            else:
                G.add_edge(transaction['Réalisé par'], transaction['Vers'], color='green')
        pos = nx.spring_layout(G)
        edges = G.edges(data=True)
        colors = [edge[2]['color'] for edge in edges]
        nx.draw(G, pos, ax=ax4, edge_color=colors, with_labels=True, node_size=500)
        ax4.set_title("Réseau de Transactions Professionnelles")
        canvas.draw()

class UIManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyse de données de paiement")
        self.root.geometry("600x400")
        self.setup_styles()
        self.setup_ui()
        self.centre_window(self.root)
        self.data_manager = DataManager()
        self.graph_manager = GraphManager(self)

    def setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', foreground='black', background='white', font=('Arial', 10), padding=10)
        style.configure('TLabel', foreground='black', font=('Arial', 12))
        style.configure('TFrame', background='lightgray')

    def setup_ui(self):
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.main_frame,
                text="🏦 Analyse des paiements en monnaie locale",
                font=('Arial', 14, 'bold')).pack(pady=10)

        # Création du bandeau gris clair pour afficher les statistiques
        self.stats_frame = tk.Frame(self.main_frame, bg="#F0F0F0", padx=10, pady=10, bd=2, relief=tk.RIDGE)
        self.stats_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(self.stats_frame, text="📅 Période :", font=('Arial', 10, 'bold'), background="#F0F0F0").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.periode_label = ttk.Label(self.stats_frame, text="...", font=('Arial', 10), background="#F0F0F0")
        self.periode_label.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(self.stats_frame, text="👥 Nombre d'utilisateurs :", font=('Arial', 10, 'bold'), background="#F0F0F0").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.nb_utilisateurs_label = ttk.Label(self.stats_frame, text="...", font=('Arial', 10), background="#F0F0F0")
        self.nb_utilisateurs_label.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(self.stats_frame, text="💳 Moyenne transactions P>P :", font=('Arial', 10, 'bold'), background="#F0F0F0").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.moyenne_transactions_PP_label = ttk.Label(self.stats_frame, text="...", font=('Arial', 10), background="#F0F0F0")
        self.moyenne_transactions_PP_label.grid(row=2, column=1, sticky=tk.W)

        ttk.Label(self.stats_frame, text="💰 Moyenne paiement U>P :", font=('Arial', 10, 'bold'), background="#F0F0F0").grid(row=3, column=0, sticky=tk.W, padx=5)
        self.moyenne_paiement_UP_label = ttk.Label(self.stats_frame, text="...", font=('Arial', 10), background="#F0F0F0")
        self.moyenne_paiement_UP_label.grid(row=3, column=1, sticky=tk.W)

        ttk.Label(self.stats_frame, text="🔄 Moyenne transactions U>U :", font=('Arial', 10, 'bold'), background="#F0F0F0").grid(row=4, column=0, sticky=tk.W, padx=5)
        self.moyenne_transactions_UU_label = ttk.Label(self.stats_frame, text="...", font=('Arial', 10), background="#F0F0F0")
        self.moyenne_transactions_UU_label.grid(row=4, column=1, sticky=tk.W)


        # Barre de progression
        self.progress_bar = ttk.Progressbar(self.main_frame, mode='determinate', length=300)
        self.progress_bar.pack(pady=5)
        self.progress_bar["value"] = 0  # Initialisation
        self.progress_bar.pack_forget()  # Cachée au début

        # Espacement pour séparer les statistiques des boutons
        ttk.Label(self.main_frame, text="").pack()

        # Boutons d'action
        ttk.Button(self.main_frame,
                text="📥 Importer des données",
                command=self.importer).pack(pady=5)
        
        ttk.Button(self.main_frame,
                text="📊 Voir l'activité des professionnels",
                command=self.show_professionals_ranking).pack(pady=5)

        # Ajout d'un espace en bas pour plus d'équilibre visuel
        ttk.Label(self.main_frame, text="").pack()
    
    def show_main_screen(self):
        """Réaffiche l'écran principal et cache l'affichage du classement des professionnels."""
        if hasattr(self, "ranking_frame"):
            self.ranking_frame.pack_forget()  # Masquer le classement
            self.ranking_frame.destroy()  # Libérer la mémoire
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Réafficher l'accueil

    def centre_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def importer(self):
        file_paths = filedialog.askopenfilenames(
            title="Sélectionner des fichiers",
            filetypes=[("Encrypted files", "*.encrypted"),
                    ("Excel files", "*.xlsx"),
                    ("All files", "*.*")]
        )
        if not file_paths:
            messagebox.showinfo("Information", "Aucun fichier n'a été sélectionné. L'opération d'importation est annulée.")
            return

        # ✅ Lancer l’importation dans un thread séparé
        threading.Thread(target=self.importer_background, args=(file_paths,), daemon=True).start()


    def importer_background(self, file_paths):
        """Effectue l'importation des fichiers en arrière-plan avec une barre de progression visible et fluide."""
        
        self.progress_bar.pack(pady=5)  # ✅ Afficher la barre de progression
        self.progress_bar["value"] = 5  # ✅ Démarrage immédiat avec un petit remplissage
        self.root.update_idletasks()

        total_files = len(file_paths)

        # ✅ Petite progression AVANT de démarrer l'import (simulé)
        for i in range(5, 20, 3):  # Progression initiale rapide (jusqu'à 20%)
            self.progress_bar["value"] = i
            self.root.update_idletasks()
            time.sleep(0.05)  # ✅ Très court pour voir la montée progressive

        # ✅ Importation réelle des fichiers avec progression jusqu'à 80%
        for i, file_path in enumerate(file_paths):
            df = self.data_manager.load_file(file_path, self.root)
            if df is not None:
                self.data_manager.add_data(df)

            # Mise à jour de la progression
            progress_value = 20 + ((i + 1) / total_files) * 60  # 20% ➡ 80%
            self.progress_bar["value"] = progress_value
            self.root.update_idletasks()

        # ✅ Animation finale fluide vers 100%
        for i in range(int(self.progress_bar["value"]), 101, 2):
            self.progress_bar["value"] = i
            self.root.update_idletasks()
            time.sleep(0.02)

        self.progress_bar.pack_forget()  # ✅ Cacher la barre après l'importation

        if not self.data_manager.df_total.empty:
            self.update_statistics()  # ✅ Mise à jour des statistiques affichées


    def display_imported_files(self, file_paths):
        """Affiche la liste des fichiers importés avec succès sur l'interface principale."""
        if not hasattr(self, "imported_files_frame"):
            # Créer le cadre d'affichage si ce n'est pas déjà fait
            self.imported_files_frame = ttk.Frame(self.main_frame, padding="10", style='TFrame')
            self.imported_files_frame.pack(fill=tk.X, padx=10, pady=5)

        # Nettoyer l'affichage précédent
        for widget in self.imported_files_frame.winfo_children():
            widget.destroy()

        # Afficher chaque fichier importé
        for file in file_paths:
            label = ttk.Label(self.imported_files_frame, text=f"📂 Fichier importé : {file}",
                            background="#D4EDDA", font=("Arial", 10, "bold"), anchor="w")
            label.pack(fill=tk.X, padx=5, pady=2)

    def update_statistics(self):
        stats = self.data_manager.get_global_statistics()
        if stats:
            self.periode_label.config(text=f"Période: {stats['periode']}")
            self.nb_utilisateurs_label.config(text=f"Nombre d'utilisateurs actifs (U+P): {stats['nb_utilisateurs']}")
            self.moyenne_transactions_PP_label.config(text=f"Moyenne des transactions P>P: {stats['moyenne_transactions_PP']:.2f}€")
            self.moyenne_paiement_UP_label.config(text=f"Moyenne de paiement U>P: {stats['moyenne_paiement_UP']:.2f}€")
            self.moyenne_transactions_UU_label.config(text=f"Moyenne des transactions U>U: {stats['moyenne_transactions_UU']:.2f}€")

    def open_professional_analysis(self):
        identifiants = self.data_manager.extraire_identifiants_professionnels()
        if not identifiants:
            messagebox.showwarning("Avertissement", "Aucune donnée disponible pour l'analyse.")
            return
        top = tk.Toplevel(self.root)
        top.title("Sélectionner un professionnel")
        top.geometry("400x200")
        frame = ttk.Frame(top, padding="10 10 10 10")
        frame.pack(expand=True, fill=tk.BOTH)
        ttk.Label(frame, text="Choisissez un professionnel:", font=('Arial', 12)).pack(pady=(0, 10))
        self.combo_box = ttk.Combobox(frame, values=identifiants, width=50)
        self.combo_box.pack()
        ttk.Label(frame, text="Recherche rapide:", font=('Arial', 12)).pack(pady=(10, 0))
        recherche_var = tk.StringVar()
        recherche_var.trace("w", lambda name, index, mode, sv=recherche_var: self.filter_identifiers(sv))
        barre_recherche = ttk.Entry(frame, textvariable=recherche_var, font=('Arial', 10))
        barre_recherche.pack(pady=(0, 20))
        btn_valider = ttk.Button(frame, text="Analyser", command=self.lancer_analyse_professionnel)
        btn_valider.pack()
        self.centre_window(top)

    def filter_identifiers(self, sv):
        terme = sv.get().upper()
        all_ids = self.data_manager.extraire_identifiants_professionnels()
        filtered = [ident for ident in all_ids if terme in ident.upper()]
        self.combo_box['values'] = filtered
        if filtered and terme in filtered[0]:
            self.combo_box.set(terme)
        else:
            self.combo_box.set('')

    def lancer_analyse_professionnel(self, num_prof=None):
        """Lance l'analyse d'un professionnel, soit depuis la ComboBox, soit via un double-clic."""
        if num_prof is None:  # Si aucun numéro n'est fourni, on le prend depuis la ComboBox
            num_prof = self.combo_box.get()

        if not num_prof:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un identifiant professionnel.")
            return

        stats = self.data_manager.compute_professional_statistics(num_prof)
        if stats is None:
            return
        
        fullname = self.data_manager.get_professional_fullname(num_prof)

        # Filtrer les données pour l'analyse du professionnel
        df_user = self.data_manager.df_total[self.data_manager.df_total.apply(
            lambda row: num_prof in str(row['Réalisé par']) or num_prof in str(row['Vers']), axis=1)]
        
        self.graph_manager.create_payment_analysis_graph(df_user, num_prof, stats, fullname, self.root)

    def show_professionals_ranking(self):
        """Affiche le classement des professionnels en remplaçant l'interface principale."""
        
        # Cacher la fenêtre principale
        self.main_frame.pack_forget()

        # Augmenter la taille de la fenêtre principale (doublée)
        self.root.geometry("1400x800")  # Largeur x Hauteur

        # Création du cadre de la nouvelle vue
        self.ranking_frame = ttk.Frame(self.root, padding="10")
        self.ranking_frame.pack(fill=tk.BOTH, expand=True)

        # Bouton Retour
        back_button = ttk.Button(self.ranking_frame, text="⬅ Retour", command=self.show_main_screen)
        back_button.pack(anchor="w", padx=5, pady=5)

        ranking = self.data_manager.compute_professionals_ranking()
        if ranking.empty:
            messagebox.showwarning("Avertissement", "Aucune donnée disponible pour le classement.")
            self.show_main_screen()  # Retour à l'accueil si rien à afficher
            return

        # Suppression de la colonne inutile
        ranking = ranking.drop(columns=['Paiements Reçu B+C'], errors='ignore')

        # Calcul de la ligne "Total"
        total_values = ranking.drop(columns=['Professionnel']).sum()
        total_row = pd.DataFrame([['Total'] + total_values.tolist()], columns=ranking.columns)

        # Ajout de la ligne "Total" en premier dans le classement
        ranking = pd.concat([total_row, ranking], ignore_index=True)

        cols = ('Professionnel', 'B2B Reçu', 'B2B Emis', 'B2C', 'Rémunération', 'Total Reçu')

        # Création d'un cadre principal
        frame = ttk.Frame(self.ranking_frame)
        frame.pack(fill=tk.BOTH, expand=True)

        # Ajout d'une barre de défilement
        tree_scroll = ttk.Scrollbar(frame, orient="vertical")
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Création du Treeview
        tree = ttk.Treeview(frame, columns=cols, show='headings', yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=tree.yview)

        # Configuration des colonnes
        for col in cols:
            tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(tree, _col, False))
            tree.column(col, anchor="center", width=120)

        # Ajout des données au tableau avec arrondi à l'unité
        for _, row in ranking.iterrows():
            values = tuple(int(row[col]) if isinstance(row[col], (int, float)) else row[col] for col in cols)
            if row['Professionnel'] == 'Total':
                tree.insert("", "end", values=values, tags=('total_row',))
            else:
                tree.insert("", "end", values=values, tags=('clickable',))

        tree.tag_configure('total_row', font=('Arial', 10, 'bold'), background='#D6EAF8')
        tree.pack(fill=tk.BOTH, expand=True)

        # Zone de recherche rapide
        search_frame = ttk.Frame(self.ranking_frame)
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(search_frame, text="🔍 Recherche rapide :", font=('Arial', 10)).pack(side=tk.LEFT)

        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, font=('Arial', 10))
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Mise à jour en temps réel de la recherche
        search_var.trace_add("write", lambda *args: self.update_treeview(tree, ranking, search_var.get()))

        # Bouton pour voir l'activité du professionnel sélectionné
        button_frame = ttk.Frame(self.ranking_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        def open_selected_professional():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Avertissement", "Veuillez sélectionner un professionnel.")
                return
            values = tree.item(selected_item, "values")
            if values and values[0] != "Total":
                num_prof = values[0].split(" - ")[0]
                self.lancer_analyse_professionnel(num_prof)

        view_button = ttk.Button(button_frame, text="📊 Voir l'activité du professionnel", command=open_selected_professional)
        view_button.pack(side=tk.LEFT, padx=5, pady=5)

        export_button = ttk.Button(button_frame, text="📤 Exporter les données", command=lambda: self.export_data(ranking))
        export_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Ajout du double-clic pour ouvrir la fiche d'un professionnel
        tree.bind("<Double-1>", functools.partial(self.on_professional_double_click, tree))

    def on_professional_double_click(self, tree, event):
        """Ouvre la fiche individuelle du professionnel sélectionné lors d'un double-clic, mais ignore les en-têtes."""
        region = tree.identify("region", event.x, event.y)

        if region != "cell":  # On vérifie que le clic est bien sur une cellule et non sur un en-tête
            return

        selected_item = tree.selection()
        if not selected_item:
            return
        
        values = tree.item(selected_item, "values")
        if values and values[0] != "Total":  # On ignore la ligne "Total"
            num_prof = values[0].split(" - ")[0]  # Récupérer uniquement le code Pxxxx
            self.lancer_analyse_professionnel(num_prof)  # Maintenant, seul num_prof est passé correctement

    def treeview_sort_column(self, tv, col, reverse):
        """Trie les colonnes du tableau en fonction du type de données (dates, nombres ou texte), en gardant 'Total' en haut."""
        l = []
        total_item = None  # Stockage de la ligne "Total"

        for k in tv.get_children(''):
            values = tv.item(k, 'values')

            if values and values[0] == "Total":  
                total_item = (values, k)  # Sauvegarde de la ligne "Total"
            else:
                value = tv.set(k, col)

                # ✅ Tri spécifique pour les dates
                if col == "Date":
                    try:
                        value = pd.to_datetime(value, format="%d-%m-%Y")  # Conversion correcte
                    except ValueError:
                        pass  # Si erreur, garder la valeur brute
                else:
                    # Tri pour les nombres
                    try:
                        value = int(value)
                    except ValueError:
                        pass

                l.append((value, k))

        # Appliquer le tri et réorganiser les lignes
        l.sort(reverse=reverse, key=lambda t: t[0])

        # ✅ Réinsérer "Total" en haut après le tri
        if total_item:
            tv.move(total_item[1], '', '0')  # Remet la ligne "Total" en haut

        for index, (_, k) in enumerate(l, start=1):  # On commence à 1 pour laisser "Total" en 0
            tv.move(k, '', index)

        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def update_treeview(self, tree, ranking, filter_text=""):
        """Met à jour le Treeview avec le texte filtré."""
        tree.delete(*tree.get_children())  # Supprime toutes les entrées existantes

        cols = ('Professionnel', 'B2B Reçu', 'B2B Emis', 'B2C', 'Rémunération', 'Total Reçu')

        # Remettre la ligne Total en premier si pas de filtre
        if filter_text == "":
            values_total = tuple(int(ranking.iloc[0][col]) if isinstance(ranking.iloc[0][col], (int, float)) else ranking.iloc[0][col] for col in cols)
            tree.insert("", "end", values=values_total, tags=('total_row',))

        # Ajout des professionnels filtrés
        for _, row in ranking.iloc[1:].iterrows():
            nom_pro = row['Professionnel']
            if filter_text.lower() in nom_pro.lower():  # Comparaison insensible à la casse
                values = tuple(int(row[col]) if isinstance(row[col], (int, float)) else row[col] for col in cols)
                tree.insert("", "end", values=values, tags=('clickable',))

    def export_data(self, ranking):
        """Exporte les données du classement des professionnels au format Excel."""
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if save_path:
            try:
                ranking.to_excel(save_path, index=False)
                messagebox.showinfo("Succès", "Les données ont été exportées avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'exportation : {e}")
    
    def export_professional_to_pdf(self, num_prof, fullname, stats, fig, df_user):
        """Exporte la fiche individuelle du professionnel en PDF avec les graphiques et les paiements bruts (multi-pages)."""
        
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Enregistrer le fichier PDF"
        )
        if not save_path:
            return  # Annulation de l'export
        
        try:
            doc = SimpleDocTemplate(save_path, pagesize=A4)
            elements = []  # Liste des éléments du PDF
            styles = getSampleStyleSheet()

            # --- PAGE 1 : Statistiques et graphiques ---
            elements.append(Paragraph(f"📄 Analyse de l'activité : {fullname} ({num_prof})", styles["Title"]))

            # Ajout des statistiques sous forme de paragraphes
            stats_text = ""
            for key, value in stats.items():
                stats_text += f"<b>{key.replace('_', ' ').capitalize()}</b> : {value}<br/>"
            elements.append(Paragraph(stats_text, styles["Normal"]))

            # Sauvegarde temporaire du graphique
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_img:
                fig.savefig(temp_img.name, format='png')
                temp_img_path = temp_img.name

            # Ajout de l'image du graphique
            elements.append(PageBreak())  # Ajout d'une page pour séparer les statistiques et les graphiques
            elements.append(Paragraph("📊 Graphiques d'analyse", styles["Title"]))
            elements.append(Image(temp_img_path, width=500, height=300))

            # --- PAGE 2+ : Transactions brutes ---
            elements.append(PageBreak())  # Nouvelle page pour les transactions
            elements.append(Paragraph(f"📄 Transactions de {fullname} ({num_prof})", styles["Title"]))

            # Définition des colonnes à afficher
            columns = ["Date", "Réalisé par", "Vers", "Montant"]
            df_filtered = df_user[columns].copy()

            # ✅ Convertir la colonne "Date" au format jj-mm-aaaa et supprimer l'heure
            df_filtered = df_filtered.copy()  # ✅ Assure que df_filtered est une copie indépendante
            df_filtered.loc[:, "Date"] = pd.to_datetime(df_filtered["Date"]).dt.strftime("%d-%m-%Y")

            # Convertir les données en liste de listes pour ReportLab
            data = [columns] + df_filtered.values.tolist()  # Ajout des en-têtes

            # Création du tableau avec pagination dynamique
            table_width = A4[0] - 40  # Largeur de la page - 20px de marge de chaque côté
            col_count = len(columns)
            col_widths = [table_width / col_count] * col_count  # Répartition égale

            table = Table(data, colWidths=col_widths)  # ✅ Largeur ajustée dynamiquement
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            elements.append(table)  # Ajout du tableau

            # Génération du PDF avec les éléments
            doc.build(elements)

            messagebox.showinfo("Succès", f"Le fichier PDF a été enregistré avec succès :\n{save_path}")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'exportation : {e}")

    def show_professional_raw_data(self, num_prof, df_user):
        """Ouvre une nouvelle fenêtre affichant les transactions brutes du professionnel sélectionné."""

        # Création de la fenêtre
        raw_data_window = tk.Toplevel(self.root)
        raw_data_window.title(f"Données brutes - {num_prof}")
        raw_data_window.geometry("1000x600")

        # Ajout d'une barre de défilement
        frame = ttk.Frame(raw_data_window)
        frame.pack(fill=tk.BOTH, expand=True)

        tree_scroll = ttk.Scrollbar(frame, orient="vertical")
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Définition des colonnes à afficher
        columns = ["Date", "Réalisé par", "Vers", "Montant"]
        df_filtered = df_user[columns].copy()

        # ✅ Convertir la colonne "Date" au format jj-mm-aaaa et supprimer l'heure
        df_filtered["Date"] = pd.to_datetime(df_filtered["Date"]).dt.strftime("%d-%m-%Y")

        tree = ttk.Treeview(frame, columns=columns, show='headings', yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=tree.yview)

        for col in columns:
            tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(tree, _col, False))
            tree.column(col, anchor="center", width=200)

        # ✅ Recalcul de la ligne "Total"
        total_montant = df_user["Montant"].sum()
        nb_utilisateurs_uniques = df_user["Réalisé par"].nunique()

        # ✅ Ajout de la ligne "Total" en haut avec le nouveau format pour "Réalisé par"
        tree.insert("", "0", values=("Total", f"{len(df_user)} / {nb_utilisateurs_uniques}", "", f"{total_montant:.0f}€"), tags=('total_row',))

        # ✅ Appliquer un style spécial pour la ligne "Total"
        tree.tag_configure('total_row', font=('Arial', 10, 'bold'), background='#D6EAF8')

        # Ajout des transactions normales (après la ligne Total)
        for _, row in df_filtered.iterrows():
            values = tuple(row[col] for col in columns)
            tree.insert("", "end", values=values)

        tree.pack(fill=tk.BOTH, expand=True)

        # Création d'un cadre pour contenir les boutons
        button_frame = ttk.Frame(raw_data_window)
        button_frame.pack(pady=10)

        # Boutons de filtrage
        btn_btb = ttk.Button(button_frame, text="Voir B2B", command=lambda: self.filter_raw_data(df_user, tree, "btb"))
        btn_ctb = ttk.Button(button_frame, text="Voir C2B", command=lambda: self.filter_raw_data(df_user, tree, "ctb"))
        btn_btc = ttk.Button(button_frame, text="Voir B2C", command=lambda: self.filter_raw_data(df_user, tree, "btc"))
        btn_conversion = ttk.Button(button_frame, text="Voir Conversions", command=lambda: self.filter_raw_data(df_user, tree, "conversion"))
        btn_tout = ttk.Button(button_frame, text="Tout Voir", command=lambda: self.filter_raw_data(df_user, tree, "tout"))

        # Placement des boutons côte à côte
        btn_btb.pack(side=tk.LEFT, padx=5)
        btn_ctb.pack(side=tk.LEFT, padx=5)
        btn_btc.pack(side=tk.LEFT, padx=5)
        btn_conversion.pack(side=tk.LEFT, padx=5)
        btn_tout.pack(side=tk.LEFT, padx=5)

        # Bouton d'exportation des transactions en Excel
        export_button = ttk.Button(raw_data_window, text="📤 Exporter les transactions",
                                command=lambda: self.export_raw_data(df_filtered, num_prof))
        export_button.pack(pady=5)

    def filter_raw_data(self, df_user, tree, filter_type):
        """Filtre les transactions affichées selon le type sélectionné."""

        # Définition des filtres
        if filter_type == "btb":
            df_filtered = df_user[(df_user["Réalisé par"].str.startswith("P")) & (df_user["Vers"].str.startswith("P"))].copy()
        elif filter_type == "ctb":
            df_filtered = df_user[(df_user["Réalisé par"].str.startswith("U")) & (df_user["Vers"].str.startswith("P"))].copy()
        elif filter_type == "btc":
            df_filtered = df_user[(df_user["Réalisé par"].str.startswith("P")) & (df_user["Vers"].str.startswith("U"))].copy()
        elif filter_type == "conversion":
            df_filtered = df_user[df_user["Vers"].str.contains("conversion", case=False, na=False)].copy()
        else:  # "tout voir"
            df_filtered = df_user.copy()

        # ✅ Correction définitive du FutureWarning
        df_filtered.loc[:, "Date"] = df_filtered["Date"].astype(str).apply(lambda x: pd.to_datetime(x).strftime("%d-%m-%Y"))

        # ✅ Suppression des anciennes données du tableau
        tree.delete(*tree.get_children())  

        # ✅ Recalcul de la ligne "Total"
        total_montant = df_filtered["Montant"].sum()
        nb_utilisateurs_uniques = df_filtered["Réalisé par"].nunique()

        # ✅ Ajout de la ligne "Total" en haut après filtrage
        tree.insert("", "0", values=("Total", f"{len(df_filtered)} / {nb_utilisateurs_uniques}", "", f"{total_montant:.0f}€"), tags=('total_row',))
        tree.tag_configure('total_row', font=('Arial', 10, 'bold'), background='#D6EAF8')

        # ✅ Ajout des transactions filtrées après la ligne "Total"
        for _, row in df_filtered.iterrows():
            values = (row["Date"], row["Réalisé par"], row["Vers"], row["Montant"])
            tree.insert("", "end", values=values)

    def export_raw_data(self, df_user, num_prof):
        """Exporte les transactions brutes du professionnel sélectionné au format Excel."""
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                                                title=f"Exporter les données brutes de {num_prof}")
        if save_path:
            try:
                df_user.to_excel(save_path, index=False)
                messagebox.showinfo("Succès", f"Les données brutes de {num_prof} ont été exportées avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'exportation : {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = UIManager(root)
    root.mainloop()
