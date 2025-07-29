🐶 **Virtual Pet AI Assistant – Flask Web App**<br><br>
📌**Overview**:<br>
This is a virtual pet simulation built using Python (Flask) and HTML/CSS/JavaScript. The pet responds to your actions and emotional inputs like a real companion, and its health and mood change over time. If you ignore your pet, it may sadly pass away — but don’t worry, you can adopt a new one!

🎯 Features:<br>
✅ Create a new pet with a custom name<br>
🍗 Feed, 🎾 Play, 🧸 Give Toy, 💬 Talk to the pet<br>
📉 Stats decay over time (hunger/mood)<br>
🧠 Emotion-aware response system (e.g., reacts to "sad", "happy", etc.)<br>
⚰️ Pet can die if neglected (health = 0)<br>
🔁 Restart the game with a new pet<br>
🖼️ Cute pet avatar and dynamic interface<br>

💻 Technologies Used:<br>

Python -- Backend logic (Flask)<br>
Flask -- API routes & state engine<br>
HTML/CSS -- Web UI<br>
JavaScript -- Frontend logic & fetch API<br>
Jinja2 -- Flask templating<br>

📁 Project Structure<br>
virtual-pet/<br>
├── app.py<br>
├── static/<br>
│   └── puppy.png<br>
├── templates/<br>
│   └── index.html<br>
└── README.md<br>

**🚀 How to Run<br>**

1. Install Flask<br>
Make sure Python is installed. Then run:<br>

"pip install flask"<br>

2. Run the App<br>
In the project folder:<br>

"python app.py"<br>

3. Open in Browser<br>
Go to:<br>

http://localhost:5000<br>

**🧠 Emotion Detection<br>**

The pet responds to how you’re feeling. Try entering:<br>

"I’m sad" → Pet will comfort you 💖<br>

"I’m happy" → Pet will jump with joy 🐾<br>

"I love you" → Pet gives you cuddles 🥰<br>

✨ Future Enhancements<br>
 Mood-based pet avatar change<br>

 Add sound effects (bark/meow)<br>

 Deploy online (Render/Heroku)<br>
