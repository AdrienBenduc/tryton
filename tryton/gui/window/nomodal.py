#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from tryton.gui.main import Main
import tryton.common as common


class NoModal(object):

    def __init__(self):
        self.parent = common.get_toplevel_window()
        self.sensible_widget = common.get_sensible_widget(self.parent)
        self.page = None
        self.parent_focus = self.parent.get_focus()

    def register(self):
        main = Main.get_main()
        self.page = main.get_page()
        if not self.page:
            self.page = main
        self.page.dialogs.append(self)
        self.sensible_widget.props.sensitive = False

    def destroy(self):
        self.page.dialogs.remove(self)
        self.sensible_widget.props.sensitive = True
        self.parent.present()
        self.parent_focus.grab_focus()
