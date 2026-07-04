import subprocess
import os
import sys

def main():
    tasks_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(os.listdir(tasks_dir))

    print("=" * 60)
    print("   RUNNING ALL PRACTICAL ASSIGNMENT 2 TASKS")
    print("=" * 60)

    passed = 0
    total  = 0

    for file in files:
        if file.startswith("task_") and file.endswith(".py"):
            total += 1
            path = os.path.join(tasks_dir, file)
            print(f"\n---> Running {file}...")
            result = subprocess.run([sys.executable, path], capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout.strip())
                passed += 1
            else:
                print(f"FAILED (Exit Code: {result.returncode})")
                print(result.stderr.strip())

    print("\n" + "=" * 60)
    print(f"Execution Completed: {passed}/{total} tasks ran successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
