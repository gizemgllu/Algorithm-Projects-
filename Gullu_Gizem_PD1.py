
# Gullu Gizem 230ADB075

# In this code, to be able to process/handle files that Professor upload, they need to be put in same project, there are file handling functions
#This code below has been written by me mostly.
#Some part when i need help, used other resouces.
# Links for resources:
# https://www.geeksforgeeks.org/fundamentals-of-algorithms/
# https://www.w3schools.com
# https://chatgpt.com


"time complexity is O(n)"
def linear_approach(numbers):
    if len(numbers) < 2:
        return 0

    latest_min = numbers[0]
    biggest_increase = 0

    # for loop for finding potential increase among each numbers
    for num in numbers[1:]:
        # starts from second element
        increase = num - latest_min

        biggest_increase = max(biggest_increase, increase)  # if bigger increase found

        latest_min = min(latest_min, num)  # if smaller number found

    return biggest_increase

"time complexity is O(n^2)"
def brute_force_approach(numbers):

    if len(numbers) < 2: # sshould be higher than 2
        return 0
        
    biggest_increase = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            increase_amount = numbers[j] - numbers[i]
            biggest_increase = max(biggest_increase, increase_amount)
    
    return biggest_increase


def process_file(filename): # File handling for professors zip
    """
    To be able to search/process integer txt files
    """
    try:
        with open(filename, 'r') as file:

            numbers = [int(line.strip()) for line in file if line.strip()]  # converts integer
            
        return numbers, len(numbers)

        # if some exceptions are found in the file it returns below
    except FileNotFoundError:
        print(f"Error: '{filename}' doesnt exist!")
        return None, 0
    except ValueError:
        print(f"Error: Invalid data!")
        return None, 0
    except Exception as e:
        print(f"Error:: {str(e)}")
        return None, 0

# this function can handle large files better than prev.
def most_efficient_file_process(filename):
    """
    this function hansles large amount of numbers like 10K, 100M etc.
    """
    try:
        count = 0
        latest_min = None
        biggest_increase = 0
        
        with open(filename, 'r') as file:  # r measn its on read mode not write
            # first numb
            for line in file:
                if line.strip():
                    latest_min = int(line.strip())
                    count = 1
                    break
            
            #  other numbers
            for line in file:
                if line.strip():
                    num = int(line.strip())
                    count += 1
                    
                    # updating
                    increase = num - latest_min
                    biggest_increase = max(biggest_increase, increase)
                    latest_min = min(latest_min, num)
        
        return biggest_increase, count
        
    except FileNotFoundError:
        print(f"Error: '{filename}' doesnt exist!")
        return None, 0
    except ValueError:
        print(f"Error: Invalid data!")
        return None, 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0

"Time complexity: O(n), Space complexity: O(1)"
def find_biggest_increase_streaming(filename):

    try:
        latest_min = float('inf')
        biggest_increase = 0
        c = 0
        "counter"

        "r means on read mode not write"
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    try:
                        num = int(line.strip())
                        c += 1
                        
                        # searches for biggest inc.
                        if latest_min != float('inf'):
                            increase = num - latest_min
                            biggest_increase = max(biggest_increase, increase)

                        # updates min
                        latest_min = min(latest_min, num)
                        
                    except ValueError:
                        print(f"Invalid number!")
                        continue
        
        if c < 2:
            return 0, c
            
        return biggest_increase, c
        
    except FileNotFoundError:
        print(f"Error: '{filename}' doesnt exist!")
        return None, 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0

"human readable format, cant be seen as normal version."
def format_file_size(size_in_bytes):

    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.1f}{unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.1f}GB"

"adds commas"
def format_number(n):

    return f"{n:,}"

def main():
    import os
    import time
    from glob import glob
    
    # includes txt files - dictionary
    data_dir = "pd1_data"
    
    # sorts according to their sizes
    files = []
    for filepath in glob(os.path.join(data_dir, "*.txt")):
        size = os.path.getsize(filepath)
        files.append((size, filepath))
    
    files.sort() # sorts by size
    

    print("*" * 100)
    print(f"{'Filename':<15} {'Size':>10} {'Elements':>12} {'Max Increase':>15} {'Time (s)':>10}")
    print("*" * 100)
    
    total_time = time.time()

    # streaming approach has been used
    for size, filepath in files:
        filename = os.path.basename(filepath)

        start_time = time.time()
        result, count = find_biggest_increase_streaming(filepath)
        process_time = time.time() - start_time
        
        if result is not None:
            print(f"{filename:<15} {format_file_size(size):>10} {format_number(count):>12} {format_number(result):>15} {process_time:>10.3f}")
    
    total_time = time.time() - total_time
    print("*" * 100)
    print(f"Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main() 