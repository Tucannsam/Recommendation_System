
import os, urllib.request, zipfile
import numpy as np
import pandas as pd

def split_ratings(ratings, test_frac=0.10, seed=0):
  rng = np.random.default_rng(seed)
  is_test = np.zeros(len(ratings), dtype=bool)

  user_left = ratings.groupby(user).size().to_dict()
  item_left = ratings.groupby(item).size().to_dict()

  for pos in rng.permutation(len(ratings)):
    row = ratings.iloc[pos]
    user, item = row[user], row[item]

  if (rng.random() < test_frac
      and user_left[user] > 1
      and item_left[item] > 1):
    is_test[pos] = True
    user_left[user] -= 1
    item_left[item] -= 1

  return ratings.iloc[~is_test].copy(), ratings.iloc[is_test].copy()


N_USERS, N_ITEMS = 943, 1682

def to_matrix(df):
    R = np.full((N_USERS, N_ITEMS), np.nan)
    R[df[user].to_numpy() - 1,
      df[item].to_numpy() - 1] = df[rating].to_numpy()
    return R

R = to_matrix(train)
known = ~np.isnan(R)

print(Matrix shape:, R.shape)
print(Known training ratings:, known.sum())

def rmse(pred, truth):
Root mean squared error, measured in stars.
return np.sqrt(np.mean((pred - truth)**2))
