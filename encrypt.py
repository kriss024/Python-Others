from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

def format_mb(size_bytes: int) -> str:
    """Convert byte size to a human-readable megabyte string."""
    return f"{size_bytes / (1024 * 1024):.2f} MB"


def generate_and_save_key(key_path: Path) -> bytes:
    """Generate a Fernet key and save it to disk."""
    key = Fernet.generate_key()
    with key_path.open("wb") as key_file:
        key_file.write(key)
    return key


def encrypt_file(source_path: Path, dest_path: Path, key: bytes) -> None:
    """Encrypt a file using Fernet (includes built-in HMAC-SHA256 integrity)."""
    fernet = Fernet(key)
    original_data = source_path.read_bytes()
    print(f"Original size: {format_mb(len(original_data))}")

    encrypted_data = fernet.encrypt(original_data)
    dest_path.write_bytes(encrypted_data)
    print(f"Encrypted size: {format_mb(len(encrypted_data))}")


def decrypt_file(encrypted_path: Path, dest_path: Path, key: bytes) -> bool:
    """Decrypt a Fernet-encrypted file and verify its integrity."""
    fernet = Fernet(key)
    encrypted_data = encrypted_path.read_bytes()
    print(f"Encrypted file size: {format_mb(len(encrypted_data))}")

    try:
        # Automatically verifies HMAC-SHA256; raises InvalidToken if tampered/corrupted
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Decryption failed: Invalid key or corrupted/tampered file.")
        return False

    dest_path.write_bytes(decrypted_data)
    print(f"Decrypted size: {format_mb(len(decrypted_data))}")
    return True


if __name__ == "__main__":
    key_file = Path("key.txt")
    original_file = Path("Linux for Beginners.zip")
    encrypted_file = Path("Linux for Beginners.enc")
    decrypted_file = Path("Linux for Beginners enc.zip")

    # 1. Generate and load key
    generate_and_save_key(key_file)
    secret_key = key_file.read_bytes()

    # 2. Encrypt
    encrypt_file(original_file, encrypted_file, secret_key)

    # 3. Decrypt & verify integrity
    if decrypt_file(encrypted_file, decrypted_file, secret_key):
        print("File decrypted and integrity verified.")