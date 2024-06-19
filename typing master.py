import time

# Sample text for the typing challenge
sample_text = (
    "The quick brown fox jumps over the lazy dog. "
    "This sentence contains every letter in the English alphabet."
)

def typing_challenge():
    print("Welcome to the Typing Challenge!")
    print("You will be shown a text. Type it as quickly and accurately as you can.")
    print("\nHere is the text:\n")
    print(sample_text)
    input("\nPress Enter when you are ready to start typing...\n")

    start_time = time.time()  # Record the start time
    user_input = input("\nStart typing now:\n")
    end_time = time.time()  # Record the end time

    time_taken = end_time - start_time
    words_per_minute = (len(user_input.split()) / time_taken) * 60

    # Calculate accuracy
    original_words = sample_text.split()
    typed_words = user_input.split()
    correct_words = sum(1 for ow, tw in zip(original_words, typed_words) if ow == tw)
    accuracy = (correct_words / len(original_words)) * 100

    print("\nTyping Challenge Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Correct words: {correct_words}/{len(original_words)}")

if __name__ == "__main__":
    typing_challenge()
