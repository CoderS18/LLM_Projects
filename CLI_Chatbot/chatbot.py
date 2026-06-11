import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_API_KEY"),
)

SYSTEM_PROMPT = '''
You are a helpful AI assistant. You are friendly, concise, and accurate.
If you don't know something, say so honestly.
'''

def chat(history,user_message):

    history.append({"role":"user","content": user_message })

    response= client.chat.completions.create(
        model="openai/gpt-oss-120b:free",  # :free = always zero cost,
        max_tokens=200,
        messages=history,
        temperature=0.7
    )

    reply=response.choices[0].message.content
    tokens=response.usage.total_tokens

    history.append({"role":"assistant","content":reply})
    
    return reply,tokens

def main():
    
    history=[{"role":"system","content":SYSTEM_PROMPT}]
    total_tokens=0

    while True:
        try:
            user_input=input("\nYou: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["quit","q","exit"]:
                print("\n The total tokens are used:",total_tokens)
                print("GoodBye!!")
                break
            
            reply,tokens=chat(history,user_input)
            total_tokens+=tokens
            print("\nAI:",reply)
            print("\nToken used:",total_tokens)

        except KeyboardInterrupt:
            print("\Interrupted. GoodBye")
            break

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()