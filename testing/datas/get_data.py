import yaml


class ReadFile:
    data_dict = None

    def getData(self, path: str = 'testing/datas/data.yml') -> dict:
        if self.data_dict is None:
            with open(path, 'r', encoding='utf-8') as file:
                self.data_dict = yaml.load(file.read(), Loader=yaml.FullLoader)
        return self.data_dict


if __name__ == '__main__':
    readfile = ReadFile()
    print(readfile.getData())
