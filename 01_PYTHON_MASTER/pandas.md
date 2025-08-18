Certainly! Let's go through the list of frequently asked Pandas interview questions for a developer with 3 years of experience. I'll provide concise answers and explanations for each of the questions mentioned:

### 1. **Basic Operations**

- **How do you create a DataFrame in Pandas?**
  - **Answer**: You can create a DataFrame using a dictionary, list of lists, or a NumPy array. Here's an example using a dictionary:
    ```python
    import pandas as pd

    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']
    }
    df = pd.DataFrame(data)
    print(df)
    ```

- **How do you select a subset of a DataFrame?**
  - **Answer**: You can use `loc[]`, `iloc[]`, or boolean indexing:
    ```python
    # Select a single column
    df['Name']

    # Select multiple columns
    df[['Name', 'City']]

    # Select a row by label
    df.loc[0]

    # Select a row by integer position
    df.iloc[0]

    # Boolean indexing
    df[df['Age'] > 24]
    ```

- **What is the difference between `loc[]` and `iloc[]`?**
  - **Answer**: `loc[]` is used for label-based indexing (i.e., by row/column labels), while `iloc[]` is used for integer-based indexing (i.e., by row/column positions).

- **How do you add or delete columns from a DataFrame?**
  - **Answer**:
    - **Add a column**:
      ```python
      df['Salary'] = [70000, 80000, 65000]
      ```
    - **Delete a column**:
      ```python
      df.drop('Salary', axis=1, inplace=True)
      ```

### 2. **Data Cleaning**

- **How do you handle missing data in Pandas?**
  - **Answer**:
    - **Drop rows with missing data**:
      ```python
      df.dropna(inplace=True)
      ```
    - **Fill missing data**:
      ```python
      df.fillna(0, inplace=True)  # Fill with 0
      df.fillna(method='ffill', inplace=True)  # Forward fill
      ```

- **How do you detect and remove duplicate rows in a DataFrame?**
  - **Answer**:
    - **Detect duplicates**:
      ```python
      df.duplicated()
      ```
    - **Remove duplicates**:
      ```python
      df.drop_duplicates(inplace=True)
      ```

- **How do you replace values in a DataFrame?**
  - **Answer**:
    ```python
    df['City'].replace({'New York': 'NYC', 'San Francisco': 'SF'}, inplace=True)
    ```

- **How do you change the data type of a DataFrame column?**
  - **Answer**:
    ```python
    df['Age'] = df['Age'].astype(float)
    ```

### 3. **Data Manipulation**

- **How do you concatenate or merge DataFrames?**
  - **Answer**:
    - **Concatenate**:
      ```python
      df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
      df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
      pd.concat([df1, df2], axis=0)
      ```
    - **Merge**:
      ```python
      df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
      df2 = pd.DataFrame({'ID': [1, 3], 'Age': [24, 22]})
      pd.merge(df1, df2, on='ID', how='inner')
      ```

- **How do you perform group-by operations?**
  - **Answer**:
    ```python
    df.groupby('City')['Age'].mean()
    ```

- **What is the difference between `apply()` and `map()` functions in Pandas?**
  - **Answer**:
    - `apply()` is used to apply a function along an axis of the DataFrame (row-wise or column-wise).
    - `map()` is used to substitute each value in a Series with another value.
    ```python
    df['Age'].apply(lambda x: x + 1)  # Increment each age by 1
    df['City'].map({'NYC': 'New York', 'SF': 'San Francisco'})  # Map values
    ```

- **How do you sort a DataFrame by multiple columns?**
  - **Answer**:
    ```python
    df.sort_values(by=['City', 'Age'], ascending=[True, False], inplace=True)
    ```

### 4. **Advanced Operations**

- **How do you pivot a DataFrame?**
  - **Answer**:
    ```python
    df.pivot(index='Name', columns='City', values='Age')
    ```
  - **Pivot table**:
    ```python
    df.pivot_table(index='Name', columns='City', values='Age', aggfunc='mean')
    ```

- **How do you use `cut()` and `qcut()` in Pandas?**
  - **Answer**:
    - `cut()` is used to bin data into discrete intervals.
      ```python
      df['Age Group'] = pd.cut(df['Age'], bins=[0, 18, 30, 60], labels=['Child', 'Young Adult', 'Adult'])
      ```
    - `qcut()` is used to create quantile-based bins.
      ```python
      df['Age Quartile'] = pd.qcut(df['Age'], 4)
      ```

