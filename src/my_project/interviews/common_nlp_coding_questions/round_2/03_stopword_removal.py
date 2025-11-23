from typing import List, Set
import re

class StopwordRemoval:
    
    # Common English stopwords
    STOPWORDS = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
        'to', 'was', 'will', 'with', 'the', 'this', 'but', 'they', 'have',
        'had', 'what', 'when', 'where', 'who', 'which', 'why', 'how'
    }
    
    def __init__(self, custom_stopwords: Set[str] = None):
        """
        Initialize with optional custom stopwords.
        
        Args:
            custom_stopwords: Optional set of additional stopwords
        """
        self.stopwords = self.STOPWORDS.copy()
        if custom_stopwords:
            self.stopwords.update(custom_stopwords)


    def remove_stopwords(self, text: str) -> str:
        """
        Remove stopwords from text and return cleaned string.
        
        Args:
            text: Input text
            
        Returns:
            Text with stopwords removed
        """

        # Convert to lowercase and tokenize
        words = re.findall(r'\b\w+\b', text.lower())

        # Filtered out stopwords
        filtered_words = [word for word in words if word not in self.stopwords]

        return ' '.join(filtered_words)


    

# Example usage
if __name__ == "__main__":
    remover = StopwordRemoval()
    
    text = """
    The quick brown fox jumps over the lazy dog. 
    This is a sample sentence with many common stopwords that 
    will be removed from the text.
    """

    print(remover.remove_stopwords(text=text))    