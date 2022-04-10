import pandas as pd


def pd_version():
    print('version:', pd.__version__, ']n')


def print_df(df):
    print('this is a data frame:\n', df)


def print_series(df, name):
    print(df[name])


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

print_series(df, "Age")
