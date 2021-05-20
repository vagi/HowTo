"""
Few plots can be built in one graph
from one dataframe/dataset Pandas
"""
import pandas as pd

history_df = pd.DataFrame(history.history)  # history.history is an inference received from trained DNN
history_df.loc[:, ['loss', 'val_loss']].plot(title='Cross-entropy Loss')
