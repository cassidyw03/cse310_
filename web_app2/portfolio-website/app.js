const express = require('express');
const app = express();
const PORT = 3000;

// Set the view engine
app.set('view engine', 'ejs');

// Serve static files
app.use(express.static('public'));

// Define routes
app.get('/', (req, res) => {
    res.render('index', { title: "Portfolio", name: "Cassidy Whitehead" });
});

app.get('/projects', (req, res) => {
    res.render('projects', { title: "Projects", projects: [
        { name: "Health Tracker App", description: "Track food, mood, and more." },
        { name: "Game Project", description: "An interactive arcade-style game." },
    ] });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
