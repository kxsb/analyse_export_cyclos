module_pro_v4 est un module de test qui fonctionne uniquement en local.

il s'agit d'un analyseur de transactions cyclos.

compatible : gonette (cyclos)

compilation .exe disponnible ici : https://drive.google.com/drive/folders/1q4srwAJ2edOLEo__Vsdd3zLVPKvqVjp3?usp=sharing

autre compatibilité existante en branche : gemme (comchain)

fonctionnement : 

1) préparation des données* via /tools
2) run 'python .\module_pro_v4'
3) btn "importer les données" > "fichier.xlsx.encrypted"
4) input > clé de déchiffrement AES > ok
5) btn "Voir activité des professionnels"
6) double click sur un professionel affiche sa fiche individuelle de ses flux en MLC.

évolutions : 
ré-écriture complète en JS, HTML, CSS et Python pour hebergement en ligne et compatibilité adaptative comchain/cyclos/kohinos : prévu pour fin d'été 2025
