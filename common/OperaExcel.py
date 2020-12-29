import xlrd
from TestCase.ApiLogin_Po.common.OperaYaml import OperaYaml
from TestCase.ApiLogin_Po.common.helper import *


class ExcelValues:
    """Excel表的列固定"""
    CaseID = 0
    Desc = 1
    Url = 2
    Data = 3
    Method = 4
    Expect = 5

    @property
    def GetCaseID(self):
        """返回CaseID列"""
        return self.CaseID

    @property
    def GetDesc(self):
        """返回Desc列"""
        return self.Desc

    @property
    def GetUrl(self):
        """返回Url列"""
        return self.Url

    @property
    def GetData(self):
        """返回Data列"""
        return self.Data

    @property
    def GetMethod(self):
        """返回Method列"""
        return self.Method

    @property
    def GetExpect(self):
        """返回Expect列"""
        return self.Expect


class OperationExcel(OperaYaml):

    @property
    def readExcel(self):
        """获取Books工作表"""
        sheets = xlrd.open_workbook(FilePath(filePath='data',fileName='data1.xlsx'))
        return sheets.sheet_by_index(0)

    def readValues(self,rowx,colx):
        """获取工作表的行、列"""
        return self.readExcel.cell_value(rowx=rowx,colx=colx)

    def readCaseID(self,rowx):
        """获取工作表接口ID"""
        return self.readValues(rowx,ExcelValues().GetCaseID)

    def readDesc(self,rowx):
        """获取工作表接口描述"""
        return self.readValues(rowx,ExcelValues().GetDesc)

    def readUrl(self,rowx):
        """获取工作表接口URL"""
        url =  self.readValues(rowx,ExcelValues().GetUrl)
        if '{bookid}' in url:
            return str(url).replace('{bookid}',readBookID())
        else:
            return url

    def readData(self,rowx):
        """获取工作表接口Data"""
        return self.readValues(rowx,ExcelValues().GetData)

    def readMethod(self,rowx):
        """获取工作表接口方法"""
        return self.readValues(rowx,ExcelValues().GetMethod)

    def readExpect(self,rowx):
        """获取工作表接口预期结果"""
        return self.readValues(rowx,ExcelValues().GetExpect)

    def readJsonValues(self,rowx):
        """获取book.yaml文件的data值,readData对应是yaml文件的book_002,004"""
        return self.readBookYaml()[self.readData(rowx)]



if __name__ == '__main__':
    obj = OperationExcel()
    print(type(obj.readJsonValues(2)))
    # print(obj.readValues(1,ExcelValues().GetExpect))
    # print(obj.readExpect(4),type(obj.readExpect(4)))
