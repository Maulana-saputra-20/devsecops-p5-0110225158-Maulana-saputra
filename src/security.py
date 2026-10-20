
def sanitize_title(title):
    if not isinstance(title, str):
        raise ValueError("Judul harus berupa teks")

    title = title.strip()

    if not title:
        raise ValueError("Judul tidak boleh kosong")

    if len(title) > 100:
        raise ValueError("Judul maksimal 100 karakter")

    return title
