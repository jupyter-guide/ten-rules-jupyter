from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import pandas as pd
from collections import OrderedDict
import time
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support
import numpy as np

def downsample(df, columnName, seed=7):
    '''Returns a balanced dataset for the given column name by downsampling
    the majority classes.
    The classification column must be of type String

    Attributes
    ----------
        data (Dataframe)
        columnName (str): column to be balanced by
        seed (int): random number seed
    '''

    valueCounts = df[columnName].value_counts()
    minCount = min([int(c) for c in valueCounts])
    value = valueCounts.index

    down_sampled_dfs = []
    for val in value:
        df_sub = df[df[columnName] == val]
        down_sampled_dfs.append(resample(df_sub,\
                                         replace = False, \
                                         n_samples = minCount, \
                                         random_state = seed)
                               )
    return pd.concat(down_sampled_dfs)

def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.2f}; misclass={:0.2f}'.format(accuracy, misclass))
    plt.show()
    
def indexer(df, columnName):

    labelIndexer =  {k:i for i,k in enumerate(df[columnName].unique())}
    labelConverter =  {i:k for i,k in enumerate(df[columnName].unique())}

    return labelIndexer, labelConverter


class MultiClassClassifier(object):
    '''Fits a multi-class classification model using mllib classification method and
    returns classification metrics.

    Attributes
    ----------
        predictor: type of multi-class classifier
        label (str): classification label
        testFraction (float): test set fraction [0.3]
        seed (int): random seed
        average (str): Type of averaging for multiclass classification metrics
                   - micro
                   - macro
                   - weighted (default)
                   - samples
    '''


    def __init__(self, predictor, label, testFraction=0.3, seed=1, average = 'weighted'):

        self.predictor = predictor
        self.label = label
        self.testFraction = testFraction
        self.seed = seed
        self.prediction = None
        self.average = average

    def fit(self, df):
        '''Dataset must at least contain the following two columns:
        label: the class labels
        features: feature vector

        Attributes
        ----------
            data (DataFrame): input data

        Returns
        -------
            map with metrics
        '''

        start = time.time()

        numClass = len(df[self.label].unique())

        # Convert label to indexedLabel
        labelIndexer, labelConverter = indexer(df, self.label)
        df['indexedLabel'] = df[self.label].map(labelIndexer)

        # Split the data into trianing and test set
        train, test = train_test_split(df, test_size=self.testFraction)

        print("\n Class\tTrain\tTest")
        for l in df[self.label].unique():
            print(f"\n{l}\t{train[train[self.label] == l].shape[0]}\t{test[test[self.label] == l].shape[0]}")

        # Train model
        clf = self.predictor.fit(train.features.tolist(), train.indexedLabel.tolist()) # Set predicting class to numeric values

        # Make prediction
        pred = clf.predict(test.features.tolist())
        scores = clf.predict_proba(test.features.tolist())

        test = test.reset_index()
        test['predictions'] = pd.Series(pred).map(labelConverter)
        positive_prob = [s[1] for s in scores]
        self.prediction = test

        metrics = OrderedDict()
        metrics["Methods"] = str(self.predictor).split('(')[0]

        precision, recall, fscore, support = precision_recall_fscore_support(test.indexedLabel, pred)
        metrics_table = OrderedDict([('Labels', df[self.label].unique()) ,
                                    ('Precision', ["%.2f"%p + '%' for p in precision]),
                                    ('Recall', ["%.2f"%r  + '%' for r in recall]),
                                    ('FScore' , ["%.2f"%f for f in fscore]),
                                    ('Support' , support),]
                                    )
        self.metrics_table = pd.DataFrame(metrics_table)

        if numClass == 2:
            metrics['AUC'] = str(roc_auc_score(test.indexedLabel, positive_prob))
            self.TPR, self.FPR, thresholds = roc_curve(test.indexedLabel, positive_prob)
            self.AUC = auc(self.TPR, self.FPR)

            metrics['F Score'] = str(f1_score(test.indexedLabel, pred))
            metrics['Accuracy'] = str(accuracy_score(test.indexedLabel, pred))
            metrics['Precision'] = str(precision_score(test.indexedLabel, pred))
            metrics['Recall'] = str(recall_score(test.indexedLabel, pred))

        else:
            metrics['F Score'] = str(f1_score(test.indexedLabel, pred, average = self.average))
            metrics['Accuracy'] = str(accuracy_score(test.indexedLabel, pred))
            metrics['Precision'] = str(precision_score(test.indexedLabel, pred, average = self.average))
            metrics['Recall'] = str(recall_score(test.indexedLabel, pred, average = self.average))

        confusionMatrix = confusion_matrix(test.indexedLabel, pred)

        if numClass > 2:
            FP = confusionMatrix.sum(axis=0) - np.diag(confusionMatrix)
            FN = confusionMatrix.sum(axis=1) - np.diag(confusionMatrix)
            TP = np.diag(confusionMatrix)
            TN = confusionMatrix.sum() - (FP + FN + TP)
        else:
            FP = confusionMatrix[0][1]
            FN = confusionMatrix[1][0]
            TP = confusionMatrix[0][0]
            TN = confusionMatrix[1][1]

        TPR = TP/(TP+FN)
        FPR = FP/(FP+TN)

        average_rate = lambda x: sum(x)/float(len(x)) if type(x) == np.ndarray else x
        TPR = average_rate(TPR)
        FPR = average_rate(FPR)

        metrics["False Positive Rate"] = str(FPR)
        metrics["True Positive Rate"] = str(TPR)

        metrics[""] = f"\nConfusion Matrix\n{df[self.label].unique()}" \
                      + f"\n{confusionMatrix}"

        end = time.time()
        print(f"\nTotal time taken: {end-start}\n")

        return metrics


def plot_roc(TPR, FPR, AUC):
    plt.title('Receiver Operating Characteristic')
    plt.plot(TPR, FPR, 'b',
    label='AUC = %0.2f'% AUC)
    plt.legend(loc='lower right')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
