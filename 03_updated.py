import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient, events

# Load environment variables
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

session_name = "forwarder_bot"

# Initialize client with bot token
client = TelegramClient(session_name, api_id, api_hash).start(bot_token=bot_token)

# Source & Destination
SOURCE_CHANNEL = "@Technicaljs_ShoppingOffers"  # Replace with the channel ID
DESTINATION_BOT = "@link_conversion_bot"

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await client.send_message(DESTINATION_BOT, event.message)
        print(f"✅ Forwarded: {event.message.text[:50]}...")
    except Exception as e:
        print(f"❌ Error forwarding: {e}")

with client:
    print("🚀 Bot is running and forwarding messages...")
    client.run_until_disconnected()
