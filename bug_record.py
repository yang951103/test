# 1.while导致的无限循环
delta = timedelta(days=group.maintain_day)
maintain_time = group.year_first_maintain_time
end_maintain_time = group.end_maintain_time
exec_dates = []
while maintain_time < end_maintain_time:
    exec_dates.append(maintain_time)
    maintain_time += delta