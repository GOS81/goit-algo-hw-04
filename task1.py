from pathlib import Path
import argparse
import shutil


def parse_args():
    parser = argparse.ArgumentParser(
        description="Копіювання файлів з сортуванням за розширеннями."
    )
    parser.add_argument(
        "--source", type=Path, required=True, help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення"
    )
    return parser.parse_args()


def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                for child in item.iterdir():
                    copy_files(child, dst)
            else:
                ext_folder = dst / (item.suffix.lstrip(".") or "no_ext")
                ext_folder.mkdir(parents=True, exist_ok=True)

                # копіюємо файл
                shutil.copy(item, ext_folder / item.name)
                print(f"Скопійовано: {item} → {ext_folder / item.name}")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")


def main():
    args = parse_args()
    print(args.source, args.dest)
    args.dest.mkdir(
        parents=True, exist_ok=True
    )  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)


if __name__ == "__main__":
    main()
