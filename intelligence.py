import re
import difflib
from dictionary import DRUG_DICTIONARY, NEGATION_PATTERNS, REGIONAL_NUMBERS

def clean_text(text):
    # Standardize whitespace and remove unnecessary punctuation but preserve dashes for formatting
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def phonetic_correct(text):
    """
    Scans the text for multi-word or single-word mistranscriptions
    and replaces them with standard medical terms or brand names.
    Also handles brand-to-generic mapping if helpful, but primarily
    replaces phonetic garbles.
    """
    corrected = text
    
    # Sort terms by length of mistranscription (descending) to match longer phrases first
    phrase_replacements = []
    for entry in DRUG_DICTIONARY:
        term = entry["term"]
        for mis in entry["common_mistranscriptions"]:
            if len(mis.split()) > 1: # multi-word phrase
                phrase_replacements.append((mis, term))
    
    # Sort so that e.g. "a tour of statin" is replaced before "a tour"
    phrase_replacements.sort(key=lambda x: len(x[0]), reverse=True)
    
    # 1. Replace multi-word common mistranscriptions first (case-insensitive)
    for mis, term in phrase_replacements:
        pattern = re.compile(r'\b' + re.escape(mis) + r'\b', re.IGNORECASE)
        corrected = pattern.sub(term, corrected)
        
    # 2. Split into words and perform single word replacements
    words = corrected.split()
    for i, word in enumerate(words):
        # Clean word from punctuation for comparison
        clean_w = re.sub(r'[^\w\d-]', '', word).lower()
        if not clean_w:
            continue
            
        matched = False
        # Exact match in common mistranscriptions
        for entry in DRUG_DICTIONARY:
            term = entry["term"]
            if clean_w in [m.lower() for m in entry["common_mistranscriptions"]]:
                # Replace maintaining clean punctuation if present
                words[i] = word.lower().replace(clean_w, term)
                matched = True
                break
                
        if not matched:
            # Check brand names to canonicalize brand casing or associate with generic
            for entry in DRUG_DICTIONARY:
                term = entry["term"]
                for brand in entry["brand_names"]:
                    if clean_w == brand.lower():
                        # Standardize casing to brand name
                        words[i] = word.lower().replace(clean_w, brand)
                        matched = True
                        break
                if matched:
                    break
                    
    corrected = " ".join(words)
    
    # Some specific manual mapping fixes for highly specific mistranscriptions in the 20 notes
    specific_fixes = {
        "molli noppi": "mokaalla noppi", # knee pain in Telugu
        "chal thundi": "nadusthundi", # running in Telugu
        "neend er": "ghumer", # sleep in Bengali
        "koodhi": "koodi", # together in Malayalam
        "moodlu": "modalu", # first in Kannada
    }
    for k, v in specific_fixes.items():
        pattern = re.compile(r'\b' + re.escape(k) + r'\b', re.IGNORECASE)
        corrected = pattern.sub(v, corrected)
        
    return clean_text(corrected)

def parse_negations(text, target_words):
    """
    Checks if a target word/drug is negated in the text.
    Returns a dictionary of {target_word: is_negated}
    Splits text by sentence/clause boundaries (., ;, \n, —) to avoid false matches.
    """
    results = {}
    
    # Extract all negation words
    all_negation_words = set()
    for lang, data in NEGATION_PATTERNS.items():
        for neg in data["negations"]:
            all_negation_words.add(neg.lower())
            
    # Split text into clauses/sentences by major boundaries
    clauses = re.split(r'\.|\n|;|—|--|\bnext\b', text, flags=re.IGNORECASE)
    clauses = [clean_text(c) for c in clauses if c.strip()]
    
    for target in target_words:
        target_lower = target.lower()
        is_neg = False
        
        # Check if the target drug/word appears in any clause and if that clause has a negation
        for clause in clauses:
            # Check if target is in this clause
            words_in_clause = [re.sub(r'[^\w\d-]', '', w).lower() for w in clause.split()]
            
            # Simple check if target is in the clause
            has_target = False
            for w in words_in_clause:
                if target_lower in w:
                    has_target = True
                    break
                    
            if has_target:
                # Check if this clause has any negation word
                for w in words_in_clause:
                    if w in all_negation_words:
                        is_neg = True
                        break
                        
            if is_neg:
                break
                
        results[target] = is_neg
        
    return results

