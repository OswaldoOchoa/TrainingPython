import re

# SIMPLE EXAMPLES

#print(re.split(r'\s*', 'Here are some words'))
#print(re.split(r'\s', 'Here are some words')) #I'm still don't get the difference.
#print(re.split(r'(\s*)', 'Here are some words'))
#print(re.split(r'(s*)', 'Here are some words'))
#print (re.split(r'[a-fA-F]', ';jpaiorjpaoitngAROBJTFl<e'))


# COMPLEX EXAMPLES

#print (re.findall(r'\d', 'ocinwe324 main st.asdvce'))
#print (re.findall(r'\d{1,5}', 'ocinwe324 main st.asdvce'))
#print (re.findall(r'\d{1,5}\s\w+\s\w+\.', 'ocinwe324 main st.asdvce'))


# PRACTICAL EXAMPLE

import re, urllib

try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn platzi'.split()
pat = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
        print('Searching: ' + s)
        try:
            u = urllib.urlopen('http://' + s + '.com')
        except Exception as ex:
            print("The site: " + s + " was not found. Error: " + str(ex))
            continue
        text = u.read()
        title = re.findall(pat, str(text))
        print(title[0])