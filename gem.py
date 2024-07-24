import google.generativeai as genai

# Replace with your actual Gemini API key (store securely)
YOUR_API_KEY = "YOUR_API_KEY"

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
  genai.configure(api_key="AIzaSyCHWaTYOioFHmeIGco0i0popVbuwlnzYEw")

  # Select the Gemini 1.5 flash model
  model = genai.GenerativeModel('gemini-1.5-flash')

  # Generate the response
  response = model.generate_content(prompt)

  return response.text

print("Welcome to the chat! Type 'quit' to exit.")

while True:
  prompt = input("You: ")
  if prompt.lower() == 'quit':
    break
  response = generate_response(prompt)
  print("Gemini: ", response)