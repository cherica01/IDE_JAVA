Code Editor JAVA with Error Assistance
Description

Ce projet est une application web permettant de :

    Écrire et compiler du code Java directement via une interface conviviale.
    Afficher les résultats de la compilation ou les erreurs sous une forme simplifiée et lisible.
    Fournir des solutions claires aux erreurs grâce à l'intégration de l'API Gemini (Gemini 1.5 Flask).

L'application utilise Django pour le backend, SQLite comme base de données et inclut une interface intuitive en une seule page.
Fonctionnalités

    Éditeur de texte : permet de rédiger du code Java.
    Compilation du code : un bouton "Compiler" exécute le code et retourne les résultats.
    Affichage des erreurs :
        Résultat brut de la compilation.
        Explications des erreurs reformulées en langage simple via l'API Gemini.
        Solutions proposées pour corriger les erreurs.
    Interface utilisateur simplifiée : navigation en une seule page.

Technologies utilisées
Backend :

    Django : pour la logique backend et l'API REST.
    SQLite : pour stocker les codes et logs.
    Gemini 1.5 Flask API : pour l’analyse des erreurs et la génération de solutions.

Frontend :

    HTML, CSS, JavaScript : pour l'interface utilisateur.
    Framework JavaScript (optionnel) : possibilité d'utiliser React pour une expérience plus interactive.
