import nltk as tk
import textmining as tx
import networkx as nx
import pylab as plt
import re
#import matplotlib as plt

#inFile = raw_input('Enter input file name: ')
#if len(inFile) < 1:
inFile = "rfc3410.txt"

try:
    file1= open(inFile,'r')
    file2= open("rfc3418.txt",'r')
except:
    print "Input file can't be opened: "
    exit()



#


doc1=file1.read()
doc2=file2.read()
ref = list()


ref =re.findall(r'RFC \s\d{4}',doc1,re.X)

ref2 = list()
ref2= set(ref)






print "REF",  ref

print "REF2", ref2



G = nx.Graph()
G.add_node("RFC 3410")
g=G.number_of_nodes()

print (g, len(ref))

for r in ref2:
    print r
    G.add_node(r)
    if r!= "RFC 3410":
        G.add_edge("RFC 3410", r)



print ("number:"+ str(G.number_of_nodes()))
node_color= ['r','b','g','cyan']

nx.draw(G, node_color=node_color, with_labels = True, node_size=1000)
plt.show()
plt.figure("test1.png")



#doc3=file3.read()
#doc4=file4.read()
#doc5=file5.read()
#ref.append(re.findall(r'RFC \s\d{4}',doc3,re.X))






#print (ref)

tdm = tx.TermDocumentMatrix()




tdm.add_doc (doc1)
tdm.add_doc(doc2)

tdm.write_csv('matrix.csv', cutoff=1)


#for row in tdm.rows(cutoff=1):
#print row
