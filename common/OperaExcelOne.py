import xlrd
from TestCase.ApiLogin_Po.common.helper import  FilePath
import json
import yaml

class ExcelValues:
    CaseID = "接口用例ID"
    CaseModel = '模块'
    CaseDesc = "接口名称"
    CasePre = '前置条件'
    CaseUrl = "请求地址"
    Headers = "请求头"
    Params = '请求参数'
    Method = "请求方法"
    Expect = "预期结果"
    StatusCode = '协议状态码'
    IsRun = '是否执行'

class OperationExcel:

    @property
    def readExcel(self):
        """获取Books工作表"""
        sheets = xlrd.open_workbook(FilePath(filePath='data', fileName='data1.xlsx'))
        return sheets.sheet_by_index(1)

    @property
    def readNrow(self):
        """获取总行数"""
        return self.readExcel.nrows

    @property
    def readNcol(self):
        """获取总列数"""
        return self.readExcel.ncols

    @property
    def readExcelDatas(self):
        datas = []
        title = self.readExcel.row_values(0)
        for rowx in range(1,self.readNrow):
            row_values = self.readExcel.row_values(rowx)
            datas.append(dict(zip(title,row_values)))
        return datas

    @property
    def runs(self):
        """获取可执行的用例"""
        run = []
        for item in self.readExcelDatas:
            isrun = item[ExcelValues.IsRun]
            if isrun == 'y':
                run.append(item)
            else:
                pass
        return run

    def case_lists(self):
        '''获取excel中的所有测试用例'''
        cases = []
        for item in self.readExcelDatas:
            cases.append(item)
        return cases

    def Params(self):
        '''对请求参数为空的出来 len(str.strip())'''
        for item in self.runs:
            params = item[ExcelValues.Params]
            if len(str(params).strip()) == 0:
                pass
            elif len(str(params).strip()) >= 0:
                #str->dict，字符串的反序列化loads
                # print(type(json.loads(params)))
                return json.loads(params)

    def case_praams(self,casePrev):
        '''
        根据前置条件找到关联的前置测试用例
        :param casePrev:前置条件（headers）
        :return:
        '''
        for item in self.case_lists():
            if casePrev in item.values():
                return item
        return None

    def preHeaders(self,preResult):
        """
        :param preResult: token的值，替换请求头的token
        :return: 返回带动态的token
        """
        for item in self.runs:
            header = item[ExcelValues.Headers]
            if "{token}" in header:
                header=str(header).replace('{token}',preResult)
                return json.loads(header)

if __name__ == '__main__':
    obj = OperationExcel()
    # for item in obj.case_lists():
    #     print(item)
