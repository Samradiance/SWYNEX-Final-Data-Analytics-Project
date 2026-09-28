#installing pandas as pd
import pandas as pd 

#importing dataset 
df=pd.read_csv("music_dataset.csv")

#printing shape of dataset
print("Dataset shape:",df.shape)

#printing first 5 rows
print("\nFirst 5 rows:")
print(df.head())

#checking if their is any null values
print("\nMissing values:")
print(df.isnull().sum())

#checking for any duplicate values
print("\nDuplicate Values")
print(df.duplicated().sum())

#finding data types of each columns
print("\nData Types:")
print(df.dtypes)

#changing release_date column data type to datetime from string
df["release_date"] = pd.to_datetime(
    df["release_date"],
    format="%d-%m-%Y"
)
print("\n")
print(df["release_date"].dtype)

duplicate_count=df.duplicated().sum()
print("\nDuplicated rows:",duplicate_count)
df=df.drop_duplicates()

missing_values=df.isnull().sum()
print("\nMissing values: ")
print(missing_values)

#finding range of popularity
print("popularity range:",df["popularity"].min(),"to",df["popularity"].max())

#finding range of danceabilty
print("Danceability range:",df["danceability"].min(),"to",df["danceability"].max())

#finding range of energy
print("Energy range:",df["energy"].min(),"to",df["energy"].max())

#saving cleaned dataset as cleaned_music_dataset.csv 
df.to_csv("cleaned_music_dataset.csv", index=False)
print("\nCleaned dataset saved succesfully")
