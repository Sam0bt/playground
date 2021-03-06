# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yali/gui/Ui/main.ui'
#
# Created: Mon Nov 24 20:29:52 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import gettext
__trans = gettext.translation('yali', fallback=True)
i18n = __trans.ugettext
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_YaliMain(object):
    def setupUi(self, YaliMain):
        YaliMain.setObjectName(_fromUtf8("YaliMain"))
        YaliMain.resize(750, 540)
        YaliMain.setStyleSheet(_fromUtf8(""))
        self.gridLayout_3 = QtGui.QGridLayout(YaliMain)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Yali = QtGui.QWidget(YaliMain)
        self.Yali.setStyleSheet(_fromUtf8(""))
        self.Yali.setObjectName(_fromUtf8("Yali"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Yali)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.screenContainer = QtGui.QHBoxLayout()
        self.screenContainer.setSpacing(0)
        self.screenContainer.setObjectName(_fromUtf8("screenContainer"))
        self.mainContent = QtGui.QScrollArea(self.Yali)
        self.mainContent.setMinimumSize(QtCore.QSize(0, 0))
        self.mainContent.setFrameShape(QtGui.QFrame.NoFrame)
        self.mainContent.setLineWidth(0)
        self.mainContent.setWidgetResizable(True)
        self.mainContent.setAlignment(QtCore.Qt.AlignCenter)
        self.mainContent.setObjectName(_fromUtf8("mainContent"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 748, 393))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mainStack = QtGui.QStackedWidget(self.scrollAreaWidgetContents)
        self.mainStack.setAutoFillBackground(False)
        self.mainStack.setObjectName(_fromUtf8("mainStack"))
        self.page = QtGui.QWidget()
        self.page.setEnabled(True)
        self.page.setObjectName(_fromUtf8("page"))
        self.mainStack.addWidget(self.page)
        self.gridLayout.addWidget(self.mainStack, 0, 0, 1, 1)
        self.mainContent.setWidget(self.scrollAreaWidgetContents)
        self.screenContainer.addWidget(self.mainContent)
        self.gridLayout_2.addLayout(self.screenContainer, 1, 0, 1, 1)
        self.menuContainer = QtGui.QFrame(self.Yali)
        self.menuContainer.setAutoFillBackground(False)
        self.menuContainer.setStyleSheet(_fromUtf8(""))
        self.menuContainer.setFrameShape(QtGui.QFrame.NoFrame)
        self.menuContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.menuContainer.setObjectName(_fromUtf8("menuContainer"))
        self.hboxlayout = QtGui.QHBoxLayout(self.menuContainer)
        self.hboxlayout.setSpacing(4)
        self.hboxlayout.setContentsMargins(10, 4, 10, 4)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.system_menu = QtGui.QToolButton(self.menuContainer)
        self.system_menu.setStyleSheet(_fromUtf8(""))
        self.system_menu.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/system-shutdown.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.system_menu.setIcon(icon)
        self.system_menu.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.system_menu.setObjectName(_fromUtf8("system_menu"))
        self.hboxlayout.addWidget(self.system_menu)
        self.releaseNotes = QtGui.QPushButton(self.menuContainer)
        self.releaseNotes.setFocusPolicy(QtCore.Qt.TabFocus)
        self.releaseNotes.setFlat(True)
        self.releaseNotes.setObjectName(_fromUtf8("releaseNotes"))
        self.hboxlayout.addWidget(self.releaseNotes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonBack = QtGui.QPushButton(self.menuContainer)
        self.buttonBack.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        self.buttonBack.setFont(font)
        self.buttonBack.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonBack.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pics/arrow-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon1)
        self.buttonBack.setFlat(True)
        self.buttonBack.setObjectName(_fromUtf8("buttonBack"))
        self.hboxlayout.addWidget(self.buttonBack)
        self.buttonNext = QtGui.QPushButton(self.menuContainer)
        self.buttonNext.setMinimumSize(QtCore.QSize(70, 0))
        self.buttonNext.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonNext.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pics/arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(icon2)
        self.buttonNext.setFlat(True)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.hboxlayout.addWidget(self.buttonNext)
        self.gridLayout_2.addWidget(self.menuContainer, 2, 0, 1, 1)
        self.headContainer = QtGui.QFrame(self.Yali)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headContainer.sizePolicy().hasHeightForWidth())
        self.headContainer.setSizePolicy(sizePolicy)
        self.headContainer.setAutoFillBackground(False)
        self.headContainer.setStyleSheet(_fromUtf8(""))
        self.headContainer.setFrameShape(QtGui.QFrame.NoFrame)
        self.headContainer.setFrameShadow(QtGui.QFrame.Raised)
        self.headContainer.setObjectName(_fromUtf8("headContainer"))
        self.gridlayout = QtGui.QGridLayout(self.headContainer)
        self.gridlayout.setMargin(10)
        self.gridlayout.setHorizontalSpacing(10)
        self.gridlayout.setVerticalSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.screenIcon = QtGui.QLabel(self.headContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenIcon.sizePolicy().hasHeightForWidth())
        self.screenIcon.setSizePolicy(sizePolicy)
        self.screenIcon.setMinimumSize(QtCore.QSize(32, 32))
        self.screenIcon.setMaximumSize(QtCore.QSize(32, 32))
        self.screenIcon.setText(_fromUtf8(""))
        self.screenIcon.setPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pics/media-optical-small.png")))
        self.screenIcon.setScaledContents(True)
        self.screenIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.screenIcon.setObjectName(_fromUtf8("screenIcon"))
        self.gridlayout.addWidget(self.screenIcon, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.headContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(134, 36))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pics/logo-on-black.png")))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridlayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.screenName = QtGui.QLabel(self.headContainer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.screenName.setFont(font)
        self.screenName.setStyleSheet(_fromUtf8(""))
        self.screenName.setText(_fromUtf8(""))
        self.screenName.setTextFormat(QtCore.Qt.RichText)
        self.screenName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.screenName.setObjectName(_fromUtf8("screenName"))
        self.horizontalLayout.addWidget(self.screenName)
        self.toggleHelp = QtGui.QPushButton(self.headContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleHelp.sizePolicy().hasHeightForWidth())
        self.toggleHelp.setSizePolicy(sizePolicy)
        self.toggleHelp.setMaximumSize(QtCore.QSize(26, 16777215))
        self.toggleHelp.setFocusPolicy(QtCore.Qt.TabFocus)
        self.toggleHelp.setStyleSheet(_fromUtf8(""))
        self.toggleHelp.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/gui/pics/system-help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggleHelp.setIcon(icon3)
        self.toggleHelp.setCheckable(True)
        self.toggleHelp.setChecked(False)
        self.toggleHelp.setDefault(False)
        self.toggleHelp.setFlat(True)
        self.toggleHelp.setObjectName(_fromUtf8("toggleHelp"))
        self.horizontalLayout.addWidget(self.toggleHelp)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.helpContentFrame = QtGui.QScrollArea(self.headContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpContentFrame.sizePolicy().hasHeightForWidth())
        self.helpContentFrame.setSizePolicy(sizePolicy)
        self.helpContentFrame.setStyleSheet(_fromUtf8("#helpContentFrame{ \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"#scrollAreaWidgetContents_2{ \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}"))
        self.helpContentFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.helpContentFrame.setWidgetResizable(True)
        self.helpContentFrame.setObjectName(_fromUtf8("helpContentFrame"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 542, 58))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.helpContent = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpContent.sizePolicy().hasHeightForWidth())
        self.helpContent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.helpContent.setFont(font)
        self.helpContent.setText(_fromUtf8(""))
        self.helpContent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.helpContent.setWordWrap(True)
        self.helpContent.setObjectName(_fromUtf8("helpContent"))
        self.gridLayout_4.addWidget(self.helpContent, 0, 0, 1, 1)
        self.helpContentFrame.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.helpContentFrame)
        self.gridlayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.headContainer, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Yali, 0, 0, 1, 1)

        self.retranslateUi(YaliMain)
        self.mainStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(YaliMain)

    def retranslateUi(self, YaliMain):
        YaliMain.setWindowTitle(i18n("Yali"))
        self.releaseNotes.setText(i18n("Release Notes"))
        self.buttonBack.setToolTip(i18n("Previous Screen"))
        self.buttonBack.setText(i18n("Back"))
        self.buttonNext.setToolTip(i18n("Next Screen"))
        self.buttonNext.setText(i18n("Next"))

