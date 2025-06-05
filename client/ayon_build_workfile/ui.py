from qtpy import QtWidgets, QtCore
from ayon_core.addon.base import AddonsManager

from .api.casting_manager import get_casting


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
        # TODO add local overrides
        AddonsManager().get("build_workfile").build_workfile(local_overrides=None)


class OverridesDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        casting = get_casting()

        for actor in casting:
            pass


class CastingLoadingDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self._loading_text = QtWidgets.QLabel(self)
        self._loading_text.setText("Loading casting, please wait")

        self._button_box = QtWidgets.QDialogButtonBox(self)
        self._button_box.rejected.connect(self.reject)


class ActorWidget(QtWidgets.QWidget):
    def __init__(self, actor, parent):
        super().__init__(parent)

        self._hbox = QtWidgets.QHBoxLayout(self)

        self._product_name_label = QtWidgets.QLabel(self._hbox)
        self._product_name_label.setText(actor.get("product_name", ""))

        self._product_type_label = QtWidgets.QLabel(self._hbox)
        self._product_type_label.setText(actor.get("product_type", ""))

        self._loader_combobox = QtWidgets.QComboBox(self._hbox)
        # TODO get possible loaders list

        self._container_label = QtWidgets.QComboBox(self._hbox)
        self._container_label.setText(actor.get("container"))


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
