import hashlib
import zipfile

zip_file_path = "C:/Users/Hubert Siluk/Desktop/intern-data/file-to-tasks/task2.zip"
user_email = "hubertsiluk@gmail.com"
EXPECTED_FILE_COUNT = 256

def calculate_sorting_key(hash_string):
    product = 1
    for char in hash_string:
        val = int(char, 16) + 1
        product *= val
    return product

def solve_task():
    hashes_list = []
    file_count = 0

    try:
        print("Starting processing...")

        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            file_list = zf.namelist()

            for file_name in file_list:
                if file_name.endswith('/'):
                    continue
                if "__MACOSX" in file_name or ".DS_Store" in file_name:
                    continue

                sha3_hasher = hashlib.sha3_256()

                with zf.open(file_name) as zipped_file:
                    while chunk := zipped_file.read(4096):
                        sha3_hasher.update(chunk)

                hashes_list.append(sha3_hasher.hexdigest())
                file_count += 1

        print(f"Files processed: {file_count}")
        if file_count != EXPECTED_FILE_COUNT:
            print(f"⚠️ WARNING! Required {EXPECTED_FILE_COUNT}, but found {file_count}.")
            print("The result might be incorrect. Check archive content.")
        else:
            print("✅ File count matches (256).")

        sorted_hashes = sorted(hashes_list, key=calculate_sorting_key)

        concatenated_hashes = "".join(sorted_hashes)

        string_with_email = concatenated_hashes + user_email.lower()

        final_hasher = hashlib.sha3_256()
        final_hasher.update(string_with_email.encode('utf-8'))

        result = final_hasher.hexdigest()

        print("FINAL SHA3-256 RESULT:")
        print(result)

    except FileNotFoundError:
        print(f"Error: ZIP file not found at path: {zip_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    solve_task()
