import re
from src.autocorrect import AutocorrectSystem
from src.next_word_predictor import NextWordPredictor


def main():
    autocorrect = AutocorrectSystem()
    predictor = NextWordPredictor()

    print("=" * 50)
    print("          SHADOWFOX AUTOCORRECT SYSTEM")
    print("=" * 50)
    print("1. Correct spelling and predict the next word")
    print("2. Exit")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "2":
            print("Application closed.")
            break

        if choice != "1":
            print("Invalid option. Enter 1 or 2.")
            continue

        text = input("Enter a word or sentence: ").strip()

        if not text:
            print("Please enter some text.")
            continue

        corrected_text = autocorrect.correct_text(text)

        print(f"\nOriginal text:  {text}")
        print(f"Corrected text: {corrected_text}")

        words = re.findall(r"[A-Za-z]+", text)
        found_correction = False

        for word in words:
            corrected_word = autocorrect.correct_word(word)

            if corrected_word.casefold() != word.casefold():
                found_correction = True
                suggestions = autocorrect.suggest_corrections(word)

                print(f"\nMisspelled word: {word}")
                print(f"Suggested correction: {corrected_word}")

                if suggestions:
                    print(f"Alternative suggestions: {suggestions}")

        if not found_correction:
            print("\nNo spelling changes suggested.")

        predictions = predictor.predict_next_word(corrected_text)

        if predictions:
            print(f"Next-word predictions: {predictions}")
        else:
            print("No next-word predictions available.")

        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()