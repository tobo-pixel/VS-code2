// import java.util.Scanner;
// public class practice {
//     public static void main(String[] args) {
//         System.out.print("Your name: ");
//         Scanner scanner = new Scanner(System.in);
//         String name = scanner.nextLine().toLowerCase();
//         char [] vowels = {'a','e','i','o','u'};
//         int noofvowels = 0;
//         for(int x = 0;x < name.length();x++){
//             char n = name.charAt(x);
//             for (int y = 0;y < vowels.length;y++){
//                 if (n == vowels[y]){
//                     noofvowels ++;
//                 }
//             }
//         }
//         System.out.println("There are " + noofvowels + " vowels in your name");
//     }
// }
import java.util.Scanner;
public class vowels{
  public static void main(String[] args){
    System.out.print("Your name: ");
    Scanner scanner = new Scanner(System.in);
    String name = scanner.nextLine().toLowerCase();
    char [] vowels = {'a','e','i','o','u'};
    int noofvowels = 0;
    for(int x = 0;x < name.length();x++){
      char n = name.charAt(x);
      for(int y = 0;y < vowels.length;y++){
        if (n == vowels[y]){
          noofvowels++;
        }
      }
    }
    System.out.println("There are " + noofvowels + " vowels in your name");
  }
}
    