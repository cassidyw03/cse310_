# Overview

{This project furthered my learning in software development by expanding my view of programming languages. Rust is different than other languages I've learned because it implements safety catches and can execute many things at the same time, or demonstrates concurrency.}

{This software demonstrates the Rust language's ability to create a very safe and secure environment. Mutable variables, like the guess variable, can be changed after. But the default variable is un-mutable. This program also uses the parse() method's Result type for error handling. Expect and match deal with invalid inputs from the user. The match expression is a powerful tool to sort through cases. }

{I did this project to follow along and learn the Rust language and syntax. I wanted to see what Rust has to offer as a language and what it projects it could be useful for in the future.}

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running and a walkthrough of the code. Focus should be on sharing what you learned about the language syntax.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

{I used cargo for building, compiling, and running the code.}

{I used Rust to develop the game. The libraries that were used were the Standard Library (std) and the Rand library. The std library provided the use of input and output as well as the cmp, comparison. The Rand library was useful to generate the random number used. This was also put into the Cargo.toml file to manage dependencies.}

# Useful Websites

- [Web Site Name](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html)
- [Web Site Name](https://www.tutorialspoint.com/rust/rust_data_types.htm)

# Future Work

- In the future I would add a GUI that is more fun than the terminal.
- This project could become a word guessing game as well. It would need an imported file with words to randomly select. It would need the secret number to change to a secret word variable and compare the user input of a string to another string instead of a number. The match logic would also need to be replaced with a simpler comparison of if statements if the word is guessed, if a letter is guessed, and if the letter doesn't fit.