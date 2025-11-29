from typing import Dict, Literal, List
import re

# ============================================================================
# METHOD 1: Using Transformers (BERT, RoBERTa, DistilBERT)
# ============================================================================
class TransformerSentimentAnalyzer:
    """
    Sentiment analysis using pre-trained transformer models.
    Install: pip install transformers torch
    """
    
    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initialize with a pre-trained model.
        
        Popular models:
        - distilbert-base-uncased-finetuned-sst-2-english (fast, lightweight)
        - cardiffnlp/twitter-roberta-base-sentiment (social media)
        - nlptown/bert-base-multilingual-uncased-sentiment (multilingual)
        """
        from transformers import pipeline
        self.classifier = pipeline('sentiment-analysis', model=model_name)

    
    def analyze(self, text: str) -> Dict:
        """Analyze sentiment using transformer model."""
        result = self.classifier(text)[0]
        return {
            'sentiment': result['label'].lower(),
            'confidence': round(result['score'], 4)
        }

    
    def batch_analyze(self, texts: List[str]) -> List[Dict]:
        """Analyze multiple texts efficiently."""
        results = self.classifier(text)

        return [
            {
                'sentiment':r['label'].lower(),
                'confidence': round(r['score'], 4)
            }
            for r in results
        ]



# ============================================================================
# TESTING AND EXAMPLES
# ============================================================================
if __name__ == "__main__":
    
    print("="*80)
    print("TRANSFORMER SENTIMENT ANALYSIS - TESTING")
    print("="*80 + "\n")
    
    # Initialize the analyzer
    print("Loading model... (this may take a moment on first run)")
    analyzer = TransformerSentimentAnalyzer()
    print("Model loaded successfully!\n")
    
    # ========================================================================
    # TEST 1: Single Text Analysis
    # ========================================================================
    print("TEST 1: Single Text Analysis")
    print("-"*80)
    
    single_text = "This movie is absolutely amazing! I loved every minute of it."
    result = analyzer.analyze(single_text)
    
    print(f"Text: {single_text}")
    print(f"Sentiment: {result['sentiment'].upper()}")
    print(f"Confidence: {result['confidence']*100:.2f}%\n")
    
    # ========================================================================
    # TEST 2: Multiple Different Sentiments
    # ========================================================================
    print("\nTEST 2: Multiple Different Sentiments")
    print("-"*80)
    
    test_cases = [
        "I absolutely love this product! It's the best thing ever!",
        "This is terrible. Worst experience of my life.",
        "It's okay, nothing special but not bad either.",
        "The customer service was outstanding and very helpful.",
        "I'm so disappointed and frustrated with this purchase.",
    ]
    
    for i, text in enumerate(test_cases, 1):
        result = analyzer.analyze(text)
        print(f"\n{i}. Text: {text}")
        print(f"   Sentiment: {result['sentiment'].upper()}")
        print(f"   Confidence: {result['confidence']*100:.2f}%")
    
    # ========================================================================
    # TEST 3: Batch Analysis (More Efficient)
    # ========================================================================
    print("\n\nTEST 3: Batch Analysis")
    print("-"*80)
    
    batch_texts = [
        "Great service!",
        "Horrible experience.",
        "Not impressed at all.",
        "Fantastic product, highly recommend!",
        "Could be better, but acceptable."
    ]
    
    batch_results = analyzer.batch_analyze(batch_texts)
    
    for text, result in zip(batch_texts, batch_results):
        print(f"\nText: {text}")
        print(f"Sentiment: {result['sentiment'].upper()} ({result['confidence']*100:.2f}%)")
    
    # ========================================================================
    # TEST 4: Edge Cases
    # ========================================================================
    print("\n\nTEST 4: Edge Cases")
    print("-"*80)
    
    edge_cases = [
        "😊❤️",  # Emojis
        "Not bad at all!",  # Negation
        "I don't hate it.",  # Double negation
        "",  # Empty (will handle gracefully)
        "Meh.",  # Ambiguous
    ]
    
    for text in edge_cases:
        if text:  # Skip empty strings
            result = analyzer.analyze(text)
            print(f"\nText: '{text}'")
            print(f"Sentiment: {result['sentiment'].upper()}")
            print(f"Confidence: {result['confidence']*100:.2f}%")
    
    # ========================================================================
    # TEST 5: Summary Statistics
    # ========================================================================
    print("\n\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)
    
    all_texts = test_cases + batch_texts
    all_results = analyzer.batch_analyze(all_texts)
    
    positive_count = sum(1 for r in all_results if r['sentiment'] == 'positive')
    negative_count = sum(1 for r in all_results if r['sentiment'] == 'negative')
    avg_confidence = sum(r['confidence'] for r in all_results) / len(all_results)
    
    print(f"\nTotal texts analyzed: {len(all_texts)}")
    print(f"Positive sentiments: {positive_count}")
    print(f"Negative sentiments: {negative_count}")
    print(f"Average confidence: {avg_confidence*100:.2f}%")
    
    print("\n" + "="*80)
    print("Testing completed!")
    print("="*80)