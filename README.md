# Coursera-Genome-Assembly-Programming-Challenge
Assembled Phi-X174 genome using Overlap Graph, Kmer Composition and De-Bruijn Graph.

<img width="794" alt="default" src="https://user-images.githubusercontent.com/33269462/44305590-1b413b00-a349-11e8-8839-915bfda8b2af.png">


## phi X 174

The phi X 174 (or ΦX174) bacteriophage is a single-stranded DNA (ssDNA) virus and the first DNA-based genome to be sequenced. This work was completed by Fred Sanger and his team in 1977. In 1962, Walter Fiers and Robert Sinsheimer had already demonstrated the physical, covalently closed circularity of ΦX174 DNA. Nobel prize winner Arthur Kornberg used ΦX174 as a model to first prove that DNA synthesized in a test tube by purified enzymes could produce all the features of a natural virus, ushering in the age of synthetic biology. In 2003, it was reported by Craig Venter's group that the genome of ΦX174 was the first to be completely assembled in vitro from synthesized oligonucleotides. The ΦX174 virus particle has also been successfully assembled in vitro. Recently, it was shown how its highly overlapping genome can be fully decompressed and still remain functional.

<img width="259" alt="default" src="https://user-images.githubusercontent.com/33269462/44305606-65c2b780-a349-11e8-9ee5-ccb3e108aa3c.png">

## Problem Description:
#### Input: 
A collection of Strings called reads of the original genome. Each read is a sub-string of the original genome(Genome can be circular also).

#### Output:
A string S of minimum length that cantains all the strings(reads) given in the input as its sub-strings.


## Algorithms:
### 01. Overlap Graph Algorithm:
#### steps:
1. Construct an overlap graph. Two reads are joined by a directed edge of weight equal to the length of the maximum overlap of these two strings.

2. Then construct a Hamiltonian path in this graph in a greedy fashion.

3. Greedy Strategy : For each read select an outgoing edge of maximum weight. Why? Because the more the overlap between the reads shorter shorter will be the length of the combined string made of these reads.

4. Then read a string spelled by this path. i.e combine to form a super string.

5. Sometimes choosing the wrong first vertex may result in longer superstring. So you should generate random index probably 2-3 times and find minimum length super string.

6. Now in the last step since genome can be circular also so remove the overlap length between last and first read.

#### Note: 
This greedy algorithm does not work with every genome as it might not give optimal solution every time.

### 02. K-Mer Composition Algorithm:
#### What is K-mer Composition?
Given a String ACGTACTAT. Its 3-mer Composition is (ACG, CGT, GTA, TAC, ACT, CTA, TAT).

#### steps:
1. Read the k-mer composition of the graph.

2. Create the De-Bruijn graph from the k-mer composition.

3. Find an eulerian cycle in the graph.

4. Construct the genome from the found cycle.

### 03. Using De-Bruijn graph from Error-Prone Reads:
#### steps:
1. Read the reads of the genome from the input.

2. Create De-Bruijn Graph from the k-mers - which are formed by spitting the reads into all substrings of length k.

3. Remove the tips from the graph.

4. Remove the bubbles from the graph.(Do not remove bubbles of long lengths. Only remove bubbles of length less than k, which is the size of a k-mer. May also have to again remove tips after removing the bubbles.)

5. Find an Eulerian cycle in the graph.

6. Form the genome from the eulerian cycle found in the graph.
