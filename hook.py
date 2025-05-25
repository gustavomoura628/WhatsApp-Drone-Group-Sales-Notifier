# TODO: Handle gemini rate limiting (in a better way)

from flask import Flask, request

from pprint import pprint
import json
import time
import random


import llm
import telegram

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

def process_text(text):

    # Rate limit handling
    while True:
        res = llm.process_message(text)
        if res is not None:
            break
        else:
            seconds = random.randint(30,120)
            print(f"Hit rate limit, sleeping for {seconds} seconds")
            time.sleep(seconds)

    print("Processing:", text)
    pprint(res)

    # UNCOMMENT FOR DEBUGGING:
    # telegram.send_message(text + "\n" + json.dumps(res))

    is_sale = res["is_sale"]
    is_drone = res["is_drone"]
    is_tinywhoop = res["is_tinywhoop"]
    product_name = res["product_name"]
    product_price = res["product_price"]


    if is_sale and is_drone and is_tinywhoop:
        telegram.send_message("Tinywhoop Sale Found!\nName: "+str(product_name)+"\nPrice: "+str(product_price)+"\nFull text: \n\n"+text)

    return

@app.route("/hook", methods=["POST"])
def hook():
    data = request.get_json()
    text = data["text"]
    process_text(text)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
