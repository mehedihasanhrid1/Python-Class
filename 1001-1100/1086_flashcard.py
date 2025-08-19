import random
import json
import os

class Flashcard:
    def __init__(self, question, answer):
        self.question = question.strip()
        self.answer = answer.strip()

    def to_dict(self):
        return {"question": self.question, "answer": self.answer}

    @staticmethod
    def from_dict(data):
        return Flashcard(data["question"], data["answer"])


class FlashcardDeck:
    def __init__(self, filename="flashcards.json"):
        self.cards = []
        self.filename = filename
        self.load()

    def add_card(self, question, answer):
        self.cards.append(Flashcard(question, answer))
        self.save()

    def remove_card(self, index):
        if 0 <= index < len(self.cards):
            del self.cards[index]
            self.save()

    def edit_card(self, index, new_q=None, new_a=None):
        if 0 <= index < len(self.cards):
            if new_q:
                self.cards[index].question = new_q
            if new_a:
                self.cards[index].answer = new_a
            self.save()

    def shuffle(self):
        random.shuffle(self.cards)

    def quiz(self, reverse=False):
        score = 0
        wrong_cards = []
        for card in self.cards:
            q, a = (card.answer, card.question) if reverse else (card.question, card.answer)
            print(f"\nQuestion: {q}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == a.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {a}")
                wrong_cards.append(card)

        print(f"\nQuiz finished! Your score: {score}/{len(self.cards)}")

        if wrong_cards:
            print("\nYou missed the following cards:")
            for c in wrong_cards:
                print(f"- {c.question} → {c.answer}")

    def list_cards(self):
        if not self.cards:
            print("No flashcards available.")
        for idx, card in enumerate(self.cards, 1):
            print(f"{idx}. {card.question} → {card.answer}")

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.cards], f, indent=4)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.cards = [Flashcard.from_dict(d) for d in data]


def main():
    deck = FlashcardDeck()

    while True:
        print("\n===== Flashcard Menu =====")
        print("1. Add flashcard")
        print("2. View all flashcards")
        print("3. Edit flashcard")
        print("4. Delete flashcard")
        print("5. Quiz (normal mode)")
        print("6. Quiz (reverse mode)")
        print("7. Shuffle cards")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            q = input("Enter question: ")
            a = input("Enter answer: ")
            deck.add_card(q, a)
        elif choice == "2":
            deck.list_cards()
        elif choice == "3":
            deck.list_cards()
            idx = int(input("Enter card number to edit: ")) - 1
            new_q = input("New question (leave blank to keep): ")
            new_a = input("New answer (leave blank to keep): ")
            deck.edit_card(idx, new_q or None, new_a or None)
        elif choice == "4":
            deck.list_cards()
            idx = int(input("Enter card number to delete: ")) - 1
            deck.remove_card(idx)
        elif choice == "5":
            deck.shuffle()
            deck.quiz()
        elif choice == "6":
            deck.shuffle()
            deck.quiz(reverse=True)
        elif choice == "7":
            deck.shuffle()
            print("Deck shuffled!")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
