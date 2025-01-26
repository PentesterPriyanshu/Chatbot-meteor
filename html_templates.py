import os
import base64

# CSS for improved UI styling
css = '''
<style>
/* Chat Container */
.chat-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 1rem;
    border-radius: 10px;
    background: #1f1f2e;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
    overflow-y: auto;
    height: 500px;
}

/* Chat Message Styling */
.chat-message {
    padding: 1.5rem;
    border-radius: 0.75rem;
    margin-bottom: 1rem;
    display: flex;
    transition: transform 0.2s ease-in-out;
}

.chat-message:hover {
    transform: scale(1.02);
}

.chat-message.user {
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);
}

.chat-message.bot {
    background: linear-gradient(135deg, #475063, #323844);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
}

/* Avatar Styling */
.chat-message .avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    overflow: hidden;
    margin-right: 1rem;
    border: 3px solid #4b5563;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease-in-out;
}

.chat-message .avatar img:hover {
    transform: rotate(360deg);
}

/* Message Content */
.chat-message .message {
    width: 100%;
    padding: 0 1rem;
    color: #ffffff;
    font-size: 1rem;
    line-height: 1.5;
    word-wrap: break-word;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Scrollbar Styling */
.chat-container::-webkit-scrollbar {
    width: 8px;
}

.chat-container::-webkit-scrollbar-track {
    background: #1f1f2e;
}

.chat-container::-webkit-scrollbar-thumb {
    background-color: #4b5563;
    border-radius: 10px;
}
</style>
'''

def convert_image_to_base64(image_path):
    """Convert an image to Base64 format."""
    with open(image_path, "rb") as image_file:
        return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

# Convert bot and user avatars to Base64
bot_avatar_base64 = convert_image_to_base64("assets/bot.png")
user_avatar_base64 = convert_image_to_base64("assets/avatar.png")
# Function to generate the bot chat message
def get_bot_template(MSG):
    bot_template = f'''
    <div class="chat-message bot">
        <div class="avatar">
            <img src="{bot_avatar_base64}" alt="Bot Avatar">
        </div>
        <div class="message">
            {MSG}
        </div>
    </div>
    '''
    return bot_template

# Function to generate the user chat message
def get_user_template(MSG):
    user_template = f'''
    <div class="chat-message user">
        <div class="avatar">
            <img src="{user_avatar_base64}" alt="User Avatar">
        </div>
        <div class="message">
            {MSG}
        </div>
    </div>
    '''
    return user_template

# Final function to render the chat interface
def render_chat(messages):
    html_content = f'''
    <div class="chat-container">
        {css}
    '''
    for message in messages:
        if message['role'] == 'bot':
            html_content += get_bot_template(message['content'])
        elif message['role'] == 'user':
            html_content += get_user_template(message['content'])
    html_content += '</div>'
    return html_content

# Example Usage
if __name__ == "__main__":
    chat_messages = [
        {"role": "user", "content": "Hello! How can I upload a file?"},
        {"role": "bot", "content": "Hi! Just drag and drop the file into the upload area."},
        {"role": "user", "content": "Great, it worked. Thanks!"},
        {"role": "bot", "content": "You're welcome! Let me know if you need any more help."}
    ]
    # Generate and save the HTML
    with open("chat_interface.html", "w", encoding="utf-8") as f:
        f.write(render_chat(chat_messages))
    print("Chat interface generated successfully! Open chat_interface.html.")
