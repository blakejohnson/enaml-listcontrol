#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Atom, Unicode, List, observe, Int
import enaml
from enaml.qt.qt_application import QtApplication


class Person(Atom):
    """ A simple class representing a person object.

    """
    last_name = Unicode()

    first_name = Unicode()

    nick_names = List(Unicode())
    
    nick_name = Unicode()
    
    index = Int()
    
    @observe('nick_name')
    def _nick_name_changed(self, new):
        print self.nick_name
        
    # @observe('index')
    # def _aux(self, change):
    #     print change


if __name__ == '__main__':
    # Create an employee with a boss
    pers = Person(
        first_name='John', last_name='Paw', nick_names = ['a', 'b', 'c'],
    )

    # Import our Enaml EmployeeView
    with enaml.imports():
        from demo_view import View

    app = QtApplication()
    # Create a view and show it.
    view = View(model = pers)
    view.show()

    app.start()
