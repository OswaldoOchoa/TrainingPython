def sort_by_name(arr):
   numbersname = []
   output = []
   sum = 0

   num2word = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', \
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', \
                13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', \
                17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', \
                30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', \
                80: 'eighty', 90: 'ninety', 100: 'hundred'}
   word2num = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, \
                'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, \
                'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, \
                'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, \
                'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, \
                'eighty': 80, 'ninety': 90, 'hundred': 100 }
                
   teenslist = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
                
                
   for numb in arr:
      if numb >= 100:
         hundreds = numb//100
         teens = numb - (hundreds*100)
         tents = (numb - hundreds*100)//10
         units = (numb - hundreds*100)%10
         if tents == 0 and units == 0:
            numbersname.append(num2word[hundreds] + ' ' + num2word[100])
         elif tents == 1:
            numbersname.append(num2word[hundreds] + ' ' + num2word[100] + ' ' + num2word[teens])
         elif tents == 0 and units != 0:
            numbersname.append(num2word[hundreds] + ' ' + num2word[100] + ' ' + num2word[units])
         elif tents > 1 and units == 0:
            numbersname.append(num2word[hundreds] + ' ' + num2word[100] + ' ' + num2word[tents*10])
         elif tents > 1 and units != 0:
            numbersname.append(num2word[hundreds] + ' ' + num2word[100] + ' ' + num2word[tents*10] + ' ' + num2word[units])
      elif 19 < numb < 100:
         tents = numb//10
         units = numb%10
         if units != 0:
            numbersname.append(num2word[tents*10] + ' ' + num2word[units])
         else:
            numbersname.append(num2word[tents*10])
      elif 0 <= numb <= 19:
         numbersname.append(num2word[numb])
   numbersname.sort()
   print(numbersname)
   for i in numbersname:
      if i in word2num.keys():
         output.append(word2num[i])
      else:
         decoding = i.split(' ')
         if 'hundred' in decoding:
            decoding.remove('hundred')
            iter1 = 0
            for iter1 in range(len(decoding)):
               if iter1 == 0 and iter1 != len(decoding)-1:
                  sum += word2num[decoding[0]] * 100
               elif iter1 == 0 and iter1 == len(decoding)-1:
                  sum += word2num[decoding[0]] * 100
                  break
               elif decoding[iter1] in teenslist:
                  sum += word2num[decoding.pop()]
                  break
               elif iter1 == len(decoding)-1:
                  sum += word2num[decoding.pop()]
                  break
               else:
                  sum += word2num[decoding.pop()]
                  sum += word2num[decoding.pop()]
                  break
               iter1 += 1
            output.append(sum)
            sum = 0
         else:
            iter3 = 0
            for iter3 in range(len(decoding)):
               if iter3 == 2:
                  sum += word2num[decoding.pop()] * 100
               else:
                  sum += word2num[decoding.pop()]
               iter3 += 1
            output.append(sum)
            sum = 0
   print(output)
         
         
         
sort_by_name([99, 100, 200, 300, 999])
#[999, 99, 100, 300, 200]
#sort_by_name([8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 20, 0])
#[11, 507, 417, 9, 99, 999, 200, 210, 0]
#[8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 20, 2, 0]