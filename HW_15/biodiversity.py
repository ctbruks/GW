import pandas as pd 

def fetch_data():

    csv_path = "DataSets/Belly_Button_Biodiversity_Metadata.csv"
    subject_df = pd.read_csv(csv_path)
    subject_df = subject_df.loc[:,["SAMPLEID", "AGE","ETHNICITY", "GENDER", "BBTYPE", "LOCATION"]]

    subject_df = subject_df.dropna(how="any")
    subject_df.head()

    for i in subject_df.SAMPLEID:
        subject_df["SAMPLEID"].replace(i, "BB_"+ str(i), inplace=True)
        
    subjects = subject_df.to_dict('records')

    path = "DataSets/belly_button_biodiversity_samples.csv"
    sample_df = pd.read_csv(path)
    desc_path = "DataSets/belly_button_biodiversity_otu_id.csv"
    desc_df = pd.read_csv(desc_path)
    new_df = pd.merge(sample_df, desc_df, on='otu_id')

    return subject_df, subjects, sample_df, desc_df, new_df

