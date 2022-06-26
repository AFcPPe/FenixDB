import sys
import xlwt
from PySide2.QtWidgets import *
from PySide2.QtCore import QStringListModel
from UI import Ui_MainWindow
import sqlite3
workbook = xlwt.Workbook(encoding='ascii')
#制表AirportCommunication
sheetAirportCommunication = workbook.add_sheet("AirportCommunication")
sheetAirportCommunication.write(0,0,'area_code')
sheetAirportCommunication.write(0,1,'icao_code')
sheetAirportCommunication.write(0,2,'airport_identifier')
sheetAirportCommunication.write(0,3,'communication_type')
sheetAirportCommunication.write(0,4,'communication_frequency')
sheetAirportCommunication.write(0,5,'frequency_units')
sheetAirportCommunication.write(0,6,'service_indicator')
sheetAirportCommunication.write(0,7,'callsign')
sheetAirportCommunication.write(0,8,'latitude')
sheetAirportCommunication.write(0,9,'longitude')
#制表AirportCommunication
sheetAirportLookup = workbook.add_sheet("AirportLookup")
sheetAirportLookup.write(0,0,'extID')
sheetAirportLookup.write(0,1,'ID')
#制表Airports
sheetAirports = workbook.add_sheet("Airports")
sheetAirports.write(0,0,'ID')
sheetAirports.write(0,1,'Name')
sheetAirports.write(0,2,'ICAO')
sheetAirports.write(0,3,'PrimaryID')
sheetAirports.write(0,4,'Latitude')
sheetAirports.write(0,5,'Longtitude')
sheetAirports.write(0,6,'Elevation')
sheetAirports.write(0,7,'TransitionAltitude')
sheetAirports.write(0,8,'TransitionLevel')
sheetAirports.write(0,9,'SpeedLimit')
sheetAirports.write(0,10,'SpeedLimitAltitude')
#制表Airways
sheetAirways = workbook.add_sheet("Airways")
#制表config
sheetconfig = workbook.add_sheet("config")
#制表Gls
sheetGls = workbook.add_sheet("Gls")
#制表GridMora
sheetGridMora = workbook.add_sheet("GridMora")
#制表Holdings
sheetHoldings = workbook.add_sheet("Holdings")
#制表ILSes
sheetILSes = workbook.add_sheet("ILSes")
#制表Markers
sheetMarkers= workbook.add_sheet("Markers")
#制表MarkerTypes
sheetMarkerTypes = workbook.add_sheet("MarkerTypes")
#制表NavaidLookup
sheetNavaidLookup = workbook.add_sheet("NavaidLookup")
#制表Navaids
sheetNavaids = workbook.add_sheet("Navaids")
#制表NavaidTypes
sheetNavaidTypes = workbook.add_sheet("NavaidTypes")
#制表Runways
sheetRunways = workbook.add_sheet("Runways")
#制表SurfaceTypes
sheetSurfaceTypes = workbook.add_sheet("SurfaceTypes")
#制表TerminalLegs
sheetTerminalLegs = workbook.add_sheet("TerminalLegs")
#制表TerminalLegsEx
sheetTerminalLegsEx = workbook.add_sheet("TerminalLegsEx")
#制表Terminals
sheetTerminals = workbook.add_sheet("Terminals")
#制表TrmLegTypes
sheetTrmLegTypes = workbook.add_sheet("TrmLegTypes")
#制表WaypointLookup
sheetWaypointLookup = workbook.add_sheet("WaypointLookup")
#制表Waypoints
sheetWaypoints = workbook.add_sheet("Waypoints")

curCol = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]



