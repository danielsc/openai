|Automobile price data (Raw)|Information about automobiles by make and model, including the price, features such as the number of cylinders and MPG, as well as an insurance risk score.<br/> The risk score is initially associated with auto price. It is then adjusted for actual risk in a process known to actuaries as symboling. A value of +3 indicates that the auto is risky, and a value of -3 that it is probably safe.<br/>**Usage**: Predict the risk score by features, using regression or multivariate classification.<br/>**Related Research**: Schlimmer, J.C. (1987). [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science. |
| CRM Appetency Labels Shared |Labels from the KDD Cup 2009 customer relationship prediction challenge ([orange_small_train_appetency.labels](http://www.sigkdd.org/site/2009/files/orange_small_train_appetency.labels)).|
|CRM Churn Labels Shared|Labels from the KDD Cup 2009 customer relationship prediction challenge ([orange_small_train_churn.labels](http://www.sigkdd.org/site/2009/files/orange_small_train_churn.labels)).|
|CRM Dataset Shared | This data comes from the KDD Cup 2009 customer relationship prediction challenge ([orange_small_train.data.zip](http://www.sigkdd.org/site/2009/files/orange_small_train.data.zip)). <br/>The dataset contains 50K customers from the French Telecom company Orange. Each customer has 230 anonymized features, 190 of which are numeric and 40 are categorical. The features are very sparse. |
|CRM Upselling Labels Shared|Labels from the KDD Cup 2009 customer relationship prediction challenge ([orange_large_train_upselling.labels](http://www.sigkdd.org/site/2009/files/orange_large_train_upselling.labels)|
|Flight Delays Data|Passenger flight on-time performance data taken from the TranStats data collection of the U.S. Department of Transportation ([On-Time](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)).<br/>The dataset covers the time period April-October 2013. Before uploading to the designer, the dataset was processed as follows: <br/>-    The dataset was filtered to cover only the 70 busiest airports in the continental US <br/>- Canceled flights were labeled as delayed by more than 15 minutes <br/>- Diverted flights were filtered out <br/>- The following columns were selected: Year, Month, DayofMonth, DayOfWeek, Carrier, OriginAirportID, DestAirportID, CRSDepTime, DepDelay, DepDel15, CRSArrTime, ArrDelay, ArrDel15, Canceled|
|German Credit Card UCI dataset|The UCI Statlog (German Credit Card) dataset ([Statlog+German+Credit+Data](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data))), using the german.data file.<br/>The dataset classifies people, described by a set of attributes, as low or high credit risks. Each example represents a person. There are 20 features, both numerical and categorical, and a binary label (the credit risk value). High credit risk entries have label = 2, low credit risk entries have label = 1. The cost of misclassifying a low risk example as high is 1, whereas the cost of misclassifying a high risk example as low is 5.|
|IMDB Movie Titles|The dataset contains information about movies that were rated in Twitter tweets: IMDB movie ID, movie name, genre, and production year. There are 17K movies in the dataset. The dataset was introduced in the paper "S. Dooms, T. De Pessemier and L. Martens. MovieTweetings: a Movie Rating Dataset Collected From Twitter. Workshop on Crowdsourcing and Human Computation for Recommender Systems, CrowdRec at RecSys 2013."|
|Movie Ratings|The dataset is an extended version of the Movie Tweetings dataset. The dataset has 170K ratings for movies, extracted from well-structured tweets on Twitter. Each instance represents a tweet and is a tuple: user ID, IMDB movie ID, rating, timestamp, number of favorites for this tweet, and number of retweets of this tweet. The dataset was made available by A. Said, S. Dooms, B. Loni and D. Tikk for Recommender Systems Challenge 2014.|