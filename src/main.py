# main.py 
import pandas as pd 

def main():
    data_1 = pd.read_csv('./data/data_train.csv')
    data_2 = pd.read_csv('./data/mLabel_tweets.csv')

    # print("First 5 rows of data_1:")
    # print(data_1.head())

    # print("\nFirst 5 rows of data_2:")
    # print(data_2.head())    

    Tweets_data_1 = data_1[['Tweet']].rename(columns={'Tweet': 'tweet'})
    Tweets_data_2 = data_2[['tweet']]

    # print("First 5 rows of Tweets_data_1:")
    # print(Tweets_data_1.head())

    # print("\nFirst 5 rows of Tweets_data_2:")
    # print(Tweets_data_2.head())


    merged_tweets = pd.concat([Tweets_data_1, Tweets_data_2], ignore_index=True)
    merged_tweets = merged_tweets.sample(frac=1).reset_index(drop=True)

    print("First 5 rows of merged_tweets (randomly ordered):")
    print(merged_tweets.head())

if __name__ == '__main__':
    main()