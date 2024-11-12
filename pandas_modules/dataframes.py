import pandas as pd

class FrameXRC:
    def create_frame(self):
        df = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['A', 'B', 'C']
        })
        return df

    def sort_df(self):
        df = self.file_reader_helper()
        sorted_df = df.sort_values(by='Date').reset_index(drop=True)
        return sorted_df

    def file_reader_helper(self):
        return pd.read_csv("./data/financial_data.csv")

