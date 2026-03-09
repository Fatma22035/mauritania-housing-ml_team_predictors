import pandas as pd
import numpy as np
import os
import csv
import re

print("="*60)
print("🔧 RÉPARATION DU CSV - CONSERVATION DE TOUTES LES LIGNES")
print("="*60)

# Chemin du fichier
fichier_final = 'data_raw/final_data_raw.csv'
fichier_backup = 'data_raw/final_data_raw_backup.csv'
fichier_corrige = 'data_raw/final_data_raw_corrige.csv'

print(f"📂 Analyse du fichier: {fichier_final}")

# Lire le fichier en mode texte pour analyser
with open(fichier_final, 'r', encoding='utf-8') as f:
    lignes_brutes = f.readlines()

print(f"📊 Lignes brutes: {len(lignes_brutes)}")

# Extraire l'en-tête
en_tete = lignes_brutes[0].strip().split(',')
nb_colonnes = len(en_tete)
print(f"📋 En-tête: {en_tete}")
print(f"📋 Nombre de colonnes attendu: {nb_colonnes}")

# Fonction pour nettoyer une ligne
def nettoyer_ligne(ligne):
    """Nettoie une ligne CSV en protégeant les virgules dans les descriptions"""
    ligne = ligne.strip()
    
    # Si la ligne a le bon nombre de virgules, on la garde telle quelle
    if ligne.count(',') == nb_colonnes - 1:
        return ligne
    
    # Sinon, on doit réparer
    print(f"\n⚠️ Ligne problématique détectée:")
    print(f"   {ligne[:200]}...")
    
    # Compter les guillemets
    guillemets = ligne.count('"')
    
    # Si nombre impair de guillemets, c'est que la description contient des virgules
    if guillemets % 2 == 1:
        print(f"   ➡️ Nombre impair de guillemets: {guillemets}")
        
        # On va protéger la description en l'entourant de guillemets
        parties = ligne.split(',')
        print(f"   ➡️ La ligne est coupée en {len(parties)} parties")
        
        # On essaie de reconstituer
        nouvelle_ligne = []
        i = 0
        while i < len(parties):
            partie = parties[i]
            if partie.startswith('"') and not partie.endswith('"'):
                # Début d'une description entre guillemets
                description = partie
                i += 1
                while i < len(parties) and not parties[i].endswith('"'):
                    description += ',' + parties[i]
                    i += 1
                if i < len(parties):
                    description += ',' + parties[i]
                nouvelle_ligne.append(description)
            else:
                nouvelle_ligne.append(partie)
            i += 1
        
        ligne_reparée = ','.join(nouvelle_ligne)
        print(f"   ✅ Ligne réparée: {ligne_reparée[:200]}...")
        return ligne_reparée
    
    return ligne

# Traiter toutes les lignes
lignes_nettoyees = [lignes_brutes[0].strip()]  # Garder l'en-tête

for i, ligne in enumerate(lignes_brutes[1:], 2):
    ligne_nettoyee = nettoyer_ligne(ligne)
    lignes_nettoyees.append(ligne_nettoyee)

print(f"\n📊 Lignes après nettoyage: {len(lignes_nettoyees)}")

# Sauvegarder le fichier corrigé
with open(fichier_corrige, 'w', encoding='utf-8') as f:
    for ligne in lignes_nettoyees:
        f.write(ligne + '\n')

print(f"\n💾 Fichier corrigé sauvegardé: {fichier_corrige}")

# Maintenant, charger avec pandas pour vérifier
try:
    df = pd.read_csv(fichier_corrige)
    print(f"\n✅ Lecture réussie avec pandas: {len(df)} lignes")
    print(f"📋 Colonnes: {list(df.columns)}")
    
    # Remplacer "Non spécifié" par NaN
    print("\n🧹 Remplacement des 'Non spécifié' par NaN...")
    
    total_avant = 0
    for col in df.columns:
        if df[col].dtype == 'object':
            count = (df[col] == 'Non spécifié').sum()
            total_avant += count
    
    print(f"🔍 Total 'Non spécifié' avant: {total_avant}")
    
    df_clean = df.replace('Non spécifié', np.nan)
    df_clean = df_clean.replace('Non spécifiée', np.nan)
    
    # Sauvegarder le fichier final propre
    fichier_final_propre = 'data_raw/final_data_raw_propre.csv'
    df_clean.to_csv(fichier_final_propre, index=False, encoding='utf-8-sig')
    print(f"💾 Fichier final propre sauvegardé: {fichier_final_propre}")
    
    # Statistiques
    print(f"\n📊 STATISTIQUES FINALES:")
    print(f"   - Total lignes: {len(df_clean)}")
    print(f"   - Sources: {df_clean['source'].unique()}")
    for source in df_clean['source'].unique():
        count = len(df_clean[df_clean['source'] == source])
        print(f"      • {source}: {count} annonces")
    
    # Option pour remplacer l'original
    reponse = input("\n🔄 Remplacer le fichier original par la version propre ? (o/n): ")
    if reponse.lower() == 'o':
        # Créer une sauvegarde de l'original
        os.rename(fichier_final, fichier_backup)
        print(f"💾 Original sauvegardé: {fichier_backup}")
        
        # Copier la version propre
        df_clean.to_csv(fichier_final, index=False, encoding='utf-8-sig')
        print(f"✅ Fichier original remplacé")
    
    print("\n👀 Aperçu:")
    colonnes_principales = ['source', 'titre', 'prix', 'type_bien', 'quartier']
    colonnes_existantes = [col for col in colonnes_principales if col in df_clean.columns]
    print(df_clean[colonnes_existantes].head(10).to_string())
    
except Exception as e:
    print(f"\n❌ Erreur lors de la lecture: {e}")
    print("💡 Il reste encore des problèmes dans le fichier")

print("\n🎉 Nettoyage terminé!")