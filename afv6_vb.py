# Naam: Ilse den Brok
# Datum: 20-11-2017
# Versie: 1.3

def main():
    try:
        bestand = "alpaca_test.txt"
        headers, seqs = lees_inhoud(bestand)
        #bestand inlezen en splitsen in headers en sequenties
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:",headers[i])
                check_is_dna = is_dna(seqs[i])
                #als het zoekwoord voorkomt in de header, print de header+sequentie
                if check_is_dna: 
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
                #controleer of het dna is
    except FileNotFoundError:
        print ("staat het bestand wel in de juiste map?")
        #error voor het geval dat het bestand niet bestaat
    except UnicodeDecodeError:
        print ("Is het bestand wel in fasta format?")
        #error voor het geval dat het geen .fasta bestand is
    except TypeError:
        print ("Is het wel een boolean?")
        #error voor het geval dat is_dna() een string ipv boolean krijgt
    except SyntaxError:
        print ("dit is niet de verwachte input")
        #error voor het geval dat knipt() niet de verwachte input krijgt
    
def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    #bestand inlezen, openen en in 2 lijsten verdelen
    seq = ""
    for line in bestand:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
            #alles dat begint met > is een header
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs
    #lijsten returnen

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    #controleer of het dna is
    if type(dna) == str:
        raise TypeError
    #als het type van dna een string is, gooi dan een TypeError op
    return dna

    
def knipt(alpaca_seq):
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^","")
        #vervang alle ^ met niks
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
        if bestand == str:
            raise SyntaxError
        #als het bestand een string is, gooi dan een SyntaxError op

main()
