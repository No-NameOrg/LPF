import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, auc, precision_recall_curve 
from sklearn.metrics import confusion_matrix

def testFile(filepath):
    """
        utility function to test existence of files passed
    """

    if not os.path.dirname(filepath):
        filepath = ''.join(['./',filepath])

    assert os.path.exists(filepath), "No such Directory as mentioned in filepath"
    
    return filepath

def drawROC(y_true, y_prob):
    ns_prob = np.ones_like(y_true, dtype=np.float_)
    
    ns_fpr, ns_tpr, _ = roc_curve(y_true, ns_prob)
    lr_fpr, lr_tpr, _ = roc_curve(y_true, y_prob)
    
    auc_score = roc_auc_score(y_true, y_prob)

    plt.title(f"ROC - Curve: AUC = {round(auc_score,2)}")
    plt.xlabel("False positive rate")
    plt.ylabel("true positive rate")
    plt.plot(lr_fpr, lr_tpr, label = "Logistic")
    plt.plot(ns_fpr, ns_tpr, label = "No Skill")
    plt.legend()
    plt.show()

def precisionRecall(y_true, y_prob):

    lr_precision, lr_recall, _ = precision_recall_curve(y_true, y_prob)
    auc_score = auc(lr_recall, lr_precision)

    plt.title(f"Precision- Recall curve : AUC - {round(auc_score, 2)}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.plot(lr_recall, lr_precision, marker = '.', label = 'Logisitic')
    plt.legend()
    plt.show()

def calConfusionMatrix(y_true, y_prob, threshold = 0.5):
    
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)

    if y_prob.ndim == 1:
        y_prob = y_prob.reshape(-1,1)
    
    if y_true.ndim == 1:
        y_true = y_true.reshape(-1,1)

    y_pred = np.apply_along_axis(lambda x: 1 if x>=threshold else 0, axis = 1, arr = y_prob)

    conf_matrix = confusion_matrix(y_true, y_pred)

    matrix = pd.DataFrame(conf_matrix, index = ['actual_0', 'actual_1'], columns = ['pred_0','pred_1'])

    return matrix