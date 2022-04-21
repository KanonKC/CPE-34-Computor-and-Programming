dna = input("DNA: ")

# TRANSCRIPT
rna = ""
for i in range(len(dna)):
    script = ''
    if dna[i] == 'A':
        script = 'U'
    if dna[i] == 'C':
        script = 'G'
    if dna[i] == 'G':
        script = 'C'
    if dna[i] == 'T':
        script = 'A'
    rna = rna + script

#print(rna)
# TRANSLATION
# Start Codon
codon = ""
for i in range(len(rna)):
    if rna[i:i+3] == "AUG":
        codon = rna[i:]
        break
#print(codon)

slate = ""
for i in range(0,len(codon),3):
    if codon[i:i+3] in ["UAA","UGA","UAG"]:
        slate = slate + codon[:i]
        break
#print(slate)
amino = len(slate) // 3

print(f"{amino} Amino acid(s)")