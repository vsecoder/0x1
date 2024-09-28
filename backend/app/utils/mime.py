from magic import Magic
import logging

try:
    mimedetect = Magic(mime=True, mime_encoding=False)
except TypeError:
    logging.error(
        "You have installed the wrong version of the 'magic' module. "
        "Please install python-magic."
    )

magic_status = bool(mimedetect)


def get_file_mimetype(path: str) -> dict:
    """
    Get file mimetype.
    :param path: file path.
    :return: dict.
    """
    try:
        # read only 2048 first bytes
        first_bytes = open(path, "rb").read(2048)
        return {"mimetype": mimedetect.from_buffer(first_bytes)}
    except Exception as e:
        return {"error": e}
