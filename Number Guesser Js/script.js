let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => {
  const randomNumber = Math.floor(Math.random() * 10);
  return randomNumber;
}

const compareGuesses = (humanGuess, compGuess, secretNumber) => {
  const humanDiff = Math.abs(secretNumber - humanGuess);
  const computerDiff = Math.abs(secretNumber - compGuess);
  if (humanDiff <= computerDiff){
    return true;
  } else{
    return false;
  }
}


const updateScore = (winner) => {
  if(winner == 'human'){
  humanScore++;
} else if(winner == 'computer'){
  computerScore++;
}
}

const advanceRound = () => {
  currentRoundNumber++;
}




