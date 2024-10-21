use std::io;
use rand::Rng;
// random put in cargo.toml file
use std::cmp::Ordering;

fn main() {
    // first message
    println!("Guess the number!");

    // generate secret number
    let secret_number = rand::thread_rng().gen_range(1..=100);

    // debugging code to display the secret number
    // println!("The secret number is: {secret_number}");

    // loop allows for many guesses
    loop {
        println!("Please input your guess.");

        // creates mutable string to hold user input as a string
        let mut guess = String::new();

        // input output, stores the input as the guess variable
        io::stdin()
            .read_line(&mut guess)
            // error handling if input fails
            .expect("Failed to read line");

        // old code using .expect
        // let guess: u32 = guess.trim().parse().expect("Please type a number!");

        // updated code without .expect
        // uses parse Result function to error handle 

        let guess: u32 = match guess.trim().parse() {
            // parse returns a Result enum that has the varients of Ok and Err
            Ok(num) => num,
            // if input was not a number (parsing fails), skip the rest of loop and prompt again
            Err(_) => continue,
            // underscore is a catchall value
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            // cmp compares
            // Match is made up of arms, in this case Ordering::Less, Greater, and Equal. It looks at each arm until a successful match is made
            // ordering enum below
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break; 
                // breaks out of infinite loop!
            }
        }

    }    
    

}
