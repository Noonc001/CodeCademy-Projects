using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {

   public new static void UpdatePosition(string keyPress, out int xCoord, out int yCoord) {

    //intialise the corrds variables
     xCoord = 0;
     yCoord = 0;

     //the switch statement determines the keypress outcome by adjusting the X or Y coords

     switch(keyPress){
       case "UpArrow":
            yCoord -= 1;
        break;
       case "DownArrow":
            yCoord += 1;
        break;
       case "LeftArrow":
           xCoord -= 1;
        break;
       case "RightArrow":
            xCoord += 1;
        break;
     }
   }


     public new static char UpdateCursor(string keyPressed){

      switch(keyPressed){ //switch statement to deal with each possible key press
        case "LeftArrow":
            return '<';
          break;
        case "RightArrow":
            return '>';
          break;
        case "UpArrow":
            return '^';
          break;
        case "DownArrow":
            return 'v';
          break;
        default:
          return 'o';
      }
    }

    // will prevent the Current Coords from going off the screen
    public new static int KeepInBounds(int CurrentCoord, int MaxCoord){
      if(CurrentCoord < 0){ 
        return 0;   //will keep coord from going off the left or top sides of screen
      } else if (CurrentCoord > MaxCoord){
        return MaxCoord -1; //This will prevent Coord going off the screen right side or bottom
      } else {
        return CurrentCoord; // carry on playing if no sides are touched
      }
    }

    //boolean didscore method
    public new static bool DidScore(int xChar, int yChar, int xFruit, int yFruit){
      if(xChar == xFruit && yChar == yFruit){   //checking if both sets of Coords Cross 
        return true;  
      } else {
        return false; //returns false if they do not
      }
    }
   
}
}
