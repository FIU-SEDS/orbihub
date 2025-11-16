import subprocess

"""for subprocess
--- for subprocess.run([], stdout, stderr) --- 
When you run a command, it can output to two different streams:
stdout (standard output) = Normal output

Success messages
Regular program output
Example: git --version outputs "git version 2.39.0"

stderr (standard error) = Error messages
Error messages
Warnings
Diagnostic info
"""

def check_command_installed(command : str) -> bool:
  try:
    subprocess.run([command, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True) # DEVNULL makes it not print out just makes it return the bool value 
    return True
  except:
    print(f"{command} not installed")
    return False

def check_python_installed() -> bool:
  return check_command_installed("git")

def check_git_installed() -> bool:
  return check_command_installed("git")

# print("python", check_python_installed())
# print("git", check_git_installed())