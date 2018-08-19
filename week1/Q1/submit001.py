# python3
import sys


class Suffix_Array:
    def __init__( self, text ):
        self.order = self.buildSuffixArray(text)

    def in_put( self ):
        self.text = sys.stdin.readline().strip()

    def Classes_of_Char( self, S, order ):
        l = len(S)
        charClass = [0] * l
        charClass[order[0]] = 0
        for i in range(1, l):
            if S[order[i]] != S[order[i - 1]]:
                charClass[order[i]] = charClass[order[i - 1]] + 1
            else:
                charClass[order[i]] = charClass[order[i - 1]]
        return charClass

    def sorting( self, S ):
        l = len(S)
        order = [0] * l
        count = dict()
        for i in range(l):
            count[S[i]] = count.get(S[i], 0) + 1
        charList = sorted(count.keys())
        prevChar = charList[0]
        for char in charList[1:]:
            count[char] += count[prevChar]
            prevChar = char
        for i in range(l - 1, -1, -1):
            c = S[i]
            count[c] = count[c] - 1
            order[count[c]] = i
        return order

    def Doubled_sort( self, S, L, order, _class ):
        length_of_string = len(S)
        count = [0] * length_of_string
        newOrder = [0] * length_of_string
        for i in range(length_of_string):
            count[_class[i]] += 1
        for j in range(1, length_of_string):
            count[j] += count[j - 1]
        for i in range(length_of_string - 1, -1, -1):
            start = (order[i] - L + length_of_string) % length_of_string
            cl = _class[start]
            count[cl] -= 1
            newOrder[count[cl]] = start
        return newOrder

    def update_Classes( self, newOrder, _class, L ):
        n = len(newOrder)
        new_Class = [0] * n
        new_Class[newOrder[0]] = 0
        for i in range(1, n):
            curr = newOrder[i]
            prev = newOrder[i - 1]
            mid = curr + L
            midPrev = (prev + L) % n
            if _class[curr] != _class[prev] or _class[mid] != _class[midPrev]:
                new_Class[curr] = new_Class[prev] + 1
            else:
                new_Class[curr] = new_Class[prev]
        return new_Class

    def buildSuffixArray( self, S ):
        length_of_string = len(S)
        order = self.sorting(S)
        _class = self.Classes_of_Char(S, order)
        L = 1
        while L < length_of_string:
            order = self.Doubled_sort(S, L, order, _class)
            _class = self.update_Classes(order, _class, L)
            L = 2 * L
        return order


class Assembling_challenge001:
    def __init__( self ):
        reads = self.readData()
        genome = self.assembly(reads)
        print(genome)

    def readData( self ):
        return list(set(sys.stdin.read().strip().split()))

    def bwtFromSuffixArray( self, text, order, alphabet=['$', 'A', 'C', 'G', 'T'] ):
        l = len(text)
        bwt = [''] * l
        for i in range(l):
            bwt[i] = text[(order[i] + l - 1) % l]

        counts = dict()
        starts = dict()
        for char in alphabet:
            counts[char] = [0] * (l + 1)
        for i in range(l):
            cuurent_Char = bwt[i]
            for char, count in counts.items():
                counts[char][i + 1] = counts[char][i]
            counts[cuurent_Char][i + 1] += 1
        current_index = 0
        for char in sorted(alphabet):
            starts[char] = current_index
            current_index += counts[char][l]
        return bwt, starts, counts

    def findLongestOverlap( self, text, patterns, k=12 ):
        order = Suffix_Array(text).order
        bwt, starts, counts = self.bwtFromSuffixArray(text, order)
        l = len(text) - 1

        occs = dict()
        for i, pattern_list in enumerate(patterns):
            pattern = pattern_list[:k]
            top = 0
            bottom = len(bwt) - 1
            current_Index = len(pattern) - 1
            while top <= bottom:
                if current_Index >= 0:
                    symbol = pattern[current_Index]
                    current_Index -= 1
                    if counts[symbol][bottom + 1] - counts[symbol][top] > 0:
                        top = starts[symbol] + counts[symbol][top]
                        bottom = starts[symbol] + counts[symbol][bottom + 1] - 1
                    else:
                        break
                else:
                    for j in range(top, bottom + 1):
                        if not order[j] in occs:
                            occs[order[j]] = []
                        occs[order[j]].append(i)
                    break
        overlap = 0
        for pos, iList in sorted(occs.items()):
            for i in iList:
                if text[pos:-1] == patterns[i][:l - pos]:
                    return i, l - pos
        return i, overlap

    def assembly( self, reads ):
        current_Index = 0
        genome = reads[0]
        firstRead = reads[current_Index]
        while True:
            current_Read = reads[current_Index]
            if 1 == len(reads):
                break
            del reads[current_Index]
            current_Index, overlap = self.findLongestOverlap(current_Read + '$', reads)
            genome += reads[current_Index][overlap:]
        current_Index, overlap = self.findLongestOverlap(reads[0] + '$', [firstRead])
        if overlap > 0:
            return genome[:-overlap]
        else:
            return genome


if __name__ == '__main__':
    Assembling_challenge001()