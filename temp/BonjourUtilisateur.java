import java.util.Scanner; // Importation de la classe Scanner pour lire l'entrée utilisateur

public class BonjourUtilisateur {
    public static void main(String[] args) {
        // Création d'un objet Scanner pour lire l'entrée de l'utilisateur
        Scanner scanner = new Scanner(System.in);

        // Demande du nom de l'utilisateur
        System.out.print("Entrez votre nom : ");
        String nom = scanner.nextLine();

        // Affichage d'un message personnalisé
        System.out.println("Bonjour, " + nom + " ! Bienvenue dans le monde de Java.");

        // Fermeture du scanner
        scanner.close();
    }
}
