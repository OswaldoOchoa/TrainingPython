def find_uniq(arr):
    if ''.join(sorted(set(arr[0].lower()))) == ''.join(sorted(set(arr[1].lower()))):
      s=0
      for s in range(len(arr)):
         if ''.join(sorted(set(arr[s].lower()))) != ''.join(sorted(set(arr[s+1].lower()))):
            return arr[s+1]
    else:
      return arr[1] if ''.join(set(arr[0].lower())) == ''.join(set(arr[2].lower())) else arr[0]

    
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
find_uniq([ '    ', 'a', '  ' ])