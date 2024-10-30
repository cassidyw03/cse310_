use std::fs::File;
use std::io::Read;
use base64::encode;

fn png_to_data_url(file_path: &str) -> Result<String, std::io::Error> {
    // Open the PNG file
    let mut file = File::open(file_path)?;
    
    // Read the file into a byte buffer
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer)?;
    
    // Encode the buffer as a Base64 string
    let base64_encoded = encode(&buffer);
    
    // Prefix with Data URL scheme for PNG
    let data_url = format!("data:image/png;base64,{}", base64_encoded);
    
    Ok(data_url)
}

fn main() {
    let file_path = ".logo.png"; // replace with your file path
    match png_to_data_url(file_path) {
        Ok(data_url) => println!("Data URL: {}", data_url),
        Err(e) => eprintln!("Error: {}", e),
    }
}
