import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv("adult.data.csv")

    df.columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ]

    df = df.replace("?", pd.NA).dropna()

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (df[~higher_education]['salary'] == '>50K').mean() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    rich_percentage = round(
        (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0]
         / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100, 1
    )

    country_total = df['native-country'].value_counts()
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_earning / country_total * 100).idxmax()
    highest_earning_country_percentage = round(
        (country_earning / country_total * 100).max(), 1
    )

    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    if len(india_rich) > 0:
        top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    else:
        top_IN_occupation = None

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degrees:", percentage_bachelors)
        print("Percentage with higher education earning >50K:", higher_education_rich)
        print("Percentage without higher education earning >50K:", lower_education_rich)
        print("Minimum work hours per week:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
