import pandas as pd
import boto3

s3 = boto3.resource('s3')

# get data from s3
data_endpoint = "https://s3.amazonaws.com/galvanize-denver-platte/cancer.csv"
df = pd.read_csv(data_endpoint)

# compute something on your ec2 instance
df['cancer_rates'] = df.cancer/df.population
df.to_csv('data/cancer_rates.csv')

# write results back to s3
with open('data/cancer_rates.csv', 'rb') as data:
    s3.Bucket('galvanize-denver-platte').put_object(Key='cancer_rates.csv',
                                                    Body=data)
