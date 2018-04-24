import numpy as np

def cartesian_product_multi(list_of_vectors):
    """ calculates the cartesian product from a list of vectors

    Parameters
    ----------
    list_of_vectors:  a list of np.arrays, each of which will be the input in the cartesian product

    Returns
    ----------
    res:  an np.array containing the repeated vectors as the columns
    """

    res = np.transpose(np.array(
                      [np.tile(np.repeat(param_list[i],
                       np.prod(param_size[i+1:])),np.prod(param_size[:i]))
                       for i in range(len(param_names))]))

    return res
