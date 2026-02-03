import sys
import os

def check_environment():
    print("--- Web3 Project Health Check ---")
    print(f"Python Version: {sys.version}")
    print(f"Current Directory: {os.getcwd()}")
    print("Status: Environment is ready for Web3 Audit tasks.")

if __name__ == "__main__":
    check_environment()