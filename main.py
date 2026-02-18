import os
import shutil

source_dir = r"C:\Users\dkoom\Desktop\Basic-File-Mover"

dest_dirs = {
    ".jpg": os.path.join(source_dir, "Pictures"),
    ".png": os.path.join(source_dir, "Pictures"),

    ".pdf": os.path.join(source_dir, "Document", "PDF"),
    ".docx": os.path.join(source_dir, "Document", "Word"),
    ".xlsx": os.path.join(source_dir, "Document", "Excel"),
    ".csv": os.path.join(source_dir, "Document", "Excel"),
    ".mp4": os.path.join(source_dir, "Video"),
}
#--------------------------------------------------------

def move_files():

    if not os.path.exists(source_dir):
        print(f"❌ No Folder {source_dir}")
        return

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isdir(file_path):
            continue

        if filename == "main.py":
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in dest_dirs:
            target_dir = dest_dirs[file_ext]

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            try:
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"✅ Moved {filename} to {os.path.basename(target_dir)}")
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

if __name__ == "__main__":
    print("Starting to organize files...")
    move_files()
    print("✨ Work completed!")
