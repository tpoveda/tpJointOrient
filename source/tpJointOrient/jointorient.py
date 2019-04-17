from functools import partial

from tpQtLib.Qt.QtCore import *
from tpQtLib.Qt.QtWidgets import *

import tpDccLib as tp
import tpMayaLib as maya
from tpQtLib.core import window
from tpQtLib.widgets import splitters
from tpMayaLib.core import decorators


class JointOrient(window.MainWindow, object):
    def __init__(self):
        super(JointOrient, self).__init__(
            name='JointOrientWindow',
            title='RigLib - Joint Orient',
            size=(350, 700),
            fixed_size=False,
            auto_run=True,
            frame_less=True,
            use_style=True
        )

    def ui(self):
        super(JointOrient, self).ui()

        ### Auto Orient Joint Widget ###

        joint_ori_widget = QWidget()
        joint_ori_widget.setLayout(QVBoxLayout())
        joint_ori_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        joint_ori_widget.layout().setContentsMargins(0, 0, 0, 0)
        joint_ori_widget.layout().setSpacing(2)

        self.main_layout.addWidget(joint_ori_widget)

        joint_ori_splitter = splitters.Splitter('JOINT ORIENT')
        joint_ori_widget.layout().addWidget(joint_ori_splitter)

        aim_axis_layout = QHBoxLayout()
        aim_axis_layout.setContentsMargins(5, 5, 5, 5)
        aim_axis_layout.setSpacing(2)

        # Aim Axis
        aim_axis_box = QGroupBox()
        aim_axis_box.setLayout(aim_axis_layout)
        aim_axis_box.setTitle('Aim Axis')
        joint_ori_widget.layout().addWidget(aim_axis_box)
        self.aim_x_radio = QRadioButton('X')
        self.aim_y_radio = QRadioButton('Y')
        self.aim_z_radio = QRadioButton('Z')
        self.aim_rev_cbx = QCheckBox('Reverse')
        self.aim_x_radio.setChecked(True)

        aim_axis_layout.addWidget(self.aim_x_radio)
        aim_axis_layout.addWidget(self.aim_y_radio)
        aim_axis_layout.addWidget(self.aim_z_radio)
        aim_axis_layout.addWidget(self.aim_rev_cbx)

        # Up Axis
        up_axis_layout = QHBoxLayout()
        up_axis_layout.setContentsMargins(5, 5, 5, 5)
        up_axis_layout.setSpacing(2)

        up_axis_box = QGroupBox()
        up_axis_box.setLayout(up_axis_layout)
        up_axis_box.setTitle('Up Axis')
        joint_ori_widget.layout().addWidget(up_axis_box)
        self.up_x_radio = QRadioButton('X')
        self.up_y_radio = QRadioButton('Y')
        self.upZRadio = QRadioButton('Z')
        self.upRevCbx = QCheckBox('Reverse')
        self.up_y_radio.setChecked(True)

        up_axis_layout.addWidget(self.up_x_radio)
        up_axis_layout.addWidget(self.up_y_radio)
        up_axis_layout.addWidget(self.upZRadio)
        up_axis_layout.addWidget(self.upRevCbx)

        # Up World Axis
        up_world_axis_layout = QHBoxLayout()
        up_world_axis_layout.setContentsMargins(5, 5, 5, 5)
        up_world_axis_layout.setSpacing(5)

        up_world_axis_box = QGroupBox()
        up_world_axis_box.setLayout(up_world_axis_layout)
        up_world_axis_box.setTitle('Up World Axis')
        joint_ori_widget.layout().addWidget(up_world_axis_box)
        self.up_world_x_spin = QDoubleSpinBox()
        self.up_world_y_spin = QDoubleSpinBox()
        self.up_world_z_spin = QDoubleSpinBox()
        self.up_world_x_spin.setDecimals(3)
        self.up_world_y_spin.setDecimals(3)
        self.up_world_z_spin.setDecimals(3)
        self.up_world_x_spin.setRange(-360, 360)
        self.up_world_y_spin.setRange(-360, 360)
        self.up_world_z_spin.setRange(-360, 360)
        self.up_world_x_spin.setLocale(QLocale.English)
        self.up_world_y_spin.setLocale(QLocale.English)
        self.up_world_z_spin.setLocale(QLocale.English)
        self.up_world_x_spin.setValue(1.0)
        up_world_x = QPushButton('X')
        up_world_y = QPushButton('Y')
        up_world_z = QPushButton('Z')
        up_world_x.setMaximumWidth(20)
        up_world_y.setMaximumWidth(20)
        up_world_z.setMaximumWidth(20)

        up_world_axis_layout.addWidget(self.up_world_x_spin)
        up_world_axis_layout.addWidget(self.up_world_y_spin)
        up_world_axis_layout.addWidget(self.up_world_z_spin)
        up_world_axis_layout.addWidget(up_world_x)
        up_world_axis_layout.addWidget(up_world_y)
        up_world_axis_layout.addWidget(up_world_z)

        joint_ori_widget.layout().addLayout(splitters.SplitterLayout())

        joint_orient_btn_layout = QHBoxLayout()
        joint_orient_btn_layout.setAlignment(Qt.AlignCenter)
        joint_ori_widget.layout().addLayout(joint_orient_btn_layout)
        spacer_item = QSpacerItem(2, 2, QSizePolicy.Minimum, QSizePolicy.Minimum)
        joint_orient_btn_layout.addSpacerItem(spacer_item)
        joint_orient_btn = QPushButton('Apply')
        self.joint_orient_cbx = QCheckBox('Hierarchy')
        joint_orient_btn.setMaximumWidth(80)
        self.joint_orient_cbx.setChecked(True)
        joint_orient_btn_layout.addWidget(joint_orient_btn)
        joint_orient_btn_layout.addWidget(self.joint_orient_cbx)

        spacer_item = QSpacerItem(2, 2, QSizePolicy.Fixed)
        self.main_layout.addSpacerItem(spacer_item)

        ### Manual Orient Joint Widget ###
        manual_joint_ori_widget = QWidget()
        manual_joint_ori_widget.setLayout(QVBoxLayout())
        manual_joint_ori_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        manual_joint_ori_widget.layout().setContentsMargins(5, 5, 5, 5)
        manual_joint_ori_widget.layout().setSpacing(10)

        self.main_layout.addWidget(manual_joint_ori_widget)

        manual_joint_ori_splitter = splitters.Splitter('MANUAL JOINT ORIENT')
        manual_joint_ori_widget.layout().addWidget(manual_joint_ori_splitter)

        manual_joint_ori_layout = QHBoxLayout()
        manual_joint_ori_widget.layout().addLayout(manual_joint_ori_layout)

        manual_joint_ori_lbl = QLabel('  X  Y  Z  ')
        self.manual_joint_ori_x_spin = QDoubleSpinBox()
        self.manual_joint_ori_y_spin = QDoubleSpinBox()
        self.manual_joint_ori_z_spin = QDoubleSpinBox()
        self.manual_joint_ori_x_spin.setDecimals(3)
        self.manual_joint_ori_y_spin.setDecimals(3)
        self.manual_joint_ori_z_spin.setDecimals(3)
        self.manual_joint_ori_x_spin.setRange(-360, 360)
        self.manual_joint_ori_y_spin.setRange(-360, 360)
        self.manual_joint_ori_z_spin.setRange(-360, 360)
        self.manual_joint_ori_x_spin.setLocale(QLocale.English)
        self.manual_joint_ori_y_spin.setLocale(QLocale.English)
        self.manual_joint_ori_z_spin.setLocale(QLocale.English)
        manualJointOriResetBtn = QPushButton('Reset')

        manual_joint_ori_layout.addWidget(manual_joint_ori_lbl)
        manual_joint_ori_layout.addWidget(self.manual_joint_ori_x_spin)
        manual_joint_ori_layout.addWidget(self.manual_joint_ori_y_spin)
        manual_joint_ori_layout.addWidget(self.manual_joint_ori_z_spin)
        manual_joint_ori_layout.addWidget(manualJointOriResetBtn)

        manual_joint_splitter_layout = QVBoxLayout()
        manual_joint_ori_widget.layout().addLayout(manual_joint_splitter_layout)

        degree_layout = QHBoxLayout()
        degree_layout.setContentsMargins(5, 5, 5, 5)
        degree_layout.setSpacing(2)

        degree_box = QGroupBox()
        degree_box.setLayout(degree_layout)
        degree_box.setStyleSheet("border:0px;")
        manual_joint_splitter_layout.layout().addWidget(degree_box)
        self.degree1_radio = QRadioButton('1')
        self.degree5_radio = QRadioButton('5')
        self.degree10_radio = QRadioButton('10')
        self.degree20_radio = QRadioButton('20')
        self.degree45_radio = QRadioButton('45')
        self.degree90_radio = QRadioButton('90')
        self.degree90_radio.setChecked(True)
        self._set_value_change(90)

        degree_layout.addWidget(self.degree1_radio)
        degree_layout.addWidget(self.degree5_radio)
        degree_layout.addWidget(self.degree10_radio)
        degree_layout.addWidget(self.degree20_radio)
        degree_layout.addWidget(self.degree45_radio)
        degree_layout.addWidget(self.degree90_radio)

        manual_joint_splitter_layout.addLayout(splitters.SplitterLayout())

        manual_joint_ori_buttons_layout = QHBoxLayout()
        manual_joint_ori_buttons_layout.setContentsMargins(2, 2, 2, 2)
        manual_joint_ori_buttons_layout.setSpacing(5)
        manual_joint_ori_widget.layout().addLayout(manual_joint_ori_buttons_layout)

        manual_joint_ori_add_btn = QPushButton('Add ( + ) ')
        manual_joint_ori_subtract_btn = QPushButton('Subract ( - ) ')

        manual_joint_ori_buttons_layout.addWidget(manual_joint_ori_add_btn)
        manual_joint_ori_buttons_layout.addWidget(manual_joint_ori_subtract_btn)

        manual_joint_ori_set_btn_layout = QVBoxLayout()
        manual_joint_ori_set_btn_layout.setAlignment(Qt.AlignCenter)
        manual_joint_ori_set_btn_layout.setContentsMargins(2, 2, 2, 2)
        manual_joint_ori_set_btn_layout.setSpacing(5)
        manual_joint_ori_widget.layout().addLayout(manual_joint_ori_set_btn_layout)

        manual_joint_ori_set_btn = QPushButton('Set')
        manual_joint_ori_set_btn.setMaximumWidth(100)
        self.manual_joint_ori_set_cbx = QCheckBox('Affect children')

        manual_joint_ori_set_btn_layout.addWidget(manual_joint_ori_set_btn)
        manual_joint_ori_set_btn_layout.addWidget(self.manual_joint_ori_set_cbx)

        set_rot_axis_widget = QWidget()
        set_rot_axis_widget.setLayout(QVBoxLayout())
        set_rot_axis_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        set_rot_axis_widget.layout().setContentsMargins(5, 5, 5, 5)
        set_rot_axis_widget.layout().setSpacing(10)

        self.main_layout.addWidget(set_rot_axis_widget)

        set_rot_axis_splitter = splitters.Splitter('SET ROTATION AXIS')
        set_rot_axis_widget.layout().addWidget(set_rot_axis_splitter)

        set_rot_axis_layout = QVBoxLayout()
        set_rot_axis_widget.layout().addLayout(set_rot_axis_layout)

        set_rot_top_layout = QHBoxLayout()
        set_rot_top_layout.setSpacing(5)
        set_rot_axis_layout.addLayout(set_rot_top_layout)
        self.set_rot_axis_box = QComboBox()
        set_rot_top_layout.addWidget(self.set_rot_axis_box)
        for rotAxis in ['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx']:
            self.set_rot_axis_box.addItem(rotAxis)
        set_rot_axis_common_btn = QPushButton('   <')
        set_rot_axis_common_btn.setMaximumWidth(45)
        set_rot_axis_common_btn.setStyleSheet("QPushButton::menu-indicator{image:url(none.jpg);}")
        self.set_rot_axis_common_btn_menu = QMenu(self)
        self._set_common_rotation_axis()
        set_rot_axis_common_btn.setMenu(self.set_rot_axis_common_btn_menu)
        set_rot_top_layout.addWidget(set_rot_axis_common_btn)

        set_rot_axis_btn_layout = QHBoxLayout()
        set_rot_axis_btn_layout.setAlignment(Qt.AlignCenter)
        set_rot_axis_layout.addLayout(set_rot_axis_btn_layout)
        set_rot_axis_btn = QPushButton('Set')
        set_rot_axis_btn.setMaximumWidth(100)
        set_rot_axis_btn_layout.addWidget(set_rot_axis_btn)

        set_rot_axis_splitter_layout = QVBoxLayout()
        set_rot_axis_widget.layout().addLayout(set_rot_axis_splitter_layout)
        set_rot_axis_splitter_layout.addLayout(splitters.SplitterLayout())

        spacer_item = QSpacerItem(2, 2, QSizePolicy.Fixed)
        self.main_layout.addSpacerItem(spacer_item)

        layout_lra_buttons = QHBoxLayout()
        self.main_layout.addLayout(layout_lra_buttons)
        display_lra_btn = QPushButton('Display LRA')
        hide_lra_btn = QPushButton('Hide LRA')
        layout_lra_buttons.addWidget(display_lra_btn)
        layout_lra_buttons.addWidget(hide_lra_btn)

        select_hierarchy_btn = QPushButton('Select Hierarchy')
        self.main_layout.addWidget(select_hierarchy_btn)

        # ==== SIGNALS ==== #
        up_world_x.clicked.connect(partial(self._reset_axis, 'x'))
        up_world_y.clicked.connect(partial(self._reset_axis, 'y'))
        up_world_z.clicked.connect(partial(self._reset_axis, 'z'))
        joint_orient_btn.clicked.connect(self.orient_joints)

        manualJointOriResetBtn.clicked.connect(self._reset_manual_orient)
        manual_joint_ori_add_btn.clicked.connect(partial(self.manual_orient_joints, 'add'))
        manual_joint_ori_subtract_btn.clicked.connect(partial(self.manual_orient_joints, 'subtract'))
        manual_joint_ori_set_btn.clicked.connect(self.set_manual_orient_joints)

        self.degree1_radio.clicked.connect(partial(self._set_value_change, 0))
        self.degree5_radio.clicked.connect(partial(self._set_value_change, 5))
        self.degree10_radio.clicked.connect(partial(self._set_value_change, 10))
        self.degree20_radio.clicked.connect(partial(self._set_value_change, 20))
        self.degree45_radio.clicked.connect(partial(self._set_value_change, 45))
        self.degree90_radio.clicked.connect(partial(self._set_value_change, 90))

        set_rot_axis_btn.clicked.connect(self.set_rot_axis)

        display_lra_btn.clicked.connect(partial(self.set_lra, True))
        hide_lra_btn.clicked.connect(partial(self.set_lra, False))
        select_hierarchy_btn.clicked.connect(self.select_hierarchy)

    def _reset_axis(self, axis):

        for spin in [self.up_world_x_spin, self.up_world_y_spin, self.up_world_z_spin]:
            spin.setValue(0.0)

        if axis == 'x':
            self.up_world_x_spin.setValue(1.0)
        elif axis == 'y':
            self.up_world_y_spin.setValue(1.0)
        elif axis == 'z':
            self.up_world_z_spin.setValue(1.0)

    def _reset_manual_orient(self):
        for spin in [self.manual_joint_ori_x_spin, self.manual_joint_ori_y_spin, self.manual_joint_ori_z_spin]:
            spin.setValue(0.0)

    def _set_value_change(self, value):
        for spin in [self.manual_joint_ori_x_spin, self.manual_joint_ori_y_spin, self.manual_joint_ori_z_spin]:
            spin.setSingleStep(value)

    def _set_common_rotation_axis(self):
        self.set_rot_axis_common_btn_menu.addAction('Wrist             (YXZ)', partial(self._set_common_rot_order, 'yxz'))
        self.set_rot_axis_common_btn_menu.addAction('Finger           (XYZ)', partial(self._set_common_rot_order, 'xyz'))
        self.set_rot_axis_common_btn_menu.addAction('Spine            (ZYX)', partial(self._set_common_rot_order, 'zyx'))
        self.set_rot_axis_common_btn_menu.addAction('Hips              (ZYX)', partial(self._set_common_rot_order, 'zyx'))
        self.set_rot_axis_common_btn_menu.addAction('Root              (ZYX)', partial(self._set_common_rot_order, 'zyx'))
        self.set_rot_axis_common_btn_menu.addAction('Upper Leg     (ZYX)', partial(self._set_common_rot_order, 'zyx'))
        self.set_rot_axis_common_btn_menu.addAction('Knee              (YXZ)', partial(self._set_common_rot_order, 'yxz'))
        self.set_rot_axis_common_btn_menu.addAction('Ankle             (XZY)', partial(self._set_common_rot_order, 'xzy'))

    def _set_common_rot_order(self, rot_axis):
        rot_order = self._get_rot_order(rot_axis)
        self.set_rot_axis_box.setCurrentIndex(rot_order)

    @staticmethod
    def _get_rot_order(rot_axis):
        rot_order = {}
        for i, order in enumerate(['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx']):
            rot_order[order] = i
            rot_order[order.upper()] = i
        return rot_order[rot_axis]

    @decorators.undo_chunk
    def orient_joints(self):

        reset_joints = []

        # Get up and aim axis
        aim_axis = [0, 0, 0]
        up_axis = [0, 0, 0]

        for i, aim_radio in enumerate([self.aim_x_radio, self.aim_y_radio, self.aim_z_radio]):
            if aim_radio.isChecked():
                aim_axis_num = i

        for i, up_radio in enumerate([self.up_x_radio, self.up_y_radio, self.upZRadio]):
            if up_radio.isChecked():
                up_axup_axis_nums_num = i

        if aim_axis_num == up_axup_axis_nums_num:
            tp.logger.warning('tpJointOrient: aim and up axis are the same, maybe orientation wont work correctly!')

        aim_axis_reverse = 1.0
        if self.aim_rev_cbx.isChecked():
            aim_axis_reverse = -1.0

        up_axis_reverse = 1.0
        if self.upRevCbx.isChecked():
            up_axis_reverse = -1.0

        aim_axis[aim_axis_num] = aim_axis_reverse
        up_axis[up_axup_axis_nums_num] = up_axis_reverse
        world_up_axis = [self.up_world_x_spin.value(), self.up_world_y_spin.value(), self.up_world_z_spin.value()]

        # Get selected joints
        if self.joint_orient_cbx.isChecked():
            maya.cmds.select(hierarchy=True)
        joints = maya.cmds.ls(selection=True, type='joint')

        # =======================================================================

        # Loop all selected joints ...
        for jnt in reversed(joints):

            # Get child node
            childs = maya.cmds.listRelatives(jnt, children=True, type=['transform', 'joint'])

            # If the joints has direct childs, unparent that childs and store names
            if childs:
                if len(childs) > 0:
                    childs = maya.cmds.parent(childs, world=True)

            # Get parent of this joints for later use
            parent = ''
            parents = maya.cmds.listRelatives(jnt, parent=True)
            if parents:
                parent = parents[0]

            # Aim to the child
            aim_target = ''
            if childs:
                for child in childs:
                    if maya.cmds.nodeType(child) == 'joint':
                        aim_target = child
                        break

            # print '//DEBUG: JNT=' + jnt + " Parent=" + parent + " AimTarget=" + aim_target + "//\n"

            if aim_target != '':

                # Apply an aim constraint from the joint to its child (target)
                maya.cmds.delete(maya.cmds.aimConstraint(aim_target, jnt, aim=aim_axis, upVector=up_axis, worldUpVector=world_up_axis,
                                               worldUpType='vector', weight=1.0))

                # Clear joint axis
                maya.cmds.joint(jnt, edit=True, zeroScaleOrient=True)
                maya.cmds.makeIdentity(jnt, apply=True)

            elif parent != '':
                reset_joints.append(jnt)

            # Reparent child
            if childs:
                if len(childs) > 0:
                    maya.cmds.parent(childs, jnt)

        for jnt in reset_joints:
            # If there is no target, the joint will take its parent orientation
            for axis in ['x', 'y', 'z']:
                maya.cmds.setAttr(jnt + '.jointOrient' + axis.upper(), maya.cmds.getAttr(jnt + '.r' + axis))
                maya.cmds.setAttr(jnt + '.r' + axis, 0)

    @decorators.undo_chunk
    def manual_orient_joints(self, type):

        if type == 'add':
            tweak = 1.0
        else:
            tweak = -1.0

        tweak_rot = [self.manual_joint_ori_x_spin.value() * tweak, self.manual_joint_ori_y_spin.value() * tweak,
                    self.manual_joint_ori_z_spin.value() * tweak]
        joints = maya.cmds.ls(selection=True, type='joint')

        for jnt in joints:
            # Adjust the rotation axis
            maya.cmds.xform(jnt, rotateAxis=[tweak_rot[0], tweak_rot[1], tweak_rot[2]], relative=True, objectSpace=True)

            # Clear joint axis
            maya.cmds.joint(jnt, edit=True, zeroScaleOrient=True)
            maya.cmds.makeIdentity(jnt, apply=True)

        maya.cmds.select(joints, replace=True)

    @decorators.undo_chunk
    def set_manual_orient_joints(self):

        tweak_rot = [self.manual_joint_ori_x_spin.value(), self.manual_joint_ori_y_spin.value(),
                    self.manual_joint_ori_z_spin.value()]
        joints = maya.cmds.ls(selection=True, type='joint')

        for jnt in joints:

            if not self.manual_joint_ori_set_cbx.isChecked():

                childs = maya.cmds.listRelatives(jnt, children=True, type=['transform', 'joint'])

                if childs:
                    if len(childs) > 0:
                        for child in childs:
                            maya.cmds.parent(child, world=True)

            # Set the rotation axis
            for i, axis in enumerate(['x', 'y', 'z']):
                maya.cmds.setAttr(jnt + '.jointOrient' + axis.upper(), tweak_rot[i])

            # Clear joint axis
            maya.cmds.joint(jnt, edit=True, zeroScaleOrient=True)
            maya.cmds.makeIdentity(jnt, apply=True)

            if childs:
                for child in childs:
                    maya.cmds.parent(child, jnt)

        maya.cmds.select(joints, replace=True)

    @decorators.undo_chunk
    def set_rot_axis(self):
        sel = maya.cmds.ls(selection=True, type=['joint', 'transform'])
        for obj in sel:
            rot_order = self._get_rot_order(self.set_rot_axis_box.currentText())
            maya.cmds.setAttr(obj + '.rotateOrder', rot_order)

    @staticmethod
    @decorators.undo_chunk
    def set_lra(state):

        sel = maya.cmds.ls(selection=True)

        for obj in sel:
            if maya.cmds.attributeQuery('displayLocalAxis', node=obj, exists=True):
                maya.cmds.setAttr(obj + '.displayLocalAxis', state)

    @staticmethod
    def select_hierarchy():

        """
        Method that selects the hierachy of the selected nodes
        """

        sel = maya.cmds.ls(selection=True)

        for obj in sel:
            maya.cmds.select(obj, hi=True, add=True)


def run():
    win = JointOrient()
    win.show()
    return win
