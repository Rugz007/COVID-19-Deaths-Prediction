import pandas as pd

def vaccines(desired_date):
    """Sample one date from the source dataset and write it to an intermediate file
    Parameters:
        desired_date: str, date to be sampled for vaccine completedness
    """
    input_filename = "./data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
    df = pd.read_csv(input_filename, compression="gzip", converters={'FIPS' : str})
    print("START:", df.shape, desired_date)
    

    # Filter by date
    desired_date = desired_date.replace("-", "/")
    df = df[df["Date"] == desired_date]

    # Output
    output_filename = "./data/CDC/vaccinations-" + desired_date[:2] + '-' + \
                    desired_date[3:5] + "-" + desired_date[6:11] + ".csv"

    # Write filtered dataframe to a file
    df.to_csv(output_filename, index=False)
    return df

def create_vaccines():
    """This function generates vaccination data for seven different dates.
    """
    dates = [
    "05-31-2021",
    "06-30-2021",
    "07-31-2021",
    "08-31-2021",
    "09-30-2021",
    "10-31-2021",
    "11-30-2021",
    "12-31-2021",
    "01-31-2022",
    "02-28-2022",
    "03-31-2022",
    "04-30-2022",
    "05-31-2022",
    "06-29-2022",
    "07-27-2022",
    "08-31-2022",
    "09-28-2022",
]

    for date in dates:
        vaccines(date)

if __name__ == "__main__":
    create_vaccines()
