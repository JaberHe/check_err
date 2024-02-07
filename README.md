# Script de Comparaison de Fichiers

Ce script Python compare deux fichiers texte pour vérifier la présence de données spécifiques dans l'un par rapport à l'autre. Il est utile pour identifier les données manquantes ou les erreurs dans un ensemble de données.

## Instructions d'utilisation

1. **Installation des dépendances**

   Assurez-vous que vous avez Python 3.x installé sur votre système.

2. **Clonage du référentiel**

   ```
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   ```

3. **Exécution du script**

   Utilisez la commande suivante pour exécuter le script :

   ```
   python3 check_err.py fichier1.txt fichier2.txt
   ```

   Assurez-vous de remplacer `fichier1.txt` et `fichier2.txt` par les chemins vers vos propres fichiers texte.

## Fonctionnalités

- **lecture_fichier_1()**: Cette fonction lit le premier fichier et crée une liste de sous-listes en fonction d'un schéma spécifique.
- **lecture_fichier_2()**: Cette fonction lit le deuxième fichier et crée une liste d'éléments.
- **comparer_listes()**: Cette fonction compare les listes générées à partir des deux fichiers pour détecter les données présentes.
- **Gestion des erreurs**: Le script vérifie la présence d'erreurs dans les données du premier fichier et les signale le cas échéant.
- **Affichage des résultats**: Le script affiche un message indiquant si les données du deuxième fichier sont complètes ou s'il en manque.

## Configuration

- Vous pouvez modifier le schéma utilisé pour différencier les éléments du premier fichier en modifiant la variable `scheme` dans le script.
- Assurez-vous d'avoir les autorisations d'exécution pour le script si nécessaire (`chmod +x check_err.py`).




