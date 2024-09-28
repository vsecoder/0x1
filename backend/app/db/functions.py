from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


class File(models.File):
    """
    File model, contains all methods for working with files.
    """
    @classmethod
    async def get_file(cls, sha256: str) -> Union[dict, None]:
        """
        Get file by sha256.
        :param sha256: file sha256.
        :return: File dict.
        """
        try:
            return await cls.get(sha256=sha256)
        except DoesNotExist:
            return None

    @classmethod
    async def create_file(
        cls, 
        sha256: str, 
        mime: str, 
        addr: str, 
        ua: str, 
        expiration: str, 
        size: int,
        password: str = None
    ) -> dict:
        if file := await cls.get_file(sha256):
            if file.removed: 
                cls.filter(sha256=sha256).update(removed=False, expiration=expiration)
        else:
            file = await cls.create(
                sha256=sha256,
                password=password,
                mime=mime,
                addr=addr,
                ua=ua,
                expiration=expiration,
                size=size
            )

        return file

    @classmethod
    async def remove_file(cls, sha256: str) -> None:
        if await cls.get_file(sha256):
            cls.filter(sha256=sha256).update(removed=True)
