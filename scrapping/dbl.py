import pandas as pd
import os

print("="*60)
print("🧹 SUPPRESSION DES DOUBLONS - ELMINASSA")
print("="*60)

# Chemin du fichier
fichier_elminassa = 'data_raw/elminassa.csv'
fichier_nettoye = 'data_raw/elminassa_sans_doublons.csv'

# Vérifier que le fichier existe
if not os.path.exists(fichier_elminassa):
    print(f"❌ Fichier non trouvé: {fichier_elminassa}")
    exit()

print(f"📂 Chargement du fichier: {fichier_elminassa}")

# Charger le fichier
df = pd.read_csv(fichier_elminassa)
print(f"📊 Lignes avant nettoyage: {len(df)}")

# Afficher les colonnes disponibles
print(f"\n📋 Colonnes disponibles: {list(df.columns)}")

# Compter les doublons basés sur le titre et le prix (les plus significatifs)
doublons_titre_prix = df.duplicated(subset=['titre', 'prix'], keep='first').sum()
print(f"\n🔍 Doublons basés sur titre+prix: {doublons_titre_prix}")

# Supprimer les doublons (garder la première occurrence)
df_sans_doublons = df.drop_duplicates(subset=['titre', 'prix'], keep='first')

print(f"📊 Lignes après suppression: {len(df_sans_doublons)}")
print(f"✅ {len(df) - len(df_sans_doublons)} doublons supprimés")

# Sauvegarder le fichier nettoyé
df_sans_doublons.to_csv(fichier_nettoye, index=False, encoding='utf-8-sig')
print(f"\n💾 Fichier nettoyé sauvegardé: {fichier_nettoye}")

# Mettre à jour le fichier original
reponse = input("\n🔄 Remplacer le fichier original par la version nettoyée ? (o/n): ")
if reponse.lower() == 'o':
    df_sans_doublons.to_csv(fichier_elminassa, index=False, encoding='utf-8-sig')
    print(f"✅ Fichier original remplacé")
else:
    print("❌ Fichier original conservé")

print("\n🎉 Nettoyage terminé!")