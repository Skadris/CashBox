import subprocess
import sys


def run_command(command):
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(e.cmd)}' failed with exit code {e.returncode}")
        print(e.stdout.decode('utf-8'))
        print(e.stderr.decode('utf-8'))
        sys.exit(1)


def main():
    print("Running llvm-cov...")

    # Run llvm-cov command here
    run_command(["cargo", "llvm-cov", "--report-dir=target/llvm-cov"])

    print("llvm-cov passed successfully.")


if __name__ == "__main__":
    main()
