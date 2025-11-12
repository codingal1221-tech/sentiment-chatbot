import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

user_name = input(Fore.MAGENTA + "Please enter your name: " + Style.RESET_ALL).strip()

if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(Fore.CYAN + "Hello, Agent " + user_name + "!" + Style.RESET_ALL)
print(Fore.CYAN + "I'm Sentiment Spy! Welcome to Sentiment Spy!" + Style.RESET_ALL)
print(Fore.CYAN + "Type a sentence and I will analyze your sentence with TextBlob and show you the sentiment." + Style.RESET_ALL)
print(Fore.CYAN + "Type 'exit' to quit, 'history' to view all conversations, or 'clear' to clear history." + Style.RESET_ALL)

while True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()

    if not user_input:
        print(Fore.YELLOW + "Please enter some text or a valid command." + Style.RESET_ALL)
        continue

    if user_input.lower() == "exit":
        print(Fore.BLUE + "Exiting Sentiment Spy. Farewell, Agent " + user_name + "! " + Style.RESET_ALL)
        break

    elif user_input.lower() == "clear":
        conversation_history.clear()
        print(Fore.RED + "Conversation history cleared!" + Style.RESET_ALL)
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(Fore.YELLOW + "No conversation history yet." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Conversation History:" + Style.RESET_ALL)
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😔"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text}{Style.RESET_ALL} (Polarity: {polarity:.2f}, Sentiment: {sentiment_type})")
        continue

    # Analyze sentiment
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😄"
    elif polarity < -0.1:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😔"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(Fore.MAGENTA + "Sentiment Detected!" + Style.RESET_ALL)
    print(f"{color}{emoji} Sentiment: {sentiment_type}{Style.RESET_ALL} | Polarity: {polarity:.2f}")
