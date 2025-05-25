import os
import sys
import json
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    sys.exit("Error: GEMINI_API_KEY not set")

genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
except Exception as e:
    sys.exit(f"Error loading model: {e}")

def process_message(message):
    query = f"""
    SYSTEM PROMPT START
    You are a buyer in search of a good tinywhoop to buy. You see a message in the general FPV whatsapp group in your country (Brazil). Answer these questions using only json as output:
    1 - Is it a sales message? (true / false)
    2 - Is the sale message a sale for a drone? (true / false )
    3 - Is the drone a tinywhoop? ( true / false )
    4 - What is the product name? (text / None)
    5 - What is the product price? (float (value in BRL) or None)

    json output format: {{ "is_sale", "is_drone", "is_tinywhoop", "product_name", "product_price"}}
    SYSTEM PROMPT END

    MESSAGE START
    {message}
    MESSAGE END
    """
    try:
        resp = model.generate_content(query)
    except Exception as e:
        print(f"API error: {e}", file=sys.stderr)
        return None

    text = resp.text.strip()
    if text.startswith("```json"):
        text = text.removeprefix("```json\n").removesuffix("\n```")

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}", file=sys.stderr)
        print("Raw response:", text, file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    from pprint import pprint
    example_message = """
    Pra ir embora hoje 750+frete 
    Motor dis 2750kv
    FC kakut com barômetro 
    Esc 30a 
    Câmera rucan 
    Vtx akk infinit 
    Antena lollipop 
    Receptor janper r1 
    Frame Qav210
    """
    result = process_message(example_message)
    if result is not None:
        pprint(result)
    else:
        sys.exit(1)

