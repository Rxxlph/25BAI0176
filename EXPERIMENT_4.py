import pandas as pd
from datetime import date

FILE_1_PATH = "/content/fraudTest.csv"
FILE_2_PATH = "/content/fraudTrain.csv"
COLUMN_A = "age"
COLUMN_B = "amt" # Changed from 'salary' to 'amt' as 'salary' is not in the dataframe

df1 = pd.read_csv(FILE_1_PATH)
df2 = pd.read_csv(FILE_2_PATH)

print("Dataset 1 Shape:", df1.shape)
print("Dataset 2 Shape:", df2.shape)

df = pd.concat([df1, df2], ignore_index=True)
print("Combined Dataset Shape:", df.shape)
print("\n--- Combined Data Preview ---")
print(df.head())

# Convert 'dob' to datetime and calculate 'age'
df['dob'] = pd.to_datetime(df['dob'])
today = pd.to_datetime(date.today())
df['age'] = (today - df['dob']).dt.days // 365
print("\n--- Age Calculation Preview ---")
print(df[['dob', 'age']].head())

df['width_bins'] = pd.cut(df[COLUMN_A], bins=4)
print("\n--- 1. Equal-Width Binning (Discretization) Results ---")
print(df[[COLUMN_A, 'width_bins']].head(10))
print("\nCounts per bin:")
print(df['width_bins'].value_counts().sort_index())

df['freq_bins'] = pd.qcut(df[COLUMN_B], q=4)
print("\n--- 2. Equal-Frequency Binning (Quantile) Results ---")
print(df[[COLUMN_B, 'freq_bins']].head(10))
print("\nCounts per bin:")
print(df['freq_bins'].value_counts().sort_index())

custom_boundaries = [0, 12, 19, 60, 100]
custom_labels = ['Child', 'Teen', 'Adult', 'Senior']
df['custom_bins'] = pd.cut(df[COLUMN_A], bins=custom_boundaries, labels=custom_labels)
print("\n--- 3. Custom Label Binning Results ---")
print(df[[COLUMN_A, 'custom_bins']].head(10))
print("\nCounts per bin:")
print(df['custom_bins'].value_counts().sort_index())

OUTPUT_PATH = "/content/final_processed_dataset.csv"
df.to_csv(OUTPUT_PATH, index=False)
print(f"\n💾 Execution complete! Combined and binned dataset saved to: {OUTPUT_PATH}")


#OUTPUT
###Dataset 1 Shape: (555719, 23)
Dataset 2 Shape: (1296675, 23)
Combined Dataset Shape: (1852394, 23)

--- Combined Data Preview ---
   Unnamed: 0 trans_date_trans_time            cc_num  \
0           0   2020-06-21 12:14:25  2291163933867244   
1           1   2020-06-21 12:14:33  3573030041201292   
2           2   2020-06-21 12:14:53  3598215285024754   
3           3   2020-06-21 12:15:15  3591919803438423   
4           4   2020-06-21 12:15:17  3526826139003047   

                               merchant        category    amt   first  \
0                 fraud_Kirlin and Sons   personal_care   2.86    Jeff   
1                  fraud_Sporer-Keebler   personal_care  29.84  Joanne   
2  fraud_Swaniawski, Nitzsche and Welch  health_fitness  41.28  Ashley   
3                     fraud_Haley Group        misc_pos  60.05   Brian   
4                 fraud_Johnston-Casper          travel   3.19  Nathan   

       last gender                       street  ...      lat      long  \
0   Elliott      M            351 Darlene Green  ...  33.9659  -80.9355   
1  Williams      F             3638 Marsh Union  ...  40.3207 -110.4360   
2     Lopez      F         9333 Valentine Point  ...  40.6729  -73.5365   
3  Williams      M  32941 Krystal Mill Apt. 552  ...  28.5697  -80.8191   
4    Massey      M     5783 Evan Roads Apt. 465  ...  44.2529  -85.0170   

   city_pop                     job         dob  \
0    333497     Mechanical engineer  1968-03-19   
1       302  Sales professional, IT  1990-01-17   
2     34496       Librarian, public  1970-10-21   
3     54767            Set designer  1987-07-25   
4      1126      Furniture designer  1955-07-06   

                          trans_num   unix_time  merch_lat  merch_long  \
0  2da90c7d74bd46a0caf3777415b3ebd3  1371816865  33.986391  -81.200714   
1  324cc204407e99f51b0d6ca0055005e7  1371816873  39.450498 -109.960431   
2  c81755dbbbea9d5c77f094348a7579be  1371816893  40.495810  -74.196111   
3  2159175b9efe66dc301f149d3d5abf8c  1371816915  28.812398  -80.883061   
4  57ff021bd3f328f8738bb535c302a31b  1371816917  44.959148  -85.884734   

   is_fraud  
0         0  
1         0  
2         0  
3         0  
4         0  

[5 rows x 23 columns]

--- Age Calculation Preview ---
         dob  age
0 1968-03-19   58
1 1990-01-17   36
2 1970-10-21   55
3 1987-07-25   39
4 1955-07-06   71

--- 1. Equal-Width Binning (Discretization) Results ---
   age     width_bins
0   58   (41.0, 61.0]
1   36  (20.92, 41.0]
2   55   (41.0, 61.0]
3   39  (20.92, 41.0]
4   71   (61.0, 81.0]
5   34  (20.92, 41.0]
6   75   (61.0, 81.0]
7   54   (41.0, 61.0]
8   53   (41.0, 61.0]
9   70   (61.0, 81.0]

Counts per bin:
width_bins
(20.92, 41.0]    590350
(41.0, 61.0]     753336
(61.0, 81.0]     375194
(81.0, 101.0]    133514
Name: count, dtype: int64

--- 2. Equal-Frequency Binning (Quantile) Results ---
      amt        freq_bins
0    2.86    (0.999, 9.64]
1   29.84    (9.64, 47.45]
2   41.28    (9.64, 47.45]
3   60.05    (47.45, 83.1]
4    3.19    (0.999, 9.64]
5   19.55    (9.64, 47.45]
6  133.93  (83.1, 28948.9]
7   10.37    (9.64, 47.45]
8    4.37    (0.999, 9.64]
9   66.54    (47.45, 83.1]

Counts per bin:
freq_bins
(0.999, 9.64]      463113
(9.64, 47.45]      463170
(47.45, 83.1]      463117
(83.1, 28948.9]    462994
Name: count, dtype: int64

--- 3. Custom Label Binning Results ---
   age custom_bins
0   58       Adult
1   36       Adult
2   55       Adult
3   39       Adult
4   71      Senior
5   34       Adult
6   75      Senior
7   54       Adult
8   53       Adult
9   70      Senior

Counts per bin:
custom_bins
Child           0
Teen            0
Adult     1321701
Senior     529947
Name: count, dtype: int64

💾 Execution complete! Combined and binned dataset saved to: /content/final_processed_dataset.csv###

