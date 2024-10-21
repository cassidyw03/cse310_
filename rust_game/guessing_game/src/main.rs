use std::io;
use rand::Rng;
// random put in cargo.toml file
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    // println!("The secret number is: {secret_number}");

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        // input output
        io::stdin()
            .read_line(&mut guess)
            // error handling
            .expect("Failed to read line");

        // let guess: u32 = guess.trim().parse().expect("Please type a number!");
        let guess: u32 = match guess.trim().parse() {
            // parse returns a Result enum that has the varients of Ok and Err
            Ok(num) => num,
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
            }
        }

    }    
    

}
