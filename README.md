### **To earn maximum profit by finding the best stock price to buy and sell**
#### **Problem**<br />

To write a program that will examine this data to pick the best time and price to buy and the best time and price to sell in order to earn the maximum profit.

#### **Solution**<br />
- Dynamic Programming is used to solve the problem of earning maximum profit. The pseudo code for the program is as follows:<br />
><i>Let profit = 0 <br />
Let min = arr[0] <br />
For k = 1 to length(arr):<br />
 If arr[k] < min, set min = arr[k]<br />
If profit < arr[k] - min, set profit = arr[k] - min<br /></i>

The beauty of this algorithm is it uses only O(n) time and O(1) memory. Also, the structure of the `main.py` script takes care of multiple stock prices data.

- The problem was assumed to have a single pass solution, ie, the trader could buy and sell stocks only once in a given day. In real life situations, there could be other possible variations like:
    * engaging in at most k number of transactions with and without Cooldown.
    * having a penalty cost (transaction fee) associated with every stock that is bought apart from the price of the stock.

#### **Project structure Overview**<br />

- [main.py](main.py): This is the main python script used to run the program.
- [maxprofit.py](maxprofit.py): This file contains a class called MaxProfit which contains the main algorithm to evaluate maximum profit from given data.
- [test.py](test.py): The test python script performs tests on the possible variations of input data.
unittest has been used to perform these tests. `unittest` has been used to perform the tests.
- [Stocks.csv](Stocks.csv): The file contains the input data in CSV format.


#### **Requirements**<br />
- Python 3.7 was used to solve the problem. The version can be checked by entering the following in the command line: <br />
`python --version` <br />
- Pandas: can be installed by the following command line: <br /> 
`pip install pandas`

#### **Running the code**<br />
To run the program:<br />
`python main.py enter-file-name.csv`

For example, the file used for this problem is Stocks.csv. The following command is used to run the program on Stocks.csv. <br />
`python main.py Stocks.csv`

#### **Running the tests**<br />
To run the tests:<br />
`python test.py`






