import random

# List of 100 questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "How many continents are there?", "answer": "7"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "How many states are there in the USA?", "answer": "50"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "How many colors are there in a rainbow?", "answer": "7"},
    {"question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"question": "What is the currency of Japan?", "answer": "Yen"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "Who was the first president of the United States?", "answer": "George Washington"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "What is the fastest land animal?", "answer": "Cheetah"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "How many bones are there in the human body?", "answer": "206"},
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "Who painted the Sistine Chapel ceiling?", "answer": "Michelangelo"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "What is the capital of China?", "answer": "Beijing"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "What is the capital of Brazil?", "answer": "Brasília"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "J.D. Salinger"},
    {"question": "What is the main ingredient in hummus?", "answer": "Chickpeas"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
    {"question": "Who wrote 'Moby Dick'?", "answer": "Herman Melville"},
    {"question": "What is the chemical symbol for iron?", "answer": "Fe"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "What is the most spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "What is the capital of the United Kingdom?", "answer": "London"},
    {"question": "What is the tallest building in the world?", "answer": "Burj Khalifa"},
    {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
    {"question": "What is the primary ingredient in a traditional Japanese miso soup?", "answer": "Miso"},
    {"question": "What is the chemical symbol for sodium?", "answer": "Na"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul"},
    {"question": "Who wrote 'The Hobbit'?", "answer": "J.R.R. Tolkien"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
    {"question": "What is the largest lake in the world?", "answer": "Caspian Sea"},
    {"question": "What is the capital of South Africa?", "answer": "Pretoria"},
    {"question": "Who was the first man to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    {"question": "What is the capital of Norway?", "answer": "Oslo"},
    {"question": "What is the largest continent?", "answer": "Asia"},
    {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
    {"question": "Who painted 'Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "What is the capital of Greece?", "answer": "Athens"},
    {"question": "What is the smallest bone in the human body?", "answer": "Stapes"},
    {"question": "What is the capital of Finland?", "answer": "Helsinki"},
    {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"},
    {"question": "What is the capital of Poland?", "answer": "Warsaw"},
    {"question": "What is the largest bird in the world?", "answer": "Ostrich"},
    {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
    {"question": "Who wrote 'War and Peace'?", "answer": "Leo Tolstoy"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "What is the main ingredient in borscht?", "answer": "Beetroot"},
    {"question": "What is the capital of Ukraine?", "answer": "Kyiv"},
    {"question": "Who wrote 'The Divine Comedy'?", "answer": "Dante Alighieri"},
    {"question": "What is the capital of Iraq?", "answer": "Baghdad"},
    {"question": "What is the largest country by area?", "answer": "Russia"},
    {"question": "What is the capital of Indonesia?", "answer": "Jakarta"},
    {"question": "Who wrote 'The Alchemist'?", "answer": "Paulo Coelho"},
    {"question": "What is the capital of Iran?", "answer": "Tehran"},
    {"question": "What is the smallest unit of matter?", "answer": "Atom"},
    {"question": "What is the capital of Chile?", "answer": "Santiago"},
    {"question": "Who wrote 'Les Misérables'?", "answer": "Victor Hugo"},
    {"question": "What is the capital of Denmark?", "answer": "Copenhagen"},
    {"question": "What is the most abundant gas in Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "What is the capital of the Philippines?", "answer": "Manila"},
    {"question": "Who wrote 'Frankenstein'?", "answer": "Mary Shelley"},
    {"question": "What is the capital of the Netherlands?", "answer": "Amsterdam"},
    {"question": "What is the speed of light in a vacuum?", "answer": "299,792,458 meters per second"},
    {"question": "What is the capital of Belgium?", "answer": "Brussels"},
    {"question": "Who wrote 'The Picture of Dorian Gray'?", "answer": "Oscar Wilde"},
    {"question": "What is the capital of Hungary?", "answer": "Budapest"},
    {"question": "What is the chemical symbol for potassium?", "answer": "K"},
]

def quiz():
    random.shuffle(questions)  # Shuffle questions to randomize the order
    user_answers = []
    score = 0
    
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        user_answer = input("Your answer: ").strip()
        user_answers.append({"question": q["question"], "user_answer": user_answer, "correct_answer": q["answer"]})
        
        if user_answer.lower() == q["answer"].lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer was: {q['answer']}\n")
    
    print("\nQuiz Complete!")
    print(f"Your final score is: {score} out of {len(questions)}\n")
    
    print("Review your answers:")
    for idx, ans in enumerate(user_answers):
        print(f"Question {idx + 1}: {ans['question']}")
        print(f"Your answer: {ans['user_answer']}")
        print(f"Correct answer: {ans['correct_answer']}")
        print()

if __name__ == "__main__":
    quiz()
