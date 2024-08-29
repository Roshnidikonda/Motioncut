def count_words(text):
    text = text.strip()
    
    if not text:
        return 0
    
    word_count = 0
    in_word = False
    
    for char in text:
        if char.isalnum():  
            if not in_word:
                in_word = True
                word_count += 1
        else:
            in_word = False
    
    return word_count

def main():
    user_input = input("Enter a sentence or paragraph: ")
    count = count_words(user_input)
    print(f"Word count: {count}")

if __name__ == "__main__":
    main()
