import time
import sys
from utils.helpers import get_random_sentence, load_sentences
from utils.helpers import calculate_wpm, calculate_accuracy

def typing_test(rounds=1):
    """Conducts the typing test for a specified number of rounds."""
    print("\n" + "="*50)
    print("         Welcome to the Enhanced Typing Test!")
    print("="*50 + "\n")
    
    total_time = 0
    total_words = 0
    total_correct = 0
    total_incorrect = 0

    for round_num in range(1, rounds + 1):
        sentence = get_random_sentence()
        print(f"Round {round_num} of {rounds}")
        print("Type the following sentence as quickly and accurately as you can:\n")
        print(f"    {sentence}\n")
        
        input("Press Enter to start...")
        start_time = time.time()
        
        typed_input = input("\nYour input: ")
        end_time = time.time()
        
        time_taken = end_time - start_time
        word_count = len(typed_input.split())
        wpm = calculate_wpm(word_count, time_taken)
        correct, incorrect, total = calculate_accuracy(sentence, typed_input)
        
        total_time += time_taken
        total_words += word_count
        total_correct += correct
        total_incorrect += incorrect
        
        print("\n" + "-"*50)
        print(f"Time Taken: {time_taken:.2f} seconds")
        print(f"Words Typed: {word_count}")
        print(f"Typing Speed: {wpm:.2f} WPM")
        print(f"Correct Words: {correct}")
        print(f"Incorrect Words: {incorrect}")
        accuracy_percentage = (correct / total) * 100 if total > 0 else 0
        print(f"Accuracy: {accuracy_percentage:.2f}%")
        print("-"*50 + "\n")
    
    # Summary after all rounds
    print("\n" + "="*50)
    print("              Test Summary")
    print("="*50 + "\n")
    overall_wpm = calculate_wpm(total_words, total_time)
    total_sentences = rounds
    average_sentence_length = len(get_random_sentence().split())
    overall_accuracy = (total_correct / (rounds * average_sentence_length)) * 100 if average_sentence_length > 0 else 0
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Total Words Typed: {total_words}")
    print(f"Overall Typing Speed: {overall_wpm:.2f} WPM")
    print(f"Total Correct Words: {total_correct}")
    print(f"Total Incorrect Words: {total_incorrect}")
    print(f"Overall Accuracy: {overall_accuracy:.2f}%")
    print("\nThank you for taking the typing test! Keep practicing to improve your speed and accuracy.\n")

def main():
    """Main function to run the typing test program."""
    try:
        print("Welcome to the Typing Test Program!")
        rounds_input = input("Enter the number of rounds you want to take (default is 1): ")
        rounds = int(rounds_input) if rounds_input.strip().isdigit() else 1
        if rounds < 1:
            print("Number of rounds must be at least 1. Setting to 1.")
            rounds = 1
        typing_test(rounds)
    except KeyboardInterrupt:
        print("\n\nTyping test interrupted. Goodbye!")
        sys.exit()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
