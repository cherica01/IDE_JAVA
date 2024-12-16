from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import subprocess
import os
import re
import shutil

def nettoyer_temp():
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.makedirs('temp', exist_ok=True)


genai.configure(api_key="AIzaSyDHjOrj5AeGEOBJpI5sBbc0t8dqJ0fA_Sk")
model = genai.GenerativeModel("gemini-1.5-flash")


def interface_principale(request):
    return render(request, 'interface.html')

@csrf_exempt
@csrf_exempt
def compiler_code(request):
    if request.method == 'POST':
        code_java = request.POST.get('code_java', '')

        # Trouver le nom de la classe publique
        match = re.search(r'public\s+class\s+(\w+)', code_java)
        nom_fichier = "Code.java"
        if match:
            nom_classe = match.group(1)
            nom_fichier = f"{nom_classe}.java"

        chemin_fichier = f"temp/{nom_fichier}"

        # Créer le répertoire temporaire
        os.makedirs('temp', exist_ok=True)
        with open(chemin_fichier, 'w') as fichier:
            fichier.write(code_java)

        # Compilation du code
        resultat_compilation = subprocess.run(
            ["javac", chemin_fichier],
            capture_output=True, text=True
        )

        if resultat_compilation.returncode == 0:
            # Exécution du code si compilation réussie
            resultat_execution = subprocess.run(
                ["java", "-cp", "temp", match.group(1)],
                capture_output=True, text=True
            )

            if resultat_execution.returncode == 0:
                # Succès de l'exécution
                commentaire = generer_commentaire(code_java)
                return JsonResponse({
                    "resultat": resultat_execution.stdout,
                    "erreurs": "",
                    "solution": "",
                    "commentaire": commentaire
                })
            else:
                # Échec lors de l'exécution
                erreurs_execution = resultat_execution.stderr
                erreurs_claires = reformuler_erreur(erreurs_execution)
                solution_execution = generer_solution(erreurs_execution)
                commentaire = generer_commentaire(erreurs_execution)
                return JsonResponse({
                    "resultat": "",
                    "erreurs": erreurs_claires,
                    "solution": solution_execution,
                    "commentaire": commentaire
                })
        else:
            # Échec lors de la compilation
            erreurs_compilation = resultat_compilation.stderr
            erreurs_claires = reformuler_erreur(erreurs_compilation)
            solution_compilation = generer_solution(erreurs_compilation)
            commentaire = generer_commentaire(erreurs_compilation)
            return JsonResponse({
                "resultat": "",
                "erreurs": erreurs_claires,
                "solution": solution_compilation,
                "commentaire": commentaire
            })

    return JsonResponse({
        "resultat": "",
        "erreurs": "Requête invalide.",
        "solution": "",
        "commentaire": ""
    })

# Fonction pour générer un commentaire à propos du code ou des erreurs
def generer_commentaire(contenu):
    prompt = f"Propose un commentaire constructif sur ce code Java ou cette erreur pour aider l'utilisateur à améliorer sa pratique de programmation . Proposez le en une phrase : \n{contenu}"
    response = model.generate_content(prompt)
    return response.text


# Fonction pour reformuler les erreurs avec Gemini
def reformuler_erreur(erreurs):
    prompt = f"Reformule ces erreurs Java de manière claire et concise pour qu'un débutant puisse les comprendre en une phrase: \n{erreurs}"
    response = model.generate_content(prompt)
    return response.text

# Fonction pour fournir des solutions aux erreurs
def generer_solution(erreurs):
    prompt = f"Donne une solution claire et précise pour corriger les erreurs suivantes en Java en une phrase , ennocez juste la solution sans repeter l'erreur: \n{erreurs}"
    response = model.generate_content(prompt)
    return response.text
