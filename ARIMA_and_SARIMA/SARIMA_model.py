from modules import *


def SARIMA_model_fit(train_data, test_data):
    training_data = train_data['Close'].values
    test_data = test_data['Close'].values
    history = [x for x in training_data]
    model_predictions = []
    N_test_observations = len(test_data)

    for time_point in range(N_test_observations):
        model = SARIMAX(history)
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        model_predictions.append(yhat)
        true_test_value = test_data[time_point]
        history.append(true_test_value)

    MSE_error = mean_squared_error(test_data, model_predictions)
    print('Testing Mean Squared Error is {}'.format(MSE_error))

    try:
        with open("Models/Sarima_"+str(int(math.sqrt(MSE_error)))+".pkl", 'wb') as f:
            pickle.dump(model, f)
    except Exception as e:
        print(e)

    return model_predictions
