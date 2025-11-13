import requests, os , json

def generate_kbc_questions(topic, num_questions=1):
    
    # Apni token key yahan se lein (ensure it's the correct one)
    # token = os.environ.get('token_key') # Better use .get() for safety
    # Agar aapne HF_TOKEN use kiya hai to:
    # token = os.environ.get('HF_TOKEN')
    
    token = os.environ['token_key'] # Aapke existing code ke hisaab se
    
    if not token:
        print("❌ Error: 'token_key' environment variable is not set.")
        return None

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json" 
    }

    # *** SYSTEM MESSAGE (Master Plan) ***
    system_instruction = (
        "You are an expert quiz master for a KBC-style game. "
        "Your task is to generate {num_questions} multiple-choice questions "
        "on the given topic and format the entire output strictly as a JSON object."
        "Do not include any other text or explanation outside the JSON."
        "\n\nJSON Schema:\n"
        "[\n"
        "  {{\n"
        "    \"question\": \"The MCQ question text.\",\n"
        "    \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"],\n"
        "    \"answer\": \"The correct option text (e.g., Option B)\",\n"
        "    \"topic\": \"The subject of the question\"\n"
        "  }},\n"
        "  // ... (for more questions)\n"
        "]"
    ).format(num_questions=num_questions)


    # *** USER MESSAGE (Dynamic Request) ***
    user_prompt = (
        f"Generate {num_questions} difficult questions for a game show. "
        f"The user's main interest/topic is: **{topic}**. "
        f"Ensure the questions are engaging and suitable for a KBC format."
    )

    payload = {
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        "model": "HuggingFaceH4/zephyr-7b-beta", # Free/Open-source model use karein
        "temperature": 0.8, # Thoda randomness (creativity) ke liye
        "max_new_tokens": 1024 # Zaroorat ke hisaab se badha sakte hain
    }
    
    print(f"Generating questions on: {topic}...")
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        try:
            response_data = response.json()
            # AI ka raw generated text nikalna
            raw_content = response_data['choices'][0]['message']['content'].strip()
            
            # JSON string ko parse karna
            # Note: Kai baar AI sirf JSON array deta hai, isliye hum [] se shuru karte hain
            if raw_content.startswith('```json'):
                raw_content = raw_content.strip('```json').strip('```').strip()
            
            questions_json = json.loads(raw_content)
            
            print("✅ Successfully Generated Questions:")
            for i, q in enumerate(questions_json):
                print(f"\n--- Question {i+1} ---")
                print(f"Q: {q.get('question')}")
                print(f"Options: {q.get('options')}")
                print(f"Answer: {q.get('answer')} (Topic: {q.get('topic')})")
            
            return questions_json

        except Exception as e:
            print(f"❌ Error during JSON parsing or data extraction: {e}")
            print("\nRaw AI Response:")
            print(response.text)
            return None

    else:
        print(f"❌ API Request Failed with status code: {response.status_code}")
        print("Error Response:")
        print(response.text)
        return None

# --- Function Call (Run the Master Plan) ---

# Yahan aap apna interest aur kitne questions chahiye, woh define karein
my_interest_topic = "Indian Mythology and Space Exploration" 
number_of_mcqs = 3

generated_data = generate_kbc_questions(my_interest_topic, number_of_mcqs)

# generated_data ko ab aap apne game logic mein use kar sakte hain
if generated_data:
    print("\n--- Game Data Ready ---")
    # Example: First question: generated_data[0]['question']