from typing import List, Dict, Tuple
import re


class TransformerNER:
    """
    Named Entity Recognition using Hugging Face Transformers.
    Install: pip install transformers torch
    """
    
    def __init__(self, model_name: str = "dslim/bert-base-NER"):
        """
        Initialize with a transformer model.
        
        Popular models:
        - dslim/bert-base-NER: BERT fine-tuned on CoNLL-2003
        - dbmdz/bert-large-cased-finetuned-conll03-english: Large BERT
        - Jean-Baptiste/roberta-large-ner-english: RoBERTa-based
        """
        from transformers import pipeline
        self.ner_pipeline = pipeline("ner", model=model_name, aggregation_strategy="simple")
    
    def extract_entities(self, text: str) -> List[Dict]:
        """Extract named entities using transformer model."""
        results = self.ner_pipeline(text)
        
        entities = []
        for entity in results:
            entities.append({
                'text': entity['word'],
                'label': entity['entity_group'],
                'score': round(entity['score'], 4),
                'start': entity['start'],
                'end': entity['end']
            })
        
        return entities
    

# ============================================================================
# TESTING AND EXAMPLES
# ============================================================================
if __name__ == "__main__":
    
    print("="*80)
    print("NAMED ENTITY RECOGNITION (NER) - TESTING")
    print("="*80 + "\n")
    
    # Test text
    test_text = """
    Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 
    Cupertino, California on April 1, 1976. The company's CEO Tim Cook announced 
    new products at the event in San Francisco. You can contact them at 
    support@apple.com or call 1-800-275-2273. Visit https://www.apple.com for 
    more information. The stock price reached $150.25 yesterday.
    """
    
    print("Test Text:")
    print(test_text)
    print("\n" + "="*80 + "\n")
    

    
    # ========================================================================
    # TEST 1: Transformer NER
    # ========================================================================
    print("\n\n" + "="*80)
    try:
        print("TEST 2: Transformer-based NER (BERT)")
        print("-"*80)
        
        print("\nLoading model... (may take a moment)")
        transformer_ner = TransformerNER()
        print("Model loaded!\n")
        
        entities = transformer_ner.extract_entities(test_text)
        
        print(f"Found {len(entities)} entities:\n")
        for entity in entities:
            print(f"  {entity['text']:25} -> {entity['label']:10} (confidence: {entity['score']*100:.2f}%)")
        
    except Exception as e:
        print(f"Transformers not available: {e}")
    
