import random

# Define a list of inspirational quotes
quotes = [
    "Make the most of yourself….for that is all there is of you. – Ralph Waldo Emerson",
    "It is never too late to be what you might have been. – George Eliot",
    "It takes courage to grow up and become who you really are. – E.E. Cummings",
    "Go confidently in the direction of your dreams. Live the life you have imagined. – Henry David Thoreau",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Whatever you are, be a good one. – Abraham Lincoln",
    "I never dreamed about success. I worked for it. – Estee Lauder",
    "Doubt kills more dreams than failure ever will. – Suzy Kassem",
    "When you find your why, you find a way to make it happen. – Eric Thomas",
    "The two most important days in your life are the day you are born and the day you find out why. – Mark Twain",
    "The best way to predict your future is to create it. – Peter Drucker",
    "You can find a better you inside of you. Why don’t you search for that? – Munia Khan",
    "Pessimism leads to weakness, optimism to power. – William James",
    "The moment you doubt whether you can fly, you cease for ever to be able to do it. – J.M. Barrie",
    "If you can dream it, then you can achieve it. – Zig Ziglar",
    "You don’t want to look back and know you could have done better. – Unknown",
    "Setting goals is the first step into turning the invisible into the visible. – Tony Robbins",
    "I attribute my success to this: I never gave or took any excuse. – Florence Nightingale",
    "Don’t let your fear decide your future. – Shalane Flanagan",
    "Only those who dare to fail greatly can ever achieve greatly. ― Robert F. Kennedy",
    "It is during our darkest moments that we must focus to see the light. — Aristotle Onassis",
    "Strength does not come from physical capacity. It comes from an indomitable will. – Mahatma Gandhi",
    "The true success is the person who invented himself. – Al Goldstein",
    "Give up on being perfect and start working on becoming yourself. – Anna Quindlen",
    "The future belongs to those who believe in the beauty of their dreams. – Franklin D. Roosevelt",
    "There is only one thing that makes a dream impossible to achieve: the fear of failure. ― Paulo Coelho",
    "Don’t downgrade your dream just to fit your reality. Upgrade your conviction to match your destiny. – John Assaraf",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "Whatever you do, do with all your might. – Marcus Tullius Cicero",
    "You were put on this Earth to achieve your greatest self, to live out your purpose, and to do it courageously. – Steve Maraboli",
    "Definiteness of purpose is the starting point of all achievement. – W. Clement Stone",
    "He who is not courageous enough to take risks will accomplish nothing in life. – Muhammad Ali",
    "All our dreams can come true, if we have the courage to pursue them. – Walt Disney",
    "You don’t manifest dreams without taking chances. – Stephen Richards",
"Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. ― Roy T. Bennett",
"Opportunities don’t happen. You create them. – Chris Grosser",
"Never underestimate the power you have to take your life in a new direction. – Germany Kent",
"I’m not telling you it is going to be easy, I’m telling you it’s going to be worth it. – Art Williams",
"Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
"Once you choose hope, anything’s possible. – Christopher Reeve",
"Life shrinks or expands in proportion to one’s courage. – Anaïs Nin",
"You cannot fail at being yourself. – Wayne Dyer",
"Fortune always favors the brave, and never helps a man who does not help himself. – P. T. Barnum",
"Success is stumbling from failure to failure with no loss of enthusiasm. – Winston S. Churchill",
"Self-belief and hard work will always earn you success. – Virat Kohli",
"Perfection is not attainable, but if we chase perfection we can catch excellence. — Vince Lombardi",
"You matter. – Unknown",
"Be a voice not an echo. – Unknown",
"You are the only one who can limit your greatness. – Unknown",
"The very best thing you can do for the whole world is to make the best of yourself. – Unknown",
"Every next level of your life will demand a different version of you. – Unknown",
"Do something today that your future self will thank you for. – Unknown",
"Create a vision that makes you wanna jump out of bed in the morning. – Unknown",
"The harder the struggle, the more glorious the triumph. – Unknown",
"Don’t try to be perfect. Just try to be better than you were yesterday. – Unknown",
"Excuses will always be there for you. Opportunity won’t. – Unknown",
"We may encounter many defeats but we must not be defeated. – Maya Angelou",
"Always believe that something wonderful is about to happen. – Coco Chanel",
"I survived because the fire inside me burned brighter than the fire around me. – Joshua Graham",
"If it doesn’t challenge you, it won’t change you. – Unknown",
"Goals may give focus, but dreams give power. – John Maxwell",
"Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
"Life is a process. We are a process. The universe is a process. – Anne Wilson Schaef",
"The greatest danger for most of us is not that our aim is too high and we miss it, but that it is too low and we reach it. – Michaelangelo",
"Perfection is not attainable, but if we chase perfection we can catch excellence. — Vince Lombardi",
"A dream does not become reality through magic; it takes sweat, determination and hard work. – Colin Powell",
"If you believe it will work out, you’ll see opportunities. If you believe it won’t, you will see obstacles. – Wayne Dyer",
"If you set goals and go after them with all the determination you can muster, your gifts will take you places that will amaze you. – Les Brown",
"Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t. – Rikki Rogers
"Don’t be afraid to start over. It’s a brand new opportunity to rebuild what you truly want. – Unknown",
"The secret of change is to focus all of your energy, not on fighting the old, but on building the new. – Socrates",
"No matter how hard times may get, always hold your head up and be strong; show them you’re not as weak as they think you are. – Unknown",
"Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. – Jamie Paolinetti",
"Your mind is a powerful thing. When you fill it with positive thoughts, your life will start to change.",
"Don’t think about what might go wrong. Think about what might go right. – Unknown",
"What the mind can conceive and believe, and the heart desire, you can achieve. ― Norman Vincent Peale",
"The struggle you’re in today is developing the strength you need for tomorrow. – Unknown",
"Success doesn’t just come and find you, you have to go out and get it. – Unknown",
"Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. You got to keep going. – Chantal Sutherland",
"Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. ― Roy T. Bennett",
"Choosing to be positive and having a grateful attitude is going to determine how you’re going to live your life. – Joel Osteen",
"If you can tune into your purpose and really align with it, setting goals so that your vision is an expression of that purpose, then life flows much more easily. – Jack Canfield",
"Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no hope at all. — Dale Carnegie",
"Until you’re broken, you don’t know what you’re made of. It gives you the ability to build yourself all over again, but stronger than ever. – Unknown",
"Learn from the past, set vivid, detailed goals for the future, and live in the only moment of time over which you have any control: now. – Denis Waitley",
"Set a goal so big that you can’t achieve it until you grow into the person who can. – Unknown",
"We don’t develop courage by being happy every day. We develop it by surviving difficult times and challenging adversity. – Barbara De Angelis",
"I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear. – Nelson Mandela",
]

Define a function to generate a random quote from the list of quotes
def get_quote():
return random.choice(quotes)

Define a function to handle user input and generate a response
def generate_response(user_input):
return get_quote()

Start the chatbot
print("Welcome to the Inspirational Quote Chatbot! Type 'quit' to exit.")
while True:
user_input = input("You: ")
if user_input.lower() == 'quit':
break
response = generate_response(user_input)
print("Chatbot:", response)
