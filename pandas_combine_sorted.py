"""
combines two dataframes by sorting the values of each cell

Parameters
----------
df1, df2 : pd.DataFrame, two dataframes to combine

Returns
-------
pd.dataframe: DataFrame of the combined values with suffices 1 and 2

"""
def combine_sorted(df1, df2):

    data_nx1  = data_n1.where(df1 >  df2, df2).fillna(df1).add_suffix('1')
    data_nx2  = data_n1.where(df1 <= df2, df2).fillna(df1).add_suffix('2')

    return pd.concat([data_nx1, data_nx2], axis=1)
