#!/usr/bin/python3

import socket
import re

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Replace the server address and port
    client.connect(('<server>', <port>))

    none_count = 0  # Counter for consecutive occurrences of "None"

    while True:
        data = b''
        while True:
            chunk = client.recv(4096)
            data += chunk
            if len(chunk) < 4096:
                breakse

        # Print the received data for debugging
        print("Received data:", data.decode('utf-8'))

        # \d+ matches a digit (equal to [0-9])
        # .{3} matches any character, except line terminators exactly three times
        m = re.search('\d+.{3}\d+', data.decode('utf-8'))

        # Check if the search was successful
        if m:
            expression = m.group(0)

            result = eval(expression)

            # Print results to screen to see script progress
            print(expression + ' = ' + str(result))

            # Encode and transfer
            data = str(result).encode('utf-8') + b'\n'
            client.send(data)

            # Reset none_count if a successful expression is found
            none_count = 0
        else:
            print("Error: No matching expression found in the received data.")
            none_count += 1

            if none_count >= 3:
                print("Terminating the program as 'None' repeated at least three times.")
                break  # Terminate the program

# Note: The script will run indefinitely until manually stopped.
