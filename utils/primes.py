import subprocess

from utils.basic_algorithms.gcdext import gcdext


def generate_prime(bits=1024):
    result = subprocess.run(["openssl", "prime", "-generate", "-bits", str(bits)],
                            capture_output=True, timeout=5, check=True)

    return int(result.stdout)


def generate_e_d(number):
    for e in range(7, number):
        if gcdext(e, number)[0] == 1:
            _, d, _ = gcdext(e, number)
            while d < 0:
                d += number

            return e, d
