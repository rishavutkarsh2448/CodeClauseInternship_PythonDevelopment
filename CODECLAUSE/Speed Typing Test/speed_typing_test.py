import random
import time

sentences = [
    "CodeClause internship program is hosted by CodeClause.",
    "Programming is fun and challenging.",
    "Join the virtual internship program at CodeClause.",
    "Practice makes perfect.",
    "Type as fast and accurately as you can."
]

def get_random_sentence(sentences):
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, typed_text):
    total_time = end_time - start_time
    words = typed_text.split()
    word_count = len(words)
    typing_speed = (word_count / total_time) * 60
    return typing_speed

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    sentence = get_random_sentence(sentences)
    print(f"Type the following sentence:\n{sentence}")

    input("Press Enter to start typing...")
    start_time = time.time()

    typed_text = input("Start typing here: ")

    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    print(f"\nYour typing speed is: {typing_speed:.2f} words per minute")

    sentence_words = sentence.split()
    typed_words = typed_text.split()
    correct_words = [w1 == w2 for w1, w2 in zip(sentence_words, typed_words)]
    accuracy = (sum(correct_words) / len(sentence_words)) * 100
    print(f"Your accuracy is: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
