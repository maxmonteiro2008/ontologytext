import nltk as tk
import textmining as tx
import networkx as nx
#import pylab as plt
import re
import matplotlib.pyplot as plt
import os

path="./rfcs/"
files=os.listdir(path)
#print files

#   Gerar o no centraldos documentos
f=files[0]
#print f
n1 = f.split('.')
G = nx.Graph()
G.add_node(n1[0])


docs=[]

try:
    for f in files:
        n1 = f.split('.')
        G.add_node(n1[0], color='r')
        doc=open(path+f,'r')
        text = doc.read()
        ref =re.findall(r'RFC \s\d{4}',text,re.X)
        docs.append(doc)
        #print ref
        for r in ref:
            print r
            G.add_node(r,color='b')
            if r!= n1[0]:
                 G.add_edge(n1[0], r)
        

except:
    print "IO Erro"



#print docs[0]
#doc1=file1.read()
#doc2=file2.read()
#ref = list()














nx.draw(G,  with_labels = True, node_size=1000)
plt.show()
#plt.figure("test1.png")



#doc3=file3.read()
#doc4=file4.read()
#doc5=file5.read()



#tdm = tx.TermDocumentMatrix()




#tdm.add_doc (doc1)
#tdm.add_doc(doc2)

#tdm.write_csv('matrix.csv', cutoff=1)


#for row in tdm.rows(cutoff=1):
#print row
