from pick import pick

class Menu:
    def pick_menu(self, device, title: str):
        options: list[str] = self.__method_list_former(device)
        option, _ = pick(options, title)
        return getattr(device, option)

    @staticmethod
    def __method_list_former(device: object):
        methods: list[str] = []
        for method_name in dir(device):
            if callable(getattr(device, method_name)) and not method_name.startswith("_"):
                methods.append(method_name)
        return methods
