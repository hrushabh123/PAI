import nltk
import random
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!,How may I help you??', 'Hi there!How can I help you', 'Hey!How can I help you']),
    (r'(admission)', ['For which program are you seeking admission?(Btech|MBA)']),
    (r'(Btech|MBA)', ['You ahve to meet specific requirements!!']),
    (r'(.*) (requirements|requirement)', ['You need to submit your transcripts and recommendation letters.']),
    (r'(.*) (document|documents)', ['SSLC marks card and 2nd PUC marks card']),
    (r'(.*) (deadline|deadlines)', ['The deadline for submission is usually in April.']),
    (r'(.*) (fees|fee|cost)', ['The fees vary depending on the program. You can find detailed information on our website.']),
    (r'(.*) (scholarship|scholarships)', ['We offer various scholarships based on merit and need. Please check our website for more information.']),
    (r'(.*) (contact|contact details)', ['You can reach us at admission@sahyadri.edu.in or call us at +123456789.']),
    (r'(.*) (Thank you|thank you)', ['Welcome!!']),
    (r'(.*)', ["I'm sorry, I'm not sure how to respond to that. Could you please rephrase?"]),
]

def admission_chatbot():
    print("Welcome to Admission Enquiry Bot. How can I assist you today?")
    chatbot = Chat(patterns, reflections)
    while True:
        user_input = input("You: ")
        if "thank you" in user_input.lower():
            print("Bot:", "Welcome!!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    admission_chatbot()