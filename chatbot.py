def get_bot_response(user_input):
    """
    Function to generate bot responses based on keywords found in user input
    Uses if/elif statements for rule-based matching with keyword detection
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Check for greeting keywords
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi there! Nice to meet you!"
    
    # Check for how are you type questions
    elif "how are you" in user_input or "how r u" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    
    # Check for positive responses
    elif "fine" in user_input or "good" in user_input or "great" in user_input or "awesome" in user_input:
        return "That's wonderful to hear!"
    
    # Check for negative responses  
    elif "bad" in user_input or "sad" in user_input or "not good" in user_input or "terrible" in user_input:
        return "I'm sorry to hear that. Hope things get better for you!"
    
    # Check for name related questions
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm ChatBot, a simple rule-based chatbot! What's your name?"
    
    # Check if user is telling their name
    elif "my name is" in user_input or "i am" in user_input or "call me" in user_input:
        return "Nice to meet you! Thanks for telling me your name."
    
    # Check for capability questions
    elif "what can you do" in user_input or "what do you do" in user_input or "your job" in user_input:
        return "I can chat with you and try to understand what you're saying!"
    
    # Check for age questions
    elif "how old" in user_input or "your age" in user_input:
        return "I don't have an age - I'm just a computer program!"
    
    # Check for location questions
    elif "where are you" in user_input or "where do you live" in user_input:
        return "I exist in the digital world, wherever there are computers!"
    
    # Check for thank you
    elif "thank you" in user_input or "thanks" in user_input or "thx" in user_input:
        return "You're very welcome! Happy to help!"
    
    # Check for help requests
    elif "help" in user_input or "assist" in user_input:
        return "I'm here to help! Just type whatever you want to say and I'll try to respond."
    
    # Check for goodbye
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input or "farewell" in user_input:
        return "Goodbye! It was nice chatting with you!"
    
    # Check for yes responses
    elif "yes" in user_input or "yeah" in user_input or "sure" in user_input or "okay" in user_input:
        return "Great! What else would you like to talk about?"
    
    # Check for no responses
    elif "no" in user_input or "nope" in user_input or "nah" in user_input:
        return "That's okay! Is there something else on your mind?"
    
    # Check for weather talk
    elif "weather" in user_input or "rain" in user_input or "sunny" in user_input or "cold" in user_input:
        return "I can't check the weather, but I hope it's nice where you are!"
    
    # Check for time questions
    elif "time" in user_input or "what time" in user_input:
        return "I don't have access to the current time, but you can check your device!"
    
    # Check for food talk
    elif "food" in user_input or "eat" in user_input or "hungry" in user_input:
        return "I don't eat food, but I'd love to hear about your favorite dishes!"
    
    # Check for hobby/interest questions
    elif "hobby" in user_input or "like to do" in user_input or "interests" in user_input:
        return "My main hobby is chatting with people like you! What do you like to do?"
    
    # Check for jokes
    elif "joke" in user_input or "funny" in user_input:
        return "I'm not great at jokes, but here's one: Why don't scientists trust atoms? Because they make up everything!"
    
    # Check for compliments
    elif "smart" in user_input or "good job" in user_input or "well done" in user_input:
        return "Thank you! That's very kind of you to say!"
    
    # Check for problems/issues
    elif "problem" in user_input or "issue" in user_input or "wrong" in user_input:
        return "I'm sorry if there's a problem. Can you tell me more about what's wrong?"
    
    else:
        # Default responses for unmatched input
        default_responses = [
            "That's interesting! Tell me more about that.",
            "I see what you're saying. Can you elaborate?",
            "That's something to think about!",
            "I'm listening. What else is on your mind?",
            "Hmm, that's a good point. What do you think about it?"
        ]
        # Use simple method to pick response (based on input length)
        response_index = len(user_input) % len(default_responses)
        return default_responses[response_index]

def main_chat_loop():
    """
    Main function containing the chat loop
    Uses while loop to keep conversation going
    """
    print("=" * 50)
    print("        FLEXIBLE RULE-BASED CHATBOT")
    print("=" * 50)
    print("Hello! I'm a chatbot that understands natural language.")
    print("Just type whatever you want to say - no need to use exact phrases!")
    print("Type 'quit' or 'exit' to end our conversation.")
    print("-" * 50)
    
    # Main chat loop
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check for exit conditions
        if user_input.lower().strip() in ['quit', 'exit']:
            print("ChatBot: Thanks for the great conversation! Goodbye!")
            break
        
        # Skip empty input
        if not user_input.strip():
            print("ChatBot: I'm here when you're ready to chat!")
            continue
        
        # Get bot response using the function
        bot_response = get_bot_response(user_input)
        
        # Display bot response
        print(f"ChatBot: {bot_response}")

# Main program execution
if __name__ == "__main__":
    print("Welcome to the Flexible Rule-Based Chatbot!")
    print("This chatbot understands keywords in your sentences.")
    print("\nExamples of what you can say:")
    print("- 'Hello there, how are you doing today?'")
    print("- 'I'm feeling pretty good right now'") 
    print("- 'Can you tell me what your name is?'")
    print("- 'Thanks a lot for your help'")
    print("- Or anything else you want to talk about!")
    
    # Start the main chat loop
    try:
        main_chat_loop()
    except KeyboardInterrupt:
        print("\nChatBot: Chat interrupted. Thanks for talking with me!")
    except Exception as e:
        print(f"\nChatBot: Oops, something went wrong: {e}")

