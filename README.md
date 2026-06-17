#### **Brute-shield**

Brute-shield is a python based brute force attack detector that prevents too many requests being made by any one user.



#### **What it does**

Brute-shield detects and prevents brute force attacks, where a user with malicious intent, makes many requests in a given time frame to guess a password or to execute any other brute force attack.



#### **How it works**

Brute-shield keeps a record of each user's requests. Within a set time period--usually a minute--the user can only make limited number for requests--usually five requests. The user is only allowed to make a request given that they have not already crossed the limit on number of requests in the current time frame.

However, users are not permanently locked out, as they are only blocked for five minutes after being detected for too many requests.



#### **Current features**

&#x20;1) Local storage -> All the data is stored in the memory of the system which the program is running on.

&#x20;2) Multiple users -> Brute-shield-v1 can handle requests from multiple users.

&#x20;3) Detection log -> Any time a user exceeds the limit on requests per minute, a log is entered of that user and stored in log.txt


#### **How to run**

git clone https://github.com/0x00-byte/brute-shield
cd brute-shield
python main.py

### **What is next ?**

Brute-shield-V2 will support persistant logging and tracking of various users using a local database, instead of relying on text files or program memory. 
So unlike V1, V2 will retain log data accross sessions-- meaning all the recorded data will survive restarts.
