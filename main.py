import sys # We need sys so that we can pass argv to QApplication

import Motor_CMD # This file holds our MainWindow and all design related things
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from PyQt4 import QtGui # Import the PyQt4 module we'll need

class MotorCMD(QtGui.QMainWindow, Motor_CMD.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        with open('HowTo', 'r') as how_to_file:
            self.how_to_label.setText(str(how_to_file.read()))

        self.browse_button.clicked.connect(self.browse_file)

        self.DFS_cutoff.valueChanged.connect(self.analyze)
        self.time_cutoff.valueChanged.connect(self.analyze)

        self.generate_button.clicked.connect(self.generate)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button_2.clicked.connect(self.clear)
        
        self.report_button.clicked.connect(self.report)
        self.browseDatabase_button.clicked.connect(self.browse_database)
        self.appendDatabase_button.clicked.connect(self.append_database)
        self.sortDatabase_button.clicked.connect(self.sort_database)

    def browse_file(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.filename_display.setText(self.filename)
        self.analyze()

    def browse_database(self):
        self.databaseFilename = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        self.databaseFilename_display.setText(self.databaseFilename)
        powerDatabase_df = pd.read_csv(str(self.databaseFilename), sep=';')
        print powerDatabase_df
        
        self.databaseBrowser.setText(str(powerDatabase_df.to_string(col_space=10, index=False)))
        
    def append_database(self):
        with open('power_database.csv', 'a') as power_database:
            self.iver_number_database = int(self.iverNumber.text())
            onefive = int(self.polynomial(1.5))
            twofive = int(self.polynomial(2.5))
            threefive = int(self.polynomial(3.5))
            fourfive = int(self.polynomial(4.5))
            power_database.write( ('\n{};{};{};{};{}').format( str(self.iver_number_database), onefive, twofive, threefive, fourfive) )

        powerDatabase_df = pd.read_csv(str(self.databaseFilename), sep=';')
        self.databaseBrowser.clear()
        self.databaseBrowser.setText(str(powerDatabase_df.to_string(col_space=10, index=False)))

    def sort_database(self):
        powerDatabase_df = pd.read_csv(str(self.databaseFilename), sep=';')
        powerDatabase_df = powerDatabase_df.sort_values('iver')
        powerDatabase_df.to_csv(str(self.databaseFilename), sep=';', index=False)
        
        self.databaseBrowser.clear()
        self.databaseBrowser.setText(str(powerDatabase_df.to_string(col_space=10, index=False)))
        

    def analyze(self):
        #Create log object.
        log = MissionLog(self.filename, self.DFS_cutoff.value(), self.time_cutoff.value())
        self.df_output = log.cleanLog()
        if log.motorType()[1] == 128:
            #print 'Smart Motor'
            self.detect_smart_label.setText('Detected')
            self.detect_analog_label.setText('')
            self.radioButton_7.setChecked(True)
        elif log.motorType()[1] == 0:
            #print 'Analog Motor'
            self.detect_analog_label.setText('Detected')
            self.detect_smart_label.setText('')
            self.radioButton_6.setChecked(True)

        #Output current mission legs and linear regression slope to gui.
        self.output_legs.setText(str(self.df_output.to_string(col_space=15, index=False)))
        
        PWR_eq = str(log.coe_3_PWR) + '(kn)^3 + ' + str(log.coe_2_PWR) + '(kn)^2 + ' + str(log.coe_1_PWR) + '(kn) + ' + str(log.coe_0_PWR)

        self.coe_label.setText(str(log.speedSlope))
        self.int_label.setText(str(log.speedIntercept))
        self.r_label.setText(str(log.rValue))
        self.power_eq_label.setText(PWR_eq)

    def report(self):
        with open('test.html', 'w+') as report_file:

            iver_number = str(int(self.Iver_lineEdit.text()))
            stripped_df = self.df_output.drop(['index', 'CMD', 'DFS', 'Seconds'], axis=1)
            
            report_file.write('<h2><center>')
            report_file.write('Iver-{}'.format(iver_number))
            report_file.write('</center></h2>')
            
            report_file.write('<h4>')
            report_file.write('Filename:<br>')
            report_file.write(str(self.filename).split('/')[-1])
            report_file.write('</h4>')
            
            xpoints = np.linspace(0.0, 6.0, 50)
            a = np.array(self.df_output['Knots'])
            b = np.array(self.df_output['Power'])
            c = np.polyfit(a, b, 3)
            self.polynomial = np.poly1d(c)
            plt.plot(a, b, 'og')
            plt.plot(xpoints, self.polynomial(xpoints), '-r')
            plt.axis([0, 6, 0, 300])
            plt.title('Power vs Speed')
            plt.xlabel('Speed in knots')
            plt.ylabel('Power in watts')
            plt.savefig('out.png', transparent = True)
            plt.clf()
            
            coe_3_PWR = round(c[0], 2)
            coe_2_PWR = round(c[1], 2)
            coe_1_PWR = round(c[2], 2)
            coe_0_PWR = round(c[3], 2)
            PWR_eq = 'Power(w) = ' + str(coe_3_PWR) + '(kn)^3 + ' + str(coe_2_PWR) + '(kn)^2 + ' + str(coe_1_PWR) + '(kn) + ' + str(coe_0_PWR)
            
            report_file.write('<div style={}>'.format('float:left'))
            report_file.write('<img src="{}" style="width:500px;height:400px;">'.format('out.png'))
            report_file.write('<br><h4>{}</h4>'.format(PWR_eq))
            report_file.write('<p>Vehicle Configuration:</p>')
            report_file.write('<p>{}</p>'.format(str(self.textEdit_notes.toPlainText())))
            report_file.write('</div>')
            
            report_file.write('<div style={}>'.format('float:right'))
            report_file.write(stripped_df.to_html())
            report_file.write('<h5>Data used in regression.<br>Step -1 is hotel load.</h5>')
            report_file.write('</div>')

    def generate(self):
        prefix = 0
        line_result = ''
        self.speed_table.clear()
        self.power_table.clear()

        try:
            if self.radioButton_6.isChecked() == True:
                prefix = 6
            elif self.radioButton_7.isChecked() == True:
                prefix = 7
            for i in np.arange(0,5.05,0.05):
                line_result = str(prefix) + ';' + str(i) + ';' + str(int(float((self.lin_coe * i) + (log.motorType()[1]))))
                self.speed_table.append(str(line_result))
        except ValueError:
            self.speed_table.setText("No Iver Number Entered... Enter And Try Again")

        try:
            self.power_table.append(str('Version = 1'))
            self.power_table.append(str('Power Items: PowListItem=[Power_WHr];[Speed_Knots]'))
            for i in np.arange(.5,5.1,0.1):
                line_result = 'PowListItem=' + str(int(self.power(i))) + ';' + str(i)
                self.power_table.append(str(line_result))
            self.power_table.append('PowTotal=' + str(self.spinBox_totalPower.value()))
            self.power_table.append('PowReserve=' + str(self.spinBox_reservePower.value()))
        except ValueError:
            self.power_table.setText("No Iver Number Entered... Enter And Try Again.")

    def clear(self):

        self.Iver_lineEdit.clear()
        self.output_legs.clear()
        self.speed_table.clear()
        self.power_table.clear()
        self.textEdit_notes.clear()
        self.r_label.setText('RSquared Value')
        self.coe_label.setText('coefficient')
        self.int_label.setText('intercept')


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MotorCMD()                   # We set the form to be our MotorCMD (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

class MissionLog(object):
    def __init__(self, filename, cutoff_dfs, cutoff_time):
        self.filename = filename
        self.cutoff_dfs = cutoff_dfs
        self.cutoff_time = cutoff_time
        self.lin_coe = 0

    def loadLog(self):
        #Load csv file as pandas dataframe.
        output = pd.read_csv(str(self.filename), sep=';')
        output.columns = output.columns.str.strip().str.replace(' ', '_')
        return output

    def collapseLog(self):
        #Collapse mission_log down to one row per mission step.
        mission_log = self.loadLog()
        # Find number of mission legs.
        num_steps = len(set(mission_log['Current_Step']))
        # Create a blank dataframe (output) for calculated data.
        columns = ['Step', 'Knots', 'CMD', 'DFS', 'Power', 'Seconds']
        index = range(num_steps)
        output = pd.DataFrame(index=index, columns=columns)
        # Find average Knots, CMD and DFS for each mission leg, set in  output.
        for i in range(num_steps):
            temp = mission_log.query('Current_Step == @i')
            # Calculating the Current_Step is a math sanity check.
            output.set_value(i, 'Step', round(temp['Current_Step'].mean(), 0))
            output.set_value(i, 'Knots', round(temp['Vehicle_Speed_(kn)'].mean(), 3))
            output.set_value(i, 'CMD', round(temp['Motor_Speed_CMD'].mean(), 0))
            output.set_value(i, 'Power', round(temp['Power_Watts'].mean(), 0))
            output.set_value(i, 'DFS', round(temp['DFS_Depth_(m)'].mean(), 3))
            # Mission files are one row per sec. Count the rows for a time count.
            output.set_value(i, 'Seconds', len(temp['Current_Step']))
        return output

    def cleanLog(self):
        output = self.collapseLog()
        # Filter out mission legs under the DFS cutoff.
        output = output[output.DFS > self.cutoff_dfs]
        # Filter out mission legs with fewer rows than leg time. One row per sec.
        output = output[output.Seconds > self.cutoff_time]
        #Add hotel load as last row (-1) of log.
        num_steps = len(set(self.loadLog()['Current_Step']))
        temp = self.loadLog().query('Vehicle_State == 6')
        if self.motorType()[1] == 128:
            temp = temp.query('Motor_Speed_CMD == 128')
        elif self.motorType()[1] == 0:
            temp = temp.query('Motor_Speed_CMD == 0')
        output.set_value(num_steps + 1, 'Step', -1)
        output.set_value(num_steps + 1, 'Knots', 0)
        output.set_value(num_steps + 1, 'CMD', (self.motorType()[1]))
        output.set_value(num_steps + 1, 'DFS', round(temp['DFS_Depth_(m)'].mean(), 0))
        output.set_value(num_steps + 1, 'Power', round(temp['Power_Watts'].mean(), 0))
        output.set_value(num_steps + 1, 'Seconds', len(temp['Current_Step']))
        output = output.astype(float)
        self.speedReg(output)
        self.powerReg(output)
        return output

    def motorType(self):
        output = self.loadLog()
        output = output.query('Vehicle_State == 6')
        mode = output['Motor_Speed_CMD'].value_counts(normalize=False, sort=True).index[0]
        if mode == 128:
            return ('Smart Motor', 128)
        elif mode == 0:
            return ('Analog Motor', 0)
        else:
            return ('Commonest CMD while parking not 0 or 128.')

    def speedReg(self, log):
        log['CMD'] = log['CMD'] - (self.motorType()[1])
        X = log['CMD']
        Y = log['Knots']
        X = np.array(X).reshape(-1, 1)
        Y = np.array(Y).reshape(-1, 1)
        reg = linear_model.LinearRegression()
        reg.fit(Y, X)
        self.rValue = round(reg.score(Y, X), 3)
        self.speedSlope = round(reg.coef_[0], 1)
        self.speedIntercept = int(self.motorType()[1])

    def powerReg(self, log):
        a = np.array(log['Knots'])
        b = np.array(log['Power'])
        c = np.polyfit(a, b, 3)
        self.polynomial = np.poly1d(c)
        self.coe_3_PWR = round(c[0], 3)
        self.coe_2_PWR = round(c[1], 3)
        self.coe_1_PWR = round(c[2], 3)
        self.coe_0_PWR = round(c[3], 3)


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function