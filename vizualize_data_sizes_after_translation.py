# Visualization of dataset sizes after machine translation using LINDAT Translator
import matplotlib.pyplot as plt
import numpy as np 

train=[130319,107088,87599,64164]
dev = [11873,10845,10570,8739]

labels = ['SQUAD 2.0 EN','SQUAD 2.0 CZ','SQUAD 1.1 EN','SQUAD 1.1 CZ']
plt.bar(range(len(train)),train) 
plt.title('Size of  dataset (Train set)')
plt.ylabel('Number of questions') 
plt.xlabel('Dataset')
plt.xticks(np.arange(len(train)), labels)
plt.savefig('train-match.pdf', bbox_inches='tight')
plt.show()

labesl = ['SQUAD 2.0 EN','SQUAD 2.0 CZ','SQUAD 1.1 EN','SQUAD 1.1 CZ']
plt.bar(range(len(dev)),dev) 
plt.title('Size of  dataset (Dev set)')
plt.ylabel('Number of question') 
plt.xlabel('Dataset')
plt.xticks(np.arange(len(train)), labels)
plt.savefig('dev-match.pdf', bbox_inches='tight')
plt.show()

