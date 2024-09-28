def get_max_lifespan(
    filesize: int,
    min_exp: int = 1 * 24 * 60 * 60,    # 1 day
    max_exp: int = 365 * 24 * 60 * 60,  # 1 year
    max_size: int = 2 * 1024 * 1024,    # 2gb
) -> int:
    """
    Get max file lifetime in seconds

    :param filesize: file size.
    :param min_exp: minimum expiration time.
    :param max_exp: maximum expiration time.
    :param max_size: file size.
    :return: File dict.
    """
    return min_exp + int((-max_exp + min_exp) * (filesize / max_size - 1) ** 3)
