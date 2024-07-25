from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Replace with your actual Gemini API key (store securely)
YOUR_API_KEY = "AIzaSyAQnTUAk7QfJaiIvgXskj_H6EZYk4pTW54"

def generate_response(prompt):
    """
    Sends a request to the Gemini 1.5 flash model using the provided prompt
    and returns the generated response.

    Args:
        prompt: The text prompt to send to the model.

    Returns:
        The generated response from the model.
    """

    # Configure the API key
    genai.configure(api_key=YOUR_API_KEY)

    # Select the Gemini 1.5 flash model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Generate the response
    response = model.generate_content(prompt)

    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = generate_response(user_message)
    return response  # Return the response directly

if __name__ == '__main__':
    app.run(debug=True)
