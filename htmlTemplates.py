css = '''
<style>
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.chat-message.user {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
.chat-message.bot {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}
.chat-message .avatar {
    width: 15%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.chat-message .avatar img {
    max-width: 60px;
    max-height: 60px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
    line-height: 1.6;
}
.chat-message .message strong {
    color: #fff;
    font-weight: 600;
}
.chat-message .message hr {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.3);
    margin: 1rem 0;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/bottts/svg?seed=syllabus" style="max-height: 60px; max-width: 60px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=student" style="max-height: 60px; max-width: 60px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
