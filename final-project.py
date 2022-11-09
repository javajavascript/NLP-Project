import csv
import string

#convert csv to 2D array 
#each subarray is [sentiment, sentence]
array = []
with open("all-data.csv") as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    array.append(row)

#convert 2D array, tokenize each sentence
#each subarray is [sentiment, word1, word2, word3, etc]
list = []
for i in range(0, len(array)):
  for j in range(0, (len(array[i]))):
    if (j % 2 == 1): #[0] = sentiment, [1] = sentence
      array[i][j] = array[i][j].split(' ') #tokenize sentence
      array[i][j] = [array[i][j-1]] + array[i][j] #sentiment + tokenized sentence 
      list.append(array[i][j])

# print(list)    
# print()

#needed to remove decimals in the sentence
def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False

#create dictionary of key = word and value = sentiment value (0,1,-1)
dict = {}
for i in range(0, len(list)):
  sentiment = 0
  if (list[i][0] == 'positive'):
    sentiment = 1
  if (list[i][0] == 'negative'):
    sentiment = -1 
  for j in range(1, len(list[i])):
    key = list[i][j].lower() #convert words to lowercase to avoid duplicates
    if (key in string.punctuation): #skip punctuation
      continue
    if (key.isdigit() or key.isnumeric() or key.isdecimal() or isfloat(key)): #skip numbers
      continue    
    if key not in dict:
      dict[key] = sentiment
    else:
      dict[key] = dict.get(key) + sentiment 

# print(dict)

#test on first sentence from file
total = 0 #total sentiment of the sentence

#print result
print(total) 
if (total >= 1):
  print('positive')
if (total <= -1):
  print('negative') 
if (total == 0):
  print('neutral')   
