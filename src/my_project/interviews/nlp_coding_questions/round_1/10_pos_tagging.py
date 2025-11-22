from transformers import pipeline
from typing import List, Dict


class SimplePOSTagger:
    """Simple POS Tagging using Hugging Face."""
    
    def __init__(self, model_name: str = "vblagoje/bert-english-uncased-finetuned-pos"):
        """
        Initialize POS tagger with Hugging Face model.
        
        Args:
            model_name: Pre-trained POS tagging model
        """
        print("Loading POS tagging model...")
        self.pos_tagger = pipeline("token-classification", model=model_name, aggregation_strategy="simple")
        print("Model loaded!\n")
    
    def tag(self, text: str) -> List[Dict]:
        """
        Tag parts of speech in text.
        
        Args:
            text: Input text
            
        Returns:
            List of dictionaries with word and POS tag
        """
        results = self.pos_tagger(text)
        
        tagged_words = []
        for result in results:
            tagged_words.append({
                "word": result["word"],
                "pos": result["entity_group"],
                "score": result["score"]
            })
        
        return tagged_words
    
    def print_results(self, text: str, tagged_words: List[Dict]):
        """Print POS tagging results."""
        print(f"Sentence: {text}")
        print("\n" + "="*80)
        print("POS Tags:")
        print("="*80)
        
        for item in tagged_words:
            print(f"{item['word']:20} → {item['pos']:10} (confidence: {item['score']:.2%})")


# POS Tag Descriptions
POS_DESCRIPTIONS = {
    "NOUN": "Noun (person, place, thing)",
    "VERB": "Verb (action, state)",
    "ADJ": "Adjective (describes noun)",
    "ADV": "Adverb (describes verb/adjective)",
    "PRON": "Pronoun (replaces noun)",
    "DET": "Determiner (the, a, an)",
    "ADP": "Adposition/Preposition (in, on, at)",
    "NUM": "Number (1, 2, three)",
    "CONJ": "Conjunction (and, or, but)",
    "PRT": "Particle (up, off, out)",
    "PUNCT": "Punctuation (. , ! ?)",
    "X": "Other"
}


def explain_pos_tags():
    """Print explanation of POS tags."""
    print("\n" + "="*80)
    print("POS TAG REFERENCE")
    print("="*80)
    for tag, description in POS_DESCRIPTIONS.items():
        print(f"{tag:10} → {description}")


# Example usage
if __name__ == "__main__":
    # Initialize POS tagger
    tagger = SimplePOSTagger()
    
    # Test sentences
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "I love programming in Python.",
        "She is reading a book about artificial intelligence.",
        "They went to the store yesterday.",
        "Machine learning models can predict outcomes."
    ]
    
    # Tag each sentence
    for i, sentence in enumerate(sentences, 1):
        print(f"\n{'='*80}")
        print(f"Example {i}")
        print(f"{'='*80}\n")
        
        tagged = tagger.tag(sentence)
        tagger.print_results(sentence, tagged)
    
    # Print POS tag reference
    explain_pos_tags()