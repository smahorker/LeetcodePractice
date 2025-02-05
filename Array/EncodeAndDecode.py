"""
If we just use a delimiter between strings, then the delimiter could show up in the
string, so it would split in between the words, special chars can show up

Cant use an array that stores the len of lists, since then you use up extra space

We cant use just a counter, since there could be integers in the string, so then
it would read that and fail

Need to use an integer + delimiter + word format, so that we can split the len of string
and the actual word apart, and read everything past the delimiter until we reach the
integer val of indicies

Encode

1. Create a string to store the result in

2. Loop through each string

3. Add the length of the string(convert from int to str to concatenate) + delimiter + str into result string

4. return result

Decode

1. Create a list to store the result, list since we need to turn it back into a list

2. Create a pointer variable which tracks our position in the string

3. Go until we reach len of the res str, which is just 1 long string of all the words

4. Create another pointer, j, which serves the purpose of pointing to fetching the length and pointing to the
end of a string

5. Loop through until str[j] != '#', increment j by 1 until then, this gives us the len of the string between [i:j]
since we start at index 0, so j will be one ahead

6. Get the length which is between str[i:j], ex. 22#, j increments twice so j = 2, and now we are looking between [0:2], which is just [0]+[1] = '22'

7. j is on the delimiter index now, so we set i = j + 1, which moves it to the index at the start of the list

8. j = i + length, pushes j one index past the word we are decoding, but allows for [i:j] to work, this also makes it so
that when we want to exit our loop after decoding every string, j = len(str) + 1, which exits the string at the end

9. Append the string from [i:j] which goes from the start of the string up til its last index, since j is 1 num ahead

10. Set i = j, since its at the first index of the next string, which is the first digit of the integer length of
the next number

11. Loop repeats, and j still fetches the length due to it being a nested while loop, states of variables dont reset due
to them being our metric of how far we are in the encoded string
"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # stores the new encoded strings
        for s in strs: # go through string by string
            res +=  str(len(s)) + "#" + s # adds len + delimiter to start of string
        return res # return encoded strings


    def decode(self, s: str) -> List[str]:
        res = [] # stores decoded strings
        i = 0 # reference point for each string

        while i < len(str): # goes until end of string
            j = i # temp var to account for int + delimiter at start
            while str[j] != '#': # starting variable is always an integer so it always executes
                j += 1 # this also accounts for strings that are >10 chars, so you need to keep this to get to next char
            length = int(str[i:j]) # goes up til the delimiter, which is the starting integer
            i = j + 1 # moves i to the actual start of string, since we are delimiter now
            j = i + length # j moves to the end of the string, its at the integer atp
            res.append(s[i:j]) # extracts the string and adds it to list, this works since :j goes one index behind, so it will be at last letter
            i = j # moves i to the integer