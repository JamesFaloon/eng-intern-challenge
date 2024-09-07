import sys 

class Translater:


    # Initialize dictionary for English and Braille 
    def __init__(self):


         # English to Braille 
        self.braille = {  
            "a": "O.....", 
            "b": "O.O...", 
            "c": "OO....", 
            "d" : "OO.O..", 
            "e": "O..O..", 
            "f": "OOO...", 
            "g": "OOOO..", 
            "h" : "O.OO..", 
            "i": ".OO...", 
            "j": ".OOO..", 
            "k": "O...O.", 
            "l" : "O.O.O.", 
            "m" : "OO..O.", 
            "n": "OO.OO.", 
            "o": "O..OO.", 
            "p": "OOO.O.", 
            "q" : "OOOOO.", 
            "r": "O.OOO.", 
            "s": ".OO.O.", 
            "t": ".OOOO.", 
            "u" : "O...OO", 
            "v" : "O.O.OO", 
            "w" : ".OOO.O", 
            "x" : "OO..OO", 
            "y" : "OO.OOO", 
            "z" : "O..OOO", 
            ' ' : "......" 
        } 


        # Braille to English 
        self.English = {} 
        for k,v in self.braille.items(): 
            self.English.update({v: k}) 
    

    # Function to deterimne if sentence is in Braile or in English 
    def checkLanguage(self, sentence):
        if (self.English.get(sentence[0:6]) == None and (sentence[0:6] != ".O.OOO" and sentence[0:6] != ".....O") ): 
            return "English"
        else:
            return "Braille"
    


    # Translate English letters to Braile strings
    def toBraille(self, sentence):
        output = ""
        digitTracker = False
        for i in range (len(sentence)):
            if (self.braille.get(sentence[i]) == None and not(sentence[i].isdigit()) and not (sentence[i].isupper())):
                return "Invalid Output"
            elif (sentence[i] == ' '):
                digitTracker = False
                output += self.braille.get(' ')
            elif (digitTracker and sentence[i] == '0'):
                output += self.braille.get('j')
            elif (digitTracker):
                output += self.braille.get(chr(96 + int(sentence[i])))
            elif (sentence[i] == '0'):
                output+=".O.OOO" 
                output+=self.braille.get("j")
                digitTracker = True
            elif (sentence[i].isdigit()):
                output+=".O.OOO" 
                output+= self.braille.get(chr(96 + int(sentence[i])))
                digitTracker = True
            elif (sentence[i].isupper()): 
                output+= ".....O" 
                output+= self.braille.get(sentence[i].lower()) 
            else : 
                output += self.braille.get(sentence[i]) 
        

        return output


    # Translate Braille strings to English letters 
    def toEnglish(self, sentence):
        output = ""
        number = False 
        uppercase = False 
        for j in range (0, len(sentence), 6): 
            toLetter = sentence[j: j+6] 
            if (self.English.get(toLetter) == None and toLetter != ".O.OOO" and toLetter != ".....O"):
                return "Invalid Output"
            elif toLetter == ".....O": 
                uppercase = True 
                continue 
            elif toLetter == ".O.OOO": 
                number = True 
                continue 
            elif (number and toLetter == ".OOO.."): 
                output+= "0"
            elif (number): 
                output+= str((ord(self.English.get(toLetter))) - ord('a') + 1)
            elif (uppercase): 
                uppercase = False 
                output+= self.English.get(toLetter).upper() 
            else : 
                output += self.English.get(toLetter) 

        return output 






# Main function to take command line inputs and translation sentences 
def main():
    translate = Translater()
    sentence = " ".join(sys.argv[1:])
    
    
    if (translate.checkLanguage(sentence) == "Braille"):
        print(translate.toEnglish(sentence))
    else :
        print(translate.toBraille(sentence))
    
    

    


main()
 

 

 

 

 

 
