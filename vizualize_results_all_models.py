# Evaluation of models and visualizations of graphs
import matplotlib.pyplot as plt
import numpy as np 
# SQUAD + BERT
labels = ['BERTc EN-EN','BERTu EN-EN','M-BERTc EN-EN','MBERTu EN-EN','bRoBERTA EN-EN','lRoBERTA EN-EN',
          'BERTc EN-CZ','BERTu EN-CZ', 'MBERTc EN-CZ','MBERTu EN-CZ','bRoBERTA EN-CZ','lRoBERTA EN-CZ',
          'BERTc EN-CZENCZ','BERTu EN-CZENCZ','MBERTc EN-CZENCZ','MBERTu EN-CZENCZ','bRoBERTA EN-CZENCZ','lRoBERTA EN-CZENCZ',
          'MBERTc CZ-CZ','MBERTu CZ-CZ', 'bRoBERTA CZ-CZ','lRoBERTA CZ-CZ']

# 2.0 data vyhodnocena na 2.0 modelu
em22 =[72.85,73.35,75.79,74.88,74.07,83.21,
       53.48,54.78,58.28,59.59,62.09,73.50,
       64.35,65.26,67.40,66.20,65.62,72.82,
       66.60,64.96,64.98,75.57]
f122 =[76.03,76.59,78.76,77.98,76.97,86.23,
       53.84,54.83,62.76,63.89,65.93,77.58,
       69.11,69.86,71.96,70.72,70.00,78.04,
       69.61,68.14,68.15,79.19]
    
         
plt.title('Results for QA trained and evaluated on SQuAD 2.0 with BERT')
ax = plt.subplot(111)

ax.set_xlabel('Model')
ax.set_ylabel('Value [%]')

ax.bar(np.arange(0,len(f122)),f122, label='F1 score',color='k')
ax.bar(np.arange(0,len(em22)),em22, label='Exact match',color='g') 
ax.set_xticks(np.arange(len(em22))) 
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
#ax.set_ylim(bottom=50)
plt.savefig('cz-all22.pdf', bbox_inches='tight')
plt.show()


# 1.1 data vyhodnocena na 2.0 modelu
em21 =[81.58,81.05,82.52,81.81,81.37,86.93,
       11.18,05.34,57.76,61.87,65.22,73.99,
       64.25,63.86,65.37,65.20,64.54,68.70,
       57.76,62.86,68.51,75.87]
f121 =[88.93,88.75,89.47,89.09,88.48,93.05,
       23.47,21.72,69.46,73.43,76.30,84.25,
       76.79,76.93,77.52,77.27,76.74,81.15,
       69.46,74.24,78.34,85.26]

plt.clf()
plt.title('Results for QA trained on SQuAD 2.0 and evaluated on SQuAD 1.1 with BERT')
ax = plt.subplot(111)

ax.set_xlabel('Model')
ax.set_ylabel('Value [%]')

ax.bar(np.arange(0,len(f121)),f121, label='F1 score',color='k')
ax.bar(np.arange(0,len(em21)),em21, label='Exact match',color='g') 
ax.set_xticks(np.arange(len(em21))) 
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
#ax.set_ylim(bottom=50)
plt.savefig('cz-all21.pdf', bbox_inches='tight')
plt.show()

# 1.1 data vyhodnocena na 1.1 modelu
em11 =[81.43,80.92,81.99,81.98,80.91,87.27,
       09.53,06.16,59.49,62.09,64.63,73.64,
       64.06,63.57,65.09,65.00,64.52,69.04,
       59.49,62.11,69.18,76.39]
f111 =[88.88,88.59,89.10,89.27,88.11,93.24,
       21.62,21.75,70.62,73.89,75.85,84.07,
       76.78,76.61,77.47,77.38,76.91,81.33,
       70.62,73.94,78.71,85.62]

plt.clf()
plt.title('Results for QA trained and evaluated on SQuAD 1.1 with BERT')
ax = plt.subplot(111)

ax.set_xlabel('Model')
ax.set_ylabel('Value [%]')

ax.bar(np.arange(0,len(f111)),f111, label='F1 score',color='k')
ax.bar(np.arange(0,len(em11)),em11, label='Exact match',color='g') 
ax.set_xticks(np.arange(len(em11))) 
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
#ax.set_ylim(bottom=50)
plt.savefig('cz-all11.pdf', bbox_inches='tight')
plt.show()




labels = ['BERTc EN-CZ','BERTu EN-CZ', 'MBERTc EN-CZ','MBERTu EN-CZ','bRoBERTA EN-CZ','lRoBERTA EN-CZ',
          'BERTc EN-CZENCZ','BERTu EN-CZENCZ','MBERTc EN-CZENCZ','MBERTu EN-CZENCZ','bRoBERTA EN-CZENCZ','lRoBERTA EN-CZENCZ',
          'MBERTc CZ-CZ','MBERTu CZ-CZ','bRoBERTA CZ-CZ','lRoBERTA CZ-CZ']
# 2.0 data vyhodnocena na 2.0 modelu
emcz =[53.48,54.78,58.28,59.59,62.09,73.50,
       64.35,65.26,67.40,66.20,65.62,72.82,
       66.60,64.96,64.98,75.57]
f1cz =[53.84,54.83,62.76,63.89,65.93,77.58,
       69.11,69.86,71.96,70.72,70.00,78.04,
       69.61,68.14,68.15,79.19]
plt.clf()
plt.title('Results for Czech QA trained and evaluated on SQuAD 2.0')
ax = plt.subplot(111)

ax.set_xlabel('Model')
ax.set_ylabel('Value [%]')

ax.bar(np.arange(0,len(f1cz)),f1cz, label='F1 score',color='k')
ax.bar(np.arange(0,len(emcz)),emcz, label='Exact match',color='g') 
ax.set_xticks(np.arange(len(emcz))) 
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
ax.set_ylim(bottom=50)
plt.savefig('allcz.pdf', bbox_inches='tight')
plt.show()
