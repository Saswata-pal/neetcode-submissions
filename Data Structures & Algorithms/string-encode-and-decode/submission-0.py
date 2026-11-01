class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            # Prepend length of string and a '#' delimiter
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the position of '#' starting from index i
            delimiter_pos = s.find("#", i)
            
            # Parse the length of the next string
            length = int(s[i:delimiter_pos])
            
            # Extract the string based on length
            start = delimiter_pos + 1
            end = start + length
            decoded.append(s[start:end])
            
            # Move index past the extracted string
            i = end
            
        return decoded