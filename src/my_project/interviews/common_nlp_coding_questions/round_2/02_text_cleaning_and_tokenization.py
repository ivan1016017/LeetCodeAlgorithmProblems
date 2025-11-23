from typing import List
from collections import Counter
import re

class TextCleanerTokenizer:

    def clean_and_tokenize_advanced(self, text: str, remove_numbers: bool = False) -> List[str]:
        """
        Advanced cleaning and tokenization with additional options.
        
        Args:
            text: Input text to clean and tokenize
            remove_numbers: If True, remove numeric tokens
            
        Returns:
            List of cleaned tokens
        """

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(pattern=r'[^\w\s]', repl='', string=text)

        # Remove extra whitespace
        text = re.sub(pattern=r'\s+', repl=' ', string=text).strip()

        # Tokenize
        tokens = text.split()

        # Optionally remove numbers
        if remove_numbers:
            tokens = [token for token in tokens if not token.isdigit()]

        return tokens
    
    
    def clean_with_regex_tokenize(self, text: str) -> List[str]:
        """
        Clean and tokenize using regex word boundaries.
        
        Args:
            text: Input text to clean and tokenize
            
        Returns:
            List of cleaned tokens
        """

        # Convert to lowercase
        text = text.lower()

        # Extract using regex

        token = re.findall(pattern=r'\b\w+\b', string=text)

        return token



# Example usage
if __name__ == "__main__":
    cleaner = TextCleanerTokenizer()
    
    text = """
    Hello, World! This is a TEST sentence with punctuation... 
    Numbers like 123 and symbols @#$ should be handled properly.
    Multiple    spaces   should be normalized.
    """

    solution = TextCleanerTokenizer()

    print(solution.clean_and_tokenize_advanced(text=text,
                                               remove_numbers=True))
    print(solution.clean_with_regex_tokenize(text=text))