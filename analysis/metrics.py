def movies_per_year(df):
  return df["release_year"].value_counts().sort_index()

def longest_and_shortest(df):
  longest = df.loc[df["duration"].idxmax(), ["title", "duration"]]
  shortest = df.loc[df["duration"].idxmin(), ["title", "duration"]]
  return longest, shortest

def top_directors