df = pd.read_csv("/content/gdrive/My Drive/Coding/Colab Notebooks/twitter.csv")
number_of_entries = df.shape[0] - 5 # subtracted 5 to deal with index errors
tweets = []
for i in range(207000):
  random.seed()
  rand_row = random.randint(0, number_of_entries)
  tweet = str(df.at[rand_row,'text'])
  tweets.append(tweet)
tweets_set = set(tweets)

results = []

for tweet in tweets:
  pol_score = sia.polarity_scores(tweet)
  if pol_score['compound'] == 0.0:
      continue
  pol_score['text'] = tweet
  results.append(pol_score)

df = pd.DataFrame.from_records(results)
df['label'] = 0
df.loc[df['compound'] > 0.1, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

key_terms = ["bioweapon","antivax","china virus","wuhan virus", "microchip"]
clean_tweets = set() 
for tweet in tweets:  
  for key_term in key_terms: 
    if key_term in tweet: 
      if tweet[0] == "@":  
        tweet = ' '.join(tweet.split()[1:]) 
      clean_tweets.add(tweet)
# print(len(clean_tweets))
df.to_pickle("twitter.pkl") # change

