import subprocess
import os
import sys

def main():
    tasks_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(os.listdir(tasks_dir))
    
    print("==================================================")
    print("     RUNNING ALL INDIVIDUAL ASSIGNMENT TASKS      ")
    print("==================================================")
    
    passed_count = 0
    total_count = 0
    
    for file in files:
        if file.startswith("task_") and file.endswith(".py"):
            total_count += 1
            file_path = os.path.join(tasks_dir, file)
            print(f"\n---> Running {file}...")
            
            result = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(result.stdout.strip())
                passed_count += 1
            else:
                print(f"FAILED (Exit Code: {result.returncode})")
                print("Error Output:")
                print(result.stderr.strip())
                
    print("\n==================================================")
    print(f"Execution Completed: {passed_count}/{total_count} tasks ran successfully.")
    print("==================================================")

if __name__ == "__main__":
    main()
