def validate_time_format(time_str):
    try:
        # Split the time string into hours, minutes, and seconds
        hours, minutes, seconds = map(int, time_str.split(':'))

        # Check if the values are within valid ranges
        if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
            return True
        else:
            return False
    except ValueError:
        return False


def convert_time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def calculate_statistics(times):
    # Calculate best time, worst time, and average time
    best_time = min(times)
    worst_time = max(times)
    average_time = sum(times) / len(times)

    return best_time, worst_time, average_time


def print_results(best_time, worst_time, average_time):
    print("Best Time:", format_time(best_time))
    print("Worst Time:", format_time(worst_time))
    print("Average Time:", format_time(average_time))


def format_time(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def main():
    # Get the number of runners (N)
    n = int(input("Enter the number of runners (N): "))

    # Collect times for N runners
    times = []
    for i in range(n):
        while True:
            try:
                time_str = input(f"Enter time for runner {i + 1} (format: SS:MM:HH): ")
                if validate_time_format(time_str):
                    times.append(convert_time_to_seconds(time_str))
                    break
                else:
                    print("Invalid time format. Please enter valid time.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # Calculate statistics
    best_time, worst_time, average_time = calculate_statistics(times)

    # Print the results
    print_results(best_time, worst_time, average_time)


if __name__ == "__main__":
    main()
