from check_times import measure_block_time
from load_data.load_primary_data import load_data as load_primary_data

with measure_block_time():
    load_primary_data()
