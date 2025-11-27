import platform

if platform.system() == 'Windows':
  print("Your on windows use batch files")
else:
  print("Your on a UNIX system use .sh files")