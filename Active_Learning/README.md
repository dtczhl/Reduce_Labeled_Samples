## Function API

The sampling methods have the standard API in the following format

```python
def sampling_function_name(X, y, n_sample, **kwargs):
    # return the index of the selected samples
```

where 
`X` is a 2D numpy matrix with rows representing the data samples, and columns representing the features of each data sample. 
`y` is a 1D numpy array representing the labels of the corresponding data samples, with -1 means unlabeled samples. 
`n_sample` is the number of samples to select in each iteration (usually 1). 
The sampling method selects `n_sample` unlabeled samples (who are valued -1 in `y`) and return their 0-based indexes. 
`kwargs` are additional arguments, such as current trained model. 
Please go to each sampling method below for more details.



## Supported Sampling Strategy

### Uncertainty-Based Methods

* Least Confident. Function and filename: `uncertainty_confident`

    ```python
        # This function requires 
        #   X: data sample
        #   y: labels. -1 for unlabeled samples
        #   n_sample: number of samples to select
        #   kwarg
        #       model: currently trained model, must has .predict() function
        #       reverse [optional]: True if want to select the samples of the largest confidence; False by default. 
        uncertainty_confident(X, y, n_sample)
    ```





