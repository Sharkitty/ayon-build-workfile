from qtpy import QtWidgets, QtCore


class BuildDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self._label = QtWidgets.QLabel(self)
        self._label.setText("Build Workfile")
        self.setWindowTitle("Build Workfile")

        self._vbox = QtWidgets.QVBoxLayout(self)

        self._button_box = QtWidgets.QDialogButtonBox(self)
        self._button_box.accepted.connect(self.build_workfile)
        self._button_box.rejected.connect(self.reject)

    def build_workfile(self):
        # build
        pass


class OverridesDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)


class CastingLoadingDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        # text: Loading casting, please wait
        self._loading_text = QtWidgets.QLabel(self)
        self._loading_text.setText("Loading casting, please wait")
        self._button_box.rejected.connect(self.reject)


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, title, error, parent):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self._error_widget = QtWidgets.QLabel(self)
        self._error_widget.setText(error)

        self._hbox = QtWidgets.QHBoxLayout(self)
        # copy to clipboard button
        # ok button
