
from src.task_manager import TaskManager
from src.security import sanitize_title


def main():
    manager = TaskManager()

    while True:
        print("\n=== SecureTask ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Selesaikan tugas")
        print("4. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            try:
                title = sanitize_title(input("Judul tugas: "))
                task = manager.add_task(title)
                print(f"Tugas berhasil ditambahkan: {task['title']}")
            except ValueError as error:
                print(f"Input tidak valid: {error}")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("Belum ada tugas.")
            else:
                for task in tasks:
                    status = "Selesai" if task["completed"] else "Belum selesai"
                    print(f"{task['id']}. {task['title']} - {status}")

        elif choice == "3":
            try:
                task_id = int(input("Masukkan ID tugas: "))
                if manager.complete_task(task_id):
                    print("Tugas berhasil diselesaikan.")
                else:
                    print("ID tugas tidak ditemukan.")
            except ValueError:
                print("ID harus berupa angka.")

        elif choice == "4":
            print("Terima kasih telah menggunakan SecureTask.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()

