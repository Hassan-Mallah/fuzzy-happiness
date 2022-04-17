import pandas as pd


def pd_version():
    print('version:', pd.__version__, '\n')


def print_df(df):
    print('this is a data frame:\n', df)


def get_series(df, name):
    return df[name]


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

s = get_series(df, "Age")

print(s.max())

# I’m interested in some basic statistics of the numerical data of my data table
print(df.describe())
