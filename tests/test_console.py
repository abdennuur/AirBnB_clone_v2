#!/usr/bin/python3
"""console tests"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """tear it down at the end of the test"""
        del cls.consol

    def tearDown(self):
        """Remove tmp file (file.json) created as result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep_8_console(self):
        """Pep8 console.py"""
        stl = pep8.StyleGuide(quiet=True)
        pp = stl.check_files(["console.py"])
        self.assertEqual(pp.total_errors, 0, 'fix Pep8')

    def test_console_docstrs(self):
        """check for docstring"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_for_emptyline(self):
        """To test empty line input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("\n")
            self.assertEqual('', fl.getvalue())

    def test_quit(self):
        """test for quit command inpout"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("quit")
            self.assertEqual('', fl.getvalue())

    def test_create(self):
        """est for create comand input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd('create User email="hoal@.com" password="1234"')
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("all User")
            # self.assertEqual(
            #     "[[User]", f.getvalue()[:7])

    def test_show(self):
        """Test for show comand input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())

    def test_destroy(self):
        """Test for destroy comand input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())

    def test_all(self):
        """Test for all command inpout"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", fl.getvalue())

    def test_update(self):
        """Test for update command inpout"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update User 12345")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("all User")
            objct = fl.getvalue()
        my_id = objct[objct.find('(')+1:objct.find(')')]
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", fl.getvalue())

    def test_alt_all(self):
        """Test alternate all commnd input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("asdfsdfsd.all()")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("State.all()")
            self.assertEqual("[]\n", fl.getvalue())

    def test_for_count(self):
        """Test for count command input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("asdfsdfsd.count()")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("State.count()")
            self.assertEqual("0\n", fl.getvalue())

    def test_for_show(self):
        """Test alternate for show command input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("safdsa.show()")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("BaseModel.show(abcd-123)")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())

    def test_destroy(self):
        """Test alternate destroy command input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("Galaxy.destroy()")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("User.destroy(12345)")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())

    def test_update(self):
        """Test alternate for destroy command input"""
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("sldkfjsl.update()")
            self.assertEqual(
                "** class doesn't exist **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("User.update(12345)")
            self.assertEqual(
                "** no instance found **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("all User")
            objct = fl.getvalue()
        my_id = objct[objct.find('(')+1:objct.find(')')]
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("User.update(" + my_id + ")")
            self.assertEqual(
                "** attribute name missing **\n", fl.getvalue())
        with patch('sys.stdout', new=StringIO()) as fl:
            self.consol.onecmd("User.update(" + my_id + ", name)")
            self.assertEqual(
                "** value missing **\n", fl.getvalue())


if __name__ == "__main__":
    unittest.main()
