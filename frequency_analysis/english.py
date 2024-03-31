characters = [0]*256

# Frequencies of letters based on the english language
characters[32] = .15 #space character
characters[97] = .082 #'a' character
characters[98] = .015 #'b' character
characters[99] = .028 #'c' character
characters[100] = .042 #'d' character
characters[101] = .127 #'e' character
characters[102] = .022 #'f' character
characters[103] = .020 #'g' character
characters[104] = .061 #'h' character
characters[105] = .070 #'i' character
characters[106] = .001 #'j' character
characters[107] = .008 #'k' character
characters[108] = .04 #'l' character
characters[109] = .024 #'m' character
characters[110] = .067 #'n' character
characters[111] = .075 #'o' character
characters[112] = .019 #'p' character
characters[113] = .001 #'q' character
characters[114] = .060 #'r' character
characters[115] = .063 #'s' character
characters[116] = .09 #'t' character
characters[117] = .028 #'u' character
characters[118] = .01 #'v' character
characters[119] = .024 #'w' character
characters[120] = .02 #'x' character
characters[121] = .001 #'y' character
characters[122] = .001 #'z' character

def compute_occurrences(m):
    number_of_occurrences = [0] * 256
    for letter in m:
        number_of_occurrences[ord(letter)] += 1
    return number_of_occurrences
