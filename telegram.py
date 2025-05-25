#!/usr/bin/env python3
import os, sys, requests

from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    sys.exit("Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID env vars")

def send_message(text: str):
    resp = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": text}
    )
    resp.raise_for_status()
    return resp.json()

if __name__=="__main__":
    if len(sys.argv)!=2:
        sys.exit("Usage: send.py \"message\"")
    print(send_message(sys.argv[1]))

