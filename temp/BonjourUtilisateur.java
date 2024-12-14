import java.util.Scanner; // Importation de la classe Scanner pour lire l'entr�e utilisateur

public class BonjourUtilisateur {
    public static void main(String[] args) {
        // Cr�ation d'un objet Scanner pour lire l'entr�e de l'utilisateur
        Scanner scanner = new Scanner(System.in);

        // Demande du nom de l'utilisateur
        System.out.print("Entrez votre nom : ");
        String nom = scanner.nextLine();

        // Affichage d'un message personnalis�
        System.out.println("Bonjour, " + nom + " ! Bienvenue dans le monde de Java.");

        // Fermeture du scanner
        scanner.close();
    }
}