- **How do you handle datetime operations in Pandas?**
  - **Answer**:
    - **Convert to datetime**:
      ```python
      df['Date'] = pd.to_datetime(df['Date'])
      ```
    - **Extract parts of the date**:
      ```python
      df['Year'] = df['Date'].dt.year
      df['Month'] = df['Date'].dt.month
      ```
    - **Date arithmetic**:
      ```python
      df['Next Year'] = df['Date'] + pd.DateOffset(years=1)
      ```

- **How do you use rolling and expanding windows in Pandas?**
  - **Answer**:
    - **Rolling window**:
      ```python
      df['Rolling Mean'] = df['Values'].rolling(window=3).mean()
      ```
    - **Expanding window**:
      ```python
      df['Expanding Sum'] = df['Values'].expanding().sum()
      ```

### 5. **Performance Optimization**

- **How do you optimize memory usage in a DataFrame?**
  - **Answer**:
    - **Downcast data types**:
      ```python
      df['IntColumn'] = pd.to_numeric(df['IntColumn'], downcast='integer')
      df['FloatColumn'] = pd.to_numeric(df['FloatColumn'], downcast='float')
      ```
    - **Use categorical data types**:
      ```python
      df['CategoryColumn'] = df['CategoryColumn'].astype('category')
      ```
    - **Remove unnecessary columns**:
      ```python
      df.drop(['UnnecessaryColumn'], axis=1, inplace=True)
      ```

- **What are some common pitfalls when working with large datasets in Pandas?**
  - **Answer**:
    - **Memory errors**: Avoid by reading data in chunks or using `Dask`.
    - **Slow performance**: Use vectorized operations instead of loops.
    - **Out-of-core computations**: Use libraries like `Dask` for handling large datasets that don't fit in memory.

### 6. **Real-World Scenarios**

- **How would you handle a dataset that is too large to fit into memory?**
  - **Answer**:
    - Read data in chunks using `pd.read_csv()` with the `chunksize` parameter.
    - Use `Dask` or `Vaex` for out-of-core computation.
    - Process the data in smaller batches and aggregate results.

- **Explain how you would clean and prepare data for machine learning using Pandas.**
  - **Answer**:
    - Handle missing data using `fillna()` or `dropna()`.
    - Perform feature engineering by creating new features from existing ones.
    - Encode categorical variables using `pd.get_dummies()` or `LabelEncoder`.
    - Normalize or standardize numerical features using techniques like min-max scaling or z-score normalization.

- **How would you merge two datasets with different keys, and what challenges might you face?**
  - **Answer**:
    - Merge datasets using `pd.merge()`, specifying different keys in the `left_on` and `right_on` parameters.
    - Challenges include handling missing keys, ensuring data types are consistent, and managing how to handle mismatched or missing data after the merge.

- **How do you export a DataFrame to a CSV file without the index?**
  - **Answer**:
    ```python
    df.to_csv('output.csv', index=False)
    ```

### 7. **Error Handling and Debugging**

- **What common errors have you encountered when using Pandas, and how do you resolve them?**
  - **Answer**:
    - **Key

Error**: Usually occurs when trying to access a column that doesn't exist. Verify column names with `df.columns`.
    - **ValueError**: Common when merging data with incompatible shapes or missing keys. Check data shapes and keys before merging.
    - **TypeError**: Occurs when performing operations on incompatible data types. Convert data types using `astype()`.

- **How do you handle operations that raise a `SettingWithCopyWarning` in Pandas?**
  - **Answer**:
    - **Explanation**: This warning occurs when trying to modify a copy of a slice from a DataFrame. To avoid this, ensure you're working with the original DataFrame or use `.loc[]` to explicitly set values.
      ```python
      df.loc[df['Age'] > 25, 'AgeGroup'] = 'Adult'
      ```

### 8. **Case Studies or Hands-On Problems**

- **Given a dataset, how would you calculate the percentage change for each row?**
  - **Answer**:
    ```python
    df['PctChange'] = df['Values'].pct_change()
    ```

- **How would you normalize data in a DataFrame?**
  - **Answer**:
    - **Min-Max Scaling**:
      ```python
      df['Normalized'] = (df['Values'] - df['Values'].min()) / (df['Values'].max() - df['Values'].min())
      ```
    - **Z-score normalization**:
      ```python
      df['Zscore'] = (df['Values'] - df['Values'].mean()) / df['Values'].std()
      ```

- **How would you create a summary report from a sales dataset?**
  - **Answer**:
    - Use group-by operations to aggregate sales data by different categories.
    - Create a pivot table to summarize data by region, product, or time period.
    - Combine these results into a comprehensive summary DataFrame.

By practicing and understanding these concepts, you'll be well-prepared to answer Pandas-related interview questions and demonstrate your expertise effectively.