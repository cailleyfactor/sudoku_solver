import pstats

# Load the profiling data from the file
p = pstats.Stats("output.prof")

# Sort the data by total time spent and print the top functions
p.sort_stats("time").print_stats(10)
