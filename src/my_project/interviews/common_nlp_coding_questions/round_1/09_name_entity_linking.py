from transformers import pipeline
from typing import List, Dict


class SimpleEntityLinker:
    """Simple Entity Linking using Hugging Face NER."""
    
    def __init__(self, model_name: str = "dslim/bert-base-NER"):
        """
        Initialize with Hugging Face NER model.
        
        Args:
            model_name: Pre-trained NER model from Hugging Face
        """
        print("Loading model...")
        self.ner = pipeline("ner", model=model_name, aggregation_strategy="simple")
        print("Model loaded!\n")
    
    def extract_entities(self, text: str) -> List[Dict]:
        """
        Extract named entities from text.
        
        Args:
            text: Input text
            
        Returns:
            List of entities with their information
        """
        results = self.ner(text)
        
        entities = []
        for entity in results:
            entities.append({
                "text": entity["word"],
                "type": entity["entity_group"],
                "score": entity["score"],
                "start": entity["start"],
                "end": entity["end"]
            })
        
        return entities
    
    def print_results(self, text: str, entities: List[Dict]):
        """Print results in a readable format."""
        print(f"Text: {text}")
        print("\n" + "="*80)
        print("Extracted Entities:")
        print("="*80)
        
        if not entities:
            print("No entities found.")
            return
        
        for ent in entities:
            print(f"\n✓ Entity: '{ent['text']}'")
            print(f"  Type: {ent['type']}")
            print(f"  Confidence: {ent['score']:.2%}")
            print(f"  Position: [{ent['start']}:{ent['end']}]")


# Example usage
if __name__ == "__main__":
    # Initialize entity linker
    linker = SimpleEntityLinker()
    
    # Test sentences
    texts = [
        "Apple announced new products in 2023.",
        "Steve Jobs founded Apple Inc. in 1976.",
        "Microsoft was founded by Bill Gates in Seattle.",
        "Barack Obama was the 44th President of the United States.",
        "Google acquired YouTube for $1.65 billion in 2006."
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n{'='*80}")
        print(f"Example {i}")
        print(f"{'='*80}\n")
        
        entities = linker.extract_entities(text)
        linker.print_results(text, entities)