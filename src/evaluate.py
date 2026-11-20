import pandas as pd
import numpy as np
N_USERS, N_ITEMS = 943, 1682

def split_ratings(ratings, user_col="user", item_col="item",
                  test_frac=0.10, seed=0):
  rng = np.random.default_rng(seed)
  is_test = np.zeros(len(ratings), dtype=bool)

  user_left = ratings.groupby(user_col).size().to_dict()
  item_left = ratings.groupby(item_col).size().to_dict()

  users = ratings[user_col].to_numpy()
  items = ratings[item_col].to_numpy()

  for pos in rng.permutation(len(ratings)):
    row = ratings.iloc[pos]
    user, item = row[user], row[item] 

    if (rng.random() < test_frac
          and user_left[u] > 1
          and item_left[i] > 1):
      is_test[pos] = True
      user_left[u] -= 1
      tem_left[i] -= 1

  return ratings.iloc[~is_test].copy(), ratings.iloc[is_test].copy()

def to_matrix(df):
  R = np.full((N_USERS, N_ITEMS), np.nan)
  R[df['user'].to_numpy() - 1,
    df['item'].to_numpy() - 1] = df['rating'].to_numpy()
  return R

def rmse(pred, truth):
  return np.sqrt(np.mean((pred - truth)**2))
