import nltk as tk
import networkx as nx
import textmining as tx
import re
import matplotlib.pyplot as plt
import os

path="./rfcs/"
files=os.listdir(path)

docs=[]
# Initiallizing the reference graph
G=nx.Graph()
G.add_node(0,{"color": "red"})

# Constructing the graph of rfcs references 
try:
    for f in files:
        doc=open(path+f,'r')
        text = doc.read()
        ref =re.findall(r'RFC \s\d{4}',text,re.X)
        docs.append(doc)
        #print ref
        for r in ref:
            print r
            G.add_node(r,{"color": "blue"})
            G.add_edge(0,r)
            
        

except:
    print "IO Erro"

nx.draw(G,  with_labels = True, node_size=1000)
plt.show()
plt.figure("test1.png")


tdm = tx.TermDocumentMatrix()



for d in len(docs):
   doc=docs[d].read()
   tdm.add_doc (doc)


tdm.write_csv('matrix.csv', cutoff=1)


for row in tdm.rows(cutoff=1):
print row
