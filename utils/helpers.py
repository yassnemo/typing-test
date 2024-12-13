import random
import os

def load_sentences(file_path='data/sentences.txt'):
    """
    Loads sentences from a text file.
    
    Parameters:
        file_path (str): Path to the sentences file.
    
    Returns:
        list: A list of sentences.
    """
    try:
        with open(file_path, 'r') as file:
            sentences = [line.strip() for line in file if line.strip()]
        if not sentences:
            print(f"Warning: No sentences found in {file_path}. Using default sentence.")
            return ["The quick brown fox jumps over the lazy dog."]
        return sentences
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        print("Using default sentence.")
        return ["The quick brown fox jumps over the lazy dog."]

def get_random_sentence():
    """
    Selects and returns a random sentence from the sentences list.
    
    Returns:
        str: A randomly selected sentence.
    """
    sentences = load_sentences()
    return random.choice(sentences) if sentences else "The quick brown fox jumps over the lazy dog."

def calculate_wpm(word_count, time_seconds):
    """
    Calculates Words Per Minute (WPM).
    
    Parameters:
        word_count (int): Number of words typed.
        time_seconds (float): Time taken in seconds.
    
    Returns:
        float: Typing speed in WPM.
    """
    minutes = time_seconds / 60
    return (word_count / minutes) if minutes > 0 else 0

def calculate_accuracy(original, typed):
    """
    Calculates the number of correct and incorrect words.
    
    Parameters:
        original (str): The original sentence.
        typed (str): The user's typed input.
    
    Returns:
        tuple: (correct_words, incorrect_words, total_words)
    """
    original_words = original.split()
    typed_words = typed.split()
    correct = 0
    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1
    total = len(original_words)
    incorrect = total - correct
    return correct, incorrect, total
