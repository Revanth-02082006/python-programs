import datetime

tasks = []
while True:
    task = input("Enter a task (or type 'exit' to stop): ")
    if task.lower() == "exit":
        break
    tasks.append({"task": task, "time": datetime.datetime.now()})

print("Your tasks:")
for t in tasks:
    print(f"- {t['task']} (Added on {t['time'].strftime('%Y-%m-%d %H:%M')})")
