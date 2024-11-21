import subprocess

def start_block(block_name):
    """
    Attempts to start a Cold Turkey block with the specified block name.
    Handles cases where the block is already active or other errors occur.

    Args:
        block_name (str): The name of the block to start.
    """
    try:
        # Command to start the block
        command = [
            "/Applications/Cold Turkey Blocker.app/Contents/MacOS/Cold Turkey Blocker",
            "-start",
            block_name
        ]
        # Run the command
        subprocess.run(command, check=True, text=True, capture_output=True)
        print(f"Block '{block_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        # Handle known errors
        if "already active" in e.stderr.lower():  # Adjust based on the actual error message
            print(f"The block '{block_name}' is already active. No further action is needed.")
        else:
            print(f"Failed to start the block '{block_name}': {e.stderr.strip()}")
    except FileNotFoundError:
        # Handle missing executable
        print("Cold Turkey Blocker executable not found. Please check the path.")
    except Exception as e:
        # Catch-all for any unexpected errors
        print(f"An unexpected error occurred while starting the block '{block_name}': {e}")


if __name__ == "__main__":
    # List of blocks to start
    blocks = ["yt", "reddit week"]
    
    for block in blocks:
        start_block(block)