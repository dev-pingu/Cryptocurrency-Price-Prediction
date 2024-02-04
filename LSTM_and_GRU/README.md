# **GRU/LSTM model implementation**

One of the major factors affecting vanilla RNNs right now would be that They arent able to store data for a long time and this leads to problems like vanishing or exploding gradient based on the weights we assign. For example if we take a sudden positive influx in data for a normal RNN then the weights are immediatly shifted to higher values without other consideration. Similarly if there is a drop then the weights are minimized immediately without any otehr consideration.

To combat this we use LSTMs(Long Short Term Memory). LSTMs have a gate based system which controls the inflow of data. Hence instead of having massive changes coming in from new data(like in RNNs) there is a smaller change occuring for ever instance of new data.

LSTMs have 3 gates, input gate, output gate and forget gate. Input gate and Output gate just path the input and output and the forget gate decides which data is kept and which is forgetten(removed/not considered).
While this works best with time series data, LSTMs are very computationally intensive. This means they take a lot more time to train and retrain(Incase of error).

GRU(Gated Recurrent Unit) combines the operations of memory updating and memory forgetting into a single operation, thereby reducing the computational cost.
