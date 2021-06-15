"""
    Active learning wrapper
"""

import glob
import re
import sys
import os


from uncertainty_confident import uncertainty_confident


class ActiveLearning:

    # Name of the sampling method
    sampling_method_name = None

    def __init__(self, sampling_method):
        self.sampling_method_name = sampling_method

        # change directory to current file
        original_path = os.getcwd()
        this_file_path = os.path.abspath(__file__)
        this_directory_name = os.path.dirname(this_file_path)
        os.chdir(this_directory_name)

        current_directory_python_files = glob.glob("./*.py")
        supported_methods = [re.search(r"\W+(.+?).py", x).group(1).lower() for x in current_directory_python_files]
        if sampling_method not in supported_methods:
            sys.exit("****** Sampling method: {sampling_method} is not supported.\n"
                     "\tPlease check if {sampling_method}.py exists under Active_Learning folder"
                     .format(sampling_method=sampling_method))

        # change back to original path
        os.chdir(original_path)

    def sample(self, X, y, n_sample, **kwargs):
        function_call_str = self.sampling_method_name + "(X=X, y=y, n_sample=n_sample, kwargs=kwargs)"
        result = eval(function_call_str)
        return result



if __name__ == "__main__":

    a = ActiveLearning("uncertainty_confident")

    a.sample(None, None, None)