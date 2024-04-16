import numpy as np
from typing import Tuple


def generate_samples_linear_reg(
    samples: int,
    features: int,
    lower_bound: int,
    upper_bound: int,
    intercept: int,
    coeffecients: np.array,
    sigma: int,
) -> Tuple[np.array, np.array]:
    """
    Return samples and label from target linear regression distribution.

    Parameters
    ----------
    samples: int
        Number of samples to be sampled
    features: int
        Number of features
    lower_bound: int
        Lower bound on values of all features
    upper_bound: int
        Upper bound on values of all features
    intercept: int
        Intercept in the linear regression target distribution
    coeffecients: np.array
        The coeffecients of features in linear regression target distribution
    sigma: int
        The standard deviation in errors

    Returns
    -------
    X: np.array
        Generated samples
    y: np.array
        Generated labels from the distribution

    """
    error = np.random.normal(0, sigma, size=samples)
    X = np.empty((samples, features))
    y = np.empty(samples)
    for sample in range(samples):
        for feature in range(features):
            X[sample][feature] = np.random.uniform(lower_bound, upper_bound, size=1)
    y = np.dot(X, coeffecients) + intercept + error

    return (X, y)
