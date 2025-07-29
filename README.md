🐶 Virtual Pet AI Assistant – Flask Web App
📌 Overview
This is a virtual pet simulation built using Python (Flask) and HTML/CSS/JavaScript. The pet responds to your actions and emotional inputs like a real companion, and its health and mood change over time. If you ignore your pet, it may sadly pass away — but don’t worry, you can adopt a new one!

🎯 Features
✅ Create a new pet with a custom name

🍗 Feed, 🎾 Play, 🧸 Give Toy, 💬 Talk to the pet

📉 Stats decay over time (hunger/mood)

🧠 Emotion-aware response system (e.g., reacts to "sad", "happy", etc.)

⚰️ Pet can die if neglected (health = 0)

🔁 Restart the game with a new pet

🖼️ Cute pet avatar and dynamic interface

💻 Technologies Used
Tool	Purpose
Python	Backend logic (Flask)
Flask	API routes & state engine
HTML/CSS	Web UI
JavaScript	Frontend logic & fetch API
Jinja2	Flask templating

📁 Project Structure
csharp
Copy
Edit
virtual-pet/
├── app.py                      # Flask backend
├── static/
│   └── puppy.png              # Pet avatar image
├── templates/
│   └── index.html             # Frontend HTML
└── README.md                  # This file
🚀 How to Run
Install Flask
Make sure Python is installed. Then run:

bash
Copy
Edit
pip install flask
Run the App
In the project folder:

bash
Copy
Edit
python app.py
Open in Browser
Go to:

arduino
Copy
Edit
http://localhost:5000
🧠 Emotion Detection
The pet responds to how you’re feeling. Try entering:

"I’m sad" → Pet will comfort you 💖

"I’m happy" → Pet will jump with joy 🐾

"I love you" → Pet gives you cuddles 🥰

📸 Screenshots (Optional)
Add screenshots here if you're uploading to GitHub for visual reference.

✨ Future Enhancements
 Mood-based pet avatar change

 Add sound effects (bark/meow)

 Deploy online (Render/Heroku)

 Use localStorage or database for saving pet state
