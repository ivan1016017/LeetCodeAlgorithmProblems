from typing import List



class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        Length-prefix each string as "<len>#<string>". The delimiter '#'
        is unambiguous because we always know the exact number of chars
        to read from the length that precedes it, so any character
        (including '#') may appear inside a string.
        """
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        n = len(s)
        while i < n:
            # Read the length up to the '#' delimiter.
            j = s.index("#", i)
            length = int(s[i:j])
            # The string is the next `length` chars after the '#'.
            start = j + 1
            strs.append(s[start:start + length])
            i = start + length
        return strs