import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, question, answer):
        self.cards.append(Flashcard(question, answer))

    def shuffle(self):
        random.shuffle(self.cards)

    def quiz(self):
        score = 0
        for card in self.cards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ")

            if user_answer.strip().lower() == card.answer.strip().lower():
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The answer is: {card.answer}\n")

        print(f"Quiz finished! Your score: {score}/{len(self.cards)}")

def main():
    deck = FlashcardDeck()
    print("Enter your flashcards (type 'done' to finish):")

    while True:
        q = input("Question: ")
        if q.lower() == 'done':
            break
        a = input("Answer: ")
        deck.add_card(q, a)

    deck.shuffle()
    deck.quiz()

if __name__ == "__main__":
    main()
