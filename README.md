# Reduce_Labeled_Samples

Methods for using as few human-labeled samples as possible, while training good machine learning models

This repo considers the following categories of methods. See each folder for more details

* [Active Learning](#active_learning)
* [Semi-Supervised Learning](#semi_supervised_learning)

## Notations

[add a figure here]

## <a id="active_learning"> Active Learning </a>

### Function API

All active learning functions are under the `Active_Learning` folder. Each sampling method has the standard API in the following format

```python
def sampling_function_name(X, y, n_sample, **kwargs):
    # return the index of samples selected
```
where `X` is a 2D numpy matrix with rows representing the data samples, and columns representing the features of each data sample. `y` is a 1D numpy array representing the labels of the corresponding data samples, with -1 means unlabeled samples. `n_sample` is the number of samples to select in each iteration (usually 1). The sampling method selects `n_sample` unlabeled samples (who are valued -1 in `y`) and return their 0-based indexes. `kwargs` are additional arguments, such as current trained model. Please go to each sampling method below for more details.



### Supported Sampling Strategy

* Uncertainty-Based Methods
    * `uncertainty_confident`. 

## <a id="semi_supervised_learning"> Semi-Supervised Learning </a>
