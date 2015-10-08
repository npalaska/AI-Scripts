import numpy as np

def main():
    dic={}
    w = open('shingles.txt', 'w', encoding='utf8') # write all the shingles
    f= open('homework.txt', encoding='utf8')
    for line in f:
            if(len(line)>1):
                k=3
                size= len(line)
                for i in range(size-k+1):
                    shingle=line[i:i+k]
                    w.write(shingle+"\n")
    f.close()
    w.close()
    unique = open('unique_shingle.txt', 'w', encoding='utf8')
    file = open('shingles.txt', 'r', encoding='utf8')
    file_contents = file.read()
    file.close()
    duplicate = []
    # counts = np.array([])
    counts = []
    word_list = file_contents.split()
    for word in word_list:
        if word not in duplicate:
            duplicate.append(word)
            # np.append(counts, [1])
            counts.append(1)
            unique.write(str(word) + "\n")
        """
        duplicatelength = len(duplicate)
        i = 0
        while i < duplicatelength:
            if duplicate[i] is word:
                counts[i] += 1
            i += 1
        """
        i = duplicate.index(word)
        counts[i] += 1

    unique.close()
    print(counts)


main()

def main1():
 dic={}
 f= open('homework.txt','r', encoding='utf8')
 for line in f:
  if(len(line)>1):
   k=2
   size= len(line)
   for i in range(size-k+1):
    shingle=line[i:i+k]
    if(shingle in dic):
      dic[shingle]=dic[shingle]+1
    else:
      dic[shingle]=1
 w = open('shingles1.txt', 'a', encoding='utf8') # we want to save the shingles in shingles.txt file
 for shingle in dic:
  print (shingle)
  w.write(shingle+"\n") # we are actually writing each shingle string into file shingles.txt
 len1 = len(dic)
 w.write("No of shingles "+str(len1))
 f.close
 w.close()

#main1()

