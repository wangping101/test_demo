# -------------封装读取Excel表数据方法-------------------
import xlrd
'''定义一个类'''
class ExcelUtil():

    def __init__(self,filePath, sheetName):
        self.data = xlrd.open_workbook(filePath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一列的key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        print(u"总行数:", self.rowNum)
        # 获取总列数
        self.colNum = self.table.ncols
        print(u"总列数:", self.colNum)

     # 读取Excel表中值
    def dict_data(self,):
        if self.rowNum <= 1:
            print("无数据可取")
        else:
            # 创建一个列表将数据放入
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
            j += 1
            return r

if __name__ == "__main__":
    filePath = "E:\\test_demo\excel\\test.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filePath, sheetName)
    print(data.dict_data())

