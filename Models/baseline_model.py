import pandas as pd
import re
from sklearn.metrics import classification_report, accuracy_score, f1_score

class KeywordFilter:
    """
    WHY: This simulates existing parental control tools that use simple word matching.
    It will help us prove that ML is better than current solutions.
    """
    def __init__(self):
        # These are words/phrases that might indicate grooming behavior
        self.keywords = [
            'old are you', 'grade are you', 'where do you live', 'phone number',
            'snapchat', 'parents home', 'what are you wearing', 'real name',
            'our secret', 'don\'t tell', 'trust me', 'special connection',
            'send me a picture', 'meet me', 'your address', 'how old', 
            'where you from', 'text me', 'call me'
        ]
    
    def predict(self, text):
        """
        HOW: Check if any dangerous keywords appear in the message
        Returns 1 (grooming) if found, 0 (normal) if not found
        """
        text_lower = text.lower()
        for keyword in self.keywords:
            if keyword in text_lower:
                return 1  # Flag as grooming
        return 0  # Flag as normal

def evaluate_baseline():
    """
    TEST: See how well our keyword filter performs on the dataset we created
    """
    print("🔍 TESTING KEYWORD FILTER (Baseline Model)")
    print("=" * 50)
    
    # Load the data we created
    df = pd.read_csv('data/synthetic_chats.csv')
    print(f"📊 Testing on {len(df)} chat samples...")
    
    # Initialize our keyword filter
    keyword_filter = KeywordFilter()
    
    # Test every message in our dataset
    predictions = []
    for text in df['text']:
        prediction = keyword_filter.predict(text)
        predictions.append(prediction)
    
    # Calculate how accurate our filter is
    accuracy = accuracy_score(df['label'], predictions)
    f1 = f1_score(df['label'], predictions)
    
    print(f"✅ Baseline Model Results:")
    print(f"   Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"   F1-Score: {f1:.4f}")
    print("\n📋 Detailed Performance Breakdown:")
    print(classification_report(df['label'], predictions, target_names=['Normal', 'Grooming']))
    
    # Show some examples of what the filter caught
    print("\n🔎 EXAMPLE PREDICTIONS:")
    print("-" * 30)
    test_messages = [
        "how old are you?",
        "gg everyone that was fun", 
        "don't tell your parents we're talking",
        "let's play again tomorrow"
    ]
    
    for msg in test_messages:
        result = keyword_filter.predict(msg)
        status = "🚨 GROOMING" if result == 1 else "✅ NORMAL"
        print(f"'{msg}' → {status}")
    
    return accuracy, f1

# This runs when we execute the file
if __name__ == "__main__":
    evaluate_baseline()