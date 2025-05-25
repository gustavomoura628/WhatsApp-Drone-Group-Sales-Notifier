# WhatsApp Drone Group Sales Notifier  
I want to buy a drone, and I'm in a local WhatsApp group for FPV drone enthusiasts. Sometimes, people sell their drones there.
  
This script will scrape all messages from the WhatsApp group, and process them with Gemini. Sales messages are then sent to my Telegram using a bot.  

# Browser Setup  
First, install violentmonkey on Firefox. Then add the violentmonkey.js script to it.  
Now open WhatsApp Web. Check the addon to make sure that _WA-DOM-Tap-Continuous_ is active.  

In a terminal, run:  
```bash
export FLASK_APP=test_hook.py
flask run -h 0.0.0.0 -p 5000
```  
And then reload the WhatsApp page. Go to a group. You should see a bunch of messages appearing in your terminal.  


# Requirements  
Just run  
```bash
pip install -r requirements.txt
```  

# Environment Variables  
Save these variables to a file called .env  
```bash
export FLASK_APP=hook.py
export GEMINI_API_KEY="YOUR_GEMINI_KEY"
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
export TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```  

Get you Telegram bot token from Botfather. You can find the chat id by sending a message to your bot and then opening `https://api.telegram.org/botTELEGRAM_BOT_TOKEN/getUpdates` in your web browser.  
You can get a Gemini api key from `https://aistudio.google.com/app/apikey`  

# Running the app  
In a terminal, run  
```bash
flask run -h 0.0.0.0 -p 5000
```