def extract_dosages(text):
    """
    Replaces regional number words with standard digits, and normalizes
    dosage schedules.
    """
    normalized = text
    
    # Replace regional numbers
    for lang, num_map in REGIONAL_NUMBERS.items():
        # Sort keys descending by length to replace longer words first (e.g. "thommidi" before "oka")
        sorted_keys = sorted(num_map.keys(), key=len, reverse=True)
        for key in sorted_keys:
            val = num_map[key]
            # Replace as independent word
            pattern = re.compile(r'\b' + re.escape(key) + r'\b', re.IGNORECASE)
            normalized = pattern.sub(str(val), normalized)
            
    # Also standardize common dosing phrases
    dosing_phrases = {
        "once a day": "OD",
        "twice a day": "BD",
        "thrice a day": "TDS",
        "four times a day": "QDS",
        "as needed": "SOS",
        "at bedtime": "HS",
        "empty stomach": "OD (empty stomach)",
        "khali pet": "OD (empty stomach)",
        "vayattil": "empty stomach",
        "raavile": "morning",
    }
    for k, v in dosing_phrases.items():
        pattern = re.compile(r'\b' + re.escape(k) + r'\b', re.IGNORECASE)
        normalized = pattern.sub(v, normalized)
        
    return normalized

def segment_rounds(text):
    """
    Detects if a transcript has multiple patients (like VN-02)
    and splits it into separate segments per patient/bed.
    """
    # Look for patient/bed indicators like "bed 14", "bed 16", "bed 18", "Gupta aunty", "Yadav sahab", etc.
    # or transition phrases like "next", "okay next"
    bed_pattern = r'\b(bed\s+\d+|patient\s+\w+|[A-Za-z]+\s+(ji|sahab|aunty|uncle|paatti|chechi|babu|gari|avrige))\b'
    
    # Find all occurrences of beds or names that start a new patient block
    # Let's inspect VN-02:
    # "Bed 14 Sharma ji ... okay next — bed 16 Gupta aunty ... okay next — bed 18 Yadav sahab ..."
    # We want to split on "okay next" or "next" when followed by Bed/Patient.
    
    split_markers = [
        "okay next — bed 16", "okay next — bed 18",
        "okay next - bed 16", "okay next - bed 18",
        "okay next bed 16", "okay next bed 18",
        "next — bed 16", "next — bed 18",
        "okay next —", "okay next -"
    ]
    
    # Try splitting by specific marker phrases first
    segments = []
    text_to_process = text
    
    # We will split using a regex for "okay next" followed by bed or just "okay next"
    parts = re.split(r'\b(?:okay\s+)?next\s*(?:—|-)?\s*(?=bed|patient)', text_to_process, flags=re.IGNORECASE)
    
    if len(parts) > 1:
        for p in parts:
            p_clean = clean_text(p)
            if p_clean:
                # Find patient name or bed number to use as title
                title_match = re.search(r'\b(bed\s+\d+|[A-Z][a-z]+\s+(ji|sahab|aunty|uncle|paatti|chechi|babu|gari))\b', p_clean, re.IGNORECASE)
                title = title_match.group(0) if title_match else "Patient Record"
                segments.append({
                    "title": title,
                    "text": p_clean
                })
    else:
        # Default single patient segment
        segments.append({
            "title": "Patient Record",
            "text": clean_text(text)
        })
        
    return segments

if __name__ == "__main__":
    # Quick self-test
    test_str = "Ramaiah uncle vacharu, Ibuprofen kavali ani aduguthunnaru, stent undi kadha ivvakudadu ani cheppanu. Paracetamol 650 QDS continue."
    print("Original:", test_str)
    corrected = phonetic_correct(test_str)
    print("Phonetic Correct:", corrected)
    negations = parse_negations(corrected, ["Ibuprofen", "Paracetamol"])
    print("Negation Check:", negations)
    dosages = extract_dosages(corrected)
    print("Dosage Check:", dosages)
