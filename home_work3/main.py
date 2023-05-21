seq = None

promt = """
Choose an option:
1. Choose a new sequence
2. Check if the sequence is a reading frame
3. Print the reverse complement
4. Print the transcript
5. Check the frequencies of 2-mers
6. Stop
"""

dna_map = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}



def get_2_mers_frequencies(seq):
    posible_2_mers = {
        "AA": 0, 
        "AC": 0, 
        "AG": 0, 
        "AT": 0, 
        "CA": 0, 
        "CC": 0, 
        "CG": 0, 
        "CT": 0, 
        "GA": 0, 
        "GC": 0, 
        "GG": 0, 
        "GT": 0, 
        "TA": 0, 
        "TC": 0, 
        "TG": 0, 
        "TT": 0 
    }

    for i in range(len(seq) - 1):
        posible_2_mers[seq[i:i+2]] += 1
    
    return posible_2_mers


def print_formated_2_mers_frequencies(seq):
    frequencies = get_2_mers_frequencies(seq)
    for key in frequencies:
        print(f'{key}:  {frequencies[key]} ({frequencies[key]/(len(seq)-1)})')




def get_transcript(seq):
    """return the transcript string"""
    transcript = ""
    for char in seq:
        if char.upper() == "T":
            transcript += "U"
        else:
            transcript += char.upper()
    return transcript


def get_complement(seq):
    """return the complementary sequence string"""
    complement = ""
    for char in seq:
        complement += dna_map[char.upper()]
    return complement

def check_valid_seq(seq):
    for i in range(len(seq)):
        if seq[i].upper() not in "ATCG":
            return False
    return True

def check_reading_frame(seq):
    """return true if seq is valid"""
    valid_chars = "ATCG"
    
    for char in seq:
        if char not in valid_chars:
            return False

    if len(seq) % 3 != 0:
        return False

    valid_ending = ["TAG", "TAA", "TGA"]
    valid_start = "ATG"
    
    if seq[:3] != valid_start:
        return False
    
    if seq[-3:] not in valid_ending:    
        return False

    return True

def check_valid_choice(choice):
    if int(choice) > 6 or int(choice) < 1:
        return False
    return True

def get_dna_seq():
    while True:
        user_input = input("Enter a DNA sequence: ")
        if not check_valid_seq(user_input):
            print("Illegal sequence, try again")
            continue
        return user_input


# Main Loop
while True:
    seq = input("Enter a DNA sequence: ").upper()
    if not check_valid_seq(seq):
        print("Illegal sequence, try again")
        continue
    else:
        break

while True:
    print(promt)

    user_choice = input("Your choice: ")
    if not check_valid_choice(user_choice):
        print("Illegal choice") # return to promt
        continue    

    if user_choice == "0":
        print("The sequence is: ", seq)

    if user_choice == "1":
        seq = get_dna_seq().upper()

    if user_choice == "2":
        if check_reading_frame(seq):
            print("Valid reading frame")
        else:
            print("The sequence does not represent a reading frame")

    if user_choice == "3":
        print(get_complement(seq)[::-1])

    if user_choice == "4":
        print(get_transcript(seq))

    if user_choice == "5":
        print_formated_2_mers_frequencies(seq)

    if user_choice == "6":
        break

print("Goodbye!")
