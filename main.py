from pathlib import Path

import matplotlib.pyplot as plt

from src.preprocess import load_data, load_project_data, preprocess_queries
from src.suggest import get_suggestions, prefix_match_suggestions


DATA_PATH = Path("data/search_data.csv")


def print_analysis(df):
    print("\nTop 10 Most Popular Queries")
    print(df.sort_values("popularity_score", ascending=False).head(10)[["query", "popularity_score"]])

    print("\nTop 10 Longest Queries")
    print(df.sort_values("query_length", ascending=False).head(10)[["query", "query_length"]])

    print("\nTop 10 Highest CTR Queries")
    print(df.sort_values("ctr", ascending=False).head(10)[["query", "ctr"]])


def plot_top_queries(df):
    top_queries = df.sort_values("popularity_score", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_queries["query"], top_queries["popularity_score"])
    plt.xlabel("Popularity Score")
    plt.ylabel("Query")
    plt.title("Top 10 Most Popular Queries")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def run_console(grouped_df):
    print("\nArama onerisi konsoluna hos geldiniz.")
    print("Cikmak icin 'q' yazin.")

    while True:
        text = input("\nArama yap: ").strip()
        if text.lower() == "q":
            break

        results = get_suggestions(text, grouped_df, top_n=5)
        if results.empty:
            print("Oneri bulunamadi.")
        else:
            print("Oneriler:")
            for _, row in results.iterrows():
                print("-", row["query"])


def main():
    if DATA_PATH.exists():
        raw_df = load_data(str(DATA_PATH))
        print("Loaded dataset from data/search_data.csv")
    else:
        raw_df = load_project_data("data")
        print("Loaded and normalized dataset from data/raw/*.csv")

    print(raw_df.head())
    print(raw_df.columns)
    print(raw_df.shape)

    grouped_df = preprocess_queries(raw_df)
    print_analysis(grouped_df)

    print("\nPrefix test for 'py':")
    print(prefix_match_suggestions("py", grouped_df))

    print("\nHybrid suggestion test for 'pyth':")
    print(get_suggestions("pyth", grouped_df))

    plot_top_queries(grouped_df)
    run_console(grouped_df)


if __name__ == "__main__":
    main()
