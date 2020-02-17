from PyQt5.QtWidgets import QUndoStack, QUndoCommand

from EffectBar.EffectBar import EffectBar
from EffectStatusBar.EffectstatusBar import EffectStatusBar
from EffectStatusBar.RangeSlider import QRangeSlider

stack = QUndoStack()


# maybe be called in EffectBar
class EffectAction(QUndoCommand):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def undo(self):
        for i in EffectStatusBar.items():
            if i.text() == self.name:
                EffectStatusBar.removeRow(i.row())

    def redo(self):
        type = EffectBar.type
        if type == 0:
            EffectBar.effect0_clicked()
        if type == 1:
            EffectBar.effect1_clicked()
        if type == 2:
            EffectBar.effect2_clicked()
        if type == 3:
            EffectBar.effect3_clicked()
        if type == 4:
            EffectBar.effect4_clicked()


# maybe be called in QRangeSlider
class TrackAction(QUndoCommand):

    def __init__(self, start, finish, change):
        super().__init__()
        self.old_start = start
        self.old_finish = finish
        self.change = change

    def undo(self):
        if self.change > self.old_finish:
            QRangeSlider._setEnd(self.old_finish)
        else:
            QRangeSlider._setStart(self.old_start)

    def redo(self):
        if self.change > self.old_finish:
            QRangeSlider._setEnd(self.change)
        else:
            QRangeSlider._setStart(self.change)