class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.OpenDB.triggered.connect(self.connectdb)
    def connectdb(self):
        openfile_name = QFileDialog.getOpenFileNames(self, '选择文件',filter="Fenix导航数据文件 (nd.db3)",dir='C:\\ProgramData\\Fenix\\Navdata')
        if openfile_name[0] != None:
            self.con = sqlite3.connect(openfile_name[0][0])
            self.cur = self.con.cursor()
            self.cur.execute("SELECT ID,ICAO FROM Airports")
            airport = self.cur.fetchall()
            # 实例化列表模型，添加数据
            slm = QStringListModel()
            self.qList = []
            for per in airport:
                self.qList.append(per[1])

            # 设置模型列表视图，加载数据列表
            slm.setStringList(self.qList)

            # 设置列表视图的模型
            self.AirportSelect.setModel(slm)
            # 单击触发自定义的槽函数
            self.AirportSelect.clicked.connect(self.selectairport)
            self.SaveAirport.clicked.connect(self.saveairport)
            self.SaveExcel.triggered.connect(self.saveexcel)
    def selectairport(self):
        # print()
        self.cur.execute("SELECT * FROM Airports WHERE ICAO=\'"+self.AirportSelect.selectedIndexes()[0].data()+"\' ")
        data = self.cur.fetchall()
        self.AirportID.setText(data[0][0].__str__())
        self.AirportName.setText(data[0][1].__str__())
        self.AirportICAO.setText(data[0][2].__str__())
        self.AirportLat.setText(data[0][4].__str__())
        self.AirportLongt.setText(data[0][5].__str__())
        self.AirportElv.setText(data[0][6].__str__())
        self.AirportTA.setText(data[0][7].__str__())
        self.AirportTL.setText(data[0][8].__str__())
        self.AirportSpd.setText(data[0][9].__str__())
        self.AirportSpdH.setText(data[0][10].__str__())
        self.cur.execute("SELECT * FROM AirportCommunication WHERE airport_identifier=\'" + self.AirportSelect.selectedIndexes()[0].data() + "\' ")
        data = self.cur.fetchall()
        if data != []:
            self.AirportAC.setText(data[0][0].__str__())
            self.AirportAICAO.setText(data[0][1].__str__())
            self.AirportCom.setText(data[0][3].__str__())
            self.AirportFreq.setText(data[0][4].__str__())
            self.AirportFreqUnit.setText(data[0][5].__str__())
            self.AirportSI.setText(data[0][6])
        # print(self.AirportSelect.selectedIndexes()[0].data())
    def saveairport(self):
        global sheetAirports
        global sheetAirportLookup
        global sheetAirportCommunication
        global curCol
        sheetAirports.write(curCol[2],0,self.AirportID.text())
        sheetAirports.write(curCol[2], 1, self.AirportName.text())
        sheetAirports.write(curCol[2], 2, self.AirportICAO.text())
        sheetAirports.write(curCol[2], 3, "")
        sheetAirports.write(curCol[2], 4, self.AirportLat.text())
        sheetAirports.write(curCol[2], 5, self.AirportLongt.text())
        sheetAirports.write(curCol[2], 6, self.AirportElv.text())
        sheetAirports.write(curCol[2], 7, self.AirportTA.text())
        sheetAirports.write(curCol[2], 8, self.AirportTL.text())
        sheetAirports.write(curCol[2], 9, self.AirportSpd.text())
        sheetAirports.write(curCol[2], 10, self.AirportSpdH.text())
        curCol[2]+=1
        sheetAirportLookup.write(curCol[1],0,self.AirportAICAO.text()+self.AirportICAO.text())
        sheetAirportLookup.write(curCol[1],1,self.AirportID.text())
        curCol[1]+=1
        sheetAirportCommunication.write(curCol[0],0,self.AirportAC.text())
        sheetAirportCommunication.write(curCol[0],1, self.AirportAICAO.text())
        sheetAirportCommunication.write(curCol[0],2, self.AirportICAO.text())
        sheetAirportCommunication.write(curCol[0],3, self.AirportCom.text())
        sheetAirportCommunication.write(curCol[0],4, self.AirportFreq.text())
        sheetAirportCommunication.write(curCol[0],5, self.AirportFreqUnit.text())
        sheetAirportCommunication.write(curCol[0],6, self.AirportSI.text())
        sheetAirportCommunication.write(curCol[0],7, self.AirportName.text())
        sheetAirportCommunication.write(curCol[0],8, self.AirportLat.text())
        sheetAirportCommunication.write(curCol[0],9, self.AirportLongt.text())
        curCol[0] += 1
    def saveexcel(self):
        global workbook
        workbook.save("Result.xls")




if __name__ == "__main__":
    # con = sqlite3.connect('C:\\ProgramData\\Fenix\\Navdata\\nd.db3')
    # cur = con.cursor()
    # cur.execute("SELECT ID,ICAO FROM Airports")
    # airport = cur.fetchall()
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())