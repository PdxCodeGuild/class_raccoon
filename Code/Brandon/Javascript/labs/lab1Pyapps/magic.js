// 8 ball js------
let eight = document.getElementById("eight");
let answer = document.getElementById("answer");
let eightball = document.getElementById("eight-ball");
let question = document.getElementById("question");

// answers for the questions---
var answers = ["It is certain", 
    "It is decidedly so", 
    "Without a doubt", 
    "Yes - definitely",
    "You may rely on it", 
    "As I see it, yes", 
    "Most likely", 
    "Outlook good",
    "Not in your wildest dreams", 
    "Yes", "Signs point to yes",
    "Don't count on it",
    "If i had to guess, I would say so.",
    "Elmo says no",
    "Did you even think that was an option?", 
    "My reply is no",
    "My sources say no", 
    "Outlook not so good",
    "Very doubtful", 
    "Reply hazy, try again", 
    "Ask again later", 
    "Better not tell you now",
    "Cannot predict now", 
    "Concentrate and ask again"
    ];


    
    question.addEventListener("keypress", function(e) {
        if (e.key == 'Enter'){
            if (question.value.length < 1) { //check for whether or not there is a question to be answered
            alert('Enter a question!');
            } 
            else {
            eightball.classList.toggle("answer-shake")
            eight.innerText = "";
            let num = Math.floor(Math.random() * (answers.length));//random number choice, multiplied by the length and used as [i]
            answer.innerText = answers[num];//uses the random [i] as the answer choice and put is in the answer block
            setTimeout(function(){
                eightball.classList.toggle("answer-shake")
            }, 1000)
            
        }
    }
    });
    // end 8 ball----






