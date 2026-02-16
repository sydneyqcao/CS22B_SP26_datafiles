### CS 22B Module 01 - Homework 1
### Name: Sydney Cao

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters. 
## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file,  bad_reads.txt. 
## 4. Print as output, the number of valid and invalid reads. 

valid_reads = []
validc = 0
invalidc = 0

infile = open("adapter_reads.txt", "r")
good = open("clean_reads.txt", "w")
bad = open("bad_reads.txt", "w")

for line in infile:
  read line.strip()
  trimmed = read[14:]
  is_valid = True

  for ch in trimmed:
    if ch != "A" and ch != "T" and ch != "C" and ch != "G":
      if_valid = False

  if is_valid: 
    good.write(trimmed + "\n")
    valid_reads.append(trimmed)
    validc += 1
  else:
    bad.write(trimmed + "\n")
    invalidc += 1

infile.close()
good.close()
bad.close()

print("Valid reads:", validc)
print("Invalid reads:", invalidc)

##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read. 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length). 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

lengths = [len(r) for r in valid_reads]

gc_list = []
for r in valid_reads:
  gc = r.count("G") + r.count("C")
  gcper = gc / len(r)
  gc_list.append(gcp)

if len(lengths) > 0:
  print("Minimum: ", min(lengths))
  print("Maximum: ", max(lengths))
  print("Avg length: ", sum(lengths)/len(lengths))
  print("Avg GC%: ", round(sum(gc_list)/len(gc_list), 3))

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads. 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).

base_counts =  {"A":0, "T":0, "C":0, "G":0}

for read in valid_reads:
  for ch in read:
    base_counts[ch] = base_counts[ch] + 1

product = 1

for key in base_counts: 
  product = product * base_counts[key]

print("Base counts: ", base_counts)
print("Product A*C*T*G: ", product)
#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.
def nt_per(seq, nt):
  count = seq.count(nt)
  percent = (count / len(seq)) * 100
  return round(percent, 2)

sequence = TTATAAGCCGATTATAAGCCCGTAACCGGTTAG

assert nt_percent("AATT","A") == 50.00
assert nt_percent("AAAA","T") == 0.00
assert nt_percent(sequence,"G") >= 0

## Use this sequence as your test sequence

