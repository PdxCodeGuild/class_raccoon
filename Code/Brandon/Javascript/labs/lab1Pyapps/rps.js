    // rps game--

    let rock = document.getElementById('rock')
    let paper = document.getElementById('paper')
    let scissors = document.getElementById('scissors')
    let resultHeader = document.getElementById('result')
    
    rock.addEventListener("click",() => game('rock'))
    paper.addEventListener("click", () => game('paper'))
    scissors.addEventListener("click", () => game('scissors'))
    
    console.log(rock)
    function game(userChoice){
        let result = ''
        let throws = [
        'rock',
        'paper',
        'scissors',]
        let computerChoice = throws[Math.floor(Math.random()*throws.length)]
    
        if (userChoice === computerChoice){
            result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Tie`;
            }
            else if (userChoice === 'paper' && computerChoice === 'rock'){
            result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Win`;
            }
            else if (userChoice === 'rock' && computerChoice === 'scissors'){
            result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Win`;
            }
            else if (userChoice === 'scissors' && computerChoice === 'rock'){
           result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Lose`;
            }
            else if (userChoice === 'rock' && computerChoice === 'paper'){
           result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Lose`;
            }
            else if (userChoice === 'paper' && computerChoice === 'scissors'){
           result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Lose`;
            }
            else if (userChoice === 'scissors' || computerChoice === 'paper'){
                result = `The computer chose ${computerChoice} and you chose ${userChoice}, you Win`;}
    
            resultHeader.innerText = result
            console.log(userChoice)
           
    
    }