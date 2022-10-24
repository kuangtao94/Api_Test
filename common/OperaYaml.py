from common.helper import *
import yaml

class OperaYaml:

    def readYaml(self):
        with open(FilePath('data','data.yaml'),encoding='utf-8') as fp:
            return list(yaml.safe_load_all(fp))

    def readBookYaml(self):
        """打印出的字典"""
        with open(FilePath(filePath='data',fileName='book.yaml'),encoding='utf-8') as fp:
            return yaml.safe_load(fp)

if __name__ == '__main__':
    obj = OperaYaml()
    print(obj.readBookYaml())
    for item in obj.readBookYaml().values():
        print(item)