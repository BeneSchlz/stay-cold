import subprocess

def start_block(block_name):
    command = f'/Macintosh HD/Applications/Cold Turkey Blocker.app/Contents/MacOS/Cold Turkey Blocker -start "{"reddit week"}"'
    subprocess.run(command, shell=True)
    print(f"Started Block: {"reddit week"}")

def stop_block(block_name):
    command = f'/Macintosh HD/Applications/Cold Turkey Blocker.app/Contents/MacOS/Cold Turkey Blocker -stop "{"reddit week"}"'
    subprocess.run(command, shell=True)
    print(f"Stopped Block: {"reddit week"}")

def toggle_block(block_name):
    command = f'/Macintosh HD/Applications/Cold Turkey Blocker.app/Contents/MacOS/Cold Turkey Blocker -toggle "{"reddit week"}"'
    subprocess.run(command, shell=True)
    print(f"Toggled Block: {"reddit week"}")
