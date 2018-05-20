from string import ascii_lowercase, ascii_uppercase 
import re

def moving_shift(s, shift):
    shifted=[]
    output=[]
    for n in s:
        if n in ascii_lowercase:
            shifted += ascii_lowercase[(ascii_lowercase.index(n)+shift)%len(ascii_lowercase)]
        elif n in ascii_uppercase:
            shifted += ascii_uppercase[(ascii_uppercase.index(n)+shift)%len(ascii_uppercase)]
        else:
            shifted += n
        shift+=1
    shifted = ''.join(shifted).split()
    fivewords=len(shifted)//5
    modfivewords=len(shifted)%5
    fourwords=len(shifted)//4
    modfourwords=len(shifted)%4
    threewords=len(shifted)//3
    modthreewords=len(shifted)%3
    if modfivewords == 0:
        for n in range(5):
            output.append(' '.join(shifted[:3]))
            del shifted[:3]
    elif fourwords<
    for n in range(5):
        words=5
        for n in range(5):
            if len(shifted)%n==0:

        if length <= words:
            for n in range(words):
                output.append(' '.join(shifted[:length]))
                del shifted[0:length]
            break
        else:
            words-=1
    print(output)
    
            
moving_shift("I should have known that you would have a perfect answer for me!!!", 1)
# ['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ', 'gwkzzyq zntyhv', ' lvz wp!!!']
