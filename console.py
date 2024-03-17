#!/usr/bin/python3
""" To define HBNB console"""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ To defines HBnB command interpreter"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """ To ignore the empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command -> exit program"""
        return True

    def do_EOF(self, line):
        """EOF signal -> exit program"""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create new class instance with given keys/values and print id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_ls = line.split(" ")

            kwargs = {}
            for ix in range(1, len(my_ls)):
                key, val = tuple(my_ls[ix].split("="))
                if val[0] == '"':
                    val = val.strip('"').replace("_", " ")
                else:
                    try:
                        val = eval(val)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = val

            if kwargs == {}:
                objct = eval(my_ls[0])()
            else:
                objct = eval(my_ls[0])(**kwargs)
                storage.new(objct)
            print(objct.id)
            objct.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """To Print string representation of instance
        Exceptions:
            SyntaxError: no args given
            NameError: no object taht has the name
            IndexError: no id given
            KeyError: no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_ls = line.split(" ")
            if my_ls[0] not in self.__classes:
                raise NameError()
            if len(my_ls) < 2:
                raise IndexError()
            objcts = storage.all()
            key = my_ls[0] + '.' + my_ls[1]
            if key in objcts:
                print(objcts[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """ To delete instance based on class name and id
        Exceptions:
            SyntaxError: no args given
            NameError: no object taht has the name
            IndexError: no id given
            KeyError: no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_ls = line.split(" ")
            if my_ls[0] not in self.__classes:
                raise NameError()
            if len(my_ls) < 2:
                raise IndexError()
            objcts = storage.all()
            key = my_ls[0] + '.' + my_ls[1]
            if key in objcts:
                del objcts[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Displays string representations of all instances of given class
        If no class specified -> display all instantiated objects"""
        if not line:
            ob = storage.all()
            print([ob[ka].__str__() for ka in ob])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            ob = storage.all(eval(args[0]))
            print([ob[ka].__str__() for ka in ob])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ To updates instanceby adding or updating attribut
        Exceptions:
            SyntaxError: no args given
            NameError: no object taht has the name
            IndexError: no id given
            KeyError: no valid id given
            AttributeError: no attribute given
            ValueError: no value given
        """
        try:
            if not line:
                raise SyntaxError()
            my_ls = split(line, " ")
            if my_ls[0] not in self.__classes:
                raise NameError()
            if len(my_ls) < 2:
                raise IndexError()
            objcts = storage.all()
            key = my_ls[0] + '.' + my_ls[1]
            if key not in objcts:
                raise KeyError()
            if len(my_ls) < 3:
                raise AttributeError()
            if len(my_ls) < 4:
                raise ValueError()
            vi = objcts[key]
            try:
                vi.__dict__[my_ls[2]] = eval(my_ls[3])
            except Exception:
                vi.__dict__[my_ls[2]] = my_ls[3]
                vi.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """ To count nbr of instances of class
        """
        cntr = 0
        try:
            my_ls = split(line, " ")
            if my_ls[0] not in self.__classes:
                raise NameError()
            objcts = storage.all()
            for key in objcts:
                nm = key.split('.')
                if nm[0] == my_ls[0]:
                    cntr += 1
            print(cntr)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """ To strip arg and return a string of command
        Args:
            args: input ls of args
        Return:
            returns str of args
        """
        new_ls = []
        new_ls.append(args[0])
        try:
            my_dct = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dct = None
        if isinstance(my_dict, dict):
            nw_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_ls.append(((nw_str.split(", "))[0]).strip('"'))
            new_ls.append(my_dct)
            return new_ls
        nw_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_ls.append(" ".join(nw_str.split(", ")))
        return " ".join(i for i in new_ls)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_ls = line.split('.')
        if len(my_ls) >= 2:
            if my_ls[1] == "all()":
                self.do_all(my_ls[0])
            elif my_ls[1] == "count()":
                self.count(my_ls[0])
            elif my_ls[1][:4] == "show":
                self.do_show(self.strip_clean(my_ls))
            elif my_ls[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_ls))
            elif my_ls[1][:6] == "update":
                args = self.strip_clean(my_ls)
                if isinstance(args, list):
                    objct = storage.all()
                    key = args[0] + ' ' + args[1]
                    for ka, vi in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(ka, vi))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
