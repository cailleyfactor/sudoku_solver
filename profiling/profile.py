import pstats

# Load the profiling data from the file
p = pstats.Stats("profile_output.prof")

# Sort the data by total time spent and print the top functions
p.sort_stats("cumulative").print_stats(10)
