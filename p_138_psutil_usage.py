# psutil.cpu_times()
# CPU時間を求める。システム全体のユーザー、システム、およびアイドルの時間を返します。
# psutil.cpu_times()
# Retrieves CPU times. Returns user, system, and idle times for the entire system.

# psutil.cpu_times_percent()
# 特定のCPU時間ごとの使用率を求める。指定された間隔でCPU時間の使用率を返します。
# psutil.cpu_times_percent()
# Retrieves CPU times percentage. Returns the percentage utilization of CPU times for a specified interval.

# psutil.virtual_memory()
# メモリの使用率に関する統計情報を求める。使用可能なメモリ、使用済みメモリ、使用率などの統計情報を返します。
# psutil.virtual_memory()
# Retrieves memory usage statistics. Returns statistics like available memory, used memory, and usage percentage.

# psutil.disk_partitions()
# マウントしているディスクパーティション情報を取得する。システム上のディスクパーティションとそのマウントポイントを返します。
# psutil.disk_partitions()
# Retrieves mounted disk partitions information. Returns the disk partitions on the system and their mount points.

# psutil.net_io_counters()
# ネットワークI/Oに関する統計情報を求める。送信および受信バイト数、パケット数などの統計情報を返します。
# psutil.net_io_counters()
# Retrieves network I/O statistics. Returns statistics like bytes sent and received, and packets sent and received.

import psutil

# Example: Library Management System

# Retrieve CPU times
cpu_times = psutil.cpu_times()
print(
    f"User time: {cpu_times.user}, System time: {cpu_times.system}, Idle time: {cpu_times.idle}"
)

# Retrieve CPU times percentage over 1 second interval
for i in range(3):
    cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
    print(f"CPU times percentage (interval {i+1}): {cpu_times_percent}")

# Retrieve virtual memory statistics
virtual_memory = psutil.virtual_memory()
print(
    f"Total memory: {virtual_memory.total}, Available memory: {virtual_memory.available}, "
    f"Memory usage: {virtual_memory.percent}%"
)

# Retrieve disk partitions information
disk_partitions = psutil.disk_partitions()
for partition in disk_partitions:
    print(
        f"Device: {partition.device}, Mount point: {partition.mountpoint}, File system type: {partition.fstype}"
    )

# Retrieve network I/O statistics
net_io_counters = psutil.net_io_counters()
print(
    f"Bytes sent: {net_io_counters.bytes_sent}, Bytes received: {net_io_counters.bytes_recv}, "
    f"Packets sent: {net_io_counters.packets_sent}, Packets received: {net_io_counters.packets_recv}"
)
