//Main class

public class Magic8 {

    //Generated random number, Static keyword used to save the value when calling the random varibale in the main method.
  
    static int random = (int) (Math.random() * 8 + 1);


    //Main Method 
    public static void main (String[] args) {


    System.out.println("Hello there!");
    System.out.println("Welcome to Magic 8 Ball");
    System.out.println("\n");
    System.out.println("Your fortune...");

   
   //switch statement to print all possible outcomes. 

   switch(random){

      case 1:
          System.out.println("Without a doubt");
        break;
      case 2:
          System.out.println("As I see it, yes");
        break;
      case 3: 
          System.out.println("It is decidedly so");
        break;
      case 4:
           System.out.println("Cannot predict now");
        break;
      case 5:
           System.out.println("My reply is no");
        break;
      case 6:
           System.out.println("My reply is no");
        break;
      case 7:
            System.out.println("Outlook not so good");
        break;
      case 8:
            System.out.println("Reply hazy, try again");
        break;
      default:
            System.out.println("Oops please roll again..Something went wrong");
        break;

    }
   }
}
