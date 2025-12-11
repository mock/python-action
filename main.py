import os
import sys

def main():
    try:
        name = os.getenv('INPUT_NAME', 'No name provided')
        print(f"Arg received: {name}")

        print("Workdir:")
        for filename in os.listdir('.'):
            print(filename)

        with open('name.txt', 'w') as file:
            file.write(f"processed-name={name}\n")

        with open(os.getenv('GITHUB_OUTPUT', '/dev/null'), 'a') as file:
            file.write(f"processed-name={name}\n")

    except Exception as e:
        print(f"::error::{e}")


if __name__ == "__main__":
    main()

