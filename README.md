# Credit_Card_Fraud
The convenience of credit card payments also comes with the risk of credit card fraud, as anyone with access to the card can use it without requiring a password. To address this issue, machine learning techniques have been employed, specifically using deep neural networks and the payments catalog as parameters. Through a practical implementation of this method, credit card fraud detection has been shown to be efficient and effective.

## Source Data
The table presented above displays a summary of the dataset, variables V1 to V28 pertain to encoded payment information, such as the location, item, and dealer details. The data is encoded to protect the privacy of the individuals involved. The 'Amount' variable represents the payment amount. The 'Class' variable, which is the most significant among the other variables, indicates whether the payment is classified as fraudulent or not.

It should be noted that the table presented only represents a fraction of the total dataset, which comprises 284,808 transactions. Such a large dataset is adequate in eliminating the effects of outliers.

<img width="1646" alt="截屏2023-03-29 17 11 56" src="https://user-images.githubusercontent.com/105031962/228668634-fb5e6816-e48a-4068-889a-a29f8f1aa7b5.png">

## Algorithm 
Logistic regression was employed as the technique in our program. The approach involved the segregation of data into two distinct regions of a coordinate system, and derivation of a regression line, represented by a machine learning generated function. Upon attainment of a relatively stable regression line, the latter was utilized as a criterion to differentiate fraudulent data.


