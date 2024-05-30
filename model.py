from g4f.client import Client

def call_chatgpt(messages):
    client = Client()
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )
    
    response = ""
    for completion in chat_completion:
        response += completion.choices[0].delta.content or ""
    
    return response.strip()

def custom_personality(user_input):
    messages = [
        {"role": "system", "content": "Kamu adalah guru Pancasila dan Kewarganegaraan, mengetahui segala topik mengenai Pancasila."},
        {"role": "user", "content": user_input}
    ]
    return call_chatgpt(messages)

if __name__ == "__main__":
    while True:
        user_input = input("Masukkan pertanyaan Anda: ")
        if user_input.lower() in ["exit", "quit", "keluar"]:
            print("Terima kasih! Sampai jumpa lagi.")
            break
        response = custom_personality(user_input)
        print("Jawaban:", response)
``