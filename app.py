from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.mood = 100
        self.alive = True

    def feed(self):
        if not self.alive:
            return f"{self.name} is no longer with us 💔"
        if self.hunger <= 10:
            return f"{self.name} is already full and happy! 🍗"
        self.hunger = max(0, self.hunger - 30)
        self.mood = min(100, self.mood + 10)
        return f"{self.name} is munching happily! 🦴"

    def play(self):
        if not self.alive:
            return f"{self.name} can't play anymore... 💀"
        self.mood = min(100, self.mood + 20)
        self.hunger = min(100, self.hunger + 15)
        return f"{self.name} is wagging its tail and running around! 🐾"

    def give_toy(self):
        if not self.alive:
            return f"{self.name} doesn't react... 🪦"
        self.mood = min(100, self.mood + 15)
        return f"{self.name} is chewing the toy with joy! 🎁"

    def update_health(self):
        if self.hunger >= 90:
            self.health = max(0, self.health - 15)
        elif self.mood <= 20:
            self.health = max(0, self.health - 5)
        else:
            self.health = min(100, self.health + 2)

        if self.health <= 0:
            self.die()

    def show_status(self):
        if not self.alive:
            return {
                "health": 0,
                "hunger": self.hunger,
                "mood": self.mood,
                "status": "dead",
                "alive": False
            }

        status = {
            "health": self.health,
            "hunger": self.hunger,
            "mood": self.mood,
            "status": "healthy",
            "alive": True
        }

        if self.health < 50:
            status["status"] = "unwell"
        elif self.mood < 40:
            status["status"] = "sad"
        elif self.hunger > 70:
            status["status"] = "hungry"
        return status

    def respond_to_emotion(self, user_input):
        if not self.alive:
            return f"{self.name} is sleeping forever now... 💀"

        msg = user_input.lower()

        if any(word in msg for word in ["sad", "tired", "upset", "depressed", "cry"]):
            self.mood = min(100, self.mood + 10)
            return f"{self.name} snuggles up close and gently licks your hand 🐶💖"
        elif any(word in msg for word in ["angry", "mad", "annoyed"]):
            self.mood = min(100, self.mood + 5)
            return f"{self.name} looks at you with puppy eyes and rests its head on your lap 🐕"
        elif any(word in msg for word in ["happy", "great", "excited", "joy", "good", "awesome"]):
            self.mood = min(100, self.mood + 5)
            return f"{self.name} barks excitedly and jumps around! 🐾✨"
        elif any(word in msg for word in ["love you", "miss you", "cute", "best"]):
            self.mood = min(100, self.mood + 7)
            return f"{self.name} rolls over and gives you the happiest tail wag ever! 🥰"
        elif any(word in msg for word in ["hello", "hi", "hey"]):
            return f"{self.name} wags tail and says *woof woof*! 👋🐶"
        elif any(word in msg for word in ["what's up", "sup", "yo"]):
            return f"{self.name} tilts its head and gives a little bark! 🐶"

        return f"{self.name} tilts its head curiously and listens to you 🤔🐾"

    def tick(self):
        if not self.alive:
            return
        self.hunger = min(100, self.hunger + 5)
        self.mood = max(0, self.mood - 3)
        self.update_health()

    def die(self):
        self.alive = False


# Global pet instance
pet = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_pet', methods=['POST'])
def start_pet():
    global pet
    name = request.json.get('pet_name', 'Pet')
    pet = VirtualPet(name)
    return jsonify(message=f"Your pet {name} is ready to play! 🐾")

@app.route('/feed', methods=['POST'])
def feed_pet():
    if pet:
        message = pet.feed()
        pet.tick()
        return jsonify(message=message, status=pet.show_status())
    return jsonify(message="Pet is not initialized.")

@app.route('/play', methods=['POST'])
def play_pet():
    if pet:
        message = pet.play()
        pet.tick()
        return jsonify(message=message, status=pet.show_status())
    return jsonify(message="Pet is not initialized.")

@app.route('/give_toy', methods=['POST'])
def give_toy():
    if pet:
        message = pet.give_toy()
        pet.tick()
        return jsonify(message=message, status=pet.show_status())
    return jsonify(message="Pet is not initialized.")

@app.route('/talk', methods=['POST'])
def talk_to_pet():
    if pet:
        user_input = request.json.get('user_input')
        message = pet.respond_to_emotion(user_input)
        pet.tick()
        return jsonify(message=message, status=pet.show_status())
    return jsonify(message="Pet is not initialized.")

@app.route('/status', methods=['POST'])
def show_status():
    if pet:
        return jsonify(status=pet.show_status())
    return jsonify(message="Pet is not initialized.")

if __name__ == "__main__":
    app.run(debug=True)
