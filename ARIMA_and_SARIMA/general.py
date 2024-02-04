from modules import *
from ARIMA_model import *
from SARIMA_model import *
# Test for staionarity


def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()
    # Plot rolling statistics:
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(block=False)
    print("Results of dickey fuller test")
    adft = adfuller(timeseries, autolag='AIC')
    # output for dft will give us without defining what the values are.
    # hence we manually write what values does it explains using a for loop
    output = pd.Series(adft[0:4], index=[
                       'Test Statistics', 'p-value', 'No. of lags used', 'Number of observations used'])
    for key, values in adft[4].items():
        output['critical value (%s)' % key] = values
    print(output)


# Import csv data
stock_data = pd.read_csv(
    'C:/Users/rijul/OneDrive/Documents/Sem 5/MI/Project/Crypto_Price_Predictor-master/Crypto_Price_Predictor-master/Kaggle Datasets/coin_Ethereum.csv')
stock_data['Date'] = pd.to_datetime(stock_data['Date'])


# plot close price
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Close Prices')
plt.plot(stock_data['Close'])
plt.title('Ethereum closing price')
plt.show()


# Distribution of the dataset
df_close = stock_data['Close']
df_close.plot(kind='kde')


test_stationarity(df_close)

# To separate the trend and the seasonality from a time series,
# we can decompose the series using the following code.
result = seasonal_decompose(df_close, model='multiplicative', period=30)

fig = plt.figure()
fig = result.plot()
fig.set_size_inches(16, 9)

# if not stationary then eliminate trend
# Eliminate trend
rcParams['figure.figsize'] = 10, 6

df_log = np.log(df_close)
moving_avg = df_log.rolling(12).mean()
std_dev = df_log.rolling(12).std()


plt.legend(loc='best')
plt.title('Moving Average')
plt.plot(std_dev, color="black", label="Standard Deviation")
plt.plot(moving_avg, color="red", label="Mean")

plt.show()

# -------- ARIMA analysis --------
print("Arima predictions:")
train_data, test_data = stock_data[0:int(
    len(stock_data)*0.7)], stock_data[int(len(stock_data)*0.7):]
model_predictions = ARIMA_model_fit(train_data=train_data, test_data=test_data)
print("Press enter to continue...")
input()

# test_set_range = stock_data[int(len(stock_data)*0.7):].index
# plt.plot(test_set_range, model_predictions, color='blue',
#          marker='o', linestyle='dashed', label='Predicted Price')
# plt.plot(test_set_range, test_data, color='red', label='Actual Price')
# plt.title('TESLA Prices Prediction')
# plt.xlabel('Date')
# plt.ylabel('Prices')
# plt.xticks(np.arange(881, 1259, 50), stock_data.Date[881:1259:50])
# plt.show()

# -------- SARIMA analysis --------
model_predictions = SARIMA_model_fit(
    train_data=train_data, test_data=test_data)

# test_set_range = stock_data[int(len(stock_data)*0.7):].index
# plt.plot(test_set_range, model_predictions, color='blue',
#          marker='o', linestyle='dashed', label='Predicted Price')
# plt.plot(test_set_range, test_data, color='red', label='Actual Price')
# plt.title('Ethereum Prices Prediction')
# plt.xlabel('Date')
# plt.ylabel('Prices')
# plt.xticks(np.arange(881, 1259, 50), stock_data.Date[881:1259:50])

# plt.show()
