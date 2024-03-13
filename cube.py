import os.path
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, random, os


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        file_ui = 'cube.ui'
        try:
            loadUi(file_ui, self)
        except:
            file = os.path.join(os.path.dirname(sys.executable), file_ui)
            loadUi(file, self)

        qfile = os.path.join(os.path.dirname(sys.executable), 'src/dark.qss')
        File = QtCore.QFile(qfile)
        if not File.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            pass
        qss = QtCore.QTextStream(File)
        self.setStyleSheet(qss.readAll())
        self.cb_dark.setChecked(True)
        self.cb_dark.stateChanged.connect(self.dark_mode)
        self.val_d = {}

        self.solutions = []
        self.r11_map = [['r11-r33', 'r11-r32', 'r11-r31'], ['r11-r21x', 'r11-r22x', 'r11-r23x'],
                        ['r11-r31x', 'r11-r32x', 'r11-r33x'], ['r11-r23', 'r11-r22', 'r11-r21']]
        self.r12_map = [['r12-r33', 'r12-r32', 'r12-r31'], ['r12-r21x', 'r12-r22x', 'r12-r23x'],
                        ['r12-r31x', 'r12-r32x', 'r12-r33x'], ['r12-r23', 'r12-r22', 'r12-r21']]
        self.r13_map = [['r13-r33', 'r13-r32', 'r13-r31'], ['r13-r21x', 'r13-r22x', 'r13-r23x'],
                        ['r13-r31x', 'r13-r32x', 'r13-r33x'], ['r13-r23', 'r13-r22', 'r13-r21']]
        self.r21_map = [['r21-r33', 'r21-r32', 'r21-r31'], ['r13-r21x', 'r12-r21x', 'r11-r21x'],
                        ['r21-r31x', 'r21-r32x', 'r21-r33x'], ['r11-r21', 'r12-r21', 'r13-r21']]
        self.r22_map = [['r22-r33', 'r22-r32', 'r22-r31'], ['r13-r22x', 'r12-r22x', 'r11-r22x'],
                        ['r22-r31x', 'r22-r32x', 'r22-r33x'], ['r11-r22', 'r12-r22', 'r13-r22']]
        self.r23_map = [['r23-r33', 'r23-r32', 'r23-r31'], ['r13-r23x', 'r12-r23x', 'r11-r23x'],
                        ['r23-r31x', 'r23-r32x', 'r23-r33x'], ['r11-r23', 'r12-r23', 'r13-r23']]
        self.r31_map = [['r13-r31', 'r12-r31', 'r11-r31'], ['r23-r31', 'r22-r31', 'r21-r31'],
                        ['r11-r31x', 'r12-r31x', 'r13-r31x'], ['r21-r31x', 'r22-r31x', 'r23-r31x']]
        self.r32_map = [['r13-r32', 'r12-r32', 'r11-r32'], ['r23-r32', 'r22-r32', 'r21-r32'],
                        ['r11-r32x', 'r12-r32x', 'r13-r32x'], ['r21-r32x', 'r22-r32x', 'r23-r32x']]
        self.r33_map = [['r13-r33', 'r12-r33', 'r11-r33'], ['r23-r33', 'r22-r33', 'r21-r33'],
                        ['r11-r33x', 'r12-r33x', 'r13-r33x'], ['r21-r33x', 'r22-r33x', 'r23-r33x']]

        self.r11_val = [['y', 'y', 'y'], ['o', 'o', 'o'], ['w', 'w', 'w'], ['r', 'r', 'r']]
        self.r12_val = [['y', 'y', 'y'], ['o', 'o', 'o'], ['w', 'w', 'w'], ['r', 'r', 'r']]
        self.r13_val = [['y', 'y', 'y'], ['o', 'o', 'o'], ['w', 'w', 'w'], ['r', 'r', 'r']]

        self.r21_val = [['b', 'b', 'b'], ['o', 'o', 'o'], ['g', 'g', 'g'], ['r', 'r', 'r']]
        self.r22_val = [['b', 'b', 'b'], ['o', 'o', 'o'], ['g', 'g', 'g'], ['r', 'r', 'r']]
        self.r23_val = [['b', 'b', 'b'], ['o', 'o', 'o'], ['g', 'g', 'g'], ['r', 'r', 'r']]

        self.r31_val = [['y', 'y', 'y'], ['b', 'b', 'b'], ['w', 'w', 'w'], ['g', 'g', 'g']]
        self.r32_val = [['y', 'y', 'y'], ['b', 'b', 'b'], ['w', 'w', 'w'], ['g', 'g', 'g']]
        self.r33_val = [['y', 'y', 'y'], ['b', 'b', 'b'], ['w', 'w', 'w'], ['g', 'g', 'g']]

        self.init_val_map = {'y': ('r11-r33', 'r11-r32', 'r11-r31',
                                   'r12-r33', 'r12-r32', 'r12-r31',
                                   'r13-r33', 'r13-r32', 'r13-r31',
                                   'r13-r31', 'r12-r31', 'r11-r31',
                                   'r13-r32', 'r12-r32', 'r11-r32',
                                   'r13-r33', 'r12-r33', 'r11-r33',), 'o': ('r11-r21x', 'r11-r22x', 'r11-r23x',
                                                                            'r12-r21x', 'r12-r22x', 'r12-r23x',
                                                                            'r13-r21x', 'r13-r22x', 'r13-r23x',
                                                                            'r13-r21x', 'r12-r21x', 'r11-r21x',
                                                                            'r13-r22x', 'r12-r22x', 'r11-r22x',
                                                                            'r13-r23x', 'r12-r23x', 'r11-r23x'),
                             'w': ('r11-r31x', 'r11-r32x', 'r11-r33x',
                                   'r12-r31x', 'r12-r32x', 'r12-r33x',
                                   'r13-r31x', 'r13-r32x', 'r13-r33x',
                                   'r11-r31x', 'r12-r31x', 'r13-r31x',
                                   'r11-r32x', 'r12-r32x', 'r13-r32x',
                                   'r11-r33x', 'r12-r33x', 'r13-r33x',), 'r': ('r11-r23', 'r11-r22', 'r11-r21',
                                                                               'r12-r23', 'r12-r22', 'r12-r21',
                                                                               'r13-r23', 'r13-r22', 'r13-r21',
                                                                               'r11-r21', 'r12-r21', 'r13-r21',
                                                                               'r11-r22', 'r12-r22', 'r13-r22',
                                                                               'r11-r23', 'r12-r23', 'r13-r23',),
                             'b': ('r21-r33', 'r21-r32', 'r21-r31',
                                   'r22-r33', 'r22-r32', 'r22-r31',
                                   'r23-r33', 'r23-r32', 'r23-r31',
                                   'r23-r31', 'r22-r31', 'r21-r31',
                                   'r23-r32', 'r22-r32', 'r21-r32',
                                   'r23-r33', 'r22-r33', 'r21-r33'), 'g': ('r21-r31x', 'r21-r32x', 'r21-r33x',
                                                                           'r22-r31x', 'r22-r32x', 'r22-r33x',
                                                                           'r23-r31x', 'r23-r32x', 'r23-r33x',
                                                                           'r21-r31x', 'r22-r31x', 'r23-r31x',
                                                                           'r21-r32x', 'r22-r32x', 'r23-r32x',
                                                                           'r21-r33x', 'r22-r33x', 'r23-r33x')}

        self.line_indexes = {'r11': 0, 'r12': 1, 'r13': 2, 'r21': 3, 'r22': 4, 'r23': 5, 'r31': 6, 'r32': 7, 'r33': 8}
        self.maps = (self.r11_map, self.r12_map, self.r13_map, self.r21_map, self.r22_map, self.r23_map, self.r31_map,
                     self.r32_map, self.r33_map)
        self.rlist = (self.r11_val, self.r12_val, self.r13_val, self.r21_val, self.r22_val, self.r23_val,
                      self.r31_val, self.r32_val, self.r33_val)

        self.s1_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        self.s2_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        self.s3_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        self.s1x_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        self.s2x_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        self.s3x_val = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]

        self.s1_map = [['r11-r33', 'r11-r32', 'r11-r31'], ['r13-r33', 'r12-r33', 'r11-r33'],
                       ['r13-r31', 'r13-r32', 'r13-r33'], ['r11-r31', 'r12-r31', 'r13-r31']]

        self.s1_label = [[self.label_2, self.label_6, self.label_9], [self.label, self.label_3, self.label_2],
                         [self.label_7, self.label_4, self.label], [self.label_9, self.label_8, self.label_7]]

        self.s2_map = [['r21-r33', 'r21-r32', 'r21-r31'], ['r22-r33', 'r22-r33', 'r21-r33'],
                       ['r23-r31', 'r23-r32', 'r23-r33'], ['r21-r31', 'r22-r31', 'r23-r31']]
        self.s2_label = [[self.label_14, self.label_11, self.label_18], [self.label_13, self.label_12, self.label_14],
                         [self.label_16, self.label_10, self.label_13], [self.label_18, self.label_17, self.label_16]]

        self.s3_map = [['r13-r21', 'r13-r22', 'r13-r23'], ['r11-r21', 'r12-r21', 'r13-r21'],
                       ['r11-r23', 'r11-r22', 'r11-r21'], ['r13-r23', 'r12-r23', 'r11-r23']]
        self.s3_label = [[self.label_32, self.label_29, self.label_36], [self.label_31, self.label_30, self.label_32],
                         [self.label_34, self.label_28, self.label_31], [self.label_36, self.label_35, self.label_34]]

        self.s1x_map = [['r13-r23x', 'r13-r22x', 'r13-r21x'], ['r11-r23x', 'r12-r23x', 'r13-r23x'],
                        ['r11-r21x', 'r11-r22x', 'r11-r23x'], ['r13-r21x', 'r12-r21x', 'r11-r21x']]
        self.s1x_label = [[self.label_59, self.label_56, self.label_63], [self.label_58, self.label_57, self.label_59],
                          [self.label_61, self.label_55, self.label_58], [self.label_63, self.label_62, self.label_61]]

        self.s2x_map = [['r13-r33x', 'r13-r32x', 'r13-r31x'], ['r11-r33x', 'r12-r33x', 'r13-r33x'],
                        ['r11-r31x', 'r11-r32x', 'r11-r33x'], ['r13-r31x', 'r12-r31x', 'r11-r31x']]
        self.s2x_label = [[self.label_23, self.label_20, self.label_27], [self.label_22, self.label_21, self.label_23],
                          [self.label_25, self.label_19, self.label_22], [self.label_27, self.label_26, self.label_25]]

        self.s3x_map = [['r23-r33x', 'r23-r32x', 'r23-r31x'], ['r21-r33x', 'r22-r33x', 'r23-r33x'],
                        ['r21-r31x', 'r21-r32x', 'r21-r33x'], ['r23-r31x', 'r22-r31x', 'r21-r31x']]
        self.s3x_label = [[self.label_50, self.label_47, self.label_54], [self.label_49, self.label_48, self.label_50],
                          [self.label_52, self.label_46, self.label_49], [self.label_54, self.label_53, self.label_52]]

        self.sides = {'r23': 0, 'r11': 1, 'r31': 2, 'r33': 3, 'r21': 4, 'r13': 5}
        self.s_maps = (self.s1_map, self.s2_map, self.s3_map, self.s1x_map, self.s2x_map, self.s3x_map)
        self.s_vals = (self.s1_val, self.s2_val, self.s3_val, self.s1x_val, self.s2x_val, self.s3x_val)
        self.s_labels = (self.s1_label, self.s2_label, self.s3_label, self.s1x_label, self.s2x_label, self.s3x_label)

        self.comboBox.addItems(('r11', 'r12', 'r13', 'r21', 'r22', 'r23', 'r31', 'r32', 'r33'))

        self.btn_right.clicked.connect(self.move_right)
        self.btn_left.clicked.connect(self.move_left)
        self.btn_reset.clicked.connect(self.reset_all)
        self.btn_mix.clicked.connect(self.mixup)


        self.sp_r11.valueChanged.connect(lambda x: self.spin_obj(self.sp_r11))
        self.sp_r12.valueChanged.connect(lambda x: self.spin_obj(self.sp_r12))
        self.sp_r13.valueChanged.connect(lambda x: self.spin_obj(self.sp_r13))
        self.sp_r21.valueChanged.connect(lambda x: self.spin_obj(self.sp_r21))
        self.sp_r22.valueChanged.connect(lambda x: self.spin_obj(self.sp_r22))
        self.sp_r23.valueChanged.connect(lambda x: self.spin_obj(self.sp_r23))
        self.sp_r31.valueChanged.connect(lambda x: self.spin_obj(self.sp_r31))
        self.sp_r32.valueChanged.connect(lambda x: self.spin_obj(self.sp_r32))
        self.sp_r33.valueChanged.connect(lambda x: self.spin_obj(self.sp_r33))

        self.spin_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.spin_obj_list = (self.sp_r11, self.sp_r12, self.sp_r13, self.sp_r21, self.sp_r22, self.sp_r23,
                              self.sp_r31, self.sp_r32, self.sp_r33)

        self.r11_labels = [[self.label_2, self.label_6, self.label_9], [self.label_61, self.label_55, self.label_58],
                           [self.label_25, self.label_19, self.label_22], [self.label_34, self.label_28, self.label_31]]
        self.r12_labels = [[self.label_3, self.label_5, self.label_8], [self.label_62, self.label_60, self.label_57],
                           [self.label_26, self.label_24, self.label_21], [self.label_35, self.label_33, self.label_30]]
        self.r13_labels = [[self.label, self.label_4, self.label_7], [self.label_63, self.label_56, self.label_59],
                           [self.label_27, self.label_20, self.label_23], [self.label_36, self.label_29, self.label_32]]
        self.r21_labels = [[self.label_14, self.label_11, self.label_18], [self.label_61, self.label_62, self.label_63],
                           [self.label_52, self.label_46, self.label_49], [self.label_31, self.label_30, self.label_32]]
        self.r22_labels = [[self.label_12, self.label_15, self.label_17], [self.label_56, self.label_60, self.label_55],
                           [self.label_53, self.label_51, self.label_48], [self.label_28, self.label_33, self.label_29]]
        self.r23_labels = [[self.label_13, self.label_10, self.label_16], [self.label_59, self.label_57, self.label_58],
                           [self.label_54, self.label_47, self.label_50], [self.label_34, self.label_35, self.label_36]]
        self.r31_labels = [[self.label_9, self.label_8, self.label_7], [self.label_18, self.label_17, self.label_16],
                           [self.label_27, self.label_26, self.label_25], [self.label_54, self.label_53, self.label_52]]
        self.r32_labels = [[self.label_6, self.label_5, self.label_4], [self.label_11, self.label_15, self.label_10],
                           [self.label_20, self.label_24, self.label_19], [self.label_47, self.label_51, self.label_46]]
        self.r33_labels = [[self.label, self.label_3, self.label_2], [self.label_13, self.label_12, self.label_14],
                           [self.label_22, self.label_21, self.label_23], [self.label_49, self.label_48, self.label_50]]

        self.line_labels = [
            self.r11_labels, self.r12_labels, self.r13_labels, self.r21_labels, self.r22_labels, self.r23_labels,
            self.r31_labels, self.r32_labels, self.r33_labels
        ]
        self.labels = (self.label_26, self.label_16, self.label_27, self.label_28, self.label_35, self.label_61,
                       self.label_59, self.label_20, self.label_23, self.label_22, self.label_63, self.label_49,
                       self.label_53, self.label_21, self.label_29, self.label_46, self.label_33, self.label_2,
                       self.label_54, self.label_51, self.label, self.label_6, self.label_32, self.label_17,
                       self.label_3, self.label_55, self.label_50, self.label_10, self.label_5, self.label_11,
                       self.label_58, self.label_25, self.label_19, self.label_57, self.label_12, self.label_30,
                       self.label_34, self.label_31, self.label_24, self.label_47, self.label_62, self.label_52,
                       self.label_60, self.label_36, self.label_9, self.label_13, self.label_56, self.label_18,
                       self.label_7, self.label_48, self.label_4, self.label_14, self.label_8, self.label_15)

        self.reset_all()

    def mixup(self):
        lns = ('r11', 'r12', 'r13', 'r21', 'r22', 'r23', 'r31', 'r32', 'r33')
        decs = ('right', 'left')
        sol = []
        rng = self.sp_number.value()
        for i in range(rng-1):
            xr = random.choice(lns)
            xd = random.choice(decs)
            sold = 'right' if xd == 'left' else 'left'
            if len(sol) == 0:
                sol.append((xr, sold))
            if len(sol) > 0:
                last = sol[-1]
                if (xr, xd) == last:
                    sol.pop()
                    pass
                else:
                    sol.append((xr, sold))
            self.move_line(xr, xd)
        self.list.clear()
        for x, i in enumerate(sol[::-1]):
            x+=1
            self.list.addItem(f'{x}) {i[0].upper()} :: {i[1].upper()}')

    def mixuper(self, num1):
        lns = ('r11', 'r12', 'r13', 'r21', 'r22', 'r23', 'r31', 'r32', 'r33')
        decs = ('right', 'left')
        sol = []
        rng = num1
        for i in range(rng-1):
            xr = random.choice(lns)
            xd = random.choice(decs)
            sold = 'right' if xd == 'left' else 'left'
            if len(sol) == 0:
                sol.append((xr, sold))
            if len(sol) > 0:
                last = sol[-1]
                if (xr, xd) == last:
                    sol.pop()
                    pass
                else:
                    sol.append((xr, sold))
            self.move_line(xr, xd)
        self.list.clear()
        for x, i in enumerate(sol[::-1]):
            x+=1
            self.list.addItem(f'{x}) {i[0].upper()} :: {i[1].upper()}')

        # if len(sol) == 10 or len(sol) == 8:
        #     with open('sols.txt', 'a') as f:
        #         f.writelines(f'{sol[::-1]}\n')

    def dark_mode(self):
        if self.cb_dark.isChecked():
            qfile = os.path.join(os.path.dirname(sys.executable), 'src/dark.qss')
            File = QtCore.QFile(qfile)
        else:
            qfile = os.path.join(os.path.dirname(sys.executable), 'src/neom.qss')
            File = QtCore.QFile(qfile)
        if not File.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            pass
        qss = QtCore.QTextStream(File)
        self.setStyleSheet(qss.readAll())

    def spin_obj(self, obj):
        rnum = obj.objectName()[-3:]
        sp_rnum = self.line_indexes[rnum]
        xv = obj.value()
        spn = self.spin_vals[sp_rnum]
        if xv > spn:
            self.move_line(rnum, 'right')
        elif xv < spn:
            self.move_line(rnum, 'left')
        if xv >= 4 or xv <= (-4):
            self.spin_vals[sp_rnum] = 0
            obj.setValue(0)
        else:
            self.spin_vals[sp_rnum] = xv

    def move_line(self, rnum, direction):
        self.info.setText(f'{rnum}-{direction}')
        # print(f' * moving {rnum} {direction}-> ')
        item = self.line_indexes[rnum]
        # print('pre-', direction, self.rlist[item])
        if direction == 'right':
            x1 = self.rlist[item].pop(0)
            self.rlist[item].append(x1)
        elif direction == 'left':
            x1 = self.rlist[item].pop()
            self.rlist[item].insert(0, x1)

        self.move_s(rnum, direction)

        # print('pre-', direction, self.rlist[item])
        # self.move_s(rnum, direction)
        self.update_value(rnum)
        self.update_value_all()
        self.set_labels()
        self.draw_labels()

    def move_s(self, rnum, direction):
        s_ix = self.sides.get(rnum, 'x')

        self.sides = {'r23': 0, 'r11': 1, 'r31': 2, 'r33': 3, 'r21': 4, 'r13': 5}
        self.s_maps = (self.s1_map, self.s2_map, self.s3_map, self.s1x_map, self.s2x_map, self.s3x_map)

        if s_ix != 'x':
            # print('prem_s:', self.s1_val)
            rev = (0, 3, 5)
            s_line = self.s_vals[s_ix]
            if s_ix in rev:
                if direction == 'right':
                    x1 = s_line.pop(0)
                    s_line.append(x1)
                else:
                    x1 = s_line.pop()
                    s_line.insert(0, x1)
            else:
                if direction == 'left':
                    x1 = s_line.pop(0)
                    s_line.append(x1)
                else:
                    x1 = s_line.pop()
                    s_line.insert(0, x1)
            # print('aftr_s:', self.s1_val)

    def update_value(self, rnum=False):
        # for keym, rmap in self.maps.items():
        # for map in rmap:
        #     ix1 = rmap.index(map)
        #     for m in map:
        #         x = self.addr.get(m,'')
        #         if x:
        #             self.addr[m] = [self.addr.get(m,[]),[ ix1, map.index(m)]]
        #         else:
        #             self.addr[m] = [ix1, map.index(m)]
        # print(' *  update_value: ')
        rn = self.line_indexes[rnum]
        for rval, mval in zip(self.rlist[rn], self.maps[rn]):
            for rv, mv in zip(rval, mval):
                self.val_d[mv] = rv

        s_ix = self.sides.get(rnum, 'x')
        if s_ix != 'x':
            for rval, mval in zip(self.s_vals[s_ix], self.s_maps[s_ix]):
                for rv, mv in zip(rval, mval):
                    self.val_d[mv] = rv

    def update_value_all(self):
        # print(' * Fnc: update_value_all |')
        x1 = f'r11 val: {self.r11_val[0]} --> '
        x3 = f'r33 val: {self.r33_val} --> '

        for idx, rmaps in enumerate(self.maps):
            j2 = 0
            for rmap in rmaps:
                j3 = 0
                for rm in rmap:
                    self.rlist[idx][j2][j3] = self.val_d[rm]
                    j3 += 1
                j2 += 1

        # update s_lines
        for ix, maps in enumerate(self.s_maps):
            for ix1, map in enumerate(maps):
                for ix2, mp in enumerate(map):
                    self.s_vals[ix][ix1][ix2] = self.val_d[mp]

        # print(x1, 'r11 val:', self.r11_val[0], self.val_d['r11-r33'])
        # print(x3, '\nr33 val:', self.r33_val, self.val_d['r11-r33'])

    def move_right(self):
        rnum = self.comboBox.currentText()
        self.move_line(rnum, 'right')

    def move_left(self):
        rnum = self.comboBox.currentText()
        self.move_line(rnum, 'left')

    def set_labels(self):
        lnames = []
        lbls = []
        for m, l in zip(self.maps, self.line_labels):
            for mp, lb in zip(m,l):
                for map, lab in zip(mp, lb):
                    rnn = (lab.objectName())
                    if rnn not in lbls:
                        lbls.append(rnn)
                        lnames.append((lab, map))
        for i in lnames:
            i[0].setText(f'{self.val_d[i[1]]}')

    def draw_labels(self):
        """
        change background after getting label's text
        :return: None
        """
        colors = {'r': '#ac3939', 'b': '#336699', 'w': '#e6e6e6', 'y': '#e6e600', 'g': '#2d8659', 'o': '#e68a00'}
        for l in self.labels:
            color = l.text()
            if color:
                l.setStyleSheet(f"background:'{colors[color]}'; border: 1px solid #808080; border-radius: 5px")

    def reset_all(self):

        for sp_val in self.spin_vals:
            sp_val = 0
        for sp in self.spin_obj_list:
            sp.setValue(0)

        k1 = 0
        for k, val in self.init_val_map.items():
            for vl in val:
                self.val_d[vl] = k
                k1 += 1

        # setting values for lines
        for ix, maps in enumerate(self.maps):
            for ix1, map in enumerate(maps):
                for ix2, mp in enumerate(map):
                    self.rlist[ix][ix1][ix2] = self.val_d[mp]

        # setting values for s_lines
        for ix, maps in enumerate(self.s_maps):
            for ix1, map in enumerate(maps):
                for ix2, mp in enumerate(map):
                    self.s_vals[ix][ix1][ix2] = self.val_d[mp]



        self.set_labels()
        self.draw_labels()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = MainScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setMinimumWidth(900)
    widget.setMinimumHeight(650)
    widget.show()
    sys.exit(app.exec_())
