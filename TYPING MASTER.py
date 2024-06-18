import time

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    
    correct = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1
    
    accuracy = (correct / len(original_words)) * 100
    return accuracy

def typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text exactly as it appears:")
    print(f"\n{text}\n")
    
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input("\nStart typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    accuracy = calculate_accuracy(text, user_input)
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    
    if accuracy == 100:
        print("Perfect typing! Well done!")
    elif accuracy >= 90:
        print("Great job! Almost perfect.")
    elif accuracy >= 75:
        print("Good effort! Keep practicing.")
    else:
        print("Keep trying! Practice makes perfect.")

typing_test()