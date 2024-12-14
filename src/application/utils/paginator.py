from django.core.paginator import Paginator as paginator


class Meta:
    page: list
    last_page: int
    total: list
    first: list
    last: list


class Paginator:
    data: list
    meta: Meta

    def __default_response(self):
        return {
            "data": list(self.pages.page(self.__page)),
            "meta": {
                "page": self.__page,
                "last_page": self.pages.num_pages,
                "total": len(self.__data),
            },
        }

    def __init__(self, data, limit, page) -> None:
        self.__limit = limit
        self.__page = page
        self.__data = data
        if type(data) is not list:
            data = [data]
        self.pages = paginator(data, self.__limit)

    @property
    def result(self):
        return self.__default_response()
