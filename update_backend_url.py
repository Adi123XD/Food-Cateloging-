import subprocess
import re
import threading
import queue
import time

# Function to read output from the subprocess
def read_output(process, output_queue):
    while True:
        output = process.stdout.readline().strip()
        if output:
            output_queue.put(output)
        if process.poll() is not None:
            break

# Start the subprocess without capturing output
process = subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://127.0.0.1:8000', '--protocol', 'http2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Queue to store output lines
output_queue = queue.Queue()

# Thread to read output
output_thread = threading.Thread(target=read_output, args=(process, output_queue))
output_thread.start()

# Wait for a few seconds for the server URL to appear
time.sleep(5)

# Read output from the queue
while True:
    try:
        output = output_queue.get_nowait()
        print(output)
        # Use regex to find the server URL
        match = re.search(r'https://\S+', output)
        if match:
            server_url = match.group(0)
            print("Server URL:", server_url)
            break  # Exit the loop once the server URL is found
    except queue.Empty:
        pass

# Wait for the output thread to finish
output_thread.join()

# Handle any remaining output after the process finishes
remaining_output = process.communicate()[0].strip()
if remaining_output:
    print(remaining_output)
