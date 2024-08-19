from flask import Flask, request, jsonify, render_template
import random
import re

app = Flask(__name__)

# Define a dictionary of keywords and corresponding responses
response_dict = {
    'stress': [
        "It sounds like you're feeling stressed. Here are a few tips: try deep breathing exercises, take regular breaks, and consider speaking to a mental health professional.",
        "Stress can be overwhelming. Have you tried mindfulness or relaxation techniques? Sometimes talking things out can also help.",
        "Managing stress is important. Try setting aside time for hobbies or activities you enjoy. If it's persistent, seeking professional help might be beneficial.",
        "Feeling stressed is common. Consider creating a stress management plan or reaching out to a counselor for personalized support."
    ],
    'anxiety': [
        "Anxiety can be tough. Practicing mindfulness and staying active might help. If it becomes overwhelming, talking to a therapist could be useful.",
        "Feeling anxious is challenging. Have you tried keeping a journal or practicing relaxation techniques? These can sometimes help manage anxiety.",
        "Managing anxiety often involves trying different strategies. Consider speaking to a mental health professional who can guide you with tailored advice.",
        "Anxiety can be managed with various techniques. Exploring relaxation exercises and talking to a counselor might provide relief."
    ],
    'depression': [
        "If you're feeling depressed, reaching out to a mental health professional can provide you with support and treatment options.",
        "Depression can be difficult to handle alone. Talking to a counselor or therapist might offer the help and guidance you need.",
        "It is important to seek professional help if you're experiencing depression. They can work with you to develop a plan for managing your symptoms.",
        "Support from a mental health professional is crucial for dealing with depression. They can help you explore effective treatment strategies."
    ],
    'pulling': [
        "If you're struggling with hair-pulling or similar behaviors, consider reaching out to a mental health professional for support and strategies.",
        "Compulsive behaviors can be challenging. A therapist might help you develop healthier coping mechanisms and address these urges.",
        "Managing hair-pulling involves understanding its triggers. Speaking with a counselor can provide you with strategies to manage and reduce this behavior.",
        "It's important to get support if you're dealing with compulsive behaviors. A mental health professional can assist you in finding effective ways to cope."
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input', '').lower()
    response = suggest_solution(user_input)
    return jsonify({'response': response})

def suggest_solution(user_input):
    # Check for keywords in the user input
    for keyword in response_dict:
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            # Return a random response from the list of responses
            return random.choice(response_dict[keyword])
    
    return "I'm here to listen. If you're comfortable sharing more, we can talk through it together."

if __name__ == '__main__':
    app.run(debug=True)

    
    