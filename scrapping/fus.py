import pandas as pd
import os

print("="*60)
print("🔄 FUSION DES FICHIERS DATA")
print("="*60)

# Chemins des fichiers
fichier_principal = 'data_raw/final_data_raw.csv'
fichier_menazel = 'data_raw/menazel.csv'
fichier_sortie = 'data_raw.csv'

# Vérifier que les fichiers existent
if not os.path.exists(fichier_principal):
    print(f"❌ Fichier principal non trouvé: {fichier_principal}")
    exit()

if not os.path.exists(fichier_menazel):
    print(f"❌ Fichier menazel non trouvé: {fichier_menazel}")
    exit()

print("📂 Chargement des fichiers...")

# Charger les deux fichiers
df_principal = pd.read_csv(fichier_principal)
df_menazel = pd.read_csv(fichier_menazel)

print(f"✅ Fichier principal: {len(df_principal)} lignes")
print(f"✅ Fichier menazel: {len(df_menazel)} lignes")
print(f"\n📋 Colonnes fichier principal: {list(df_principal.columns)}")
print(f"📋 Colonnes fichier menazel: {list(df_menazel.columns)}")

# Aligner les colonnes de menazel sur celles du principal
print("\n🔄 Alignement des colonnes...")

# Créer un dictionnaire de mapping
colonnes_manquantes = []

for col in df_principal.columns:
    if col not in df_menazel.columns:
        # Si la colonne n'existe pas dans menazel, on l'ajoute avec valeur par défaut
        df_menazel[col] = "Non spécifié"
        colonnes_manquantes.append(col)

print(f"✅ Colonnes ajoutées à menazel: {colonnes_manquantes}")

# Garder seulement les colonnes du principal dans le même ordre
df_menazel_aligné = df_menazel[df_principal.columns]

print("\n🔄 Fusion des données...")

# Fusionner les deux dataframes
df_final = pd.concat([df_principal, df_menazel_aligné], ignore_index=True)

# Supprimer les doublons basés sur l'URL si la colonne existe
if 'url' in df_final.columns:
    avant = len(df_final)
    df_final = df_final.drop_duplicates(subset=['url'], keep='first')
    apres = len(df_final)
    print(f"✅ Doublons supprimés: {avant - apres} lignes en moins")

# Sauvegarder le résultat
df_final.to_csv(fichier_sortie, index=False, encoding='utf-8-sig')

print("\n" + "="*60)
print("📊 RÉSULTAT DE LA FUSION")
print("="*60)
print(f"📁 Fichier final: {fichier_sortie}")
print(f"📊 Total lignes: {len(df_final)}")
print(f"\n📋 Répartition par source:")
print(df_final['source'].value_counts())

print("\n✅ Fusion terminée avec succès!")